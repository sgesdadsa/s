using System;

namespace NEXEmailMarketing.Models
{
    /// <summary>
    /// Representa um template HTML para emails
    /// </summary>
    public class EmailTemplate
    {
        public int Id { get; set; }
        public string Name { get; set; } = string.Empty;
        public string Description { get; set; } = string.Empty;
        public string Category { get; set; } = string.Empty; // newsletter, promotional, transactional

        // Conteúdo
        public string HtmlContent { get; set; } = string.Empty;
        public string CssStyles { get; set; } = string.Empty;

        // Preview
        public string ThumbnailPath { get; set; } = string.Empty;
        public string PreviewText { get; set; } = string.Empty;

        // Variáveis disponíveis no template
        public string AvailableVariables { get; set; } = string.Empty; // JSON format

        // Metadata
        public bool IsActive { get; set; } = true;
        public DateTime CreatedAt { get; set; } = DateTime.Now;
        public DateTime UpdatedAt { get; set; } = DateTime.Now;
        public int TimesUsed { get; set; } = 0;
    }

    /// <summary>
    /// Configuração de SMTP
    /// </summary>
    public class SmtpConfig
    {
        public int Id { get; set; }
        public string Name { get; set; } = string.Empty;
        public string Host { get; set; } = string.Empty;
        public int Port { get; set; } = 587;
        public string Username { get; set; } = string.Empty;
        public string Password { get; set; } = string.Empty;
        public bool UseSsl { get; set; } = true;
        public bool IsDefault { get; set; } = false;
        public bool IsActive { get; set; } = true;

        // Rate limiting
        public int MaxEmailsPerDay { get; set; } = 500;
        public int EmailsSentToday { get; set; } = 0;
        public DateTime LastResetDate { get; set; } = DateTime.Today;

        public DateTime CreatedAt { get; set; } = DateTime.Now;
    }

    /// <summary>
    /// Log de envio de email
    /// </summary>
    public class EmailLog
    {
        public int Id { get; set; }
        public int CampaignId { get; set; }
        public int ContactId { get; set; }
        public string ContactEmail { get; set; } = string.Empty;

        public string Status { get; set; } = string.Empty; // queued, sending, sent, failed, bounced, opened, clicked
        public DateTime StatusUpdatedAt { get; set; } = DateTime.Now;

        public string ErrorMessage { get; set; } = string.Empty;
        public int RetryCount { get; set; } = 0;

        // Tracking
        public bool WasOpened { get; set; } = false;
        public DateTime? OpenedAt { get; set; }
        public int OpenCount { get; set; } = 0;

        public bool WasClicked { get; set; } = false;
        public DateTime? ClickedAt { get; set; }
        public int ClickCount { get; set; } = 0;

        public DateTime CreatedAt { get; set; } = DateTime.Now;
    }
}
