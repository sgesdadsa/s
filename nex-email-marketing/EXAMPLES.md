# 💡 Exemplos Práticos - NEX Email Marketing Pro

## 📝 Casos de Uso Reais e LEGÍTIMOS

---

## Exemplo 1: Newsletter Semanal de Blog

### Cenário
Você tem um blog e quer enviar resumo semanal para assinantes.

### Setup

```csharp
// 1. Criar template de newsletter
var templateService = new TemplateService();

var context = new TemplateContext
{
    Type = TemplateType.Newsletter,
    Title = "Resumo Semanal - Meu Blog",
    Subtitle = "Os melhores artigos da semana",
    CompanyName = "Meu Blog Tech",
    CompanyAddress = "Rua Exemplo, 123 - São Paulo/SP",
    LogoUrl = "https://meublog.com/logo.png",
    PrimaryColor = "#007bff",
    SecondaryColor = "#28a745",
    CallToActionText = "Ver Todos os Artigos",
    CallToActionUrl = "https://meublog.com/artigos",
    Articles = new List<Article>
    {
        new Article
        {
            Title = "10 Dicas de C# que Todo Dev Deveria Saber",
            Content = "Descubra técnicas avançadas de C# que vão otimizar seu código...",
            ImageUrl = "https://meublog.com/images/csharp-tips.jpg",
            ReadMoreUrl = "https://meublog.com/artigos/10-dicas-csharp"
        },
        new Article
        {
            Title = "Introdução ao Design Patterns em .NET",
            Content = "Aprenda os padrões mais utilizados na indústria...",
            ImageUrl = "https://meublog.com/images/design-patterns.jpg",
            ReadMoreUrl = "https://meublog.com/artigos/design-patterns"
        }
    }
};

var htmlTemplate = templateService.GenerateTemplate(context);
```

### Resultado
Email profissional com:
- Header com logo e título
- 2 artigos com imagem e preview
- Link "Leia mais" para cada artigo
- CTA para ver todos os artigos
- Footer com endereço e unsubscribe

---

## Exemplo 2: Promoção de E-commerce

### Cenário
Loja virtual fazendo promoção de 50% para clientes cadastrados.

### Setup

```csharp
var context = new TemplateContext
{
    Type = TemplateType.Promotional,
    Title = "SUPER PROMOÇÃO DE VERÃO!",
    Subtitle = "Aproveite enquanto durar",
    IntroText = "Olá! Preparamos uma oferta especial só para você. " +
                "Todos os produtos com 50% de desconto por 24 horas!",

    CompanyName = "Minha Loja Virtual",
    CompanyAddress = "Av. Paulista, 1000 - São Paulo/SP",

    PrimaryColor = "#ff6b6b",
    SecondaryColor = "#ffd93d",

    DiscountPercentage = "50",
    CouponCode = "VERAO50",
    UrgencyText = "Promoção válida apenas por 24 horas! Não perca!",

    ProductImageUrl = "https://minhaloja.com/images/promo-verao.jpg",

    CallToActionText = "APROVEITAR AGORA",
    CallToActionUrl = "https://minhaloja.com/promo-verao?utm_source=email&utm_campaign=verao50"
};

var htmlTemplate = templateService.GenerateTemplate(context);

// Criar campanha
var campaign = new Campaign
{
    Name = "Promoção Verão 2026",
    Subject = "🌞 50% OFF em TUDO - Só hoje!",
    FromName = "Minha Loja Virtual",
    FromEmail = "promo@minhaloja.com",
    ReplyToEmail = "contato@minhaloja.com",
    HtmlContent = htmlTemplate,

    // Targeting: Apenas clientes que compraram nos últimos 6 meses
    TargetSegment = "clientes_ativos",

    // Rate limiting
    EmailsPerMinute = 30,
    EmailsPerHour = 500,
    DelayBetweenEmails = 2000,

    // Compliance
    IncludeUnsubscribeLink = true,
    IncludePhysicalAddress = true,
    PhysicalAddress = "Av. Paulista, 1000 - São Paulo/SP - CEP 01310-000",

    TrackOpens = true,
    TrackClicks = true
};

// Salvar campanha
var db = new DatabaseService();
int campaignId = db.AddCampaign(campaign);
```

---

## Exemplo 3: Lançamento de Produto

### Cenário
Startup lançando novo app para clientes beta.

### Setup

```csharp
var context = new TemplateContext
{
    Type = TemplateType.Product,
    Title = "Apresentamos: NEX Task Manager",
    IntroText = "Você foi selecionado para testar nosso novo gerenciador de " +
                "tarefas antes do lançamento oficial!",

    CompanyName = "NEX Apps",
    CompanyAddress = "Rua das Startups, 42 - Florianópolis/SC",
    LogoUrl = "https://nexapps.com/logo.png",

    PrimaryColor = "#6c5ce7",
    SecondaryColor = "#00b894",

    ProductImageUrl = "https://nexapps.com/images/task-manager-hero.png",

    Price = "GRÁTIS para Beta Testers",
    OldPrice = "R$ 49,90/mês após lançamento",

    Features = new List<string>
    {
        "Sincronização em tempo real entre dispositivos",
        "Suporte a projetos ilimitados",
        "Colaboração em equipe",
        "Integração com calendário",
        "Notificações inteligentes",
        "Temas personalizáveis"
    },

    CallToActionText = "COMEÇAR TESTE GRÁTIS",
    CallToActionUrl = "https://nexapps.com/beta?invite={{email}}"
};

var htmlTemplate = templateService.GenerateTemplate(context);
```

---

## Exemplo 4: Validação de Lista de Emails

### Cenário
Você recebeu 10.000 emails de formulário no site e quer validar antes de enviar.

### Código

```csharp
var validationService = new EmailValidationService();

// Lista de emails brutos
var emails = new List<string>
{
    "joao@gmail.com",
    "maria@gmial.com",  // typo
    "pedro@empresa.com.br",
    "invalido@dominio-inexistente-xyz123.com",
    "duplicate@test.com",
    "duplicate@test.com",
    "temp@10minutemail.com"  // descartável
};

// Remover duplicatas
emails = validationService.RemoveDuplicates(emails);
Console.WriteLine($"Após remover duplicatas: {emails.Count}");

// Validar cada email
var results = validationService.ValidateBulk(emails, checkDomain: true);

foreach (var result in results)
{
    var validation = result.Value;

    Console.WriteLine($"\nEmail: {result.Key}");
    Console.WriteLine($"Válido: {validation.IsValid}");

    if (validation.HasTypo)
    {
        Console.WriteLine($"⚠️ Possível erro: {validation.SuggestedFix}");
    }

    if (validation.IsDisposable)
    {
        Console.WriteLine("⚠️ Email descartável");
    }

    if (!validation.DomainExists)
    {
        Console.WriteLine("❌ Domínio não existe");
    }

    foreach (var error in validation.Errors)
    {
        Console.WriteLine($"❌ Erro: {error}");
    }
}

// Estatísticas
var stats = validationService.GetValidationStats(emails);
Console.WriteLine($"\n📊 Estatísticas:");
Console.WriteLine($"Total: {stats.Total}");
Console.WriteLine($"Válidos: {stats.Valid} ({stats.ValidPercentage:F1}%)");
Console.WriteLine($"Inválidos: {stats.Invalid}");
Console.WriteLine($"Descartáveis: {stats.Disposable}");
Console.WriteLine($"Com typos: {stats.WithTypos}");

// Filtrar apenas válidos
var validEmails = emails.Where(e =>
{
    var result = validationService.ValidateEmail(e);
    return result.IsValid && !result.IsDisposable;
}).ToList();

Console.WriteLine($"\n✅ Emails válidos finais: {validEmails.Count}");
```

---

## Exemplo 5: Segmentação Avançada

### Cenário
Enviar emails diferentes baseado em comportamento do usuário.

### Código

```csharp
var db = new DatabaseService();

// Segmento 1: Clientes VIP (compraram > R$ 1000 nos últimos 30 dias)
var vipContacts = db.GetAllContacts()
    .Where(c => c.IsSubscribed &&
                c.Tags.Contains("vip") &&
                c.GetEngagementRate() > 50)
    .ToList();

// Segmento 2: Inativos (não abriram emails há 90 dias)
var inactiveContacts = db.GetAllContacts()
    .Where(c => c.IsSubscribed &&
                c.LastOpenedAt != null &&
                (DateTime.Now - c.LastOpenedAt.Value).TotalDays > 90)
    .ToList();

// Segmento 3: Novos (cadastrados há menos de 7 dias)
var newContacts = db.GetAllContacts()
    .Where(c => c.IsSubscribed &&
                (DateTime.Now - c.SubscribedAt).TotalDays <= 7)
    .ToList();

// Campanha 1: VIPs - Desconto exclusivo 70%
var campaignVip = new Campaign
{
    Name = "VIP - Desconto Exclusivo 70%",
    Subject = "{{name}}, oferta VIP só para você!",
    TargetSegment = "vip",
    // ... configurar template premium
};

// Campanha 2: Inativos - Reengajamento
var campaignReengagement = new Campaign
{
    Name = "Reengajamento - Sentimos sua falta",
    Subject = "Sentimos sua falta, {{name}}! Volte e ganhe 20% OFF",
    TargetSegment = "inactive",
    // ... configurar template reengajamento
};

// Campanha 3: Novos - Welcome Series
var campaignWelcome = new Campaign
{
    Name = "Boas-vindas - Novos Clientes",
    Subject = "Bem-vindo, {{name}}! Aqui está seu guia de início",
    TargetSegment = "new",
    // ... configurar template welcome
};

// Enviar cada campanha para seu segmento
var emailService = new EmailSendingService();
var smtpConfig = db.GetAllSmtpConfigs().First(c => c.IsDefault);

await emailService.SendCampaignAsync(campaignVip, vipContacts,
    smtpConfig, vipTemplate);
```

---

## Exemplo 6: A/B Testing de Subject Lines

### Cenário
Testar qual subject line tem melhor taxa de abertura.

### Código

```csharp
var contacts = db.GetSubscribedContacts();

// Dividir lista em 2 grupos aleatórios
var random = new Random();
var shuffled = contacts.OrderBy(c => random.Next()).ToList();

var groupA = shuffled.Take(shuffled.Count / 2).ToList();
var groupB = shuffled.Skip(shuffled.Count / 2).ToList();

// Variante A: Subject line direto
var campaignA = new Campaign
{
    Name = "A/B Test - Variante A",
    Subject = "Promoção de 50% em todos os produtos",
    // ... mesmo conteúdo para ambos
};

// Variante B: Subject line com curiosidade
var campaignB = new Campaign
{
    Name = "A/B Test - Variante B",
    Subject = "Você não vai acreditar nesta oferta...",
    // ... mesmo conteúdo
};

// Enviar
await emailService.SendCampaignAsync(campaignA, groupA, smtpConfig, template);
await emailService.SendCampaignAsync(campaignB, groupB, smtpConfig, template);

// Após 24h, comparar resultados
Console.WriteLine($"Variante A:");
Console.WriteLine($"  Enviados: {campaignA.EmailsSent}");
Console.WriteLine($"  Aberturas: {campaignA.EmailsOpened}");
Console.WriteLine($"  Taxa: {campaignA.GetOpenRate():F2}%");

Console.WriteLine($"\nVariante B:");
Console.WriteLine($"  Enviados: {campaignB.EmailsSent}");
Console.WriteLine($"  Aberturas: {campaignB.EmailsOpened}");
Console.WriteLine($"  Taxa: {campaignB.GetOpenRate():F2}%");

// Usar o vencedor para resto da lista
```

---

## Exemplo 7: Automação de Boas-Vindas (Welcome Email)

### Cenário
Enviar série de 3 emails automaticamente quando alguém se cadastra.

### Email 1: Imediato (Boas-vindas)

```csharp
var welcomeContext = new TemplateContext
{
    Type = TemplateType.Basic,
    Title = "Bem-vindo à Nossa Comunidade!",
    IntroText = "Estamos muito felizes em ter você conosco! " +
                "Para começar, aqui está um guia rápido de como aproveitar " +
                "ao máximo nossa plataforma.",

    CompanyName = "Minha Plataforma",
    PrimaryColor = "#007bff",

    CallToActionText = "COMPLETAR MEU PERFIL",
    CallToActionUrl = "https://plataforma.com/perfil?new=true"
};
```

### Email 2: +3 dias (Recursos)

```csharp
var resourcesContext = new TemplateContext
{
    Type = TemplateType.Newsletter,
    Title = "Recursos Essenciais para Você",
    IntroText = "Agora que você já está familiarizado, " +
                "conheça recursos avançados que vão turbinar sua produtividade!",

    Articles = new List<Article>
    {
        new Article
        {
            Title = "5 Atalhos que Economizam Horas",
            Content = "Aprenda os atalhos mais úteis..."
        },
        new Article
        {
            Title = "Como Integrar com Outras Ferramentas",
            Content = "Conecte sua conta com Google, Slack..."
        }
    }
};
```

### Email 3: +7 dias (Oferta Especial)

```csharp
var specialOfferContext = new TemplateContext
{
    Type = TemplateType.Promotional,
    Title = "Oferta Especial de Boas-Vindas!",
    IntroText = "Como agradecimento por fazer parte da nossa comunidade, " +
                "aqui está um desconto exclusivo de 30% no upgrade para Premium!",

    DiscountPercentage = "30",
    CouponCode = "WELCOME30",
    UrgencyText = "Válido apenas por 48 horas!",

    CallToActionText = "USAR MEU DESCONTO",
    CallToActionUrl = "https://plataforma.com/upgrade?coupon=WELCOME30"
};
```

---

## Exemplo 8: Recuperação de Carrinho Abandonado

### Cenário
E-commerce enviando email para quem deixou produtos no carrinho.

### Setup

```csharp
// Dados do carrinho (viriam do seu sistema)
var abandonedCart = new
{
    UserEmail = "cliente@example.com",
    UserName = "João Silva",
    Items = new[]
    {
        new { Product = "Tênis Nike Air", Price = 299.90, Image = "url" },
        new { Product = "Camisa Polo", Price = 89.90, Image = "url" }
    },
    Total = 389.80,
    CartUrl = "https://loja.com/carrinho?id=abc123"
};

var template = $@"
<!DOCTYPE html>
<html>
<head><meta charset='UTF-8'></head>
<body style='font-family: Arial;'>
    <h1>Olá {abandonedCart.UserName}!</h1>

    <p>Percebemos que você deixou alguns itens no carrinho:</p>

    <table style='width: 100%; border-collapse: collapse;'>
        {string.Join("", abandonedCart.Items.Select(item => $@"
        <tr style='border-bottom: 1px solid #eee;'>
            <td><img src='{item.Image}' style='width: 80px;'></td>
            <td>{item.Product}</td>
            <td>R$ {item.Price:F2}</td>
        </tr>"))}
        <tr style='font-weight: bold;'>
            <td colspan='2'>Total:</td>
            <td>R$ {abandonedCart.Total:F2}</td>
        </tr>
    </table>

    <p>
        <a href='{abandonedCart.CartUrl}'
           style='background: #28a745; color: white; padding: 15px 40px;
                  text-decoration: none; border-radius: 5px; display: inline-block;'>
            FINALIZAR COMPRA AGORA
        </a>
    </p>

    <p style='color: #dc3545;'>
        <strong>⏰ Atenção!</strong> Seu carrinho expira em 24 horas.
        Finalize agora para garantir esses produtos!
    </p>

    <p style='font-size: 12px; color: #666;'>
        Sua Loja - Endereço Completo
        <br>
        <a href='{{{{unsubscribe}}}}'>Cancelar inscrição</a>
    </p>
</body>
</html>";

var campaign = new Campaign
{
    Name = "Recuperação de Carrinho - João Silva",
    Subject = "João, você esqueceu algo no carrinho! 🛒",
    FromName = "Sua Loja",
    FromEmail = "vendas@sualoja.com",
    HtmlContent = template
};
```

---

## Exemplo 9: Monitoramento em Tempo Real

### Cenário
Acompanhar envio de campanha em tempo real com eventos.

### Código

```csharp
var emailService = new EmailSendingService();

// Subscrever eventos
emailService.EmailSent += (sender, e) =>
{
    Console.WriteLine($"✅ Enviado para {e.Contact.Email} às {e.SentAt:HH:mm:ss}");

    // Atualizar UI ou banco de dados
    e.Contact.EmailsReceived++;
    db.UpdateContact(e.Contact);
};

emailService.EmailFailed += (sender, e) =>
{
    Console.WriteLine($"❌ Falha ao enviar para {e.Contact.Email}");
    Console.WriteLine($"   Erro: {e.ErrorMessage}");

    // Log de erro
    var log = new EmailLog
    {
        CampaignId = e.Campaign.Id,
        ContactId = e.Contact.Id,
        ContactEmail = e.Contact.Email,
        Status = "failed",
        ErrorMessage = e.ErrorMessage,
        CreatedAt = DateTime.Now
    };

    // Salvar log
};

emailService.ProgressUpdated += (sender, e) =>
{
    Console.WriteLine($"📊 Progresso: {e.Progress}% " +
                      $"({e.SentEmails}/{e.TotalEmails})");

    // Atualizar barra de progresso na UI
    campaign.Progress = e.Progress;
    db.UpdateCampaign(campaign);
};

// Enviar campanha
await emailService.SendCampaignAsync(campaign, contacts, smtpConfig, template);

Console.WriteLine("✅ Campanha concluída!");
```

---

## Exemplo 10: Limpeza de Lista (List Hygiene)

### Cenário
Remover contatos inativos e com bounces para manter lista saudável.

### Código

```csharp
var db = new DatabaseService();
var allContacts = db.GetAllContacts();

Console.WriteLine($"📊 Total de contatos: {allContacts.Count}");

// 1. Identificar hard bounces (emails inválidos)
var hardBounces = allContacts
    .Where(c => c.BounceType == "hard")
    .ToList();

Console.WriteLine($"❌ Hard bounces: {hardBounces.Count}");

foreach (var contact in hardBounces)
{
    contact.IsValid = false;
    contact.IsSubscribed = false;
    db.UpdateContact(contact);
    Console.WriteLine($"   Desativado: {contact.Email}");
}

// 2. Identificar inativos (não abriram há 180 dias)
var inactiveThreshold = DateTime.Now.AddDays(-180);
var inactives = allContacts
    .Where(c => c.IsSubscribed &&
                c.EmailsReceived > 5 &&  // Recebeu pelo menos 5 emails
                c.EmailsOpened == 0 &&    // Nunca abriu
                c.SubscribedAt < inactiveThreshold)
    .ToList();

Console.WriteLine($"😴 Inativos (180+ dias): {inactives.Count}");

// Opção 1: Remover automaticamente
foreach (var contact in inactives)
{
    contact.IsSubscribed = false;
    contact.UnsubscribedAt = DateTime.Now;
    contact.UnsubscribeReason = "Inativo por 180 dias";
    db.UpdateContact(contact);
}

// Opção 2: Campanha de reengajamento antes de remover
var reengagementCampaign = new Campaign
{
    Name = "Última Chance - Queremos você de volta!",
    Subject = "{{name}}, ainda quer receber nossos emails?",
    // Template pedindo confirmação
};

// Enviar para inativos
// Se não abrirem em 30 dias, remover

// 3. Remover duplicatas (mesmo email cadastrado 2x)
var emailGroups = allContacts
    .GroupBy(c => c.Email.ToLower())
    .Where(g => g.Count() > 1);

foreach (var group in emailGroups)
{
    Console.WriteLine($"🔄 Duplicata encontrada: {group.Key}");

    // Manter o mais recente, remover os outros
    var toKeep = group.OrderByDescending(c => c.SubscribedAt).First();
    var toRemove = group.Where(c => c.Id != toKeep.Id);

    foreach (var contact in toRemove)
    {
        db.DeleteContact(contact.Id);
        Console.WriteLine($"   Removido duplicata ID: {contact.Id}");
    }
}

// 4. Estatísticas finais
var stats = db.GetStatistics();
Console.WriteLine($"\n📊 Lista limpa:");
Console.WriteLine($"   Total: {stats["TotalContacts"]}");
Console.WriteLine($"   Ativos: {stats["SubscribedContacts"]}");
Console.WriteLine($"   Taxa de qualidade: " +
                  $"{(double)stats["SubscribedContacts"] / stats["TotalContacts"] * 100:F1}%");
```

---

## 🎯 Mais Recursos

Para mais exemplos, consulte:
- **README.md** - Documentação completa
- **QUICK_START.md** - Guia de início rápido
- **Código-fonte** - Comentários detalhados

---

**NEX Email Marketing Pro - Exemplos Práticos de Uso Legítimo**
