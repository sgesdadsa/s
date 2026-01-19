@echo off
REM Script de Inicialização do MyLLM Studio

title MyLLM Studio
color 0A

cls
echo.
echo  ================================================
echo     MyLLM Studio - Interface Visual
echo  ================================================
echo.

REM Verificar se está na pasta correta
if not exist "myllm" (
    echo ERRO: Execute este script dentro da pasta myllm-cli!
    echo.
    pause
    exit /b 1
)

REM Menu principal
:menu
cls
echo.
echo  ================================================
echo     MyLLM Studio - Menu de Inicializacao
echo  ================================================
echo.
echo  1. Iniciar MyLLM Studio (Navegador automatico)
echo  2. Iniciar Studio (Sem abrir navegador)
echo  3. Iniciar na porta personalizada
echo  4. Carregar modelo primeiro
echo  5. Ver status dos modelos
echo  6. Build executavel standalone
echo  7. Criar atalho no desktop
echo  8. Sair
echo.
echo  ================================================
echo.

set /p choice="Escolha uma opcao (1-8): "

if "%choice%"=="1" goto start_auto
if "%choice%"=="2" goto start_manual
if "%choice%"=="3" goto start_custom
if "%choice%"=="4" goto load_model
if "%choice%"=="5" goto check_status
if "%choice%"=="6" goto build_exe
if "%choice%"=="7" goto create_shortcut
if "%choice%"=="8" goto end

echo Opcao invalida!
timeout /t 2 >nul
goto menu

:start_auto
cls
echo.
echo  ================================================
echo     Iniciando MyLLM Studio...
echo  ================================================
echo.
echo  O navegador sera aberto automaticamente.
echo  URL: http://localhost:8090
echo.
echo  Pressione Ctrl+C para parar o servidor
echo  ================================================
echo.
timeout /t 2 >nul

python -m myllm.studio_cli start
if errorlevel 1 (
    echo.
    echo ERRO ao iniciar Studio!
    echo.
    echo Tente:
    echo   python run_studio.py
    echo.
    pause
)
goto menu

:start_manual
cls
echo.
echo  ================================================
echo     Iniciando MyLLM Studio (Sem navegador)...
echo  ================================================
echo.
echo  Abra manualmente: http://localhost:8090
echo.
echo  Pressione Ctrl+C para parar
echo  ================================================
echo.
timeout /t 2 >nul

python -m myllm.studio_cli start --no-browser
if errorlevel 1 (
    python run_studio.py
)
goto menu

:start_custom
cls
echo.
echo  ================================================
echo     Porta Personalizada
echo  ================================================
echo.
set /p port="Digite a porta (ex: 8091): "

if "%port%"=="" (
    echo Porta invalida!
    timeout /t 2 >nul
    goto menu
)

echo.
echo Iniciando na porta %port%...
echo URL: http://localhost:%port%
echo.
timeout /t 2 >nul

python -m myllm.studio_cli start --port %port%
goto menu

:load_model
cls
echo.
echo  ================================================
echo     Carregar Modelo
echo  ================================================
echo.
echo Modelos disponiveis:
echo.
python -m myllm.cli ls
echo.
echo ================================================
echo.
set /p model="Digite o nome do modelo para carregar: "

if "%model%"=="" (
    echo Nenhum modelo especificado!
    timeout /t 2 >nul
    goto menu
)

echo.
echo Carregando %model% com GPU maximo...
echo.
python -m myllm.cli load "%model%" --gpu max

echo.
echo Modelo carregado!
echo.
set /p start_studio="Iniciar Studio agora? (s/n): "

if /i "%start_studio%"=="s" (
    goto start_auto
)

pause
goto menu

:check_status
cls
echo.
echo  ================================================
echo     Status dos Modelos
echo  ================================================
echo.
python -m myllm.cli ps
echo.
echo ================================================
echo.
pause
goto menu

:build_exe
cls
echo.
echo  ================================================
echo     Build Executavel
echo  ================================================
echo.
echo Isso vai criar um executavel standalone.
echo Pode levar alguns minutos...
echo.
set /p confirm="Continuar? (s/n): "

if /i not "%confirm%"=="s" goto menu

echo.
call build_studio.bat
echo.
pause
goto menu

:create_shortcut
cls
echo.
echo  ================================================
echo     Criar Atalho
echo  ================================================
echo.

python -m myllm.studio_cli desktop

echo.
pause
goto menu

:end
cls
echo.
echo  ================================================
echo     Obrigado por usar MyLLM Studio!
echo  ================================================
echo.
echo  Para iniciar novamente:
echo    INICIAR_STUDIO.bat
echo.
echo  Ou diretamente:
echo    python -m myllm.studio_cli start
echo    python run_studio.py
echo.
echo  ================================================
echo.
timeout /t 3
exit /b 0
