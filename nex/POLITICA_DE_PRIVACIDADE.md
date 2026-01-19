# 🔒 POLÍTICA DE PRIVACIDADE E ANONIMATO - NEX PLATFORM

**Versão 1.0 - Última atualização: 19 de Janeiro de 2026**

---

## 🛡️ COMPROMISSO COM SUA PRIVACIDADE

O **NEX Platform** foi desenvolvido com **PRIVACIDADE E ANONIMATO** como prioridade máxima. Esta política descreve como seus dados são tratados, armazenados e protegidos.

---

## 1. PRINCÍPIOS FUNDAMENTAIS

### 1.1. Privacidade por Design

O NEX Platform segue os princípios de **Privacy by Design**:

✅ **ZERO RASTREAMENTO**
- Não rastreamos suas atividades
- Não coletamos dados de uso
- Não enviamos telemetria
- Não usamos analytics externos

✅ **PROCESSAMENTO LOCAL**
- Todos os dados são processados localmente em sua máquina
- Nenhum dado pessoal é enviado para servidores externos
- Você mantém controle total sobre seus dados

✅ **ANONIMATO GARANTIDO**
- Não exigimos informações pessoais identificáveis
- Não criamos perfis de usuário
- Não compartilhamos dados com terceiros
- Não vendemos informações

✅ **TRANSPARÊNCIA TOTAL**
- Código aberto disponível para auditoria
- Documentação clara sobre funcionamento
- Sem práticas obscuras ou ocultas

---

## 2. DADOS COLETADOS E ARMAZENAMENTO

### 2.1. Dados Armazenados LOCALMENTE

O NEX Platform armazena os seguintes dados **APENAS EM SUA MÁQUINA**:

#### 2.1.1. Dados de Configuração
- Configurações do sistema (porta, idioma, tema)
- Preferências de IDE (editor, compilador)
- Modelos de IA configurados (local ou API)
- **LOCALIZAÇÃO:** `/nex/backend/.env` e `/nex/config/`

#### 2.1.2. Dados de Projetos
- Código-fonte de seus projetos
- Arquivos compilados (.exe, .jar, etc.)
- Histórico de builds
- Configurações de projeto (.sln, .csproj, etc.)
- **LOCALIZAÇÃO:** `/nex/projects/`

#### 2.1.3. Dados de IA e Memória
- Histórico de conversas com AI Agent
- Embeddings vetoriais (ChromaDB)
- Contexto e memória do agente
- Melhorias aprendidas
- **LOCALIZAÇÃO:** `/nex/ai_models/` e `/nex/database/vector_db/`

#### 2.1.4. Banco de Dados Local
- Usuários do sistema (locais)
- Projetos e aplicações criadas
- Logs de operações
- Configurações administrativas
- **LOCALIZAÇÃO:** `/nex/backend/nex.db` ou PostgreSQL local

#### 2.1.5. Logs do Sistema
- Logs técnicos de operação
- Registros de erros
- Histórico de builds
- Debug logs
- **LOCALIZAÇÃO:** `/nex/logs/`

### 2.2. Dados NÃO Coletados

❌ **NUNCA COLETAMOS:**
- Nome real, CPF, RG, documentos
- Endereço físico ou localização GPS
- Número de telefone
- Email (exceto se você criar usuário local voluntariamente)
- Dados bancários ou financeiros
- Histórico de navegação na web
- Dados biométricos
- Dados de redes sociais
- Contatos ou lista de amigos
- Informações do dispositivo (hardware ID, serial)
- Endereço IP ou informações de rede
- Dados de outras aplicações instaladas
- Screenshots ou capturas de tela não autorizadas

---

## 3. ANONIMATO E NAVEGAÇÃO

### 3.1. Navegação no NEX Platform

#### 3.1.1. Interface Web (localhost:8000)
- ✅ Acesso **100% LOCAL** via http://localhost:8000
- ✅ Nenhuma conexão externa é feita automaticamente
- ✅ Cookies são usados **APENAS** para sessão local
- ✅ Nenhum cookie de rastreamento de terceiros
- ✅ Sem analytics (Google Analytics, etc.)
- ✅ Sem pixel tracking
- ✅ Sem fingerprinting

#### 3.1.2. Pesquisas e Busca de Código
- Toda pesquisa é feita **LOCALMENTE** no seu código
- Nenhuma query de busca é enviada externamente
- Histórico de pesquisa armazenado apenas localmente
- Você pode limpar histórico a qualquer momento

#### 3.1.3. WebSocket Real-Time
- Comunicação **APENAS LOCAL** (localhost)
- Mensagens não são roteadas externamente
- Criptografia opcional para comunicação local
- Você pode desabilitar WebSocket se preferir

### 3.2. Proteção de Identidade

#### 3.2.1. Usuário Anônimo
Você pode usar o NEX Platform **SEM CRIAR CONTA**:
- Acesso direto após instalação
- Sem necessidade de registro
- Sem email ou verificação
- Modo "guest" totalmente funcional

#### 3.2.2. Usuários Locais
Se criar usuário local (opcional):
- Dados armazenados **APENAS LOCALMENTE**
- Senha criptografada (bcrypt hash)
- Você escolhe username (não precisa ser nome real)
- Email opcional (pode usar fictício para testes)

### 3.3. Recomendações de Anonimato

Para **MÁXIMO ANONIMATO**, recomendamos:

🔒 **Nível 1 - Básico**
- Use usuário local sem email real
- Limpe logs regularmente
- Não compartilhe projetos com dados pessoais

🔒 **Nível 2 - Avançado**
- Use VPN ao acessar APIs externas
- Criptografe disco/partição onde NEX está instalado
- Use máquina virtual para isolamento
- Desabilite logs do sistema

🔒 **Nível 3 - Máximo**
- Use Tails OS ou Whonix
- Tor Browser para acesso a documentação online
- Não configure APIs de terceiros
- Use apenas modelos LLM locais (offline)
- Criptografia full-disk (BitLocker, LUKS)

---

## 4. APIs E SERVIÇOS EXTERNOS

### 4.1. APIs Configuradas por Você

O NEX Platform **NÃO inclui** APIs externas por padrão. Se você configurar:

#### 4.1.1. OpenAI API (Opcional)
- **Você** fornece sua chave API
- Dados enviados: prompts e código para análise
- **LEIA:** https://openai.com/privacy
- **CONTROLE:** Você pode remover API a qualquer momento

#### 4.1.2. Outras APIs de IA (Opcional)
- Anthropic Claude API
- Google PaLM API
- Hugging Face API
- **RESPONSABILIDADE:** Leia política de privacidade de cada serviço

### 4.2. Modelos LLM Locais (Recomendado)

Para **PRIVACIDADE TOTAL**, use modelos locais:
- ✅ **Llama**, **Mistral**, **Phi**, etc. (GGUF format)
- ✅ Processamento 100% offline
- ✅ Nenhum dado enviado externamente
- ✅ Total controle e privacidade
- ✅ Sem custos de API

### 4.3. Conexões de Rede Monitoráveis

Você pode monitorar todas as conexões:
```bash
# Windows
netstat -ano | findstr :8000

# Linux
ss -tunap | grep :8000
```

O NEX Platform **APENAS** escuta em:
- `localhost:8000` (interface web)
- `localhost:5432` (PostgreSQL - se configurado)
- `localhost:6379` (Redis - se configurado)

**NENHUMA CONEXÃO EXTERNA** é feita sem sua autorização explícita.

---

## 5. SEGURANÇA DE DADOS

### 5.1. Criptografia

#### 5.1.1. Senhas
- Armazenadas com **bcrypt** (hash salt único)
- Nunca armazenamos senhas em texto plano
- Não há como recuperar senha (apenas reset)

#### 5.1.2. Dados Sensíveis
- Chaves API criptografadas em `.env`
- Tokens de sessão com expiração
- Recomendamos criptografia de disco

#### 5.1.3. Comunicação
- HTTPS disponível para produção
- WebSocket pode usar WSS (criptografado)
- Certificados SSL self-signed incluídos

### 5.2. Acesso aos Dados

#### 5.2.1. Controle Total
Você tem **CONTROLE TOTAL**:
- ✅ Acesse todos os arquivos diretamente
- ✅ Exporte dados a qualquer momento
- ✅ Delete dados permanentemente
- ✅ Faça backup quando quiser
- ✅ Migre para outro sistema

#### 5.2.2. Ninguém Mais Tem Acesso
- ❌ Desenvolvedores **NÃO TÊM** acesso aos seus dados
- ❌ Não há backdoors ou acesso remoto
- ❌ Não há "reset de senha" via email
- ❌ Não há sincronização com nuvem

### 5.3. Proteção contra Ameaças

#### 5.3.1. Prevenção de SQL Injection
- Uso de ORM (SQLAlchemy) com queries parametrizadas
- Validação de entrada com Pydantic
- Sanitização de dados

#### 5.3.2. Prevenção de XSS
- Sanitização de HTML
- Content Security Policy (CSP)
- Escape de caracteres especiais

#### 5.3.3. Proteção CSRF
- Tokens CSRF em formulários
- Validação de origem de requisições
- SameSite cookies

---

## 6. DIREITOS DO USUÁRIO (LGPD/GDPR)

### 6.1. Direito de Acesso
✅ **VOCÊ PODE:**
- Acessar todos os seus dados a qualquer momento
- Exportar dados em formato legível
- Verificar o que está armazenado

**COMO:** Acesse diretamente `/nex/backend/nex.db` ou use endpoints da API.

### 6.2. Direito de Retificação
✅ **VOCÊ PODE:**
- Corrigir dados incorretos
- Atualizar informações
- Modificar configurações

**COMO:** Use interface administrativa ou edite arquivos diretamente.

### 6.3. Direito de Exclusão (Right to be Forgotten)
✅ **VOCÊ PODE:**
- Deletar conta de usuário
- Remover projetos
- Limpar histórico e logs
- Desinstalar completamente

**COMO:**
```bash
# Deletar tudo
rm -rf /nex/

# Ou usar interface administrativa
DELETE /api/users/{user_id}
```

### 6.4. Direito de Portabilidade
✅ **VOCÊ PODE:**
- Exportar todos os dados em JSON
- Migrar para outro sistema
- Fazer backup completo

**COMO:**
```bash
# Backup completo
tar -czf nex_backup.tar.gz /nex/
```

### 6.5. Direito de Oposição
✅ **VOCÊ PODE:**
- Desabilitar funcionalidades
- Recusar uso de IA
- Desativar logs
- Usar modo offline

**COMO:** Configure em `/nex/backend/.env`.

---

## 7. LOGS E AUDITORIA

### 7.1. Logs do Sistema

Logs armazenam **APENAS dados técnicos**:
- Timestamp de operações
- Tipo de operação (build, debug, etc.)
- Resultado (sucesso/erro)
- Mensagens de erro técnicas

**NÃO registramos:**
- Conteúdo de código ou arquivos
- Dados pessoais
- Senhas ou tokens
- Conversas privadas

### 7.2. Gerenciamento de Logs

```bash
# Localização
/nex/logs/

# Listar logs
ls -lh /nex/logs/

# Deletar logs
rm -rf /nex/logs/*

# Desabilitar logs (em .env)
ENABLE_LOGGING=False
```

### 7.3. Retenção de Logs

- **Padrão:** Logs mantidos por 30 dias
- **Você controla:** Configure retenção em settings
- **Rotação:** Logs rotacionados automaticamente
- **Limpeza:** Você pode deletar a qualquer momento

---

## 8. COMPARTILHAMENTO DE DADOS

### 8.1. Nunca Compartilhamos

❌ **NUNCA compartilhamos seus dados com:**
- Empresas de publicidade
- Brokers de dados
- Redes sociais
- Governo (exceto ordem judicial)
- Terceiros não autorizados
- Parceiros comerciais
- Analytics providers

### 8.2. Exceções Legais

⚖️ Dados podem ser divulgados **APENAS** se:
- Ordem judicial válida exigir
- Lei aplicável obrigar
- Para proteger direitos e segurança

**NOTA:** Como dados são locais, desenvolvedores **NÃO TÊM ACESSO** para fornecer.

---

## 9. CRIANÇAS E MENORES

### 9.1. Idade Mínima

- ✅ NEX Platform é destinado a usuários **18+ anos**
- ⚠️ Menores de 18 anos precisam autorização de responsável legal
- ❌ Não coletamos intencionalmente dados de menores

### 9.2. Responsabilidade Parental

Se menor de 18 anos usar:
- Pais/responsáveis devem supervisionar uso
- Responsáveis legais aceitam estes termos
- Recomendamos controle parental adicional

---

## 10. APLICAÇÕES CRIADAS POR VOCÊ

### 10.1. Sua Responsabilidade

Se criar aplicações que coletam dados:
- ✅ **VOCÊ DEVE** fornecer sua própria política de privacidade
- ✅ **VOCÊ DEVE** cumprir LGPD, GDPR e outras leis
- ✅ **VOCÊ DEVE** obter consentimento de usuários
- ✅ **VOCÊ DEVE** proteger dados coletados
- ✅ **VOCÊ DEVE** permitir que usuários deletem dados

### 10.2. Não Somos Responsáveis

NEX Platform **NÃO É RESPONSÁVEL** por:
- Políticas de privacidade de suas aplicações
- Dados coletados por software que você criar
- Violações de privacidade por suas apps
- Uso inadequado de dados por terceiros

---

## 11. SEGURANÇA E BOAS PRÁTICAS

### 11.1. Recomendações de Segurança

🔐 **RECOMENDAMOS FORTEMENTE:**

1. **Sistema Operacional**
   - Mantenha SO atualizado
   - Use firewall ativo
   - Instale antivírus/antimalware

2. **Senhas**
   - Use senha forte (12+ caracteres)
   - Não reutilize senhas
   - Use gerenciador de senhas

3. **Rede**
   - Use VPN para privacidade
   - Evite WiFi público para desenvolvimento
   - Configure firewall para bloquear conexões não autorizadas

4. **Backup**
   - Faça backups regulares
   - Armazene backups criptografados
   - Teste restauração periodicamente

5. **Criptografia**
   - Criptografe disco (BitLocker/LUKS)
   - Use HTTPS em produção
   - Proteja chaves API

### 11.2. Incidentes de Segurança

Se detectar violação de segurança:
1. Documente o incidente
2. Relate aos desenvolvedores (se aplicável)
3. Troque senhas e tokens
4. Revogue acesso a APIs comprometidas
5. Restaure de backup limpo

---

## 12. MUDANÇAS NA POLÍTICA

### 12.1. Notificação de Mudanças

Quando esta política for atualizada:
- ✅ Versão e data serão atualizadas no topo
- ✅ Notificação será exibida no sistema
- ✅ Histórico de versões disponível
- ✅ Uso continuado implica aceitação

### 12.2. Seu Controle

Se não concordar com mudanças:
- Você pode parar de usar o NEX Platform
- Você pode exportar seus dados
- Você pode desinstalar o sistema

---

## 13. TRANSPARÊNCIA E AUDITORIA

### 13.1. Código Aberto

O NEX Platform é **open source**:
- ✅ Código-fonte disponível para revisão
- ✅ Você pode auditar funcionalidades
- ✅ Comunidade pode verificar segurança
- ✅ Sem "caixas pretas" ou código oculto

### 13.2. Verificação Independente

Você pode verificar:
```bash
# Ver conexões de rede
netstat -ano | findstr :8000

# Inspecionar banco de dados
sqlite3 /nex/backend/nex.db
.tables
.schema users

# Verificar arquivos
ls -la /nex/
```

---

## 14. CONTATO E DÚVIDAS

Para questões sobre privacidade:
- 📧 Consulte documentação incluída
- 📁 Revise código-fonte
- 💬 Comunidade (quando disponível)
- 🐛 Reporte preocupações de segurança

---

## 15. RESUMO - GARANTIAS DE PRIVACIDADE

### ✅ GARANTIMOS:

| Item | Status | Detalhes |
|------|--------|----------|
| **Zero Rastreamento** | ✅ | Sem analytics, telemetria ou tracking |
| **Processamento Local** | ✅ | Tudo roda na sua máquina |
| **Sem Coleta de Dados** | ✅ | Não coletamos informações pessoais |
| **Anonimato** | ✅ | Você pode usar anonimamente |
| **Sem Compartilhamento** | ✅ | Dados nunca compartilhados |
| **Controle Total** | ✅ | Você gerencia todos os dados |
| **Código Aberto** | ✅ | Auditável e transparente |
| **Criptografia** | ✅ | Senhas e dados sensíveis protegidos |
| **Sem Backdoors** | ✅ | Nenhum acesso remoto oculto |
| **LGPD/GDPR Compliant** | ✅ | Respeita direitos do usuário |

---

## 📌 COMPROMISSO FINAL

**O NEX Platform foi desenvolvido com respeito máximo à sua privacidade.**

- 🔒 Seus dados são **SEUS**
- 🏠 Tudo processado **LOCALMENTE**
- 🙈 Nós **NÃO VEMOS** nada
- 🚫 **ZERO rastreamento**
- 🔐 **Máxima segurança** e anonimato

**Você tem nosso compromisso de privacidade e transparência total.**

---

**© 2026 NEX Platform - Privacidade e Anonimato Garantidos**

**Versão: 1.0**
**Data: 19 de Janeiro de 2026**

---

**🔒 SUA PRIVACIDADE É NOSSA PRIORIDADE 🔒**
