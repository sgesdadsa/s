"""
Teste Simples - Verifica se o basico funciona
Execute: python test_simple.py
"""

import sys
import os

print("=" * 50)
print("MyLLM CLI - Teste Simples")
print("=" * 50)
print()

# Teste 1: Python version
print("[1/6] Testando versão do Python...")
print(f"  Python {sys.version}")
if sys.version_info < (3, 8):
    print("  ERRO: Python 3.8+ necessário")
    sys.exit(1)
print("  ✓ OK")
print()

# Teste 2: Import basico
print("[2/6] Testando imports básicos...")
try:
    import json
    import pathlib
    print("  ✓ Módulos padrão OK")
except ImportError as e:
    print(f"  ✗ ERRO: {e}")
    sys.exit(1)
print()

# Teste 3: Dependencias opcionais
print("[3/6] Testando dependências opcionais...")
missing = []

try:
    import click
    print("  ✓ click instalado")
except ImportError:
    print("  ✗ click NÃO instalado")
    missing.append("click")

try:
    import rich
    print("  ✓ rich instalado")
except ImportError:
    print("  ✗ rich NÃO instalado")
    missing.append("rich")

try:
    import llama_cpp
    print("  ✓ llama-cpp-python instalado")
except ImportError:
    print("  ✗ llama-cpp-python NÃO instalado (opcional)")

try:
    import fastapi
    print("  ✓ fastapi instalado")
except ImportError:
    print("  ✗ fastapi NÃO instalado")
    missing.append("fastapi")

print()

# Teste 4: Estrutura do projeto
print("[4/6] Verificando estrutura do projeto...")
if os.path.exists("myllm"):
    print("  ✓ Diretório myllm/ existe")

    files = ["__init__.py", "cli.py", "config.py", "models.py", "chat.py", "server.py"]
    for f in files:
        path = os.path.join("myllm", f)
        if os.path.exists(path):
            print(f"  ✓ {f} existe")
        else:
            print(f"  ✗ {f} NÃO existe")
else:
    print("  ✗ Diretório myllm/ NÃO encontrado")
    print("  Execute este script dentro do diretório myllm-cli/")
    sys.exit(1)
print()

# Teste 5: Setup.py
print("[5/6] Verificando setup.py...")
if os.path.exists("setup.py"):
    print("  ✓ setup.py existe")
else:
    print("  ✗ setup.py NÃO existe")
print()

# Teste 6: Import do módulo
print("[6/6] Testando import do módulo myllm...")
try:
    sys.path.insert(0, os.getcwd())
    import myllm
    print(f"  ✓ Módulo myllm importado com sucesso")
    print(f"  Versão: {getattr(myllm, '__version__', 'unknown')}")
except Exception as e:
    print(f"  ✗ ERRO ao importar: {e}")
    import traceback
    traceback.print_exc()
print()

# Resumo
print("=" * 50)
print("RESUMO")
print("=" * 50)

if missing:
    print("❌ Dependências faltando:")
    for dep in missing:
        print(f"   - {dep}")
    print()
    print("Para instalar:")
    print(f"   pip install {' '.join(missing)}")
else:
    print("✅ Todas as dependências básicas instaladas!")

print()
print("Próximos passos:")
print("  1. Se faltam deps: pip install click rich fastapi uvicorn")
print("  2. Instalar MyLLM: pip install -e .")
print("  3. Ou executar diretamente: python -m myllm.cli --help")
print()
