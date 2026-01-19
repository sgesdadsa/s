@echo off
REM Instalacao Basica - Sem llama-cpp-python
echo ====================================
echo MyLLM CLI - Instalacao Basica
echo ====================================
echo.
echo Esta instalacao NAO inclui llama-cpp-python
echo Isso permite testar a CLI sem compilar bibliotecas C++
echo.

echo [1/3] Instalando dependencias basicas...
pip install click rich requests pyyaml tabulate
if errorlevel 1 (
    echo ERRO ao instalar dependencias basicas
    pause
    exit /b 1
)

echo.
echo [2/3] Instalando FastAPI e Uvicorn...
pip install fastapi uvicorn pydantic
if errorlevel 1 (
    echo ERRO ao instalar FastAPI
    pause
    exit /b 1
)

echo.
echo [3/3] Instalando MyLLM CLI...
pip install -e .
if errorlevel 1 (
    echo ERRO ao instalar MyLLM CLI
    pause
    exit /b 1
)

echo.
echo ====================================
echo Instalacao Basica Concluida!
echo ====================================
echo.
echo NOTA: Para carregar modelos GGUF, voce precisara instalar:
echo   pip install llama-cpp-python
echo.
echo Ou com suporte CUDA (GPU NVIDIA):
echo   pip install llama-cpp-python --force-reinstall --no-cache-dir
echo.
echo Por enquanto, voce pode testar a CLI:
echo   myllm --help
echo   myllm config show
echo.
pause
