# 🚀 Guia Rápido - NEX Email Marketing Pro

## ⚡ Início Rápido em 5 Minutos

### 1️⃣ Aceitar Termos

Ao abrir o programa, **LEIA e ACEITE** os termos de uso:

- ✅ Use apenas para marketing legítimo
- ✅ Tenha consentimento dos destinatários
- ✅ Inclua link de unsubscribe
- ✅ Respeite leis anti-spam

### 2️⃣ Configurar SMTP

**Opção 1: Gmail (Para Testes)**

```
Host: smtp.gmail.com
Port: 587
Email: seu-email@gmail.com
Senha: Use App Password (não senha normal)
SSL: Sim
```

Como criar App Password no Gmail:
1. Vá em Conta Google > Segurança
2. Ative "Verificação em duas etapas"
3. Clique em "Senhas de app"
4. Gere senha para "Email"
5. Use essa senha no NEX

**Opção 2: SendGrid (Recomendado para Produção)**

```
Host: smtp.sendgrid.net
Port: 587
Username: apikey
Password: Sua API Key do SendGrid
SSL: Sim
```

Como obter API Key:
1. Crie conta em sendgrid.com (100 emails/dia grátis)
2. Vá em Settings > API Keys
3. Create API Key > Full Access
4. Copie a key

### 3️⃣ Adicionar Contatos

**IMPORTANTE:** Adicione apenas pessoas que **autorizaram** receber seus emails!

**Método 1: Adicionar Manualmente**
- Clique em "Contatos" > "Novo"
- Preencha email, nome, etc.
- Marque "Opt-in confirmado"

**Método 2: Importar CSV**
- Prepare arquivo CSV:
  ```csv
  email,nome,empresa
  joao@example.com,João Silva,Empresa XYZ
  maria@example.com,Maria Santos,ABC Corp
  ```
- Clique em "Contatos" > "Importar"
- Selecione arquivo
- Mapear colunas
- Importar

### 4️⃣ Criar Template

**Opção 1: Usar Gerador Automático**

1. Clique em "Templates" > "Novo Template Automático"
2. Escolha tipo:
   - **Newsletter** - Para notícias e atualizações
   - **Promocional** - Para ofertas e descontos
   - **Produto** - Para lançamento de produtos
3. Preencha:
   - Título: "Promoção de Verão!"
   - Cores: Primária #007bff, Secundária #28a745
   - Sua empresa, logo, endereço
   - Texto principal
   - Botão (CTA)
4. Clique em "Gerar Template"
5. Visualize e salve

**Opção 2: HTML Personalizado**

Se você sabe HTML:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset='UTF-8'>
    <style>
        body { font-family: Arial; }
        .button {
            background: #007bff;
            color: white;
            padding: 12px 30px;
            text-decoration: none;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>Olá {{name}}!</h1>

    <p>Confira nossa nova promoção!</p>

    <a href="https://seusite.com/promo" class="button">
        Ver Promoção
    </a>

    <hr>
    <p style="font-size: 12px;">
        Sua Empresa - Rua Exemplo, 123
        <br>
        <a href="{{unsubscribe}}">Cancelar inscrição</a>
    </p>
</body>
</html>
```

### 5️⃣ Criar Campanha

1. Clique em "Campanhas" > "Nova Campanha"
2. Preencha:
   - **Nome:** "Promoção Verão 2026"
   - **Assunto:** "🌞 50% OFF em toda loja - Só hoje!"
   - **De:** "Sua Empresa <contato@suaempresa.com>"
   - **Responder para:** "contato@suaempresa.com"
3. Selecione template criado
4. Escolha destinatários:
   - Todos os contatos
   - Ou segmento específico
5. Configure envio:
   - **Emails/minuto:** 20 (seguro para iniciar)
   - **Delay:** 3000ms (3 segundos)
6. Salve campanha

### 6️⃣ Enviar Teste

**SEMPRE envie teste antes da campanha real!**

1. Abra a campanha
2. Clique em "Enviar Teste"
3. Digite seu email pessoal
4. Verifique:
   - ✅ Aparência no desktop
   - ✅ Aparência no mobile
   - ✅ Link de unsubscribe funciona
   - ✅ Botões funcionam
   - ✅ Imagens carregam
   - ✅ Texto correto (sem erros)

### 7️⃣ Enviar Campanha

Se o teste estiver OK:

1. Clique em "Enviar Campanha"
2. Confirme que:
   - ✅ Todos têm opt-in
   - ✅ Link de unsubscribe incluído
   - ✅ Endereço físico incluído
3. Clique em "Confirmar Envio"
4. Acompanhe progresso em tempo real

---

## 📊 Acompanhar Resultados

### Dashboard Principal

Após envio, visualize:

- **Taxa de Entrega:** % de emails que chegaram
- **Taxa de Abertura:** % que abriram o email
- **Taxa de Cliques:** % que clicaram em links
- **Bounces:** Emails que retornaram
- **Unsubscribes:** Cancelamentos

### Interpretar Métricas

**Taxa de Entrega > 95%** ✅ Excelente
- Se menor: Limpe sua lista, remova bounces

**Taxa de Abertura 15-25%** ✅ Bom
- Se menor: Melhore subject line, teste horários

**Taxa de Cliques 2-5%** ✅ Bom
- Se menor: CTA mais claro, conteúdo relevante

**Unsubscribe < 0.5%** ✅ Bom
- Se maior: Revise frequência e relevância

---

## 🎯 Checklist de Envio

Antes de enviar qualquer campanha, verifique:

### Legal ⚖️
- [ ] Todos os contatos deram opt-in
- [ ] Link de unsubscribe incluído e funcional
- [ ] Endereço físico da empresa no rodapé
- [ ] Subject line honesto (não enganoso)
- [ ] Identificado como marketing/publicidade

### Técnico 🔧
- [ ] SMTP configurado corretamente
- [ ] Rate limiting adequado (não muito rápido)
- [ ] Teste enviado e aprovado
- [ ] Template responsivo (mobile-friendly)
- [ ] Imagens hospedadas (URLs válidas)
- [ ] Links funcionando

### Conteúdo 📝
- [ ] Texto sem erros de português
- [ ] CTA claro e visível
- [ ] Relevante para o público
- [ ] Valor agregado (não só venda)
- [ ] Personalização (uso de {{name}})

---

## 💡 Dicas Rápidas

### Para Iniciantes

1. **Comece Pequeno**
   - Envie para 50-100 contatos primeiro
   - Teste diferentes subject lines
   - Aprenda com as métricas

2. **Frequência Ideal**
   - 1x por semana: Newsletters
   - 2-3x por mês: Promoções
   - Nunca diariamente!

3. **Melhor Horário**
   - Terça ou Quinta-feira
   - 10h-11h da manhã
   - Ou 14h-15h da tarde

4. **Subject Line Matador**
   - Curto (< 50 caracteres)
   - Personalizado: "{{name}}, oferta especial!"
   - Crie curiosidade
   - Evite CAPSLOCK e !!!

5. **Limpe sua Lista**
   - A cada 6 meses
   - Remova inativos (não abrem há 6+ meses)
   - Remova bounces hard imediatamente

---

## 🚨 O Que NÃO Fazer

### ❌ NUNCA:

1. **Comprar Lista de Emails**
   - Ilegal na maioria dos países
   - Alta taxa de spam
   - Má reputação instantânea

2. **Adicionar Sem Permissão**
   - Coletar emails de sites
   - Adicionar cartões de visita
   - Emails de eventos sem opt-in

3. **Enganar no Subject**
   - "RE: Sua encomenda" (quando não há)
   - "FW: Urgente" (fake)
   - Clickbait extremo

4. **Ignorar Unsubscribes**
   - É ILEGAL enviar após unsubscribe
   - Multa de até $43.000 por email (EUA)

5. **Enviar Muito Rápido**
   - 10.000 emails em 5 minutos = BAN
   - Use rate limiting sempre

---

## 🛟 Problemas Comuns

### "Emails caindo no SPAM"

**Soluções:**
1. Configure SPF/DKIM no seu domínio
2. Use domínio próprio (não Gmail/Hotmail)
3. Reduza frequência de envio
4. Melhore relevância do conteúdo
5. Remova inativos da lista

### "Taxa de abertura muito baixa"

**Soluções:**
1. Teste diferentes subject lines
2. Envie em horários melhores
3. Segmente seu público
4. Use nome de remetente reconhecível
5. Limpe lista de inativos

### "Muitos bounces"

**Soluções:**
1. Use validação de emails do sistema
2. Remova bounces hard imediatamente
3. Implemente double opt-in
4. Limpe lista regularmente

### "Provedor bloqueou meu IP"

**Soluções:**
1. Pare envios por 24h
2. Entre em contato com provedor
3. Reduza rate limiting pela metade
4. Verifique se não há reclamações de spam
5. Considere warm-up do IP novo

---

## 📞 Suporte

- 📖 **Documentação Completa:** Veja README.md
- 🐛 **Bugs:** Reporte via GitHub Issues
- 💬 **Dúvidas:** Consulte FAQ no README

---

## ✅ Pronto para Começar!

Agora você tem tudo para:
1. Configurar seu SMTP
2. Adicionar contatos (COM opt-in!)
3. Criar templates profissionais
4. Enviar campanhas legítimas
5. Analisar resultados

**Lembre-se: Use com responsabilidade! 🛡️**

**Email marketing funciona quando:**
- ✅ Você tem permissão
- ✅ Conteúdo é relevante
- ✅ Frequência é adequada
- ✅ Você respeita seu público

**Boa sorte com suas campanhas! 🚀📧**

---

**NEX Email Marketing Pro - Marketing Legítimo e Profissional**
