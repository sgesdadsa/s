using System;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;
using System.Linq;
using MailKit.Net.Smtp;
using MailKit.Security;
using MimeKit;
using NEXEmailMarketing.Models;

namespace NEXEmailMarketing.Services
{
    /// <summary>
    /// Serviço de envio de emails com rate limiting e retry logic
    /// </summary>
    public class EmailSendingService
    {
        private readonly SemaphoreSlim _rateLimiter;
        private DateTime _lastEmailSent = DateTime.MinValue;
        private int _emailsSentThisMinute = 0;
        private DateTime _minuteStartTime = DateTime.Now;

        public event EventHandler<EmailSentEventArgs>? EmailSent;
        public event EventHandler<EmailFailedEventArgs>? EmailFailed;
        public event EventHandler<ProgressEventArgs>? ProgressUpdated;

        private CancellationTokenSource? _cancellationTokenSource;

        public EmailSendingService()
        {
            _rateLimiter = new SemaphoreSlim(1, 1);
        }

        /// <summary>
        /// Envia um email individual
        /// </summary>
        public async Task<SendResult> SendEmailAsync(
            SmtpConfig smtpConfig,
            string toEmail,
            string toName,
            string subject,
            string htmlBody,
            string? plainTextBody = null,
            List<string>? attachments = null)
        {
            var result = new SendResult { Email = toEmail };

            try
            {
                var message = new MimeMessage();
                message.From.Add(new MailboxAddress(smtpConfig.Name, smtpConfig.Username));
                message.To.Add(new MailboxAddress(toName, toEmail));
                message.Subject = subject;

                var builder = new BodyBuilder
                {
                    HtmlBody = htmlBody,
                    TextBody = plainTextBody ?? StripHtml(htmlBody)
                };

                // Adicionar anexos se houver
                if (attachments != null)
                {
                    foreach (var attachment in attachments)
                    {
                        builder.Attachments.Add(attachment);
                    }
                }

                message.Body = builder.ToMessageBody();

                // Enviar via SMTP
                using var client = new SmtpClient();

                await client.ConnectAsync(smtpConfig.Host, smtpConfig.Port,
                    smtpConfig.UseSsl ? SecureSocketOptions.StartTls : SecureSocketOptions.None);

                await client.AuthenticateAsync(smtpConfig.Username, smtpConfig.Password);
                await client.SendAsync(message);
                await client.DisconnectAsync(true);

                result.Success = true;
                result.SentAt = DateTime.Now;
            }
            catch (Exception ex)
            {
                result.Success = false;
                result.ErrorMessage = ex.Message;
            }

            return result;
        }

        /// <summary>
        /// Envia campanha completa com rate limiting
        /// </summary>
        public async Task SendCampaignAsync(
            Campaign campaign,
            List<Contact> recipients,
            SmtpConfig smtpConfig,
            string htmlTemplate,
            CancellationToken cancellationToken = default)
        {
            _cancellationTokenSource = CancellationTokenSource.CreateLinkedTokenSource(cancellationToken);
            var token = _cancellationTokenSource.Token;

            var totalRecipients = recipients.Count;
            var sentCount = 0;
            var failedCount = 0;

            campaign.Status = "sending";
            campaign.TotalRecipients = totalRecipients;

            foreach (var contact in recipients)
            {
                if (token.IsCancellationRequested)
                {
                    campaign.Status = "paused";
                    break;
                }

                // Rate limiting - respeita limites para não ser bloqueado
                await ApplyRateLimitingAsync(campaign);

                // Personalizar conteúdo para este contato
                var personalizedHtml = PersonalizeContent(htmlTemplate, contact);

                // Enviar email
                var result = await SendEmailAsync(
                    smtpConfig,
                    contact.Email,
                    contact.Name,
                    campaign.Subject,
                    personalizedHtml);

                if (result.Success)
                {
                    sentCount++;
                    campaign.EmailsSent++;
                    campaign.EmailsDelivered++;

                    EmailSent?.Invoke(this, new EmailSentEventArgs
                    {
                        Contact = contact,
                        Campaign = campaign,
                        SentAt = result.SentAt
                    });
                }
                else
                {
                    failedCount++;
                    campaign.EmailsBounced++;

                    EmailFailed?.Invoke(this, new EmailFailedEventArgs
                    {
                        Contact = contact,
                        Campaign = campaign,
                        ErrorMessage = result.ErrorMessage
                    });

                    // Retry logic para falhas temporárias
                    if (ShouldRetry(result.ErrorMessage))
                    {
                        await Task.Delay(5000, token); // Aguarda 5s antes de retry
                        var retryResult = await SendEmailAsync(smtpConfig, contact.Email,
                            contact.Name, campaign.Subject, personalizedHtml);

                        if (retryResult.Success)
                        {
                            sentCount++;
                            failedCount--;
                        }
                    }
                }

                // Atualizar progresso
                campaign.Progress = (int)((double)sentCount / totalRecipients * 100);

                ProgressUpdated?.Invoke(this, new ProgressEventArgs
                {
                    TotalEmails = totalRecipients,
                    SentEmails = sentCount,
                    FailedEmails = failedCount,
                    Progress = campaign.Progress
                });
            }

            campaign.Status = sentCount == totalRecipients ? "sent" : "partially_sent";
            campaign.SentAt = DateTime.Now;
        }

        /// <summary>
        /// Aplica rate limiting para evitar bloqueios
        /// </summary>
        private async Task ApplyRateLimitingAsync(Campaign campaign)
        {
            await _rateLimiter.WaitAsync();

            try
            {
                // Resetar contador se passou 1 minuto
                if ((DateTime.Now - _minuteStartTime).TotalMinutes >= 1)
                {
                    _emailsSentThisMinute = 0;
                    _minuteStartTime = DateTime.Now;
                }

                // Verificar limite por minuto
                if (_emailsSentThisMinute >= campaign.EmailsPerMinute)
                {
                    var waitTime = 60000 - (int)(DateTime.Now - _minuteStartTime).TotalMilliseconds;
                    if (waitTime > 0)
                    {
                        await Task.Delay(waitTime);
                    }
                    _emailsSentThisMinute = 0;
                    _minuteStartTime = DateTime.Now;
                }

                // Delay entre emails
                var timeSinceLastEmail = (DateTime.Now - _lastEmailSent).TotalMilliseconds;
                if (timeSinceLastEmail < campaign.DelayBetweenEmails)
                {
                    await Task.Delay(campaign.DelayBetweenEmails - (int)timeSinceLastEmail);
                }

                _lastEmailSent = DateTime.Now;
                _emailsSentThisMinute++;
            }
            finally
            {
                _rateLimiter.Release();
            }
        }

        /// <summary>
        /// Personaliza conteúdo do email com dados do contato
        /// </summary>
        private string PersonalizeContent(string template, Contact contact)
        {
            var personalized = template;

            // Variáveis padrão disponíveis
            var variables = new Dictionary<string, string>
            {
                { "{{name}}", contact.Name },
                { "{{email}}", contact.Email },
                { "{{company}}", contact.Company },
                { "{{phone}}", contact.Phone },
                { "{{custom1}}", contact.CustomField1 },
                { "{{custom2}}", contact.CustomField2 },
                { "{{custom3}}", contact.CustomField3 },
                { "{{year}}", DateTime.Now.Year.ToString() },
                { "{{date}}", DateTime.Now.ToString("dd/MM/yyyy") },
                { "{{unsubscribe}}", $"http://localhost:8000/unsubscribe?email={contact.Email}&id={contact.Id}" }
            };

            foreach (var variable in variables)
            {
                personalized = personalized.Replace(variable.Key, variable.Value);
            }

            return personalized;
        }

        /// <summary>
        /// Remove HTML tags para criar versão texto
        /// </summary>
        private string StripHtml(string html)
        {
            var text = System.Text.RegularExpressions.Regex.Replace(html, "<.*?>", string.Empty);
            return text.Trim();
        }

        /// <summary>
        /// Verifica se deve fazer retry baseado no erro
        /// </summary>
        private bool ShouldRetry(string errorMessage)
        {
            var temporaryErrors = new[] { "timeout", "connection", "temporary", "try again" };
            return temporaryErrors.Any(e => errorMessage.ToLower().Contains(e));
        }

        /// <summary>
        /// Pausa envio de campanha
        /// </summary>
        public void PauseCampaign()
        {
            _cancellationTokenSource?.Cancel();
        }

        /// <summary>
        /// Envia email de teste
        /// </summary>
        public async Task<SendResult> SendTestEmailAsync(
            SmtpConfig smtpConfig,
            string testEmail,
            string subject,
            string htmlContent)
        {
            return await SendEmailAsync(smtpConfig, testEmail, "Test Recipient",
                "[TEST] " + subject, htmlContent);
        }

        // Event Args
        public class EmailSentEventArgs : EventArgs
        {
            public Contact Contact { get; set; } = null!;
            public Campaign Campaign { get; set; } = null!;
            public DateTime SentAt { get; set; }
        }

        public class EmailFailedEventArgs : EventArgs
        {
            public Contact Contact { get; set; } = null!;
            public Campaign Campaign { get; set; } = null!;
            public string ErrorMessage { get; set; } = string.Empty;
        }

        public class ProgressEventArgs : EventArgs
        {
            public int TotalEmails { get; set; }
            public int SentEmails { get; set; }
            public int FailedEmails { get; set; }
            public int Progress { get; set; }
        }

        public class SendResult
        {
            public bool Success { get; set; }
            public string Email { get; set; } = string.Empty;
            public DateTime SentAt { get; set; }
            public string ErrorMessage { get; set; } = string.Empty;
        }
    }
}
