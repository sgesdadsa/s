@echo off
REM Quick Start Script for MyLLM CLI on Windows

echo ================================
echo MyLLM CLI - Quick Start
echo ================================
echo.

REM Check if myllm is installed
myllm --version >nul 2>&1
if errorlevel 1 (
    echo MyLLM CLI is not installed. Running installation...
    echo.
    call install.bat
    if errorlevel 1 (
        echo Installation failed. Please check the error messages above.
        pause
        exit /b 1
    )
)

echo MyLLM CLI is installed!
echo.

REM Configure models directory
echo Setting up models directory...
set DEFAULT_MODELS_DIR=C:\progeto\lmstudio-community
set /p MODELS_DIR="Enter your models directory [%DEFAULT_MODELS_DIR%]: "

if "%MODELS_DIR%"=="" set MODELS_DIR=%DEFAULT_MODELS_DIR%

echo Configuring models directory: %MODELS_DIR%
myllm config set models_directory "%MODELS_DIR%"
echo.

REM List available models
echo Scanning for models...
myllm ls
echo.

REM Ask if user wants to load a model
set /p LOAD_MODEL="Do you want to load a model now? (y/n): "

if /i "%LOAD_MODEL%"=="y" (
    echo.
    echo Available models listed above.
    echo.
    set /p MODEL_NAME="Enter model name or path: "

    if not "%MODEL_NAME%"=="" (
        echo Loading model: %MODEL_NAME%
        myllm load "%MODEL_NAME%" --gpu max
        echo.

        REM Ask if user wants to start chatting
        set /p START_CHAT="Start chatting now? (y/n): "
        if /i "%START_CHAT%"=="y" (
            echo.
            echo Starting chat session...
            echo Type /exit to quit the chat.
            echo.
            myllm chat
        )
    )
)

echo.
echo ================================
echo Quick Start Complete!
echo ================================
echo.
echo Useful commands:
echo   myllm ls              - List models
echo   myllm load ^<model^>    - Load a model
echo   myllm ps              - See loaded models
echo   myllm chat            - Start chatting
echo   myllm server start    - Start API server
echo   myllm --help          - Get help
echo.
echo For detailed documentation, see README.md
echo.

pause
