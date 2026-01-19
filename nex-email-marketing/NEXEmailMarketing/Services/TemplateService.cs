using System;
using System.Collections.Generic;
using System.Text;
using NEXEmailMarketing.Models;

namespace NEXEmailMarketing.Services
{
    /// <summary>
    /// Serviço de geração e gerenciamento de templates HTML para emails
    /// </summary>
    public class TemplateService
    {
        /// <summary>
        /// Gera template HTML profissional baseado em contexto
        /// </summary>
        public string GenerateTemplate(TemplateContext context)
        {
            return context.Type switch
            {
                TemplateType.Newsletter => GenerateNewsletterTemplate(context),
                TemplateType.Promotional => GeneratePromotionalTemplate(context),
                TemplateType.Product => GenerateProductTemplate(context),
                TemplateType.Announcement => GenerateAnnouncementTemplate(context),
                TemplateType.Event => GenerateEventTemplate(context),
                _ => GenerateBasicTemplate(context)
            };
        }

        /// <summary>
        /// Template de Newsletter
        /// </summary>
        private string GenerateNewsletterTemplate(TemplateContext context)
        {
            return $@"
<!DOCTYPE html>
<html lang='pt-BR'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>{context.Title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
        }}
        .header {{
            background-color: {context.PrimaryColor};
            color: white;
            padding: 40px 20px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 28px;
        }}
        .content {{
            padding: 40px 20px;
        }}
        .article {{
            margin-bottom: 30px;
            border-bottom: 1px solid #eee;
            padding-bottom: 20px;
        }}
        .article h2 {{
            color: {context.PrimaryColor};
            font-size: 22px;
        }}
        .article p {{
            line-height: 1.6;
            color: #333;
        }}
        .button {{
            display: inline-block;
            background-color: {context.SecondaryColor};
            color: white;
            padding: 12px 30px;
            text-decoration: none;
            border-radius: 5px;
            margin: 10px 0;
        }}
        .footer {{
            background-color: #333;
            color: white;
            padding: 20px;
            text-align: center;
            font-size: 12px;
        }}
        .footer a {{
            color: {context.PrimaryColor};
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <div class='container'>
        <!-- Header -->
        <div class='header'>
            {(string.IsNullOrEmpty(context.LogoUrl) ? "" : $"<img src='{context.LogoUrl}' alt='Logo' style='max-width: 150px; margin-bottom: 20px;'>")}
            <h1>{context.Title}</h1>
            <p>{context.Subtitle}</p>
        </div>

        <!-- Content -->
        <div class='content'>
            <p>Olá {{{{name}}}},</p>

            <p>{context.IntroText}</p>

            <!-- Articles -->
            {GenerateArticles(context.Articles)}

            <!-- Call to Action -->
            {(string.IsNullOrEmpty(context.CallToActionText) ? "" : $@"
            <div style='text-align: center; margin: 30px 0;'>
                <a href='{context.CallToActionUrl}' class='button'>{context.CallToActionText}</a>
            </div>")}
        </div>

        <!-- Footer -->
        <div class='footer'>
            <p>{context.CompanyName}</p>
            <p>{context.CompanyAddress}</p>
            <p>
                <a href='{{{{unsubscribe}}}}'>Cancelar inscrição</a>
            </p>
            <p>&copy; {{{{year}}}} {context.CompanyName}. Todos os direitos reservados.</p>
        </div>
    </div>
</body>
</html>";
        }

        /// <summary>
        /// Template Promocional
        /// </summary>
        private string GeneratePromotionalTemplate(TemplateContext context)
        {
            return $@"
<!DOCTYPE html>
<html lang='pt-BR'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>{context.Title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, {context.PrimaryColor} 0%, {context.SecondaryColor} 100%);
        }}
        .container {{
            max-width: 600px;
            margin: 20px auto;
            background-color: #ffffff;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 20px rgba(0,0,0,0.2);
        }}
        .header {{
            background-color: {context.PrimaryColor};
            color: white;
            padding: 60px 20px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 36px;
            font-weight: bold;
        }}
        .discount-badge {{
            background-color: {context.SecondaryColor};
            color: white;
            font-size: 48px;
            font-weight: bold;
            padding: 30px;
            margin: 20px 0;
            border-radius: 50%;
            display: inline-block;
            width: 120px;
            height: 120px;
            line-height: 120px;
        }}
        .content {{
            padding: 40px 20px;
            text-align: center;
        }}
        .content h2 {{
            color: {context.PrimaryColor};
            font-size: 28px;
        }}
        .content p {{
            font-size: 18px;
            line-height: 1.6;
            color: #555;
        }}
        .cta-button {{
            display: inline-block;
            background-color: {context.SecondaryColor};
            color: white;
            padding: 20px 50px;
            text-decoration: none;
            border-radius: 50px;
            font-size: 20px;
            font-weight: bold;
            margin: 30px 0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }}
        .urgency {{
            background-color: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 15px;
            margin: 20px 0;
            text-align: left;
        }}
        .footer {{
            background-color: #f8f9fa;
            padding: 20px;
            text-align: center;
            font-size: 12px;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class='container'>
        <!-- Header -->
        <div class='header'>
            <h1>{context.Title}</h1>
            {(string.IsNullOrEmpty(context.DiscountPercentage) ? "" : $@"
            <div class='discount-badge'>{context.DiscountPercentage}%</div>
            <p style='font-size: 20px; margin: 10px 0;'>DE DESCONTO</p>")}
        </div>

        <!-- Content -->
        <div class='content'>
            <p>Olá {{{{name}}}},</p>

            <h2>{context.Subtitle}</h2>

            <p>{context.IntroText}</p>

            {(string.IsNullOrEmpty(context.ProductImageUrl) ? "" : $@"
            <img src='{context.ProductImageUrl}' alt='Produto' style='max-width: 100%; height: auto; margin: 20px 0;'>")}

            <!-- Urgency -->
            {(string.IsNullOrEmpty(context.UrgencyText) ? "" : $@"
            <div class='urgency'>
                <strong>⏰ Atenção!</strong> {context.UrgencyText}
            </div>")}

            <!-- CTA -->
            <a href='{context.CallToActionUrl}' class='cta-button'>{context.CallToActionText}</a>

            <p style='color: #999; font-size: 14px;'>
                Use o cupom: <strong style='color: {context.PrimaryColor};'>{context.CouponCode}</strong>
            </p>
        </div>

        <!-- Footer -->
        <div class='footer'>
            <p>{context.CompanyName} | {context.CompanyAddress}</p>
            <p><a href='{{{{unsubscribe}}}}' style='color: #666;'>Cancelar inscrição</a></p>
        </div>
    </div>
</body>
</html>";
        }

        /// <summary>
        /// Template de Produto
        /// </summary>
        private string GenerateProductTemplate(TemplateContext context)
        {
            return $@"
<!DOCTYPE html>
<html lang='pt-BR'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>{context.Title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: 'Helvetica Neue', Arial, sans-serif;
            background-color: #f9f9f9;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
        }}
        .header {{
            background-color: #ffffff;
            padding: 20px;
            border-bottom: 3px solid {context.PrimaryColor};
        }}
        .product-showcase {{
            padding: 40px 20px;
            text-align: center;
        }}
        .product-image {{
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 3px 15px rgba(0,0,0,0.1);
        }}
        .product-title {{
            font-size: 32px;
            color: {context.PrimaryColor};
            margin: 20px 0;
        }}
        .product-description {{
            font-size: 16px;
            line-height: 1.8;
            color: #555;
            text-align: left;
            padding: 0 20px;
        }}
        .price {{
            font-size: 36px;
            color: {context.SecondaryColor};
            font-weight: bold;
            margin: 20px 0;
        }}
        .old-price {{
            font-size: 20px;
            color: #999;
            text-decoration: line-through;
            margin-right: 10px;
        }}
        .features {{
            text-align: left;
            padding: 20px;
            background-color: #f8f9fa;
            margin: 20px;
            border-radius: 10px;
        }}
        .features ul {{
            list-style: none;
            padding: 0;
        }}
        .features li {{
            padding: 10px 0;
            border-bottom: 1px solid #eee;
        }}
        .features li:before {{
            content: '✓';
            color: {context.PrimaryColor};
            font-weight: bold;
            margin-right: 10px;
        }}
        .buy-button {{
            display: inline-block;
            background-color: {context.SecondaryColor};
            color: white;
            padding: 18px 60px;
            text-decoration: none;
            border-radius: 5px;
            font-size: 18px;
            font-weight: bold;
            margin: 30px 0;
        }}
        .footer {{
            background-color: #333;
            color: white;
            padding: 20px;
            text-align: center;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class='container'>
        <!-- Header -->
        <div class='header'>
            {(string.IsNullOrEmpty(context.LogoUrl) ? "" : $"<img src='{context.LogoUrl}' alt='Logo' style='max-height: 50px;'>")}
        </div>

        <!-- Product Showcase -->
        <div class='product-showcase'>
            {(string.IsNullOrEmpty(context.ProductImageUrl) ? "" : $@"
            <img src='{context.ProductImageUrl}' alt='{context.Title}' class='product-image'>")}

            <h1 class='product-title'>{context.Title}</h1>

            <div class='price'>
                {(string.IsNullOrEmpty(context.OldPrice) ? "" : $"<span class='old-price'>{context.OldPrice}</span>")}
                {context.Price}
            </div>

            <div class='product-description'>
                <p>{context.IntroText}</p>
            </div>

            <!-- Features -->
            <div class='features'>
                <h3 style='color: {context.PrimaryColor}; margin-top: 0;'>Características:</h3>
                <ul>
                    {GenerateFeaturesList(context.Features)}
                </ul>
            </div>

            <a href='{context.CallToActionUrl}' class='buy-button'>{context.CallToActionText}</a>

            <p style='color: #999; font-size: 14px; margin-top: 20px;'>
                Frete grátis para todo Brasil • Garantia de 30 dias
            </p>
        </div>

        <!-- Footer -->
        <div class='footer'>
            <p>{context.CompanyName} | {context.CompanyAddress}</p>
            <p><a href='{{{{unsubscribe}}}}' style='color: #fff;'>Cancelar inscrição</a></p>
        </div>
    </div>
</body>
</html>";
        }

        /// <summary>
        /// Template Básico/Genérico
        /// </summary>
        private string GenerateBasicTemplate(TemplateContext context)
        {
            return $@"
<!DOCTYPE html>
<html lang='pt-BR'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>{context.Title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
        }}
        .container {{
            max-width: 600px;
            margin: 20px auto;
            background-color: #ffffff;
            padding: 40px;
        }}
        h1 {{
            color: {context.PrimaryColor};
        }}
        p {{
            line-height: 1.6;
            color: #333;
        }}
        .button {{
            display: inline-block;
            background-color: {context.SecondaryColor};
            color: white;
            padding: 12px 30px;
            text-decoration: none;
            border-radius: 5px;
            margin: 20px 0;
        }}
        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            font-size: 12px;
            color: #666;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class='container'>
        <h1>{context.Title}</h1>

        <p>Olá {{{{name}}}},</p>

        <p>{context.IntroText}</p>

        {(string.IsNullOrEmpty(context.CallToActionText) ? "" : $@"
        <a href='{context.CallToActionUrl}' class='button'>{context.CallToActionText}</a>")}

        <div class='footer'>
            <p>{context.CompanyName}</p>
            <p><a href='{{{{unsubscribe}}}}'>Cancelar inscrição</a></p>
        </div>
    </div>
</body>
</html>";
        }

        /// <summary>
        /// Template de Anúncio
        /// </summary>
        private string GenerateAnnouncementTemplate(TemplateContext context)
        {
            return GenerateBasicTemplate(context);
        }

        /// <summary>
        /// Template de Evento
        /// </summary>
        private string GenerateEventTemplate(TemplateContext context)
        {
            return GenerateNewsletterTemplate(context);
        }

        // Helper methods
        private string GenerateArticles(List<Article>? articles)
        {
            if (articles == null || articles.Count == 0) return string.Empty;

            var sb = new StringBuilder();
            foreach (var article in articles)
            {
                sb.Append($@"
                <div class='article'>
                    <h2>{article.Title}</h2>
                    {(string.IsNullOrEmpty(article.ImageUrl) ? "" : $"<img src='{article.ImageUrl}' alt='{article.Title}' style='max-width: 100%; height: auto; margin: 10px 0;'>")}
                    <p>{article.Content}</p>
                    {(string.IsNullOrEmpty(article.ReadMoreUrl) ? "" : $"<a href='{article.ReadMoreUrl}' style='color: #007bff;'>Leia mais →</a>")}
                </div>");
            }
            return sb.ToString();
        }

        private string GenerateFeaturesList(List<string>? features)
        {
            if (features == null || features.Count == 0) return string.Empty;

            var sb = new StringBuilder();
            foreach (var feature in features)
            {
                sb.Append($"<li>{feature}</li>");
            }
            return sb.ToString();
        }
    }

    // Supporting classes
    public enum TemplateType
    {
        Newsletter,
        Promotional,
        Product,
        Announcement,
        Event,
        Basic
    }

    public class TemplateContext
    {
        public TemplateType Type { get; set; }
        public string Title { get; set; } = string.Empty;
        public string Subtitle { get; set; } = string.Empty;
        public string IntroText { get; set; } = string.Empty;

        // Branding
        public string CompanyName { get; set; } = string.Empty;
        public string CompanyAddress { get; set; } = string.Empty;
        public string LogoUrl { get; set; } = string.Empty;

        // Colors
        public string PrimaryColor { get; set; } = "#007bff";
        public string SecondaryColor { get; set; } = "#28a745";

        // CTA
        public string CallToActionText { get; set; } = string.Empty;
        public string CallToActionUrl { get; set; } = string.Empty;

        // Promotional
        public string DiscountPercentage { get; set; } = string.Empty;
        public string CouponCode { get; set; } = string.Empty;
        public string UrgencyText { get; set; } = string.Empty;

        // Product
        public string ProductImageUrl { get; set; } = string.Empty;
        public string Price { get; set; } = string.Empty;
        public string OldPrice { get; set; } = string.Empty;
        public List<string>? Features { get; set; }

        // Newsletter
        public List<Article>? Articles { get; set; }
    }

    public class Article
    {
        public string Title { get; set; } = string.Empty;
        public string Content { get; set; } = string.Empty;
        public string ImageUrl { get; set; } = string.Empty;
        public string ReadMoreUrl { get; set; } = string.Empty;
    }
}
