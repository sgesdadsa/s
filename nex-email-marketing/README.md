# 📧 NEX Email Marketing Pro

**Sistema profissional de email marketing legítimo em C#**

---

## ⚠️ AVISO LEGAL IMPORTANTE

Este software foi desenvolvido **EXCLUSIVAMENTE** para email marketing **LEGAL E ÉTICO**.

### ✅ USO PERMITIDO:

- Email marketing com opt-in (consentimento)
- Newsletters para assinantes autorizados
- Campanhas promocionais legítimas
- Emails transacionais (confirmações, etc.)
- Comunicação com clientes existentes

### ❌ USO PROIBIDO:

- ❌ **SPAM** (emails não solicitados)
- ❌ Compra/venda de listas de emails
- ❌ Phishing ou fraude
- ❌ Envio sem consentimento
- ❌ Violação de leis anti-spam
- ❌ Qualquer atividade ilegal

**Violações podem resultar em:**
- Processo criminal
- Multas pesadas (até $43.000 por email - CAN-SPAM Act)
- Banimento de provedores
- Prisão (dependendo da gravidade)

---

## 🎯 Características

### ✅ Funcionalidades Profissionais

1. **Validação de Emails**
   - Verificação de formato (RFC 5322)
   - Detecção de typos comuns
   - Verificação de domínio (DNS)
   - Identificação de emails descartáveis
   - Remoção de duplicatas
   - Estatísticas de validação

2. **Templates HTML Automáticos**
   - 5 tipos de templates profissionais
   - Geração automática baseada em contexto
   - Personalização com variáveis
   - Responsivo para mobile
   - Newsletter, Promocional, Produto, Anúncio, Evento

3. **Envio Inteligente**
   - Rate limiting automático (evita bloqueios)
   - Retry logic para falhas temporárias
   - Múltiplos provedores SMTP
   - Delay entre emails configurável
   - Pausar/retomar campanhas

4. **Gestão de Contatos**
   - Importação em massa
   - Segmentação por tags
   - Opt-in/Opt-out tracking
   - Double opt-in suportado
   - Gerenciamento de bounces
   - Estatísticas de engajamento

5. **Campanhas**
   - Criação e agendamento
   - Targeting por segmentos
   - Personalização de conteúdo
   - Estatísticas em tempo real
   - Tracking de aberturas e cliques

6. **Estatísticas e Métricas**
   - Taxa de entrega (Delivery Rate)
   - Taxa de abertura (Open Rate)
   - Taxa de cliques (Click Rate)
   - Taxa de bounce
   - Taxa de unsubscribe
   - ROI de campanhas

7. **Conformidade Legal**
   - Unsubscribe obrigatório
   - Physical address incluído
   - Opt-in tracking
   - Logs de consentimento
   - LGPD/GDPR compliant

---

## 🚀 Como Usar

### 1. Instalação

```bash
# Clone o repositório
cd nex-email-marketing

# Abra no Visual Studio
NEXEmailMarketing.sln

# Build o projeto
dotnet build

# Ou execute diretamente
dotnet run
```

### 2. Configuração Inicial

1. **Configurar SMTP**
   - Vá em "Configurações" > "SMTP"
   - Adicione seu servidor SMTP
   - Recomendados:
     - **Gmail**: smtp.gmail.com:587 (use App Password)
     - **SendGrid**: smtp.sendgrid.net:587
     - **AWS SES**: email-smtp.us-east-1.amazonaws.com:587
     - **Mailgun**: smtp.mailgun.org:587

2. **Importar Contatos**
   - Vá em "Contatos" > "Importar"
   - Use apenas contatos que **autorizaram** receber emails
   - Suporta CSV, TXT (um email por linha)

3. **Criar Template**
   - Vá em "Templates" > "Novo"
   - Escolha tipo (Newsletter, Promocional, etc.)
   - Personalize cores, texto, CTA

4. **Criar Campanha**
   - Vá em "Campanhas" > "Nova"
   - Defina assunto, remetente
   - Escolha template
   - Selecione segmento de contatos
   - Configure rate limiting

5. **Enviar/Agendar**
   - Envie teste primeiro!
   - Revise tudo
   - Clique em "Enviar Campanha"

---

## 📊 Arquitetura do Sistema

```
NEXEmailMarketing/
├── Models/                    # Modelos de dados
│   ├── Contact.cs            # Modelo de contato
│   ├── Campaign.cs           # Modelo de campanha
│   └── EmailTemplate.cs      # Modelo de template
│
├── Services/                  # Lógica de negócio
│   ├── EmailValidationService.cs   # Validação de emails
│   ├── EmailSendingService.cs      # Envio de emails
│   ├── TemplateService.cs          # Geração de templates
│   └── DatabaseService.cs          # Persistência (SQLite)
│
├── Forms/                     # Interface (WinForms)
│   ├── MainForm.cs           # Tela principal
│   ├── ContactsForm.cs       # Gestão de contatos
│   ├── CampaignsForm.cs      # Gestão de campanhas
│   ├── TemplatesForm.cs      # Gestão de templates
│   └── SettingsForm.cs       # Configurações
│
└── Program.cs                 # Entry point
```

---

## 🛡️ Segurança e Privacidade

### Rate Limiting (Anti-Bloqueio)

O sistema implementa rate limiting automático para evitar ser marcado como spammer:

- **30 emails/minuto** (padrão seguro)
- **500 emails/hora** (limite recomendado)
- **2 segundos** entre cada email
- Ajustável por campanha

### Bounce Handling

- Hard bounces: Email removido automaticamente
- Soft bounces: Retry automático (até 3x)
- Contagem de bounces por contato
- Desativação automática após 5 bounces

### Unsubscribe

- Link de unsubscribe em **TODOS** os emails
- Processamento imediato (sem login necessário)
- Registro de motivo de cancelamento
- Respeita lista de supressão

---

## 📈 Boas Práticas

### 1. Construa sua Lista Organicamente

✅ **FAÇA:**
- Formulário de inscrição no seu site
- Double opt-in (confirme por email)
- Ofereça valor em troca (ebook, desconto)
- Deixe claro o que vão receber

❌ **NÃO FAÇA:**
- Comprar listas de emails
- Adicionar pessoas sem permissão
- Usar emails coletados de sites
- Forçar inscrição

### 2. Respeite seu Público

✅ **FAÇA:**
- Envie conteúdo relevante
- Respeite frequência (não diário)
- Segmente seu público
- Permita escolha de frequência

❌ **NÃO FAÇA:**
- Enviar emails demais
- Conteúdo genérico
- Clickbait enganoso
- Ignorar unsubscribes

### 3. Mantenha Boa Reputação

✅ **FAÇA:**
- Warm-up do IP/domínio
- Comece com poucos emails
- Aumente volume gradualmente
- Monitore métricas

❌ **NÃO FAÇA:**
- Enviar 10.000 emails de uma vez
- Ignorar bounces
- Usar palavras de spam (GRÁTIS!!!)
- Subject lines enganosos

### 4. Conformidade Legal

✅ **OBRIGATÓRIO:**
- Nome e endereço físico no rodapé
- Link de unsubscribe funcional
- Processar unsubscribes em 10 dias (CAN-SPAM)
- Consentimento documentado (LGPD)
- Não enviar após unsubscribe

---

## 🔧 Configurações Recomendadas

### Para Iniciantes (Lista < 1.000)

```
Emails por minuto: 20
Emails por hora: 300
Delay entre emails: 3000ms (3 segundos)
Provedor: Gmail (com App Password)
```

### Para Intermediário (Lista 1.000-10.000)

```
Emails por minuto: 30
Emails por hora: 500
Delay entre emails: 2000ms (2 segundos)
Provedor: SendGrid ou Mailgun
Warm-up: 7 dias
```

### Para Avançado (Lista > 10.000)

```
Emails por minuto: 50-100
Emails por hora: 1000-2000
Delay entre emails: 1000ms (1 segundo)
Provedor: AWS SES ou SendGrid Pro
Warm-up: 14 dias
IP dedicado recomendado
```

---

## 📧 Provedores SMTP Recomendados

### 1. **Gmail** (Gratuito - Pequeno Volume)
- **Limite:** 500/dia
- **Configuração:**
  - Host: smtp.gmail.com
  - Port: 587
  - SSL: Sim
  - Senha: Use App Password (não senha normal)
- **Bom para:** Testes, listas pequenas < 500

### 2. **SendGrid** (Freemium)
- **Limite:** 100/dia grátis, planos pagos a partir de $15/mês
- **Configuração:**
  - Host: smtp.sendgrid.net
  - Port: 587
  - User: apikey
  - Pass: Sua API Key
- **Bom para:** Pequeno/médio porte

### 3. **AWS SES** (Pay-as-you-go)
- **Preço:** $0.10 por 1.000 emails
- **Configuração:**
  - Host: email-smtp.us-east-1.amazonaws.com
  - Port: 587
  - User: SMTP User (do console)
  - Pass: SMTP Password
- **Bom para:** Grande volume, custo-benefício

### 4. **Mailgun** (Freemium)
- **Limite:** 5.000/mês grátis primeiro mês
- **Configuração:**
  - Host: smtp.mailgun.org
  - Port: 587
- **Bom para:** Desenvolvedores, APIs

---

## 📝 Variáveis Disponíveis em Templates

Use estas variáveis nos seus templates HTML:

```html
{{name}}         - Nome do contato
{{email}}        - Email do contato
{{company}}      - Empresa do contato
{{phone}}        - Telefone
{{custom1}}      - Campo customizado 1
{{custom2}}      - Campo customizado 2
{{custom3}}      - Campo customizado 3
{{year}}         - Ano atual
{{date}}         - Data atual
{{unsubscribe}}  - Link de cancelamento (OBRIGATÓRIO)
```

### Exemplo:

```html
<p>Olá {{name}},</p>

<p>Estamos felizes em ter você como cliente da {{company}}!</p>

<p>
  <a href="{{unsubscribe}}">Cancelar inscrição</a>
</p>

<p>© {{year}} Minha Empresa</p>
```

---

## 🎨 Tipos de Templates

### 1. Newsletter
- Layout limpo e organizado
- Múltiplos artigos
- Imagens e textos
- Links para blog

### 2. Promocional
- Design chamativo
- Badge de desconto
- Senso de urgência
- CTA grande

### 3. Produto
- Foco no produto
- Imagem destaque
- Lista de características
- Preço e CTA

### 4. Anúncio
- Simples e direto
- Uma mensagem principal
- CTA claro

### 5. Evento
- Data e local em destaque
- Agenda do evento
- Botão de inscrição

---

## 📊 Métricas Importantes

### Taxa de Entrega (> 95% é bom)
```
Delivery Rate = (Enviados - Bounces) / Enviados * 100
```

### Taxa de Abertura (15-25% é bom)
```
Open Rate = Aberturas / Entregues * 100
```

### Taxa de Cliques (2-5% é bom)
```
Click Rate = Cliques / Entregues * 100
```

### Taxa de Unsubscribe (< 0.5% é bom)
```
Unsubscribe Rate = Cancelamentos / Entregues * 100
```

---

## 🚨 Solução de Problemas

### Emails indo para SPAM

**Causas comuns:**
- Falta de autenticação SPF/DKIM
- Conteúdo com muitos links
- Palavras de spam no assunto
- Alta taxa de bounce
- Muitas reclamações de spam

**Soluções:**
- Configure SPF e DKIM no seu domínio
- Use domínio próprio (não Gmail/Hotmail)
- Evite CAPSLOCK e !!! no assunto
- Limpe sua lista (remova inativos)
- Warm-up gradual

### Alta Taxa de Bounce

**Causas:**
- Lista desatualizada
- Emails inválidos
- Typos nos emails

**Soluções:**
- Use a validação de emails do sistema
- Remova hard bounces automaticamente
- Double opt-in para novos contatos
- Limpe lista regularmente (6 meses)

### Bloqueio de Provedor

**Causas:**
- Enviou muito rápido (rate limit)
- Muitas reclamações de spam
- IP/domínio com má reputação

**Soluções:**
- Reduza rate limiting
- Pause campanha por 24h
- Entre em contato com provedor
- Considere IP dedicado

---

## 🔒 Conformidade com Leis

### CAN-SPAM Act (EUA)

✅ **Obrigatório:**
- Endereço físico no rodapé
- Subject line honesto (não enganoso)
- Link de opt-out funcional
- Processar opt-out em 10 dias
- Identificar como publicidade

### LGPD (Brasil)

✅ **Obrigatório:**
- Consentimento explícito
- Finalidade clara da coleta
- Direito de acesso aos dados
- Direito de exclusão
- Segurança dos dados

### GDPR (Europa)

✅ **Obrigatório:**
- Consentimento inequívoco
- Direito ao esquecimento
- Portabilidade de dados
- Notificação de vazamentos
- DPO se aplicável

---

## 💡 Dicas de Marketing

### Melhore Taxa de Abertura

1. **Subject Line:**
   - Curto (< 50 caracteres)
   - Crie curiosidade
   - Personalize com nome
   - Teste A/B

2. **Sender Name:**
   - Use nome real (não "noreply")
   - Consistente (sempre o mesmo)
   - Reconhecível

3. **Timing:**
   - Terça a Quinta são melhores
   - 10h-11h ou 14h-15h
   - Evite fins de semana
   - Teste para seu público

### Melhore Taxa de Cliques

1. **CTA (Call-to-Action):**
   - Botão visível e grande
   - Texto acionável ("Baixe agora", não "Clique aqui")
   - Cor contrastante
   - Um CTA principal

2. **Conteúdo:**
   - Relevante e valioso
   - Escanável (bullets, títulos)
   - Imagens otimizadas
   - Mobile-friendly

3. **Segmentação:**
   - Envie para quem interessa
   - Personalize conteúdo
   - Histórico de compras
   - Comportamento

### Reduza Unsubscribes

1. **Frequência:**
   - Não envie demais
   - Dê opção de frequência
   - Semanal ou quinzenal ideal

2. **Valor:**
   - Sempre agregue valor
   - Não só promoções
   - Conteúdo educacional
   - Exclusividades

3. **Expectativa:**
   - Cumpra o prometido no opt-in
   - Seja consistente
   - Transparente

---

## 🛠️ Desenvolvimento

### Tecnologias Utilizadas

- **C# .NET 6.0**
- **Windows Forms** (Interface)
- **SQLite** (Banco de dados)
- **MailKit** (Envio SMTP)
- **MimeKit** (Formatação de emails)
- **HtmlAgilityPack** (Parse HTML)

### Estrutura de Dados

**Banco de dados:** `nex_email_marketing.db` (SQLite)

**Tabelas:**
- `Contacts` - Contatos e opt-ins
- `Campaigns` - Campanhas de email
- `EmailTemplates` - Templates HTML
- `SmtpConfigs` - Configurações SMTP
- `EmailLogs` - Logs de envio

---

## 📄 Licença

© 2026 NEX Platform

**Uso permitido apenas para marketing legítimo e ético.**

Este software não pode ser usado para:
- Spam
- Phishing
- Fraude
- Qualquer atividade ilegal

---

## 🙏 Suporte

- 📧 Email: support@nexplatform.com
- 📖 Documentação: Incluída no projeto
- 🐛 Issues: Reporte bugs via GitHub Issues

---

## ⚖️ Disclaimer Final

**IMPORTANTE: LEIA COM ATENÇÃO**

O NEX Email Marketing Pro é uma ferramenta **PROFISSIONAL** para email marketing **LEGÍTIMO**.

**VOCÊ É RESPONSÁVEL POR:**
- Obter consentimento de todos os destinatários
- Cumprir leis anti-spam (CAN-SPAM, LGPD, GDPR)
- Incluir opt-out em todos os emails
- Usar apenas para fins legais e éticos

**NÃO NOS RESPONSABILIZAMOS POR:**
- Uso ilegal ou antiético da ferramenta
- Violações de leis anti-spam
- Multas ou processos resultantes de mau uso
- Banimento de provedores de email
- Qualquer dano causado pelo uso inadequado

**AO USAR ESTE SOFTWARE, VOCÊ CONCORDA EM:**
- Usar apenas para email marketing legítimo
- Respeitar todas as leis aplicáveis
- Não enviar spam ou emails não solicitados
- Assumir total responsabilidade pelo uso

---

**📧 Use com responsabilidade. Respeite seu público. Seja legal e ético. 🛡️**

---

**© 2026 NEX Platform - Email Marketing Legítimo**
