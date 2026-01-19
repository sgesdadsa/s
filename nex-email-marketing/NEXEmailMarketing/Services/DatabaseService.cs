using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SQLite;
using System.IO;
using System.Linq;
using NEXEmailMarketing.Models;
using Newtonsoft.Json;

namespace NEXEmailMarketing.Services
{
    /// <summary>
    /// Serviço de banco de dados SQLite
    /// </summary>
    public class DatabaseService
    {
        private readonly string _connectionString;
        private readonly string _dbPath;

        public DatabaseService(string dbPath = "nex_email_marketing.db")
        {
            _dbPath = dbPath;
            _connectionString = $"Data Source={dbPath};Version=3;";
            InitializeDatabase();
        }

        /// <summary>
        /// Inicializa banco de dados e cria tabelas
        /// </summary>
        private void InitializeDatabase()
        {
            if (!File.Exists(_dbPath))
            {
                SQLiteConnection.CreateFile(_dbPath);
            }

            using var connection = new SQLiteConnection(_connectionString);
            connection.Open();

            // Criar tabelas
            var commands = new[]
            {
                // Contacts
                @"CREATE TABLE IF NOT EXISTS Contacts (
                    Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Email TEXT NOT NULL UNIQUE,
                    Name TEXT,
                    Company TEXT,
                    Phone TEXT,
                    CustomField1 TEXT,
                    CustomField2 TEXT,
                    CustomField3 TEXT,
                    IsSubscribed INTEGER DEFAULT 1,
                    IsVerified INTEGER DEFAULT 0,
                    IsValid INTEGER DEFAULT 1,
                    SubscribedAt TEXT,
                    SubscriptionSource TEXT,
                    DoubleOptIn INTEGER DEFAULT 0,
                    DoubleOptInConfirmedAt TEXT,
                    UnsubscribedAt TEXT,
                    UnsubscribeReason TEXT,
                    BounceCount INTEGER DEFAULT 0,
                    LastBounceAt TEXT,
                    BounceType TEXT,
                    EmailsReceived INTEGER DEFAULT 0,
                    EmailsOpened INTEGER DEFAULT 0,
                    LinksClicked INTEGER DEFAULT 0,
                    LastOpenedAt TEXT,
                    LastClickedAt TEXT,
                    Tags TEXT,
                    Segment TEXT,
                    CreatedAt TEXT,
                    UpdatedAt TEXT,
                    Notes TEXT
                )",

                // Campaigns
                @"CREATE TABLE IF NOT EXISTS Campaigns (
                    Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT NOT NULL,
                    Subject TEXT,
                    FromName TEXT,
                    FromEmail TEXT,
                    ReplyToEmail TEXT,
                    HtmlContent TEXT,
                    PlainTextContent TEXT,
                    TemplateId INTEGER,
                    TargetSegment TEXT,
                    TargetTags TEXT,
                    ScheduledAt TEXT,
                    IsScheduled INTEGER DEFAULT 0,
                    IsSent INTEGER DEFAULT 0,
                    SentAt TEXT,
                    Status TEXT DEFAULT 'draft',
                    Progress INTEGER DEFAULT 0,
                    TotalRecipients INTEGER DEFAULT 0,
                    EmailsSent INTEGER DEFAULT 0,
                    EmailsDelivered INTEGER DEFAULT 0,
                    EmailsBounced INTEGER DEFAULT 0,
                    EmailsOpened INTEGER DEFAULT 0,
                    LinksClicked INTEGER DEFAULT 0,
                    Unsubscribes INTEGER DEFAULT 0,
                    SpamComplaints INTEGER DEFAULT 0,
                    EmailsPerMinute INTEGER DEFAULT 30,
                    EmailsPerHour INTEGER DEFAULT 500,
                    DelayBetweenEmails INTEGER DEFAULT 2000,
                    TrackOpens INTEGER DEFAULT 1,
                    TrackClicks INTEGER DEFAULT 1,
                    IncludeUnsubscribeLink INTEGER DEFAULT 1,
                    IncludePhysicalAddress INTEGER DEFAULT 1,
                    PhysicalAddress TEXT,
                    CreatedAt TEXT,
                    UpdatedAt TEXT,
                    Notes TEXT
                )",

                // Templates
                @"CREATE TABLE IF NOT EXISTS EmailTemplates (
                    Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT NOT NULL,
                    Description TEXT,
                    Category TEXT,
                    HtmlContent TEXT,
                    CssStyles TEXT,
                    ThumbnailPath TEXT,
                    PreviewText TEXT,
                    AvailableVariables TEXT,
                    IsActive INTEGER DEFAULT 1,
                    CreatedAt TEXT,
                    UpdatedAt TEXT,
                    TimesUsed INTEGER DEFAULT 0
                )",

                // SMTP Configs
                @"CREATE TABLE IF NOT EXISTS SmtpConfigs (
                    Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT NOT NULL,
                    Host TEXT NOT NULL,
                    Port INTEGER DEFAULT 587,
                    Username TEXT,
                    Password TEXT,
                    UseSsl INTEGER DEFAULT 1,
                    IsDefault INTEGER DEFAULT 0,
                    IsActive INTEGER DEFAULT 1,
                    MaxEmailsPerDay INTEGER DEFAULT 500,
                    EmailsSentToday INTEGER DEFAULT 0,
                    LastResetDate TEXT,
                    CreatedAt TEXT
                )",

                // Email Logs
                @"CREATE TABLE IF NOT EXISTS EmailLogs (
                    Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    CampaignId INTEGER,
                    ContactId INTEGER,
                    ContactEmail TEXT,
                    Status TEXT,
                    StatusUpdatedAt TEXT,
                    ErrorMessage TEXT,
                    RetryCount INTEGER DEFAULT 0,
                    WasOpened INTEGER DEFAULT 0,
                    OpenedAt TEXT,
                    OpenCount INTEGER DEFAULT 0,
                    WasClicked INTEGER DEFAULT 0,
                    ClickedAt TEXT,
                    ClickCount INTEGER DEFAULT 0,
                    CreatedAt TEXT
                )",

                // Indexes for performance
                @"CREATE INDEX IF NOT EXISTS idx_contacts_email ON Contacts(Email)",
                @"CREATE INDEX IF NOT EXISTS idx_contacts_subscribed ON Contacts(IsSubscribed)",
                @"CREATE INDEX IF NOT EXISTS idx_campaigns_status ON Campaigns(Status)",
                @"CREATE INDEX IF NOT EXISTS idx_emaillogs_campaign ON EmailLogs(CampaignId)",
                @"CREATE INDEX IF NOT EXISTS idx_emaillogs_contact ON EmailLogs(ContactId)"
            };

            foreach (var sql in commands)
            {
                using var cmd = new SQLiteCommand(sql, connection);
                cmd.ExecuteNonQuery();
            }
        }

        #region Contacts

        public void AddContact(Contact contact)
        {
            using var connection = new SQLiteConnection(_connectionString);
            connection.Open();

            var sql = @"INSERT INTO Contacts (
                Email, Name, Company, Phone, CustomField1, CustomField2, CustomField3,
                IsSubscribed, IsVerified, IsValid, SubscribedAt, SubscriptionSource,
                DoubleOptIn, Tags, Segment, CreatedAt, UpdatedAt
            ) VALUES (
                @Email, @Name, @Company, @Phone, @CustomField1, @CustomField2, @CustomField3,
                @IsSubscribed, @IsVerified, @IsValid, @SubscribedAt, @SubscriptionSource,
                @DoubleOptIn, @Tags, @Segment, @CreatedAt, @UpdatedAt
            )";

            using var cmd = new SQLiteCommand(sql, connection);
            cmd.Parameters.AddWithValue("@Email", contact.Email);
            cmd.Parameters.AddWithValue("@Name", contact.Name);
            cmd.Parameters.AddWithValue("@Company", contact.Company);
            cmd.Parameters.AddWithValue("@Phone", contact.Phone);
            cmd.Parameters.AddWithValue("@CustomField1", contact.CustomField1);
            cmd.Parameters.AddWithValue("@CustomField2", contact.CustomField2);
            cmd.Parameters.AddWithValue("@CustomField3", contact.CustomField3);
            cmd.Parameters.AddWithValue("@IsSubscribed", contact.IsSubscribed ? 1 : 0);
            cmd.Parameters.AddWithValue("@IsVerified", contact.IsVerified ? 1 : 0);
            cmd.Parameters.AddWithValue("@IsValid", contact.IsValid ? 1 : 0);
            cmd.Parameters.AddWithValue("@SubscribedAt", contact.SubscribedAt.ToString("o"));
            cmd.Parameters.AddWithValue("@SubscriptionSource", contact.SubscriptionSource);
            cmd.Parameters.AddWithValue("@DoubleOptIn", contact.DoubleOptIn ? 1 : 0);
            cmd.Parameters.AddWithValue("@Tags", contact.Tags);
            cmd.Parameters.AddWithValue("@Segment", contact.Segment);
            cmd.Parameters.AddWithValue("@CreatedAt", DateTime.Now.ToString("o"));
            cmd.Parameters.AddWithValue("@UpdatedAt", DateTime.Now.ToString("o"));

            cmd.ExecuteNonQuery();
        }

        public List<Contact> GetAllContacts()
        {
            var contacts = new List<Contact>();

            using var connection = new SQLiteConnection(_connectionString);
            connection.Open();

            var sql = "SELECT * FROM Contacts ORDER BY CreatedAt DESC";

            using var cmd = new SQLiteCommand(sql, connection);
            using var reader = cmd.ExecuteReader();

            while (reader.Read())
            {
                contacts.Add(ReadContact(reader));
            }

            return contacts;
        }

        public List<Contact> GetSubscribedContacts()
        {
            var contacts = new List<Contact>();

            using var connection = new SQLiteConnection(_connectionString);
            connection.Open();

            var sql = "SELECT * FROM Contacts WHERE IsSubscribed = 1 AND IsValid = 1";

            using var cmd = new SQLiteCommand(sql, connection);
            using var reader = cmd.ExecuteReader();

            while (reader.Read())
            {
                contacts.Add(ReadContact(reader));
            }

            return contacts;
        }

        public void UpdateContact(Contact contact)
        {
            using var connection = new SQLiteConnection(_connectionString);
            connection.Open();

            var sql = @"UPDATE Contacts SET
                Name = @Name,
                Company = @Company,
                Phone = @Phone,
                IsSubscribed = @IsSubscribed,
                IsValid = @IsValid,
                BounceCount = @BounceCount,
                EmailsReceived = @EmailsReceived,
                EmailsOpened = @EmailsOpened,
                LinksClicked = @LinksClicked,
                Tags = @Tags,
                Segment = @Segment,
                UpdatedAt = @UpdatedAt
                WHERE Id = @Id";

            using var cmd = new SQLiteCommand(sql, connection);
            cmd.Parameters.AddWithValue("@Id", contact.Id);
            cmd.Parameters.AddWithValue("@Name", contact.Name);
            cmd.Parameters.AddWithValue("@Company", contact.Company);
            cmd.Parameters.AddWithValue("@Phone", contact.Phone);
            cmd.Parameters.AddWithValue("@IsSubscribed", contact.IsSubscribed ? 1 : 0);
            cmd.Parameters.AddWithValue("@IsValid", contact.IsValid ? 1 : 0);
            cmd.Parameters.AddWithValue("@BounceCount", contact.BounceCount);
            cmd.Parameters.AddWithValue("@EmailsReceived", contact.EmailsReceived);
            cmd.Parameters.AddWithValue("@EmailsOpened", contact.EmailsOpened);
            cmd.Parameters.AddWithValue("@LinksClicked", contact.LinksClicked);
            cmd.Parameters.AddWithValue("@Tags", contact.Tags);
            cmd.Parameters.AddWithValue("@Segment", contact.Segment);
            cmd.Parameters.AddWithValue("@UpdatedAt", DateTime.Now.ToString("o"));

            cmd.ExecuteNonQuery();
        }

        public void DeleteContact(int id)
        {
            using var connection = new SQLiteConnection(_connectionString);
            connection.Open();

            var sql = "DELETE FROM Contacts WHERE Id = @Id";

            using var cmd = new SQLiteCommand(sql, connection);
            cmd.Parameters.AddWithValue("@Id", id);
            cmd.ExecuteNonQuery();
        }

        private Contact ReadContact(SQLiteDataReader reader)
        {
            return new Contact
            {
                Id = reader.GetInt32(0),
                Email = reader.GetString(1),
                Name = reader.IsDBNull(2) ? "" : reader.GetString(2),
                Company = reader.IsDBNull(3) ? "" : reader.GetString(3),
                Phone = reader.IsDBNull(4) ? "" : reader.GetString(4),
                CustomField1 = reader.IsDBNull(5) ? "" : reader.GetString(5),
                CustomField2 = reader.IsDBNull(6) ? "" : reader.GetString(6),
                CustomField3 = reader.IsDBNull(7) ? "" : reader.GetString(7),
                IsSubscribed = reader.GetInt32(8) == 1,
                IsVerified = reader.GetInt32(9) == 1,
                IsValid = reader.GetInt32(10) == 1,
                Tags = reader.IsDBNull(25) ? "" : reader.GetString(25),
                Segment = reader.IsDBNull(26) ? "" : reader.GetString(26)
            };
        }

        #endregion

        #region Campaigns

        public int AddCampaign(Campaign campaign)
        {
            using var connection = new SQLiteConnection(_connectionString);
            connection.Open();

            var sql = @"INSERT INTO Campaigns (
                Name, Subject, FromName, FromEmail, ReplyToEmail,
                HtmlContent, Status, CreatedAt, UpdatedAt
            ) VALUES (
                @Name, @Subject, @FromName, @FromEmail, @ReplyToEmail,
                @HtmlContent, @Status, @CreatedAt, @UpdatedAt
            ); SELECT last_insert_rowid();";

            using var cmd = new SQLiteCommand(sql, connection);
            cmd.Parameters.AddWithValue("@Name", campaign.Name);
            cmd.Parameters.AddWithValue("@Subject", campaign.Subject);
            cmd.Parameters.AddWithValue("@FromName", campaign.FromName);
            cmd.Parameters.AddWithValue("@FromEmail", campaign.FromEmail);
            cmd.Parameters.AddWithValue("@ReplyToEmail", campaign.ReplyToEmail);
            cmd.Parameters.AddWithValue("@HtmlContent", campaign.HtmlContent);
            cmd.Parameters.AddWithValue("@Status", campaign.Status);
            cmd.Parameters.AddWithValue("@CreatedAt", DateTime.Now.ToString("o"));
            cmd.Parameters.AddWithValue("@UpdatedAt", DateTime.Now.ToString("o"));

            return Convert.ToInt32(cmd.ExecuteScalar());
        }

        public List<Campaign> GetAllCampaigns()
        {
            var campaigns = new List<Campaign>();

            using var connection = new SQLiteConnection(_connectionString);
            connection.Open();

            var sql = "SELECT * FROM Campaigns ORDER BY CreatedAt DESC";

            using var cmd = new SQLiteCommand(sql, connection);
            using var reader = cmd.ExecuteReader();

            while (reader.Read())
            {
                campaigns.Add(ReadCampaign(reader));
            }

            return campaigns;
        }

        public void UpdateCampaign(Campaign campaign)
        {
            using var connection = new SQLiteConnection(_connectionString);
            connection.Open();

            var sql = @"UPDATE Campaigns SET
                Status = @Status,
                Progress = @Progress,
                EmailsSent = @EmailsSent,
                EmailsDelivered = @EmailsDelivered,
                EmailsBounced = @EmailsBounced,
                EmailsOpened = @EmailsOpened,
                LinksClicked = @LinksClicked,
                UpdatedAt = @UpdatedAt
                WHERE Id = @Id";

            using var cmd = new SQLiteCommand(sql, connection);
            cmd.Parameters.AddWithValue("@Id", campaign.Id);
            cmd.Parameters.AddWithValue("@Status", campaign.Status);
            cmd.Parameters.AddWithValue("@Progress", campaign.Progress);
            cmd.Parameters.AddWithValue("@EmailsSent", campaign.EmailsSent);
            cmd.Parameters.AddWithValue("@EmailsDelivered", campaign.EmailsDelivered);
            cmd.Parameters.AddWithValue("@EmailsBounced", campaign.EmailsBounced);
            cmd.Parameters.AddWithValue("@EmailsOpened", campaign.EmailsOpened);
            cmd.Parameters.AddWithValue("@LinksClicked", campaign.LinksClicked);
            cmd.Parameters.AddWithValue("@UpdatedAt", DateTime.Now.ToString("o"));

            cmd.ExecuteNonQuery();
        }

        private Campaign ReadCampaign(SQLiteDataReader reader)
        {
            return new Campaign
            {
                Id = reader.GetInt32(0),
                Name = reader.GetString(1),
                Subject = reader.IsDBNull(2) ? "" : reader.GetString(2),
                FromName = reader.IsDBNull(3) ? "" : reader.GetString(3),
                FromEmail = reader.IsDBNull(4) ? "" : reader.GetString(4),
                HtmlContent = reader.IsDBNull(6) ? "" : reader.GetString(6),
                Status = reader.IsDBNull(15) ? "draft" : reader.GetString(15),
                Progress = reader.IsDBNull(16) ? 0 : reader.GetInt32(16),
                EmailsSent = reader.IsDBNull(18) ? 0 : reader.GetInt32(18),
                EmailsDelivered = reader.IsDBNull(19) ? 0 : reader.GetInt32(19)
            };
        }

        #endregion

        #region SMTP Configs

        public void AddSmtpConfig(SmtpConfig config)
        {
            using var connection = new SQLiteConnection(_connectionString);
            connection.Open();

            var sql = @"INSERT INTO SmtpConfigs (
                Name, Host, Port, Username, Password, UseSsl,
                IsDefault, IsActive, CreatedAt
            ) VALUES (
                @Name, @Host, @Port, @Username, @Password, @UseSsl,
                @IsDefault, @IsActive, @CreatedAt
            )";

            using var cmd = new SQLiteCommand(sql, connection);
            cmd.Parameters.AddWithValue("@Name", config.Name);
            cmd.Parameters.AddWithValue("@Host", config.Host);
            cmd.Parameters.AddWithValue("@Port", config.Port);
            cmd.Parameters.AddWithValue("@Username", config.Username);
            cmd.Parameters.AddWithValue("@Password", config.Password);
            cmd.Parameters.AddWithValue("@UseSsl", config.UseSsl ? 1 : 0);
            cmd.Parameters.AddWithValue("@IsDefault", config.IsDefault ? 1 : 0);
            cmd.Parameters.AddWithValue("@IsActive", config.IsActive ? 1 : 0);
            cmd.Parameters.AddWithValue("@CreatedAt", DateTime.Now.ToString("o"));

            cmd.ExecuteNonQuery();
        }

        public List<SmtpConfig> GetAllSmtpConfigs()
        {
            var configs = new List<SmtpConfig>();

            using var connection = new SQLiteConnection(_connectionString);
            connection.Open();

            var sql = "SELECT * FROM SmtpConfigs WHERE IsActive = 1";

            using var cmd = new SQLiteCommand(sql, connection);
            using var reader = cmd.ExecuteReader();

            while (reader.Read())
            {
                configs.Add(new SmtpConfig
                {
                    Id = reader.GetInt32(0),
                    Name = reader.GetString(1),
                    Host = reader.GetString(2),
                    Port = reader.GetInt32(3),
                    Username = reader.IsDBNull(4) ? "" : reader.GetString(4),
                    Password = reader.IsDBNull(5) ? "" : reader.GetString(5),
                    UseSsl = reader.GetInt32(6) == 1,
                    IsDefault = reader.GetInt32(7) == 1,
                    IsActive = reader.GetInt32(8) == 1
                });
            }

            return configs;
        }

        #endregion

        #region Statistics

        public Dictionary<string, int> GetStatistics()
        {
            var stats = new Dictionary<string, int>();

            using var connection = new SQLiteConnection(_connectionString);
            connection.Open();

            // Total contacts
            using (var cmd = new SQLiteCommand("SELECT COUNT(*) FROM Contacts", connection))
            {
                stats["TotalContacts"] = Convert.ToInt32(cmd.ExecuteScalar());
            }

            // Subscribed contacts
            using (var cmd = new SQLiteCommand("SELECT COUNT(*) FROM Contacts WHERE IsSubscribed = 1", connection))
            {
                stats["SubscribedContacts"] = Convert.ToInt32(cmd.ExecuteScalar());
            }

            // Total campaigns
            using (var cmd = new SQLiteCommand("SELECT COUNT(*) FROM Campaigns", connection))
            {
                stats["TotalCampaigns"] = Convert.ToInt32(cmd.ExecuteScalar());
            }

            // Sent campaigns
            using (var cmd = new SQLiteCommand("SELECT COUNT(*) FROM Campaigns WHERE Status = 'sent'", connection))
            {
                stats["SentCampaigns"] = Convert.ToInt32(cmd.ExecuteScalar());
            }

            return stats;
        }

        #endregion
    }
}
