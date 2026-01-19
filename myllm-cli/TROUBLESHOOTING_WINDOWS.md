# Solução de Problemas - Windows

Guia completo para resolver problemas no Windows.

## 🔍 Diagnóstico Rápido

Execute o script de diagnóstico:

```cmd
diagnose.bat
```

Ele irá verificar:
- Python instalado
- pip funcionando
- Dependências instaladas
- MyLLM CLI instalado

## ❌ Problemas Comuns

### 1. "Python não é reconhecido"

**Sintoma:**
```
'python' não é reconhecido como um comando interno ou externo
```

**Solução:**

**Opção A**: Reinstalar Python
1. Baixe: https://www.python.org/downloads/
2. Durante instalação, **MARQUE**: "Add Python to PATH"
3. Clique "Install Now"
4. Reinicie o terminal

**Opção B**: Adicionar ao PATH manualmente
1. Encontre onde Python está instalado (geralmente `C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python3XX\`)
2. Abra "Variáveis de Ambiente" (Win + R > `sysdm.cpl` > Aba "Avançado")
3. Clique "Variáveis de Ambiente"
4. Em "Variáveis do Sistema", edite "Path"
5. Adicione:
   - `C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python3XX\`
   - `C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python3XX\Scripts\`

### 2. "pip não é reconhecido"

**Solução:**
```cmd
# Use python -m pip ao invés de pip
python -m pip install --upgrade pip
```

### 3. "myllm não é reconhecido"

**Sintoma:**
```
'myllm' não é reconhecido como um comando interno ou externo
```

**Soluções:**

**Opção A**: Use python -m
```cmd
python -m myllm.cli --help
```

**Opção B**: Reinstale com pip
```cmd
cd C:\myllm-cli
pip uninstall myllm -y
pip install -e .
```

**Opção C**: Adicione Scripts ao PATH
Adicione às variáveis de ambiente:
```
C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python3XX\Scripts
```

### 4. "Failed to install llama-cpp-python"

**Sintoma:**
```
ERROR: Could not build wheels for llama-cpp-python
Microsoft Visual C++ 14.0 or greater is required
```

**Causa:** Falta o compilador C++ do Visual Studio

**Solução 1 - Instalar Build Tools (Recomendado):**

1. Baixe: https://visualstudio.microsoft.com/downloads/
2. Role até "Tools for Visual Studio"
3. Baixe "Build Tools for Visual Studio 2022"
4. Execute o instalador
5. Selecione "Desktop development with C++"
6. Clique "Install"
7. Reinicie o computador
8. Tente novamente:
```cmd
pip install llama-cpp-python
```

**Solução 2 - Pular llama-cpp-python (Temporário):**

Use a instalação básica sem suporte a modelos:
```cmd
install_basic.bat
```

Isso instala tudo exceto llama-cpp-python, permitindo testar a CLI.

### 5. "ModuleNotFoundError: No module named 'click'"

**Sintoma:**
```
ModuleNotFoundError: No module named 'click'
# ou
ModuleNotFoundError: No module named 'rich'
```

**Solução:**
```cmd
# Instale as dependências básicas
pip install click rich requests pyyaml tabulate fastapi uvicorn pydantic
```

### 6. "ImportError: DLL load failed"

**Sintoma:**
```
ImportError: DLL load failed while importing _ctypes
```

**Solução:**

1. Reinstale Python
2. Ou instale Visual C++ Redistributable:
   - Baixe: https://aka.ms/vs/17/release/vc_redist.x64.exe
   - Execute o instalador

### 7. "PermissionError" ao instalar

**Sintoma:**
```
PermissionError: [WinError 5] Access is denied
```

**Solução:**

**Opção A**: Execute como Administrador
```cmd
# Clique direito no CMD/PowerShell
# "Executar como Administrador"
pip install -e .
```

**Opção B**: Instale para o usuário
```cmd
pip install -e . --user
```

### 8. Setup.py não funciona

**Sintoma:**
```
error: invalid command 'bdist_wheel'
```

**Solução:**
```cmd
pip install --upgrade setuptools wheel
pip install -e .
```

## 🔧 Instalação Passo a Passo (Do Zero)

Se nada funcionou, siga este processo completo:

### Passo 1: Limpar Instalações Antigas

```cmd
pip uninstall myllm -y
pip uninstall llama-cpp-python -y
```

### Passo 2: Atualizar pip e setuptools

```cmd
python -m pip install --upgrade pip setuptools wheel
```

### Passo 3: Instalar Dependências Básicas

```cmd
pip install click rich requests pyyaml tabulate
pip install fastapi uvicorn pydantic
```

### Passo 4: Testar Instalação Básica

```cmd
cd C:\myllm-cli
python test_simple.py
```

Se tudo estiver OK, continue.

### Passo 5: Instalar MyLLM CLI

```cmd
pip install -e .
```

### Passo 6: Testar

**Opção A**: Comando direto
```cmd
myllm --help
```

**Opção B**: Python module
```cmd
python -m myllm.cli --help
```

### Passo 7: (Opcional) Instalar llama-cpp-python

Apenas se você tem Visual Studio Build Tools instalado:

```cmd
pip install llama-cpp-python
```

Com CUDA (GPU NVIDIA):
```cmd
set CMAKE_ARGS=-DLLAMA_CUBLAS=on
pip install llama-cpp-python --force-reinstall --no-cache-dir
```

## 🧪 Scripts de Teste

### Teste 1: Verificar Python
```cmd
python --version
python -c "import sys; print(sys.executable)"
```

### Teste 2: Verificar pip
```cmd
pip --version
python -m pip --version
```

### Teste 3: Verificar Módulos
```cmd
python -c "import click; print('click OK')"
python -c "import rich; print('rich OK')"
python -c "import fastapi; print('fastapi OK')"
```

### Teste 4: Verificar MyLLM
```cmd
python test_simple.py
```

### Teste 5: Importar MyLLM
```cmd
python -c "import myllm; print(myllm.__version__)"
```

## 🎯 Instalação Alternativa

Se a instalação normal não funcionar, use este método alternativo:

### Método 1: Sem pip install -e

Adicione o diretório ao PYTHONPATH:

```cmd
# No PowerShell
$env:PYTHONPATH="C:\myllm-cli"
python C:\myllm-cli\myllm\cli.py --help
```

```cmd
# No CMD
set PYTHONPATH=C:\myllm-cli
python C:\myllm-cli\myllm\cli.py --help
```

### Método 2: Criar Executável Batch

Crie `myllm.bat` em `C:\myllm-cli\`:

```batch
@echo off
python C:\myllm-cli\myllm\cli.py %*
```

Adicione `C:\myllm-cli` ao PATH e use:
```cmd
myllm --help
```

### Método 3: Python -m sempre

Crie um alias/script:

`run_myllm.bat`:
```batch
@echo off
cd C:\myllm-cli
python -m myllm.cli %*
```

## 📝 Checklist de Diagnóstico

Use esta checklist para identificar o problema:

- [ ] Python 3.8+ instalado
- [ ] Python no PATH
- [ ] pip funciona
- [ ] Dependências instaladas (click, rich, etc)
- [ ] MyLLM importa sem erros: `python -c "import myllm"`
- [ ] Scripts dentro de myllm-cli/
- [ ] setup.py existe
- [ ] myllm --help funciona (ou python -m myllm.cli --help)

## 🆘 Ainda Não Funciona?

Se nada disso funcionou:

1. **Execute diagnose.bat** e copie a saída
2. **Execute test_simple.py** e copie a saída
3. **Copie erros exatos** que você está vendo
4. **Informe sua versão do Python**: `python --version`
5. **Informe seu Windows**: `winver`

### Informações Úteis para Debug

```cmd
# Sistema
winver
systeminfo | findstr /C:"OS"

# Python
python --version
python -c "import sys; print(sys.executable)"
python -c "import sys; print(sys.path)"

# pip
pip --version
pip list

# MyLLM
cd C:\myllm-cli
dir myllm
python test_simple.py
```

## ✅ Solução Rápida (Se tudo falhar)

Execute em sequência:

```cmd
cd C:\myllm-cli

REM 1. Diagnóstico
python test_simple.py

REM 2. Instalar deps básicas
pip install click rich requests pyyaml tabulate fastapi uvicorn pydantic

REM 3. Testar import
python -c "import myllm"

REM 4. Usar diretamente
python -m myllm.cli --help
python -m myllm.cli config show
```

Se isso funcionar, crie `myllm.bat`:
```batch
@echo off
cd C:\myllm-cli
python -m myllm.cli %*
```

E adicione `C:\myllm-cli` ao PATH.

## 💡 Dicas Finais

1. **Sempre use CMD como Administrador** para instalar
2. **Reinicie o terminal** após instalar Python ou modificar PATH
3. **Use `python -m pip`** ao invés de `pip` se houver problemas
4. **Use `python -m myllm.cli`** ao invés de `myllm` se houver problemas
5. **Não precisa de llama-cpp-python** para testar a CLI
6. **Instale Visual Studio Build Tools** só se for usar llama-cpp-python

Boa sorte! 🚀
