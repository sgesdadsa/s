@echo off
REM MyLLM CLI Installation Script for Windows

echo ================================
echo MyLLM CLI Installation
echo ================================
echo.

REM Check Python version
echo Checking Python version...
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed.
    echo Please install Python 3.8 or higher from https://www.python.org/
    pause
    exit /b 1
)

python --version
echo.

REM Check pip
echo Checking pip...
pip --version >nul 2>&1
if errorlevel 1 (
    echo Error: pip is not installed.
    echo Please ensure pip is installed with Python.
    pause
    exit /b 1
)

echo pip found
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install dependencies.
    pause
    exit /b 1
)

echo Dependencies installed
echo.

REM Install MyLLM CLI
echo Installing MyLLM CLI...
pip install -e .
if errorlevel 1 (
    echo Error: Failed to install MyLLM CLI.
    pause
    exit /b 1
)

echo MyLLM CLI installed
echo.

REM Test installation
echo Testing installation...
myllm --version >nul 2>&1
if errorlevel 1 (
    echo Warning: Installation may be incomplete.
    echo Try running: myllm --help
) else (
    echo Installation successful!
)

echo.
echo ================================
echo Installation Complete!
echo ================================
echo.
echo Quick Start:
echo   1. Set your models directory:
echo      myllm config set models_directory "C:\progeto\lmstudio-community"
echo.
echo   2. List available models:
echo      myllm ls
echo.
echo   3. Load a model:
echo      myllm load gpt-oss-20b
echo.
echo   4. Start chatting:
echo      myllm chat
echo.
echo For more information, run: myllm --help
echo.

pause
