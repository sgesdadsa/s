@echo off
REM Daily usage script for MyLLM CLI
REM This script provides a menu for common tasks

:menu
cls
echo ========================================
echo     MyLLM CLI - Daily Usage Menu
echo ========================================
echo.
echo 1. Load Model and Chat
echo 2. Start API Server
echo 3. Stop API Server
echo 4. Check Server Status
echo 5. List Available Models
echo 6. List Loaded Models
echo 7. Unload All Models
echo 8. Configuration
echo 9. Exit
echo.
set /p choice="Select an option (1-9): "

if "%choice%"=="1" goto load_chat
if "%choice%"=="2" goto start_server
if "%choice%"=="3" goto stop_server
if "%choice%"=="4" goto server_status
if "%choice%"=="5" goto list_models
if "%choice%"=="6" goto loaded_models
if "%choice%"=="7" goto unload_all
if "%choice%"=="8" goto config_menu
if "%choice%"=="9" goto end

echo Invalid choice. Press any key to try again.
pause >nul
goto menu

:load_chat
cls
echo ========================================
echo     Load Model and Chat
echo ========================================
echo.
myllm ls
echo.
set /p model="Enter model name to load: "
if "%model%"=="" (
    echo No model specified.
    pause
    goto menu
)

echo.
echo Loading model: %model%
myllm load "%model%" --gpu max

if errorlevel 1 (
    echo.
    echo Failed to load model.
    pause
    goto menu
)

echo.
echo Starting chat session...
echo Type /exit to quit the chat.
echo.
pause
myllm chat
goto menu

:start_server
cls
echo ========================================
echo     Start API Server
echo ========================================
echo.
myllm ps
echo.
set /p confirm="Start server with loaded models? (y/n): "
if /i "%confirm%"=="y" (
    myllm server start
    echo.
    echo Server started! Press any key to continue.
    pause >nul
)
goto menu

:stop_server
cls
echo ========================================
echo     Stop API Server
echo ========================================
echo.
myllm server stop
echo.
pause
goto menu

:server_status
cls
echo ========================================
echo     Server Status
echo ========================================
echo.
myllm server status
echo.
pause
goto menu

:list_models
cls
echo ========================================
echo     Available Models
echo ========================================
echo.
myllm ls
echo.
pause
goto menu

:loaded_models
cls
echo ========================================
echo     Loaded Models
echo ========================================
echo.
myllm ps
echo.
pause
goto menu

:unload_all
cls
echo ========================================
echo     Unload All Models
echo ========================================
echo.
set /p confirm="Unload all models? (y/n): "
if /i "%confirm%"=="y" (
    myllm unload --all
    echo.
    echo All models unloaded.
)
echo.
pause
goto menu

:config_menu
cls
echo ========================================
echo     Configuration
echo ========================================
echo.
echo 1. Show current configuration
echo 2. Set models directory
echo 3. Set server port
echo 4. Back to main menu
echo.
set /p config_choice="Select an option (1-4): "

if "%config_choice%"=="1" (
    echo.
    myllm config show
    echo.
    pause
    goto config_menu
)

if "%config_choice%"=="2" (
    echo.
    set /p models_dir="Enter models directory path: "
    if not "%models_dir%"=="" (
        myllm config set models_directory "%models_dir%"
        echo Configuration updated.
    )
    echo.
    pause
    goto config_menu
)

if "%config_choice%"=="3" (
    echo.
    set /p port="Enter server port (default 8080): "
    if not "%port%"=="" (
        myllm config set server.port %port%
        echo Configuration updated.
    )
    echo.
    pause
    goto config_menu
)

if "%config_choice%"=="4" goto menu

echo Invalid choice.
pause
goto config_menu

:end
echo.
echo Thank you for using MyLLM CLI!
exit /b 0
