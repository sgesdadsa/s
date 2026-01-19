using System;

namespace NEXEmailMarketing.Models
{
    /// <summary>
    /// Representa uma campanha de email marketing
    /// </summary>
    public class Campaign
    {
        public int Id { get; set; }
        public string Name { get; set; } = string.Empty;
        public string Subject { get; set; } = string.Empty;
        public string FromName { get; set; } = string.Empty;
        public string FromEmail { get; set; } = string.Empty;
        public string ReplyToEmail { get; set; } = string.Empty;

        // Conteúdo
        public string HtmlContent { get; set; } = string.Empty;
        public string PlainTextContent { get; set; } = string.Empty;
        public int TemplateId { get; set; }

        // Targeting
        public string TargetSegment { get; set; } = string.Empty;
        public string TargetTags { get; set; } = string.Empty;

        // Scheduling
        public DateTime? ScheduledAt { get; set; }
        public bool IsScheduled { get; set; } = false;
        public bool IsSent { get; set; } = false;
        public DateTime? SentAt { get; set; }

        // Status
        public string Status { get; set; } = "draft"; // draft, scheduled, sending, sent, paused, failed
        public int Progress { get; set; } = 0; // 0-100

        // Statistics
        public int TotalRecipients { get; set; } = 0;
        public int EmailsSent { get; set; } = 0;
        public int EmailsDelivered { get; set; } = 0;
        public int EmailsBounced { get; set; } = 0;
        public int EmailsOpened { get; set; } = 0;
        public int LinksClicked { get; set; } = 0;
        public int Unsubscribes { get; set; } = 0;
        public int SpamComplaints { get; set; } = 0;

        // Rate limiting (IMPORTANTE para não ser bloqueado)
        public int EmailsPerMinute { get; set; } = 30; // Limite seguro
        public int EmailsPerHour { get; set; } = 500;
        public int DelayBetweenEmails { get; set; } = 2000; // ms

        // Tracking
        public bool TrackOpens { get; set; } = true;
        public bool TrackClicks { get; set; } = true;

        // Compliance (OBRIGATÓRIO para legalidade)
        public bool IncludeUnsubscribeLink { get; set; } = true;
        public bool IncludePhysicalAddress { get; set; } = true;
        public string PhysicalAddress { get; set; } = string.Empty;

        // Metadata
        public DateTime CreatedAt { get; set; } = DateTime.Now;
        public DateTime UpdatedAt { get; set; } = DateTime.Now;
        public string Notes { get; set; } = string.Empty;

        /// <summary>
        /// Calcula taxa de abertura (Open Rate)
        /// </summary>
        public double GetOpenRate()
        {
            if (EmailsDelivered == 0) return 0;
            return (double)EmailsOpened / EmailsDelivered * 100;
        }

        /// <summary>
        /// Calcula taxa de cliques (Click Rate)
        /// </summary>
        public double GetClickRate()
        {
            if (EmailsDelivered == 0) return 0;
            return (double)LinksClicked / EmailsDelivered * 100;
        }

        /// <summary>
        /// Calcula taxa de bounce
        /// </summary>
        public double GetBounceRate()
        {
            if (EmailsSent == 0) return 0;
            return (double)EmailsBounced / EmailsSent * 100;
        }

        /// <summary>
        /// Calcula taxa de entrega (Delivery Rate)
        /// </summary>
        public double GetDeliveryRate()
        {
            if (EmailsSent == 0) return 0;
            return (double)EmailsDelivered / EmailsSent * 100;
        }
    }
}
