using System;

namespace NEXEmailMarketing.Models
{
    /// <summary>
    /// Representa um contato na lista de email marketing
    /// </summary>
    public class Contact
    {
        public int Id { get; set; }
        public string Email { get; set; } = string.Empty;
        public string Name { get; set; } = string.Empty;
        public string Company { get; set; } = string.Empty;
        public string Phone { get; set; } = string.Empty;

        // Campos personalizados
        public string CustomField1 { get; set; } = string.Empty;
        public string CustomField2 { get; set; } = string.Empty;
        public string CustomField3 { get; set; } = string.Empty;

        // Status
        public bool IsSubscribed { get; set; } = true;
        public bool IsVerified { get; set; } = false;
        public bool IsValid { get; set; } = true;

        // Opt-in tracking (IMPORTANTE para conformidade legal)
        public DateTime SubscribedAt { get; set; } = DateTime.Now;
        public string SubscriptionSource { get; set; } = string.Empty;
        public bool DoubleOptIn { get; set; } = false;
        public DateTime? DoubleOptInConfirmedAt { get; set; }

        // Unsubscribe tracking
        public DateTime? UnsubscribedAt { get; set; }
        public string UnsubscribeReason { get; set; } = string.Empty;

        // Bounce tracking
        public int BounceCount { get; set; } = 0;
        public DateTime? LastBounceAt { get; set; }
        public string BounceType { get; set; } = string.Empty; // hard, soft

        // Engagement tracking
        public int EmailsReceived { get; set; } = 0;
        public int EmailsOpened { get; set; } = 0;
        public int LinksClicked { get; set; } = 0;
        public DateTime? LastOpenedAt { get; set; }
        public DateTime? LastClickedAt { get; set; }

        // Segmentation
        public string Tags { get; set; } = string.Empty; // CSV format
        public string Segment { get; set; } = string.Empty;

        // Metadata
        public DateTime CreatedAt { get; set; } = DateTime.Now;
        public DateTime UpdatedAt { get; set; } = DateTime.Now;
        public string Notes { get; set; } = string.Empty;

        /// <summary>
        /// Verifica se o contato pode receber emails
        /// </summary>
        public bool CanReceiveEmails()
        {
            return IsSubscribed && IsValid && BounceType != "hard";
        }

        /// <summary>
        /// Taxa de engajamento (opens + clicks / emails received)
        /// </summary>
        public double GetEngagementRate()
        {
            if (EmailsReceived == 0) return 0;
            return (double)(EmailsOpened + LinksClicked) / EmailsReceived * 100;
        }
    }
}
