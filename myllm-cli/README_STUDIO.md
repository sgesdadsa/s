# 🎨 MyLLM Studio

**Interface Visual Moderna para MyLLM CLI**

Inspirado no Visual Studio Code, MyLLM Studio oferece uma experiência visual completa para interagir com seus modelos LLM locais.

![MyLLM Studio](https://img.shields.io/badge/MyLLM-Studio-blue?style=for-the-badge)
![Version](https://img.shields.io/badge/version-1.0.0-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-orange?style=for-the-badge)

---

## ✨ Características

### 🎯 Interface Moderna
- **Tema Dark** inspirado no VS Code
- **Layout Responsivo** para todos os tamanhos de tela
- **Sidebar** com navegação e status
- **Tabs** para múltiplas views
- **Status Bar** com informações em tempo real

### 💬 Chat Inteligente
- Conversas em tempo real com modelos LLM
- Histórico de mensagens
- Suporte a Markdown
- Auto-scroll
- Avatares para user e AI

### 🖥️ Console Integrado
- Execute comandos CLI pela interface
- Visualização de resultados
- Syntax highlighting
- Histórico de comandos

### ⚙️ Configuração Visual
- Ajuste todos os parâmetros sem editar arquivos
- Formulários intuitivos
- Validação em tempo real
- Salvamento automático

### 🔄 Sincronização em Tempo Real
- WebSocket para comunicação instantânea
- Múltiplos clientes sincronizados
- Status connection em tempo real
- Broadcast de mensagens

---

## 🚀 Início Rápido

### Windows (Mais Fácil)

```cmd
cd C:\myllm-cli
INICIAR_STUDIO.bat
```

Escolha opção 1 no menu.

### Linha de Comando

```cmd
# Iniciar Studio
python -m myllm.studio_cli start

# Ou
python run_studio.py
```

Abre automaticamente em `http://localhost:8090`

---

## 📦 Instalação

### Opção 1: Instalação Completa

```cmd
cd C:\myllm-cli
pip install -r requirements.txt
```

### Opção 2: Instalar Apenas Studio

```cmd
pip install fastapi uvicorn[standard] websockets python-multipart
```

### Opção 3: Verificar Instalação

```cmd
python -c "import fastapi, uvicorn, websockets; print('OK!')"
```

---

## 🎯 Como Usar

### 1. Preparar Ambiente

```cmd
# Instalar dependências
pip install -r requirements.txt

# Configurar diretório de modelos
python -m myllm.cli config set models_directory "C:\seu\caminho"
```

### 2. Carregar Modelo

```cmd
# Listar modelos disponíveis
python -m myllm.cli ls

# Carregar modelo
python -m myllm.cli load gpt-oss-20b --gpu max
```

### 3. Iniciar Studio

```cmd
# Método 1: Script Windows
INICIAR_STUDIO.bat

# Método 2: Comando direto
python -m myllm.studio_cli start

# Método 3: Script Python
python run_studio.py
```

### 4. Usar Interface

1. O navegador abrirá automaticamente
2. Veja modelos carregados na sidebar
3. Comece a conversar no chat
4. Ou execute comandos no console

---

## 🛠️ Comandos

### Iniciar Studio

```cmd
# Básico
myllm studio start

# Porta customizada
myllm studio start --port 8091

# Sem abrir navegador
myllm studio start --no-browser

# Host específico
myllm studio start --host 127.0.0.1
```

### Build Executável

```cmd
# Criar executável standalone
myllm studio build

# Ou use o script
build_studio.bat
```

### Criar Atalho

```cmd
# Criar atalho no desktop
myllm studio desktop
```

---

## 📸 Screenshots

### Interface Principal

```
┌──────────────────────────────────────────────────────┐
│ 🚀 MyLLM Studio              ⚙️ Config  🔌 Connect │
├──────┬───────────────────────────────────────────────┤
│      │ 💬 Chat │ 🖥️ Console │ ⚙️ Settings         │
│ 📁   ├───────────────────────────────────────────────┤
│Models│                                               │
│  •   │  💬 Chat Interface                           │
│GPT-20│                                               │
│      │  ┌─────────────────────────────────────────┐ │
│ 💬   │  │ You: Como funciona um transformer?     │ │
│Chat  │  │ AI: Um transformer é uma arquitetura...│ │
│      │  └─────────────────────────────────────────┘ │
│ 🖥️   │                                               │
│Consol│  ┌────────────────────────────────────────┐  │
│      │  │ Type message...                  [Send]│  │
│ ⚙️   │  └────────────────────────────────────────┘  │
│Config│                                               │
├──────┴───────────────────────────────────────────────┤
│ 🟢 Connected        │        Model: gpt-oss-20b     │
└──────────────────────────────────────────────────────┘
```

---

## 🎨 Personalização

### Temas

O Studio usa um tema dark inspirado no VS Code com variáveis CSS:

```css
--bg-primary: #1e1e1e      /* Fundo principal */
--bg-secondary: #252526     /* Sidebar/painéis */
--accent-blue: #007acc      /* Destaque azul */
--accent-green: #4ec9b0     /* Sucesso */
```

### Modificar Cores

Edite o arquivo `myllm/studio_server.py` na seção `:root` do CSS.

---

## 🌐 Acesso Remoto

### Na Rede Local

```cmd
# Inicie com host 0.0.0.0
myllm studio start --host 0.0.0.0

# Descubra seu IP
ipconfig

# Acesse de outro dispositivo
http://SEU_IP:8090
```

### Via Internet (Tunnel)

```cmd
# Use ngrok
ngrok http 8090

# Ou outro serviço de tunneling
```

⚠️ **Aviso**: Não exponha à internet pública sem autenticação!

---

## 🔌 API WebSocket

### Conectar

```javascript
const ws = new WebSocket('ws://localhost:8090/ws');

ws.onopen = () => console.log('Connected!');
ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Received:', data);
};
```

### Enviar Mensagem

```javascript
ws.send(JSON.stringify({
    type: 'chat',
    message: 'Hello, AI!'
}));
```

### Executar Comando

```javascript
ws.send(JSON.stringify({
    type: 'command',
    command: 'ls'
}));
```

### Sincronizar Dados

```javascript
ws.send(JSON.stringify({
    type: 'sync',
    data: { config: {...} }
}));
```

---

## 🐛 Solução de Problemas

### Studio Não Inicia

```cmd
# Verificar dependências
pip install uvicorn fastapi websockets

# Testar Python
python run_studio.py
```

### Porta em Uso

```cmd
# Use outra porta
myllm studio start --port 8091
```

### Modelo Não Responde

```cmd
# Verificar se modelo está carregado
python -m myllm.cli ps

# Carregar modelo
python -m myllm.cli load seu-modelo
```

### WebSocket Não Conecta

1. Verifique firewall
2. Tente localhost ao invés de 0.0.0.0
3. Verifique se porta está livre
4. Reinicie o browser

---

## 📊 Performance

### Otimizações

- Use modelos quantizados (Q4_K_M)
- Ative GPU offload máximo
- Configure batch size adequado
- Use SSD para modelos

### Monitoramento

```cmd
# Logs detalhados
myllm studio start --log-level debug
```

---

## 🏗️ Build e Deploy

### Criar Executável Windows

```cmd
# Método 1: Script
build_studio.bat

# Método 2: PyInstaller direto
pyinstaller --onefile --windowed run_studio.py
```

### Deploy em Servidor

```cmd
# Com Uvicorn
uvicorn myllm.studio_server:app --host 0.0.0.0 --port 8090

# Com múltiplos workers
uvicorn myllm.studio_server:app --workers 4

# Com SSL (HTTPS)
uvicorn myllm.studio_server:app --ssl-keyfile key.pem --ssl-certfile cert.pem
```

---

## 📚 Documentação

- **STUDIO_GUIDE.md** - Guia completo do Studio
- **README.md** - Documentação principal MyLLM CLI
- **WINDOWS_GUIDE.md** - Guia Windows
- **QUICKSTART.md** - Início rápido

---

## 🎓 Tutoriais

### Tutorial 1: Primeira Conversa

1. Instale MyLLM CLI
2. Configure diretório de modelos
3. Carregue um modelo
4. Inicie o Studio
5. Converse no chat

### Tutorial 2: Build Executável

1. Instale PyInstaller
2. Execute `build_studio.bat`
3. Executável em `dist/`
4. Distribua o .exe

### Tutorial 3: Acesso Remoto

1. Inicie com `--host 0.0.0.0`
2. Configure firewall
3. Compartilhe URL com IP
4. Acesse de qualquer dispositivo

---

## 🚀 Roadmap

### v1.1 (Próximo)
- [ ] Streaming responses
- [ ] Múltiplas conversas (tabs)
- [ ] Histórico persistente
- [ ] Exportar conversas

### v1.2
- [ ] Temas customizáveis
- [ ] Plugins/Extensions
- [ ] Autenticação de usuários
- [ ] API REST adicional

### v2.0
- [ ] Mobile app (React Native)
- [ ] Electron app nativo
- [ ] Voice input/output
- [ ] Multi-language support

---

## 🤝 Contribuindo

Contribuições são bem-vindas!

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

---

## 📝 Changelog

### v1.0.0 (2024-01-19)
- ✨ Lançamento inicial
- 💬 Interface de chat
- 🖥️ Console de comandos
- ⚙️ Painel de configurações
- 🔄 WebSocket real-time
- 🎨 Tema dark VS Code
- 📦 Build executável

---

## 📄 Licença

MIT License - veja [LICENSE](LICENSE) para detalhes.

---

## ❤️ Créditos

Desenvolvido para a comunidade de LLMs locais.

Tecnologias usadas:
- FastAPI - Web framework
- Uvicorn - ASGI server
- WebSockets - Comunicação real-time
- Rich - CLI beautification
- Click - CLI framework

---

## 🎉 Conclusão

MyLLM Studio transforma a experiência de usar LLMs locais, oferecendo uma interface visual moderna e intuitiva.

**Comece agora:**

```cmd
cd C:\myllm-cli
INICIAR_STUDIO.bat
```

Divirta-se! 🚀

---

**Versão**: 1.0.0
**Data**: Janeiro 2024
**Autor**: MyLLM Team

[⬆️ Voltar ao topo](#-myllm-studio)
