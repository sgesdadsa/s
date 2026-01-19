# 🔨 NEX IDE Builder - Guia Completo

**IDE Completo com Debug, Build, Visual Designer e Production Pipeline**

## 🎯 O que é NEX IDE Builder?

Sistema completo de desenvolvimento que permite:
- ✅ Criar projetos em múltiplas linguagens
- ✅ Editar código com syntax highlighting
- ✅ Debug em tempo real
- ✅ Build para executável (.exe, .jar, etc.)
- ✅ Designer visual de forms (drag-and-drop)
- ✅ Gerenciar versões (.sln, .csproj)
- ✅ Pipeline de produção automatizado
- ✅ IA que melhora código automaticamente

---

## 🚀 Linguagens Suportadas

### C# (.NET)
- ✅ Console Apps
- ✅ WinForms
- ✅ WPF
- ✅ ASP.NET Core
- ✅ .sln e .csproj

### VB.NET
- ✅ Console Apps
- ✅ WinForms
- ✅ .vbproj

### Java
- ✅ Console Apps
- ✅ Swing GUI
- ✅ JAR packaging

### Python
- ✅ Scripts
- ✅ PyInstaller para .exe

### C++
- ✅ Console Apps
- ✅ Makefile support
- ✅ G++ compiler

---

## 📦 API Endpoints

### Criar Projeto

```http
POST /api/ide/project/create
Content-Type: application/json

{
  "name": "MeuApp",
  "language": "csharp",
  "type": "winforms"
}
```

**Resposta:**
```json
{
  "id": "proj_20240119123456",
  "name": "MeuApp",
  "language": "csharp",
  "type": "winforms",
  "path": "projects/proj_20240119123456",
  "status": "created"
}
```

### Build Projeto

```http
POST /api/ide/project/{project_id}/build
Content-Type: application/json

{
  "config": "Release"
}
```

**Resposta:**
```json
{
  "success": true,
  "exe_path": "projects/proj_xxx/bin/Release/MeuApp.exe",
  "output": "Build succeeded...",
  "status": "completed"
}
```

### Debug Session

```http
POST /api/ide/debug/start
Content-Type: application/json

{
  "project_id": "proj_20240119123456"
}
```

**Resposta:**
```json
{
  "success": true,
  "session_id": "debug_xxx",
  "message": "Debug session started"
}
```

### Visual Designer

```http
POST /api/ide/designer/form/create
Content-Type: application/json

{
  "name": "Form1",
  "title": "Minha Janela",
  "type": "winforms",
  "language": "csharp"
}
```

### Production Build

```http
POST /api/ide/production/build
Content-Type: application/json

{
  "doc_url": "https://example.com/specs.json",
  "name": "AppProdução",
  "language": "csharp",
  "type": "winforms"
}
```

**Resposta:**
```json
{
  "success": true,
  "build_id": "build_xxx",
  "download_url": "/api/download/build_xxx",
  "package_path": "downloads/AppProducao_v1.0.0.zip"
}
```

---

## 🎨 Visual Designer

### Criar Form

```python
# Via API
form_data = {
    "name": "MainForm",
    "title": "My Application",
    "size": {"width": 800, "height": 600},
    "type": "winforms",
    "language": "csharp"
}

response = requests.post(
    "http://localhost:8000/api/ide/designer/form/create",
    json=form_data
)

form = response.json()
form_id = form['id']
```

### Adicionar Controles

```python
# Adicionar Button
control_data = {
    "type": "Button",
    "name": "btnSave",
    "properties": {
        "Text": "Salvar",
        "BackColor": "Blue"
    },
    "position": {"x": 100, "y": 50},
    "size": {"width": 100, "height": 30}
}

response = requests.post(
    f"http://localhost:8000/api/ide/designer/form/{form_id}/control/add",
    json=control_data
)
```

### Gerar Código

```python
# Gerar código C# WinForms
response = requests.get(
    f"http://localhost:8000/api/ide/designer/form/{form_id}/generate"
)

code = response.json()['code']

# code contém:
# - designer: Form1.Designer.cs
# - main: Form1.cs
# - program: Program.cs
```

---

## 🐛 Sistema de Debug

### Iniciar Debug

```python
# Start debug session
response = requests.post(
    "http://localhost:8000/api/ide/debug/start",
    json={"project_id": project_id}
)

session_id = response.json()['session_id']
```

### Set Breakpoint

```python
# Set breakpoint
response = requests.post(
    f"http://localhost:8000/api/ide/debug/{session_id}/breakpoint",
    json={
        "file": "Program.cs",
        "line": 15
    }
)
```

### Conectar via WebSocket

```javascript
const ws = new WebSocket('ws://localhost:8000/ws/debug');

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);

    if (data.type === 'breakpoint_hit') {
        console.log('Breakpoint hit!', data);
        // Show variables, stack trace, etc.
    }
};

// Step through code
ws.send(JSON.stringify({
    type: 'debug_step',
    session_id: session_id,
    action: 'step_over'
}));
```

---

## 🏭 Production Pipeline

### Build de Produção

#### Opção 1: Via URL de Documentação

```python
response = requests.post(
    "http://localhost:8000/api/ide/production/build",
    json={
        "doc_url": "https://docs.myapp.com/specs.json",
        "language": "csharp",
        "type": "winforms"
    }
)

result = response.json()
download_url = result['download_url']

# Download do package
package = requests.get(f"http://localhost:8000{download_url}")
with open('app.zip', 'wb') as f:
    f.write(package.content)
```

#### Opção 2: Via Arquivo de Credenciais

```python
# credentials.json
{
    "name": "MyApp",
    "language": "csharp",
    "type": "winforms",
    "version": "1.0.0",
    "features": [
        "database_connection",
        "user_authentication",
        "reporting"
    ],
    "database": {
        "type": "postgresql",
        "connection_string": "..."
    }
}

# Build
response = requests.post(
    "http://localhost:8000/api/ide/production/build",
    json={
        "credentials_file": "credentials.json"
    }
)
```

### Processo de Production Build

1. **Parse Specs** - Lê especificações (URL ou arquivo)
2. **Generate Project** - Cria projeto baseado nas specs
3. **Generate Code** - IA gera código necessário
4. **Build** - Compila para executável
5. **Package** - Cria ZIP com exe + readme
6. **Upload** - Disponibiliza para download

---

## 📐 Exemplo Completo: Criar App WinForms

### 1. Criar Projeto

```python
import requests

API_URL = "http://localhost:8000"

# Criar projeto
project_response = requests.post(
    f"{API_URL}/api/ide/project/create",
    json={
        "name": "MeuApp",
        "language": "csharp",
        "type": "winforms"
    }
)

project = project_response.json()
project_id = project['id']
print(f"Projeto criado: {project_id}")
```

### 2. Criar Form Visual

```python
# Criar form
form_response = requests.post(
    f"{API_URL}/api/ide/designer/form/create",
    json={
        "name": "MainForm",
        "title": "Meu Aplicativo",
        "size": {"width": 800, "height": 600},
        "type": "winforms",
        "language": "csharp"
    }
)

form = form_response.json()
form_id = form['id']

# Adicionar Label
requests.post(
    f"{API_URL}/api/ide/designer/form/{form_id}/control/add",
    json={
        "type": "Label",
        "name": "lblTitle",
        "properties": {"Text": "Bem-vindo!"},
        "position": {"x": 200, "y": 50},
        "size": {"width": 200, "height": 30}
    }
)

# Adicionar TextBox
requests.post(
    f"{API_URL}/api/ide/designer/form/{form_id}/control/add",
    json={
        "type": "TextBox",
        "name": "txtNome",
        "properties": {},
        "position": {"x": 200, "y": 100},
        "size": {"width": 300, "height": 25}
    }
)

# Adicionar Button
requests.post(
    f"{API_URL}/api/ide/designer/form/{form_id}/control/add",
    json={
        "type": "Button",
        "name": "btnSalvar",
        "properties": {"Text": "Salvar"},
        "position": {"x": 250, "y": 150},
        "size": {"width": 100, "height": 30}
    }
)
```

### 3. Gerar Código

```python
# Gerar código do form
code_response = requests.get(
    f"{API_URL}/api/ide/designer/form/{form_id}/generate"
)

code = code_response.json()['code']

# Salvar arquivos no projeto
# code['designer'] -> MainForm.Designer.cs
# code['main'] -> MainForm.cs
# code['program'] -> Program.cs
```

### 4. Build

```python
# Build projeto
build_response = requests.post(
    f"{API_URL}/api/ide/project/{project_id}/build",
    json={"config": "Release"}
)

build_result = build_response.json()

if build_result['success']:
    exe_path = build_result['exe_path']
    print(f"Build sucesso! EXE: {exe_path}")
else:
    print(f"Build falhou: {build_result.get('errors')}")
```

### 5. Download

```python
# Se foi production build
if 'download_url' in build_result:
    download_url = build_result['download_url']

    # Download do ZIP
    package_response = requests.get(f"{API_URL}{download_url}")

    with open('MeuApp_Release.zip', 'wb') as f:
        f.write(package_response.content)

    print("Package baixado: MeuApp_Release.zip")
```

---

## 🔧 Configuração

### MSBuild (C#/VB.NET)

Para compilar projetos .NET, você precisa:

1. **Visual Studio 2022** ou
2. **Build Tools for Visual Studio 2022**

Download: https://visualstudio.microsoft.com/downloads/

### Java

```bash
# Instalar JDK
choco install openjdk

# Verificar
javac -version
```

### Python

```bash
# Instalar PyInstaller
pip install pyinstaller
```

### C++

```bash
# Instalar MinGW
choco install mingw

# Verificar
g++ --version
```

---

## 📊 Gerenciamento de Versões

### Atualizar Versão

```python
response = requests.post(
    f"{API_URL}/api/ide/project/{project_id}/version",
    json={"version": "2.0.0"}
)
```

### Build Múltiplas Versões

```python
# Build versão 1.0.0
build_v1 = requests.post(
    f"{API_URL}/api/ide/project/{project_id}/build",
    json={"config": "Release", "version": "1.0.0"}
)

# Atualizar para 2.0.0
update_version(project_id, "2.0.0")

# Build versão 2.0.0
build_v2 = requests.post(
    f"{API_URL}/api/ide/project/{project_id}/build",
    json={"config": "Release", "version": "2.0.0"}
)
```

---

## 🤖 AI Code Improver

### Melhorar Código Automaticamente

```python
# Analisar projeto
response = requests.post(
    f"{API_URL}/api/ide/ai/improve",
    json={"project_id": project_id}
)

suggestions = response.json()['suggestions']

for suggestion in suggestions:
    print(f"[{suggestion['type']}] {suggestion['message']}")
    # Ex: [performance] Use StringBuilder instead of string concatenation
```

### Aplicar Melhorias

```python
# Aplicar todas sugestões automaticamente
response = requests.post(
    f"{API_URL}/api/ide/ai/improve/apply",
    json={
        "project_id": project_id,
        "auto_apply": True
    }
)
```

---

## 🎯 Casos de Uso

### Caso 1: Criar App Desktop Rápido

```bash
# 1. Criar projeto WinForms
# 2. Usar Visual Designer para criar interface
# 3. Gerar código automaticamente
# 4. Build para .exe
# 5. Download e distribuir
```

### Caso 2: Desenvolvimento com Debug

```bash
# 1. Criar projeto
# 2. Escrever código
# 3. Definir breakpoints
# 4. Iniciar debug
# 5. Step through, inspecionar variáveis
# 6. Corrigir bugs
# 7. Build final
```

### Caso 3: Production Build Automatizado

```bash
# 1. Cliente envia URL da documentação
# 2. NEX lê especificações
# 3. IA gera projeto completo
# 4. Build automático
# 5. Package e download
# 6. Cliente recebe .zip com .exe pronto
```

---

## 📚 Documentação Completa

- **NEX Platform**: `C:\nex\README.md`
- **Installation**: `COMO_INSTALAR_NEX.md`
- **IDE Builder**: Este documento
- **API Reference**: http://localhost:8000/docs

---

## 🚀 Começar Agora

```cmd
# 1. Instalar NEX
cd C:\nex
INSTALAR_NEX.bat

# 2. Iniciar
INICIAR_NEX.bat

# 3. Testar IDE Builder
# Abra: http://localhost:8000/docs
# Teste: POST /api/ide/project/create
```

---

**NEX IDE Builder** - Build anything, anywhere! 🔨🚀
