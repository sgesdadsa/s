@echo off
REM Build MyLLM Studio as standalone executable

echo ============================================
echo   MyLLM Studio - Build Script
echo ============================================
echo.

echo [1/5] Checking PyInstaller...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo PyInstaller not found. Installing...
    pip install pyinstaller
)
echo OK: PyInstaller ready
echo.

echo [2/5] Installing dependencies...
pip install uvicorn fastapi websockets
echo OK: Dependencies installed
echo.

echo [3/5] Creating build specification...
echo.

REM Create PyInstaller spec file
python -c "import PyInstaller.__main__; PyInstaller.__main__.run([
    '--name=MyLLM-Studio',
    '--onefile',
    '--windowed',
    '--icon=NONE',
    '--hidden-import=uvicorn',
    '--hidden-import=fastapi',
    '--hidden-import=websockets',
    '--hidden-import=myllm.studio_server',
    '--hidden-import=myllm.studio_cli',
    '--add-data=myllm;myllm',
    'run_studio.py'
])"

if errorlevel 1 (
    echo Build failed!
    pause
    exit /b 1
)

echo.
echo ============================================
echo   Build Complete!
echo ============================================
echo.
echo Executable location:
echo   dist\MyLLM-Studio.exe
echo.
echo To run:
echo   dist\MyLLM-Studio.exe
echo.
echo Or double-click the file in the dist folder.
echo.
pause
