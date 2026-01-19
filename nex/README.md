# NEX Platform - Plataforma Completa de IA Autônoma

**Sistema Inteligente Auto-Evolutivo com Store de Apps**

## 🚀 Visão Geral

NEX é uma plataforma completa que combina:
- 🤖 IA Agent autônoma com auto-aprendizado
- 📱 Criador de APKs (aplicativos Android)
- 🏪 App Store integrada
- 💾 Banco de dados com memória vetorial
- 🔄 WebSocket real-time
- 👥 Sistema administrativo completo
- 🧠 Auto-melhoria e atualização do próprio sistema
- 🎯 Contexto e memória persistente

## 📁 Estrutura do Projeto

```
C:\nex\
├── backend/                    # Backend Python (FastAPI)
│   ├── app/
│   │   ├── ai_agent/          # Sistema de IA Agent
│   │   │   ├── agent_core.py  # Core do agente
│   │   │   ├── auto_learn.py  # Auto-aprendizado
│   │   │   ├── memory.py      # Sistema de memória
│   │   │   └── self_improve.py # Auto-melhoria
│   │   ├── api/               # APIs REST
│   │   ├── database/          # Modelos e DB
│   │   ├── websocket/         # WebSocket handlers
│   │   ├── apk_builder/       # Construtor de APKs
│   │   ├── store/             # App Store
│   │   └── admin/             # Sistema admin
│   ├── models/                # Modelos ML/LLM
│   └── data/                  # Dados e cache
│
├── frontend/                   # Frontend (React/Vue)
│   ├── admin/                 # Painel admin
│   ├── store/                 # Loja de apps
│   ├── chat/                  # Interface chat
│   └── dashboard/             # Dashboard
│
├── database/                   # Database
│   ├── postgresql/            # Dados estruturados
│   ├── vector_db/             # Embeddings (ChromaDB)
│   └── migrations/            # Migrações
│
├── mobile/                     # Apps mobile
│   ├── android/               # App Android
│   └── templates/             # Templates APK
│
├── ai_models/                  # Modelos IA
│   ├── local_llm/             # LLMs locais
│   ├── embeddings/            # Modelos embedding
│   └── fine_tuned/            # Modelos ajustados
│
├── services/                   # Microserviços
│   ├── auth/                  # Autenticação
│   ├── storage/               # Armazenamento
│   ├── queue/                 # Filas (Celery)
│   └── cache/                 # Cache (Redis)
│
├── deployment/                 # Deploy
│   ├── docker/                # Containers
│   ├── kubernetes/            # K8s configs
│   └── scripts/               # Scripts deploy
│
├── docs/                       # Documentação
├── tests/                      # Testes
└── config/                     # Configurações

```

## 🏗️ Arquitetura

### 1. Backend (FastAPI + Python)
- FastAPI para APIs REST
- WebSocket para real-time
- Celery para tarefas assíncronas
- Redis para cache
- PostgreSQL + Vector DB

### 2. IA Agent System
- **Auto-Learning**: RAG + Fine-tuning
- **Memory**: Vector embeddings + Context window
- **Self-Improvement**: Code generation e testing
- **Multi-Agent**: Especialização por tarefa

### 3. Database
- **PostgreSQL**: Dados estruturados
- **ChromaDB/Qdrant**: Vetores e memória
- **Redis**: Cache e sessões
- **MongoDB**: Logs e analytics

### 4. App Store
- Upload de apps
- Versionamento
- Distribuição
- Monetização

### 5. APK Builder
- Build automatizado
- Signing
- Otimização
- Distribuição

## 🚀 Stack Tecnológica

### Backend
```python
- FastAPI (API REST)
- WebSocket (Real-time)
- SQLAlchemy (ORM)
- Alembic (Migrations)
- Celery (Tasks)
- Redis (Cache)
- LangChain (AI Orchestration)
- ChromaDB (Vector Store)
```

### Frontend
```javascript
- React (UI)
- TypeScript
- TailwindCSS
- Socket.io (WebSocket)
- Zustand (State)
- React Query
```

### IA/ML
```python
- LangChain (Orchestration)
- LlamaIndex (RAG)
- Transformers (Models)
- Sentence-Transformers (Embeddings)
- AutoGPT (Agent)
- LangGraph (Multi-agent)
```

### DevOps
```
- Docker
- Kubernetes
- GitHub Actions
- Nginx
- Prometheus + Grafana
```

## 📦 Instalação

### 1. Clonar/Extrair
```cmd
cd C:\nex
```

### 2. Instalar Backend
```cmd
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configurar Database
```cmd
# PostgreSQL
python scripts/setup_database.py

# Vector DB
python scripts/setup_vectordb.py
```

### 4. Instalar Frontend
```cmd
cd frontend
npm install
```

### 5. Executar
```cmd
# Backend
python run_backend.py

# Frontend
npm run dev

# All-in-one
python run_all.py
```

## 🤖 IA Agent - Capacidades

### 1. Auto-Aprendizado
```python
# O agente aprende com cada interação
agent.learn_from_conversation(conversation)
agent.update_knowledge_base(new_info)
agent.fine_tune_on_feedback(feedback)
```

### 2. Auto-Melhoria
```python
# Melhora o próprio código
agent.analyze_code()
agent.suggest_improvements()
agent.implement_changes()
agent.test_changes()
```

### 3. Memória Persistente
```python
# Memória de longo prazo
agent.store_memory(conversation, embeddings)
agent.recall_similar(query)
agent.build_context_window()
```

### 4. Multi-Agente
```python
# Agentes especializados
- CodeAgent: Escreve e melhora código
- ChatAgent: Conversa com usuários
- AdminAgent: Gerencia sistema
- BuildAgent: Cria APKs
- StoreAgent: Gerencia loja
```

## 🏪 App Store

### Funcionalidades
- ✅ Upload de apps
- ✅ Versionamento automático
- ✅ Review e aprovação
- ✅ Distribuição
- ✅ Analytics
- ✅ Monetização
- ✅ Updates automáticos

### API
```python
POST /api/store/upload      # Upload app
GET  /api/store/apps         # Listar apps
GET  /api/store/app/{id}     # Detalhes
POST /api/store/install/{id} # Instalar
POST /api/store/update/{id}  # Atualizar
```

## 📱 APK Builder

### Processo
1. Upload código/projeto
2. Configuração automática
3. Build com Gradle
4. Signing com keystore
5. Otimização (ProGuard)
6. Upload para Store

### Automação
```python
builder = APKBuilder()
builder.load_project(path)
builder.configure()
builder.build()
builder.sign()
builder.optimize()
builder.publish()
```

## 💾 Sistema de Banco de Dados

### PostgreSQL (Estruturado)
```sql
- users (usuários)
- apps (aplicativos)
- conversations (conversas)
- transactions (transações)
- analytics (analytics)
```

### Vector DB (Memória IA)
```python
- conversation_embeddings
- code_embeddings
- knowledge_base
- context_memory
```

### Redis (Cache)
```python
- session_cache
- api_cache
- websocket_state
```

## 🔌 WebSocket Real-Time

### Channels
```javascript
ws://nex.local/ws/chat       // Chat
ws://nex.local/ws/admin      // Admin
ws://nex.local/ws/build      // Build status
ws://nex.local/ws/store      // Store updates
ws://nex.local/ws/agent      // Agent status
```

### Events
```javascript
// Chat
{ type: 'message', data: {...} }
{ type: 'typing', user: 'Agent' }

// Build
{ type: 'build_started', app_id: 123 }
{ type: 'build_progress', percent: 45 }
{ type: 'build_complete', apk_url: '...' }

// Agent
{ type: 'agent_thinking', task: '...' }
{ type: 'agent_learning', info: '...' }
{ type: 'agent_improved', changes: [...] }
```

## 👥 Sistema Administrativo

### Painel Admin
- 📊 Dashboard com métricas
- 👤 Gestão de usuários
- 📱 Gestão de apps
- 💬 Moderação de chat
- 🤖 Controle do agente
- 📈 Analytics
- ⚙️ Configurações

### Permissões
```python
- SuperAdmin: Controle total
- Admin: Gestão de apps e usuários
- Moderator: Moderação
- Developer: Upload de apps
- User: Uso normal
```

## 🧠 Auto-Aprendizado e Melhoria

### RAG (Retrieval-Augmented Generation)
```python
# Agent busca conhecimento relevante
context = agent.retrieve_relevant_knowledge(query)
response = agent.generate_with_context(query, context)
agent.store_new_knowledge(response)
```

### Fine-Tuning Pipeline
```python
# Agent se ajusta com dados
agent.collect_training_data()
agent.prepare_dataset()
agent.fine_tune_model()
agent.evaluate_improvements()
agent.deploy_new_version()
```

### Self-Modification
```python
# Agent melhora próprio código
agent.analyze_performance()
agent.identify_bottlenecks()
agent.generate_improvements()
agent.test_changes()
agent.apply_if_better()
```

## 🔐 Segurança

- 🔑 JWT Authentication
- 🛡️ Role-based access (RBAC)
- 🔒 Encryption at rest
- 🌐 HTTPS only
- 🚫 Rate limiting
- 📝 Audit logs
- 🔐 API key management

## 📊 Analytics

- 📈 User metrics
- 📱 App downloads
- 💬 Chat analytics
- 🤖 Agent performance
- 🏪 Store metrics
- 💰 Revenue tracking

## 🌐 APIs

### REST API
```
POST   /api/auth/login
POST   /api/auth/register
GET    /api/user/profile
GET    /api/apps
POST   /api/apps/create
POST   /api/chat/message
GET    /api/agent/status
POST   /api/admin/users
```

### WebSocket API
```javascript
ws.send({ type: 'chat', message: '...' })
ws.send({ type: 'build', action: 'start' })
ws.send({ type: 'agent', command: '...' })
```

## 🚀 Deployment

### Docker
```bash
docker-compose up -d
```

### Kubernetes
```bash
kubectl apply -f deployment/
```

### Manual
```bash
# Backend
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Frontend
npm run build
serve -s build

# Workers
celery -A app.worker worker -l info
```

## 📚 Documentação

- [Início Rápido](docs/quickstart.md)
- [Guia de Instalação](docs/installation.md)
- [API Reference](docs/api.md)
- [IA Agent Guide](docs/agent.md)
- [App Store Guide](docs/store.md)
- [APK Builder](docs/apk_builder.md)
- [Admin Guide](docs/admin.md)

## 🎯 Roadmap

### Fase 1 (Atual)
- [x] Arquitetura base
- [x] Backend FastAPI
- [x] Database setup
- [ ] IA Agent básico
- [ ] Chat interface
- [ ] Admin panel

### Fase 2
- [ ] App Store
- [ ] APK Builder
- [ ] Auto-learning
- [ ] Memory system
- [ ] Multi-agent

### Fase 3
- [ ] Self-improvement
- [ ] Advanced analytics
- [ ] Mobile apps
- [ ] Marketplace
- [ ] API pública

### Fase 4
- [ ] AGI capabilities
- [ ] Auto-evolution
- [ ] Distributed system
- [ ] Global scale

## 💡 Conceitos Avançados

### 1. Agent Auto-Evolution
O agente pode:
- Analisar próprio desempenho
- Identificar fraquezas
- Gerar melhorias
- Testar mudanças
- Deploy automático

### 2. Collective Intelligence
Múltiplos agentes:
- Especializam-se em tarefas
- Compartilham conhecimento
- Colaboram em projetos
- Evoluem juntos

### 3. Continuous Learning
- Aprende com cada interação
- Atualiza conhecimento
- Melhora respostas
- Adapta-se ao contexto

## 🛠️ Desenvolvimento

### Setup Dev
```bash
# Clone
git clone <repo>
cd nex

# Install
pip install -r requirements-dev.txt
npm install

# Run tests
pytest
npm test

# Run dev
python run_dev.py
```

### Contributing
1. Fork projeto
2. Create branch
3. Make changes
4. Run tests
5. Submit PR

## 📄 Licença

MIT License

## 🆘 Suporte

- 📧 Email: support@nex.platform
- 💬 Discord: discord.gg/nex
- 📖 Docs: docs.nex.platform
- 🐛 Issues: github.com/nex/issues

---

**NEX Platform** - O futuro da IA autônoma começa aqui! 🚀
