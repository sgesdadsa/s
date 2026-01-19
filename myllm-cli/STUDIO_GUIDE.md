# MyLLM Studio - Guia Completo

Interface visual estilo VS Code para MyLLM CLI.

## 🎨 O que é MyLLM Studio?

MyLLM Studio é uma interface web moderna e visual para interagir com seus modelos LLM locais. Inspirado no Visual Studio Code, oferece:

- 💬 **Chat Interface** - Converse com seus modelos em tempo real
- 🖥️ **Console** - Execute comandos CLI visualmente
- ⚙️ **Settings** - Configure tudo pela interface
- 🔄 **Real-time Sync** - Sincronização em tempo real via WebSockets
- 🎨 **Dark Theme** - Interface moderna estilo VS Code

## 🚀 Início Rápido

### Método 1: Linha de Comando

```cmd
# Iniciar MyLLM Studio
python -m myllm.studio_cli start

# Ou se tiver instalado:
myllm studio start

# Especificar porta
myllm studio start --port 8090

# Não abrir navegador automaticamente
myllm studio start --no-browser
```

### Método 2: Script Direto

```cmd
# Execute o script standalone
python run_studio.py
```

### Método 3: Executável (Windows)

```cmd
# Build primeiro (uma vez)
build_studio.bat

# Depois execute
dist\MyLLM-Studio.exe
```

## 📦 Instalação

### Pré-requisitos

```cmd
# Instalar dependências do Studio
pip install uvicorn fastapi websockets

# Ou instalar tudo
pip install -r requirements.txt
```

### Criar Atalho no Desktop

```cmd
# Criar atalho automaticamente
myllm studio desktop
```

## 🎯 Recursos

### 1. Interface de Chat

- Chat em tempo real com seus modelos
- Histórico de conversas
- Markdown support
- Auto-scroll
- Múltiplas conversas simultâneas

### 2. Console de Comandos

Execute comandos CLI pela interface:

- `ls` - Listar modelos
- `ps` - Ver modelos carregados
- `config show` - Ver configuração

### 3. Configurações

Configure visualmente:

- Diretório de modelos
- Porta do servidor
- Temperatura
- Max tokens
- GPU settings

### 4. Sincronização em Tempo Real

- WebSocket connection
- Atualizações ao vivo
- Status em tempo real
- Múltiplos clientes

## 📖 Uso

### Abrir MyLLM Studio

```cmd
cd C:\myllm-cli
python -m myllm.studio_cli start
```

Abre automaticamente em: `http://localhost:8090`

### Interface

```
┌─────────────────────────────────────────┐
│ 🚀 MyLLM Studio          ⚙️ Config  🔌   │
├─────┬───────────────────────────────────┤
│     │ Chat │ Console │ Settings         │
│ 📁  ├───────────────────────────────────┤
│     │                                   │
│ 💬  │  💬 Chat Interface                │
│     │                                   │
│ 🖥️  │  User: Hello!                    │
│     │  AI: Hi! How can I help?         │
│ ⚙️  │                                   │
│     │  [Type message...]         [Send]│
│     │                                   │
├─────┴───────────────────────────────────┤
│ 🟢 Connected  │  Model: gpt-oss-20b     │
└─────────────────────────────────────────┘
```

### Workflow Típico

1. **Carregar Modelo** (via CLI primeiro):
   ```cmd
   python -m myllm.cli load gpt-oss-20b
   ```

2. **Iniciar Studio**:
   ```cmd
   python -m myllm.studio_cli start
   ```

3. **Usar Interface**:
   - Abrir no navegador (abre automático)
   - Começar a conversar no chat
   - Ou executar comandos no console

## 🔧 Configuração Avançada

### Porta Customizada

```cmd
myllm studio start --port 8080
```

### Host Customizado

```cmd
myllm studio start --host 127.0.0.1 --port 8090
```

### Modo Produção

```cmd
# Com mais workers
uvicorn myllm.studio_server:app --host 0.0.0.0 --port 8090 --workers 4
```

## 🎨 Customização

### Tema

O tema dark é baseado no VS Code e pode ser customizado editando o CSS em `studio_server.py`.

### Cores Principais

```css
--bg-primary: #1e1e1e     /* Fundo principal */
--bg-secondary: #252526    /* Sidebar */
--bg-tertiary: #2d2d30     /* Header */
--accent-blue: #007acc     /* Ações primárias */
--accent-green: #4ec9b0    /* Sucesso */
```

## 📱 Acessar de Outros Dispositivos

### Na Mesma Rede

1. Inicie com host 0.0.0.0:
   ```cmd
   myllm studio start --host 0.0.0.0
   ```

2. Descubra seu IP:
   ```cmd
   ipconfig
   ```

3. Acesse de outro dispositivo:
   ```
   http://SEU_IP:8090
   ```

### Via Internet (Avançado)

Use um serviço de tunneling como ngrok:

```cmd
# Instalar ngrok
# https://ngrok.com/download

# Criar tunnel
ngrok http 8090

# Use a URL fornecida
```

## 🏗️ Build Executável

### Windows

```cmd
# Método 1: Script automatizado
build_studio.bat

# Método 2: Manual
pip install pyinstaller
pyinstaller --onefile --windowed --name MyLLM-Studio run_studio.py

# Executável estará em: dist\MyLLM-Studio.exe
```

### Linux/Mac

```bash
# Instalar PyInstaller
pip install pyinstaller

# Build
pyinstaller --onefile --name myllm-studio run_studio.py

# Executável em: dist/myllm-studio
```

## 🔄 Sincronização

### WebSocket API

O Studio usa WebSockets para comunicação em tempo real:

```javascript
// Conectar
ws = new WebSocket('ws://localhost:8090/ws');

// Enviar mensagem de chat
ws.send(JSON.stringify({
    type: 'chat',
    message: 'Hello!'
}));

// Executar comando
ws.send(JSON.stringify({
    type: 'command',
    command: 'ls'
}));

// Sync data
ws.send(JSON.stringify({
    type: 'sync',
    data: { ... }
}));
```

### Integração com Outros Apps

```python
import asyncio
import websockets
import json

async def send_message():
    async with websockets.connect('ws://localhost:8090/ws') as ws:
        # Enviar mensagem
        await ws.send(json.dumps({
            'type': 'chat',
            'message': 'Hello from Python!'
        }))

        # Receber resposta
        response = await ws.recv()
        data = json.loads(response)
        print(data)

asyncio.run(send_message())
```

## 🐛 Solução de Problemas

### Porta em Uso

```cmd
# Erro: Address already in use

# Solução 1: Use outra porta
myllm studio start --port 8091

# Solução 2: Encontre e mate o processo
netstat -ano | findstr :8090
taskkill /PID <numero> /F
```

### WebSocket não Conecta

1. Verifique se o servidor está rodando
2. Verifique firewall
3. Tente desabilitar antivírus temporariamente
4. Use localhost ao invés de 0.0.0.0

### Navegador não Abre

```cmd
# Execute sem --browser e abra manualmente
myllm studio start --no-browser

# Depois abra:
# http://localhost:8090
```

### Modelo não Responde

1. Verifique se o modelo está carregado:
   ```cmd
   python -m myllm.cli ps
   ```

2. Carregue um modelo:
   ```cmd
   python -m myllm.cli load modelo
   ```

3. Reinicie o Studio

## 📊 Performance

### Otimizações

- Use GPU offload máximo
- Ajuste batch size
- Configure workers do Uvicorn
- Use cache do navegador

### Monitoramento

Veja logs em tempo real:

```cmd
# Com mais detalhes
myllm studio start --log-level debug
```

## 🔐 Segurança

### Acesso Local Apenas

```cmd
# Bind apenas localhost (mais seguro)
myllm studio start --host 127.0.0.1
```

### Acesso Rede

```cmd
# Todos os IPs (menos seguro)
myllm studio start --host 0.0.0.0
```

**Nota**: Não exponha à internet sem autenticação!

## 🎓 Exemplos

### Exemplo 1: Chat Simples

1. Carregue modelo:
   ```cmd
   python -m myllm.cli load gpt-oss-20b
   ```

2. Inicie Studio:
   ```cmd
   myllm studio start
   ```

3. Chat na interface web

### Exemplo 2: API Custom

```python
# Seu próprio cliente
import requests

response = requests.post('http://localhost:8090/api/chat', json={
    'message': 'Hello!'
})

print(response.json())
```

### Exemplo 3: Integração Desktop

Crie um atalho que:
1. Carrega modelo
2. Inicia Studio
3. Abre navegador

```batch
@echo off
python -m myllm.cli load gpt-oss-20b
python -m myllm.studio_cli start
```

## 📚 Recursos Adicionais

- **README.md** - Documentação principal
- **WINDOWS_GUIDE.md** - Guia Windows
- **QUICKSTART.md** - Início rápido
- **API Documentation** - Em breve

## 🎉 Roadmap

Próximas features:

- [ ] Múltiplas conversas (tabs)
- [ ] Histórico persistente
- [ ] Exportar conversas
- [ ] Temas customizáveis
- [ ] Plugins/Extensions
- [ ] Mobile app
- [ ] Autenticação
- [ ] Compartilhamento de conversas
- [ ] Streaming responses
- [ ] Voice input/output

## 💡 Dicas

1. **Use atalhos de teclado** - Shift+Enter para nova linha
2. **Mantenha modelo carregado** - Evite recarregar
3. **Monitor RAM/VRAM** - Use GPU-Z ou Task Manager
4. **Múltiplas janelas** - Abra várias abas do navegador
5. **Customize tema** - Edite o CSS direto no código

## 🆘 Ajuda

Se precisar de ajuda:

1. Verifique TROUBLESHOOTING_WINDOWS.md
2. Execute: `myllm studio --help`
3. Veja logs no console
4. Reporte issues no GitHub

---

**Desenvolvido com ❤️ para a comunidade de LLMs locais**

Divirta-se! 🚀
