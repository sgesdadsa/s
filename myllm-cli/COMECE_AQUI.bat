@echo off
REM ================================================
REM COMECE AQUI - Script de Inicio para MyLLM CLI
REM ================================================

color 0A
cls

echo.
echo  ============================================
echo    MyLLM CLI - Instalacao e Configuracao
echo  ============================================
echo.
echo  Este script ira guia-lo pela instalacao
echo.
pause

:menu
cls
echo.
echo  ============================================
echo    MyLLM CLI - Menu Principal
echo  ============================================
echo.
echo  1. Executar Diagnostico
echo  2. Instalar Dependencias Basicas
echo  3. Instalar MyLLM CLI
echo  4. Testar Instalacao
echo  5. Configurar e Usar
echo  6. Solucionar Problemas
echo  7. Sair
echo.
echo  ============================================
echo.

set /p choice="Escolha uma opcao (1-7): "

if "%choice%"=="1" goto diagnose
if "%choice%"=="2" goto install_deps
if "%choice%"=="3" goto install_myllm
if "%choice%"=="4" goto test
if "%choice%"=="5" goto configure
if "%choice%"=="6" goto troubleshoot
if "%choice%"=="7" goto end

echo Opcao invalida!
timeout /t 2 >nul
goto menu

:diagnose
cls
echo.
echo  ============================================
echo    Executando Diagnostico...
echo  ============================================
echo.

if exist diagnose.bat (
    call diagnose.bat
) else (
    echo Arquivo diagnose.bat nao encontrado!
    echo.
    echo Execute este script dentro da pasta myllm-cli\
    pause
    goto menu
)

pause
goto menu

:install_deps
cls
echo.
echo  ============================================
echo    Instalando Dependencias Basicas
echo  ============================================
echo.

echo Verificando Python...
python --version
if errorlevel 1 (
    echo.
    echo ERRO: Python nao encontrado!
    echo.
    echo Instale Python 3.8+ de:
    echo https://www.python.org/downloads/
    echo.
    echo IMPORTANTE: Marque "Add Python to PATH" durante a instalacao!
    echo.
    pause
    goto menu
)

echo.
echo Atualizando pip...
python -m pip install --upgrade pip setuptools wheel

echo.
echo Instalando bibliotecas essenciais...
pip install click rich requests pyyaml tabulate

echo.
echo Instalando FastAPI e Uvicorn...
pip install fastapi uvicorn pydantic

echo.
echo ============================================
echo  Dependencias basicas instaladas!
echo ============================================
echo.
echo NOTA: llama-cpp-python nao foi instalado ainda.
echo       Isso requer Visual Studio Build Tools.
echo.
echo Para usar modelos GGUF, voce precisara instalar:
echo   pip install llama-cpp-python
echo.
echo Com GPU NVIDIA (CUDA):
echo   pip install llama-cpp-python --force-reinstall --no-cache-dir
echo.
pause
goto menu

:install_myllm
cls
echo.
echo  ============================================
echo    Instalando MyLLM CLI
echo  ============================================
echo.

echo Instalando MyLLM CLI em modo desenvolvimento...
echo.

pip install -e .

if errorlevel 1 (
    echo.
    echo ERRO na instalacao!
    echo.
    echo Tente:
    echo   1. Execute como Administrador
    echo   2. Ou tente: pip install -e . --user
    echo   3. Ou veja: TROUBLESHOOTING_WINDOWS.md
    echo.
    pause
    goto menu
)

echo.
echo ============================================
echo  MyLLM CLI instalado com sucesso!
echo ============================================
echo.
pause
goto menu

:test
cls
echo.
echo  ============================================
echo    Testando Instalacao
echo  ============================================
echo.

echo [1/3] Teste simples...
if exist test_simple.py (
    python test_simple.py
) else (
    echo test_simple.py nao encontrado!
)

echo.
echo [2/3] Testando comando myllm...
myllm --version 2>nul
if errorlevel 1 (
    echo.
    echo Comando 'myllm' nao funciona diretamente.
    echo.
    echo Tentando metodo alternativo...
    python -m myllm.cli --version 2>nul
    if errorlevel 1 (
        echo.
        echo ERRO: MyLLM nao esta instalado corretamente!
        echo.
        echo Execute a opcao 3 (Instalar MyLLM CLI) primeiro.
        echo.
    ) else (
        echo.
        echo OK! Use: python -m myllm.cli
        echo.
    )
) else (
    echo OK! Comando 'myllm' funciona!
)

echo.
echo [3/3] Testando help...
echo.
myllm --help 2>nul
if errorlevel 1 (
    python -m myllm.cli --help 2>nul
)

echo.
pause
goto menu

:configure
cls
echo.
echo  ============================================
echo    Configurar e Usar MyLLM CLI
echo  ============================================
echo.

echo Primeiro, vamos configurar o diretorio dos modelos.
echo.
echo Onde estao seus arquivos .gguf?
echo Exemplo: C:\progeto\lmstudio-community
echo.

set /p models_dir="Digite o caminho completo: "

if "%models_dir%"=="" (
    echo Nenhum caminho fornecido!
    pause
    goto menu
)

echo.
echo Configurando diretorio: %models_dir%
echo.

REM Tentar comando direto
myllm config set models_directory "%models_dir%" 2>nul
if errorlevel 1 (
    REM Tentar metodo alternativo
    python -m myllm.cli config set models_directory "%models_dir%"
)

echo.
echo Verificando modelos disponiveis...
echo.

myllm ls 2>nul
if errorlevel 1 (
    python -m myllm.cli ls
)

echo.
echo ============================================
echo.
echo Comandos uteis:
echo.
echo   Ver modelos:     myllm ls
echo   Carregar modelo: myllm load nome-do-modelo
echo   Chat:            myllm chat
echo   Configuracao:    myllm config show
echo   Ajuda:           myllm --help
echo.
echo Se 'myllm' nao funcionar, use:
echo   python -m myllm.cli <comando>
echo.
echo Exemplo:
echo   python -m myllm.cli ls
echo   python -m myllm.cli config show
echo.
pause
goto menu

:troubleshoot
cls
echo.
echo  ============================================
echo    Solucionar Problemas
echo  ============================================
echo.
echo.
echo Problemas comuns:
echo.
echo 1. "Python nao reconhecido"
echo    - Reinstale Python e marque "Add to PATH"
echo.
echo 2. "myllm nao reconhecido"
echo    - Use: python -m myllm.cli ao inves de myllm
echo    - Ou adicione Scripts ao PATH
echo.
echo 3. "Failed to install llama-cpp-python"
echo    - Instale Visual Studio Build Tools
echo    - Ou use sem ele (CLI funciona sem modelos)
echo.
echo 4. "ModuleNotFoundError"
echo    - Execute opcao 2 (Instalar Dependencias)
echo.
echo Para detalhes completos, leia:
echo   TROUBLESHOOTING_WINDOWS.md
echo.
echo.
set /p view="Abrir guia de solucao de problemas? (s/n): "
if /i "%view%"=="s" (
    if exist TROUBLESHOOTING_WINDOWS.md (
        start notepad TROUBLESHOOTING_WINDOWS.md
    )
)
pause
goto menu

:end
cls
echo.
echo  ============================================
echo    MyLLM CLI - Obrigado!
echo  ============================================
echo.
echo  Para usar MyLLM CLI:
echo.
echo    myllm --help
echo.
echo  Ou:
echo.
echo    python -m myllm.cli --help
echo.
echo  Documentacao completa:
echo    - README.md
echo    - WINDOWS_GUIDE.md
echo    - QUICKSTART.md
echo    - TROUBLESHOOTING_WINDOWS.md
echo.
echo  ============================================
echo.
timeout /t 3
exit /b 0
