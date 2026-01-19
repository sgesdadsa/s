# 🚀 NEX Platform - Guia de Instalação Completa

## 📦 O Que Você Recebeu

**NEX-Platform.zip** contém:

### 1. **NEX Platform** (C:\nex)
Plataforma completa com:
- ✅ Backend FastAPI com IA Agent
- ✅ WebSocket real-time
- ✅ Banco de dados
- ✅ App Store
- ✅ APK Builder
- ✅ Admin Panel
- ✅ Auto-aprendizado e auto-melhoria
- ✅ Memória persistente
- ✅ Multi-agent system

### 2. **MyLLM Studio** (C:\nex\myllm-cli)
Interface visual estilo VS Code:
- ✅ Chat com modelos locais
- ✅ Console de comandos
- ✅ Configuração visual
- ✅ WebSocket sync

---

## 🎯 Instalação Rápida (5 minutos)

### Passo 1: Extrair ZIP

```cmd
# Extrair NEX-Platform.zip para C:\
# Isso criará C:\nex automaticamente
```

### Passo 2: Instalar NEX Platform

```cmd
# Abrir CMD como Administrador
cd C:\nex
INSTALAR_NEX.bat
```

O instalador vai:
1. ✅ Verificar Python
2. ✅ Criar estrutura completa
3. ✅ Instalar todas dependências
4. ✅ Configurar banco de dados
5. ✅ Configurar IA Agent
6. ✅ Criar atalhos
7. ✅ Testar instalação

### Passo 3: Iniciar

```cmd
# Método 1: Atalho no Desktop
# Clique em: "NEX Platform.bat"

# Método 2: Manual
cd C:\nex
INICIAR_NEX.bat

# Método 3: Script direto
cd C:\nex\backend
venv\Scripts\activate
python -m uvicorn app.main:app --reload
```

### Passo 4: Acessar

Abre automaticamente em:
- **API**: http://localhost:8000
- **Docs**: http://localhost:8000/docs
- **Admin**: http://localhost:8000/admin

---

## 💡 MyLLM Studio (Opcional)

Se quiser usar a interface visual para modelos locais:

```cmd
cd C:\nex\myllm-cli
INICIAR_STUDIO.bat
```

Abre em: http://localhost:8090

---

## 📚 Estrutura Instalada

```
C:\nex\
├── INSTALAR_NEX.bat         ← Execute este primeiro
├── INICIAR_NEX.bat           ← Inicia plataforma
├── ABRIR_NEX.bat             ← Abre no navegador
│
├── backend/                  ← Backend Python
│   ├── app/
│   │   ├── main.py          ← Servidor principal
│   │   ├── ai_agent/        ← IA Agent system
│   │   ├── api/             ← APIs REST
│   │   ├── database/        ← Database models
│   │   ├── websocket/       ← WebSocket
│   │   ├── apk_builder/     ← APK builder
│   │   ├── store/           ← App Store
│   │   └── admin/           ← Admin panel
│   ├── requirements.txt      ← Dependências
│   └── venv/                ← Ambiente virtual
│
├── myllm-cli/               ← MyLLM Studio
│   ├── INICIAR_STUDIO.bat
│   └── ...
│
├── database/                 ← Databases
├── ai_models/               ← Modelos IA
├── static/                  ← Arquivos estáticos
├── uploads/                 ← Uploads
└── README.md                ← Documentação
```

---

## 🎮 Primeiros Passos

### 1. Explorar API

Acesse: http://localhost:8000/docs

Você verá:
- `/api/auth` - Autenticação
- `/api/users` - Usuários
- `/api/apps` - Apps
- `/api/chat` - Chat com IA
- `/api/admin` - Admin
- `/api/store` - App Store
- `/ws/{client_id}` - WebSocket

### 2. Testar IA Agent

```bash
# Via API
curl http://localhost:8000/api/agent/status

# Ou abra: http://localhost:8000/docs
# Teste o endpoint /api/agent/status
```

### 3. Conectar via WebSocket

```javascript
// No navegador
const ws = new WebSocket('ws://localhost:8000/ws/user123');

ws.onopen = () => {
    console.log('Conectado!');

    // Enviar mensagem para IA
    ws.send(JSON.stringify({
        type: 'chat',
        message: 'Olá! Como você funciona?'
    }));
};

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('IA respondeu:', data);
};
```

### 4. Usar App Store

```cmd
# Upload de app
POST /api/store/upload

# Listar apps
GET /api/store/apps

# Instalar app
POST /api/store/install/{app_id}
```

---

## 🤖 IA Agent - Comandos

### Via WebSocket

```javascript
// Chat
ws.send(JSON.stringify({
    type: 'chat',
    message: 'Explique auto-aprendizado'
}));

// Executar comando
ws.send(JSON.stringify({
    type: 'command',
    command: 'status'
}));

// Melhorar-se
ws.send(JSON.stringify({
    type: 'agent_improve'
}));

// Build APK
ws.send(JSON.stringify({
    type: 'build',
    project: { name: 'MyApp', ... }
}));
```

---

## ⚙️ Configuração

### Arquivo: `backend/.env`

```env
# Servidor
PORT=8000
HOST=0.0.0.0
DEBUG=True

# Database
DATABASE_URL=sqlite:///./nex.db

# Segurança
SECRET_KEY=nex-secret-key-change-in-production

# CORS
CORS_ORIGINS=["http://localhost:3000","http://localhost:8000"]
```

### Modelos IA

```cmd
# Colocar modelos GGUF em:
C:\nex\ai_models\local_llm\

# Configurar no código:
# backend/app/ai_agent/agent_core.py
```

---

## 📱 MyLLM Studio

### Usar Modelos Locais

```cmd
# 1. Configurar diretório
cd C:\nex\myllm-cli
python -m myllm.cli config set models_directory "C:\nex\ai_models\local_llm"

# 2. Carregar modelo
python -m myllm.cli load seu-modelo

# 3. Iniciar Studio
INICIAR_STUDIO.bat
```

---

## 🔧 Solução de Problemas

### "Python não encontrado"

```cmd
# Instale Python 3.10+
# https://www.python.org/downloads/

# Marque "Add to PATH"
```

### "Porta 8000 em uso"

```cmd
# Mudar porta em backend/.env
PORT=8001

# Ou matar processo
netstat -ano | findstr :8000
taskkill /PID <numero> /F
```

### "Erro ao instalar dependências"

```cmd
# Instalar manualmente
cd C:\nex\backend
venv\Scripts\activate
pip install -r requirements.txt
```

### "IA Agent não responde"

```cmd
# Verificar logs
cd C:\nex\backend
venv\Scripts\activate
python -m uvicorn app.main:app --reload --log-level debug
```

---

## 📊 Recursos Avançados

### 1. Auto-Aprendizado

O Agent aprende automaticamente:
- De cada conversa
- De feedbacks
- De erros e correções
- Melhora respostas com o tempo

### 2. Auto-Melhoria

O Agent pode:
- Analisar próprio código
- Sugerir melhorias
- Implementar mudanças
- Testar alterações

### 3. Memória Persistente

- Vector database para contexto
- Histórico de conversas
- Conhecimento acumulado
- Recall inteligente

### 4. Multi-Agent

- CodeAgent: Código
- ChatAgent: Conversas
- AdminAgent: Gestão
- BuildAgent: APKs
- StoreAgent: Loja

---

## 🌐 Integração

### Com Frontend React

```javascript
// src/api/nex.js
const API_URL = 'http://localhost:8000';

export const chat = async (message) => {
    const response = await fetch(`${API_URL}/api/chat/message`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
    });
    return response.json();
};
```

### Com Apps Mobile

```kotlin
// Android
val ws = WebSocketClient("ws://SEU_IP:8000/ws/user123")
ws.connect()
ws.send("""{"type":"chat","message":"Hello"}""")
```

---

## 📈 Monitoramento

### Ver Status

```cmd
GET /health
GET /api/agent/status
```

### Logs

```cmd
# Logs em tempo real
cd C:\nex\backend
tail -f logs/nex.log
```

---

## 🎯 Próximos Passos

1. **Explorar API**: http://localhost:8000/docs
2. **Testar WebSocket**: Conectar e enviar mensagens
3. **Configurar IA**: Ajustar modelos e parâmetros
4. **Criar Apps**: Usar APK Builder
5. **Customizar**: Adaptar para suas necessidades

---

## 📚 Documentação Completa

- **NEX Platform**: `C:\nex\README.md`
- **MyLLM Studio**: `C:\nex\myllm-cli\README_STUDIO.md`
- **API Docs**: http://localhost:8000/docs

---

## 🆘 Suporte

### Guias Incluídos

- `LEIA_PRIMEIRO.txt` - Início rápido
- `TROUBLESHOOTING_WINDOWS.md` - Problemas comuns
- `WINDOWS_GUIDE.md` - Guia Windows completo
- `STUDIO_GUIDE.md` - Guia MyLLM Studio

### Ajuda Rápida

```cmd
# Backend
cd C:\nex\backend
venv\Scripts\activate
python -m uvicorn app.main:app --help

# MyLLM Studio
cd C:\nex\myllm-cli
python -m myllm.cli --help
```

---

## ✅ Checklist de Instalação

- [ ] Extraiu NEX-Platform.zip em C:\
- [ ] Python 3.10+ instalado
- [ ] Executou INSTALAR_NEX.bat
- [ ] Instalação completou sem erros
- [ ] INICIAR_NEX.bat funciona
- [ ] http://localhost:8000 abre
- [ ] http://localhost:8000/docs mostra API
- [ ] WebSocket conecta
- [ ] IA Agent responde
- [ ] (Opcional) MyLLM Studio funciona

---

## 🎉 Parabéns!

Você instalou com sucesso a **NEX Platform** - uma plataforma completa de IA autônoma!

**Comece agora:**

```cmd
cd C:\nex
INICIAR_NEX.bat
```

E acesse: http://localhost:8000/docs

**Divirta-se!** 🚀

---

**Versão**: 1.0.0
**Data**: Janeiro 2024

[⬆️ Voltar ao topo](#-nex-platform---guia-de-instalação-completa)
