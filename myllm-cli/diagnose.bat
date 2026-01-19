@echo off
REM Script de Diagnóstico para MyLLM CLI
echo ====================================
echo MyLLM CLI - Diagnostico
echo ====================================
echo.

echo [1/5] Verificando Python...
python --version
if errorlevel 1 (
    echo ERRO: Python nao encontrado!
    echo Instale Python 3.8+ de: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo OK: Python encontrado
echo.

echo [2/5] Verificando pip...
pip --version
if errorlevel 1 (
    echo ERRO: pip nao encontrado!
    pause
    exit /b 1
)
echo OK: pip encontrado
echo.

echo [3/5] Testando imports basicos...
python -c "import sys; print('Python OK')"
if errorlevel 1 (
    echo ERRO: Problema com Python
    pause
    exit /b 1
)
echo OK: Python funcional
echo.

echo [4/5] Verificando dependencias instaladas...
echo Checando: click
python -c "import click" 2>nul
if errorlevel 1 (
    echo   FALTANDO: click
    set MISSING=1
) else (
    echo   OK: click
)

echo Checando: rich
python -c "import rich" 2>nul
if errorlevel 1 (
    echo   FALTANDO: rich
    set MISSING=1
) else (
    echo   OK: rich
)

echo Checando: llama_cpp
python -c "import llama_cpp" 2>nul
if errorlevel 1 (
    echo   FALTANDO: llama-cpp-python
    set MISSING=1
) else (
    echo   OK: llama-cpp-python
)

echo Checando: fastapi
python -c "import fastapi" 2>nul
if errorlevel 1 (
    echo   FALTANDO: fastapi
    set MISSING=1
) else (
    echo   OK: fastapi
)

echo Checando: uvicorn
python -c "import uvicorn" 2>nul
if errorlevel 1 (
    echo   FALTANDO: uvicorn
    set MISSING=1
) else (
    echo   OK: uvicorn
)

echo.

if defined MISSING (
    echo [!] Algumas dependencias estao faltando!
    echo.
    set /p INSTALL="Deseja instalar as dependencias agora? (s/n): "
    if /i "%INSTALL%"=="s" (
        echo.
        echo Instalando dependencias...
        pip install click rich requests pyyaml tabulate
        echo.
        echo Instalando FastAPI e Uvicorn...
        pip install fastapi uvicorn pydantic
        echo.
        echo NOTA: llama-cpp-python sera instalado depois
        echo Por enquanto, vamos testar sem ele
    )
) else (
    echo [OK] Todas as dependencias basicas instaladas!
)

echo.
echo [5/5] Verificando instalacao do MyLLM...
where myllm >nul 2>&1
if errorlevel 1 (
    echo [!] MyLLM CLI nao esta instalado
    echo.
    echo Para instalar, execute:
    echo   pip install -e .
    echo.
    echo Ou tente executar diretamente:
    echo   python -m myllm.cli --help
) else (
    echo [OK] MyLLM CLI instalado!
    echo.
    echo Testando comando...
    myllm --help
)

echo.
echo ====================================
echo Diagnostico Concluido
echo ====================================
echo.
echo Proximos passos:
echo   1. Se faltam dependencias, instale-as
echo   2. Para instalar MyLLM: pip install -e .
echo   3. Para usar: myllm --help
echo.
pause
