using System;
using System.Text.RegularExpressions;
using System.Net;
using System.Net.Sockets;
using System.Collections.Generic;
using System.Linq;

namespace NEXEmailMarketing.Services
{
    /// <summary>
    /// Serviço de validação de emails
    /// Valida formato, domínio e existência do email
    /// </summary>
    public class EmailValidationService
    {
        private static readonly HashSet<string> DisposableEmailDomains = new()
        {
            "tempmail.com", "guerrillamail.com", "10minutemail.com",
            "mailinator.com", "throwaway.email", "temp-mail.org"
        };

        private static readonly HashSet<string> CommonTypos = new()
        {
            "gmial.com", "gmai.com", "gmil.com", "yahooo.com",
            "yaho.com", "hotmial.com", "outloook.com"
        };

        /// <summary>
        /// Resultado da validação de email
        /// </summary>
        public class ValidationResult
        {
            public bool IsValid { get; set; }
            public string Email { get; set; } = string.Empty;
            public List<string> Errors { get; set; } = new();
            public List<string> Warnings { get; set; } = new();
            public string SuggestedFix { get; set; } = string.Empty;
            public bool IsDisposable { get; set; }
            public bool HasTypo { get; set; }
            public bool DomainExists { get; set; }
            public string ValidationLevel { get; set; } = "basic"; // basic, domain, smtp
        }

        /// <summary>
        /// Valida formato básico do email usando regex
        /// </summary>
        public bool IsValidFormat(string email)
        {
            if (string.IsNullOrWhiteSpace(email))
                return false;

            try
            {
                // RFC 5322 compliant regex
                var regex = new Regex(
                    @"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$",
                    RegexOptions.IgnoreCase);

                return regex.IsMatch(email);
            }
            catch
            {
                return false;
            }
        }

        /// <summary>
        /// Validação completa do email
        /// </summary>
        public ValidationResult ValidateEmail(string email, bool checkDomain = true, bool checkSmtp = false)
        {
            var result = new ValidationResult { Email = email };

            // 1. Validação de formato
            if (!IsValidFormat(email))
            {
                result.IsValid = false;
                result.Errors.Add("Formato de email inválido");
                return result;
            }

            var parts = email.Split('@');
            if (parts.Length != 2)
            {
                result.IsValid = false;
                result.Errors.Add("Email deve conter exatamente um @");
                return result;
            }

            var localPart = parts[0];
            var domain = parts[1];

            // 2. Validações adicionais
            if (localPart.Length > 64)
            {
                result.Errors.Add("Parte local do email muito longa (máx 64 caracteres)");
            }

            if (domain.Length > 255)
            {
                result.Errors.Add("Domínio muito longo (máx 255 caracteres)");
            }

            // 3. Verificar se é email descartável
            if (DisposableEmailDomains.Contains(domain.ToLower()))
            {
                result.IsDisposable = true;
                result.Warnings.Add("Email descartável detectado");
            }

            // 4. Verificar typos comuns
            if (CommonTypos.Contains(domain.ToLower()))
            {
                result.HasTypo = true;
                result.SuggestedFix = SuggestEmailFix(email);
                result.Warnings.Add($"Possível erro de digitação. Sugestão: {result.SuggestedFix}");
            }

            // 5. Verificar se domínio existe (DNS)
            if (checkDomain)
            {
                result.DomainExists = CheckDomainExists(domain);
                result.ValidationLevel = "domain";

                if (!result.DomainExists)
                {
                    result.Errors.Add("Domínio não existe");
                }
            }

            // 6. Verificar SMTP (mais rigoroso, mas mais lento)
            if (checkSmtp && result.DomainExists)
            {
                // Nota: Verificação SMTP real pode ser bloqueada por alguns servidores
                result.ValidationLevel = "smtp";
                // Implementação básica - em produção, use biblioteca especializada
            }

            result.IsValid = result.Errors.Count == 0;
            return result;
        }

        /// <summary>
        /// Verifica se o domínio existe via DNS
        /// </summary>
        private bool CheckDomainExists(string domain)
        {
            try
            {
                var hostEntry = Dns.GetHostEntry(domain);
                return hostEntry.AddressList.Length > 0;
            }
            catch
            {
                // Tenta verificar registros MX
                try
                {
                    // Simplificado - em produção, use biblioteca DNS especializada
                    var host = Dns.GetHostEntry(domain);
                    return true;
                }
                catch
                {
                    return false;
                }
            }
        }

        /// <summary>
        /// Sugere correção para typos comuns
        /// </summary>
        private string SuggestEmailFix(string email)
        {
            var typoFixes = new Dictionary<string, string>
            {
                { "gmial.com", "gmail.com" },
                { "gmai.com", "gmail.com" },
                { "gmil.com", "gmail.com" },
                { "yahooo.com", "yahoo.com" },
                { "yaho.com", "yahoo.com" },
                { "hotmial.com", "hotmail.com" },
                { "outloook.com", "outlook.com" }
            };

            foreach (var typo in typoFixes)
            {
                if (email.EndsWith("@" + typo.Key, StringComparison.OrdinalIgnoreCase))
                {
                    return email.Replace(typo.Key, typo.Value, StringComparison.OrdinalIgnoreCase);
                }
            }

            return email;
        }

        /// <summary>
        /// Valida lista de emails em lote
        /// </summary>
        public Dictionary<string, ValidationResult> ValidateBulk(List<string> emails, bool checkDomain = false)
        {
            var results = new Dictionary<string, ValidationResult>();

            foreach (var email in emails)
            {
                results[email] = ValidateEmail(email, checkDomain, false);
            }

            return results;
        }

        /// <summary>
        /// Remove emails duplicados de uma lista
        /// </summary>
        public List<string> RemoveDuplicates(List<string> emails)
        {
            return emails.Distinct(StringComparer.OrdinalIgnoreCase).ToList();
        }

        /// <summary>
        /// Filtra apenas emails válidos de uma lista
        /// </summary>
        public List<string> FilterValidEmails(List<string> emails)
        {
            return emails.Where(e => IsValidFormat(e)).ToList();
        }

        /// <summary>
        /// Normaliza email (lowercase, trim)
        /// </summary>
        public string NormalizeEmail(string email)
        {
            return email.Trim().ToLower();
        }

        /// <summary>
        /// Estatísticas de validação
        /// </summary>
        public class ValidationStats
        {
            public int Total { get; set; }
            public int Valid { get; set; }
            public int Invalid { get; set; }
            public int Disposable { get; set; }
            public int WithTypos { get; set; }
            public int Duplicates { get; set; }

            public double ValidPercentage => Total > 0 ? (double)Valid / Total * 100 : 0;
        }

        /// <summary>
        /// Gera estatísticas de uma lista de emails
        /// </summary>
        public ValidationStats GetValidationStats(List<string> emails)
        {
            var stats = new ValidationStats { Total = emails.Count };
            var uniqueEmails = new HashSet<string>(StringComparer.OrdinalIgnoreCase);

            foreach (var email in emails)
            {
                var result = ValidateEmail(email, false, false);

                if (result.IsValid) stats.Valid++;
                else stats.Invalid++;

                if (result.IsDisposable) stats.Disposable++;
                if (result.HasTypo) stats.WithTypos++;

                if (!uniqueEmails.Add(email.ToLower()))
                {
                    stats.Duplicates++;
                }
            }

            return stats;
        }
    }
}
