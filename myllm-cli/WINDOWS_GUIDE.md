# MyLLM CLI - Guia para Windows

Guia completo de instalação e uso do MyLLM CLI no Windows.

## 📋 Requisitos

- Windows 10 ou 11
- Python 3.8 ou superior
- (Opcional) GPU NVIDIA com CUDA para aceleração

## 🚀 Instalação Rápida

### Passo 1: Instalar Python

1. Baixe Python em https://www.python.org/downloads/
2. Durante a instalação, **marque a opção "Add Python to PATH"**
3. Clique em "Install Now"
4. Verifique a instalação:
```cmd
python --version
```

### Passo 2: Instalar MyLLM CLI

```cmd
# Navegue até a pasta do projeto
cd C:\caminho\para\myllm-cli

# Execute o instalador
install.bat
```

Ou instale manualmente:
```cmd
pip install -e .
```

### Passo 3: Configurar Diretório dos Modelos

```cmd
# Configure o caminho onde seus modelos .gguf estão
myllm config set models_directory "C:\progeto\lmstudio-community"
```

### Passo 4: Verificar Modelos

```cmd
myllm ls
```

### Passo 5: Carregar e Usar

```cmd
# Carregar modelo
myllm load gpt-oss-20b-GGUF --gpu max

# Iniciar chat
myllm chat
```

## 🎯 Início Rápido Automático

Use o script de início rápido:

```cmd
quickstart.bat
```

Este script irá:
1. Verificar a instalação
2. Configurar o diretório de modelos
3. Listar modelos disponíveis
4. Carregar um modelo
5. Iniciar o chat

## 🎮 Menu de Uso Diário

Para facilitar o uso diário, use o menu interativo:

```cmd
cd examples
daily_usage.bat
```

Este menu oferece:
- Carregar modelo e iniciar chat
- Iniciar/parar servidor API
- Listar modelos
- Gerenciar configurações

## 🔧 Configuração GPU (NVIDIA)

### Verificar CUDA

```cmd
nvidia-smi
```

Se o comando funcionar, você tem CUDA instalado.

### Instalar com Suporte CUDA

```cmd
# Desinstalar versão atual
pip uninstall llama-cpp-python -y

# Instalar com CUDA (Windows com Visual Studio)
set CMAKE_ARGS=-DLLAMA_CUBLAS=on
pip install llama-cpp-python --force-reinstall --no-cache-dir
```

**Nota**: Você precisará do Visual Studio ou Build Tools instalados.

### Instalar Visual Studio Build Tools

1. Baixe em: https://visualstudio.microsoft.com/downloads/
2. Instale "Desktop development with C++"
3. Reinicie o terminal
4. Tente instalar novamente

## 📝 Comandos Principais

### Gerenciar Modelos

```cmd
# Listar modelos disponíveis
myllm ls

# Carregar modelo
myllm load gpt-oss-20b

# Carregar com GPU máximo
myllm load gpt-oss-20b --gpu max

# Carregar com configurações personalizadas
myllm load gpt-oss-20b --identifier meu-gpt --context-length 4096

# Ver modelos carregados
myllm ps

# Descarregar modelo
myllm unload meu-gpt

# Descarregar todos
myllm unload --all
```

### Chat

```cmd
# Iniciar chat (usa o primeiro modelo carregado)
myllm chat

# Chat com modelo específico
myllm chat meu-gpt
```

**Comandos no Chat:**
- `/clear` - Limpar histórico
- `/system <prompt>` - Definir prompt do sistema
- `/exit` ou `/quit` - Sair

### Servidor API

```cmd
# Iniciar servidor
myllm server start

# Iniciar em porta específica
myllm server start --port 8080

# Verificar status
myllm server status

# Parar servidor
myllm server stop
```

### Configuração

```cmd
# Ver configuração atual
myllm config show

# Definir valores
myllm config set models_directory "C:\meus\modelos"
myllm config set server.port 8080
myllm config set default_model_params.temperature 0.7

# Obter valor específico
myllm config get models_directory
```

## 🌐 Usar API com Python

### Instalar OpenAI SDK

```cmd
pip install openai
```

### Exemplo de Uso

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8080/v1",
    api_key="nao-necessario"
)

response = client.chat.completions.create(
    model="meu-gpt",
    messages=[
        {"role": "user", "content": "Olá!"}
    ]
)

print(response.choices[0].message.content)
```

## 🔍 Estrutura de Diretórios

```
C:\progeto\lmstudio-community\
├── gpt-oss-20b-GGUF\
│   └── gpt-oss-20b.gguf
├── llama-7b-GGUF\
│   └── llama-7b.gguf
└── outros-modelos\
    └── modelo.gguf
```

MyLLM CLI irá encontrar todos os arquivos `.gguf` recursivamente.

## ⚙️ Configuração Recomendada

### Para GPU com 8GB VRAM (Ex: RTX 3060)

```cmd
myllm config set default_model_params.gpu_layers -1
myllm config set default_model_params.context_length 2048
myllm load modelo --gpu max --context-length 2048
```

### Para GPU com 12GB+ VRAM (Ex: RTX 4070)

```cmd
myllm config set default_model_params.gpu_layers -1
myllm config set default_model_params.context_length 4096
myllm load modelo --gpu max --context-length 4096
```

### Para CPU Apenas (Sem GPU)

```cmd
myllm config set default_model_params.gpu_layers 0
myllm config set advanced.threads 8
myllm load modelo --gpu 0
```

## 🐛 Solução de Problemas

### "myllm não é reconhecido como comando"

**Solução 1**: Adicione Python Scripts ao PATH
```cmd
# Adicione ao PATH:
C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python3X\Scripts
```

**Solução 2**: Use Python diretamente
```cmd
python -m myllm
```

### "Failed to load model"

**Causas comuns:**
1. **Memória insuficiente**
   - Reduza context length: `--context-length 1024`
   - Reduza GPU: `--gpu 0.5`

2. **Caminho errado**
   - Verifique: `myllm ls`
   - Use caminho completo

3. **Formato errado**
   - Use apenas arquivos `.gguf`

### "Server already running"

```cmd
# Pare o servidor primeiro
myllm server stop

# Se não funcionar, encontre o processo
tasklist | findstr python
taskkill /F /PID <numero_do_processo>
```

### GPU não está sendo usada

1. Verifique CUDA:
```cmd
nvidia-smi
```

2. Reinstale com CUDA:
```cmd
pip uninstall llama-cpp-python -y
set CMAKE_ARGS=-DLLAMA_CUBLAS=on
pip install llama-cpp-python --force-reinstall --no-cache-dir
```

3. Verifique ao carregar:
```cmd
myllm load modelo --gpu max
myllm ps  # Deve mostrar gpu_layers > 0
```

## 💡 Dicas

1. **Use caminhos absolutos**
   ```cmd
   myllm config set models_directory "C:\progeto\lmstudio-community"
   ```

2. **Mantenha modelos carregados**
   - Evite recarregar frequentemente
   - Use `myllm ps` para ver o que está carregado

3. **Scripts em lote**
   - Crie arquivos `.bat` para tarefas repetitivas
   - Veja `examples/daily_usage.bat` como exemplo

4. **Variáveis de ambiente**
   ```cmd
   # Definir temporariamente
   set MYLLM_CONFIG_DIR=C:\minha\config
   ```

## 📚 Recursos Adicionais

- [README.md](README.md) - Documentação completa
- [QUICKSTART.md](QUICKSTART.md) - Guia de início rápido
- [OPTIMIZATION.md](OPTIMIZATION.md) - Otimização de desempenho
- [examples/](examples/) - Exemplos de código

## 🆘 Ajuda

```cmd
# Ajuda geral
myllm --help

# Ajuda de comando específico
myllm load --help
myllm chat --help
myllm server --help
```

## ✅ Checklist de Instalação

- [ ] Python instalado e no PATH
- [ ] MyLLM CLI instalado (`myllm --version` funciona)
- [ ] Diretório de modelos configurado
- [ ] Pelo menos um modelo .gguf no diretório
- [ ] `myllm ls` mostra seus modelos
- [ ] Modelo carregado com sucesso
- [ ] Chat funciona
- [ ] (Opcional) GPU CUDA configurado

## 🎉 Pronto!

Agora você está pronto para usar o MyLLM CLI!

Comece com:
```cmd
myllm load gpt-oss-20b --gpu max
myllm chat
```

Divirta-se! 🚀
