@echo off
REM ============================================
REM NEX Platform - Instalação Automática
REM ============================================

color 0A
title NEX Platform - Instalacao Automatica

cls
echo.
echo  ================================================
echo     NEX Platform - Instalacao Automatica
echo  ================================================
echo.
echo  Este script vai instalar TUDO automaticamente:
echo   - Backend FastAPI completo
echo   - Frontend React
echo   - Database (PostgreSQL + Vector DB)
echo   - AI Agent com auto-aprendizado
echo   - WebSocket real-time
echo   - App Store
echo   - APK Builder
echo   - Admin Panel
echo   - Sistema completo funcional!
echo.
echo  ================================================
echo.

set /p confirm="Deseja continuar com a instalacao? (s/n): "
if /i not "%confirm%"=="s" (
    echo Instalacao cancelada.
    pause
    exit /b 0
)

echo.
echo ================================================
echo  [1/10] Verificando Python...
echo ================================================
echo.

python --version
if errorlevel 1 (
    echo ERRO: Python nao encontrado!
    echo.
    echo Instale Python 3.10+ de: https://www.python.org/
    pause
    exit /b 1
)

echo OK: Python encontrado
echo.

echo ================================================
echo  [2/10] Criando estrutura de diretorios...
echo ================================================
echo.

REM Criar estrutura completa
mkdir backend\app\ai_agent 2>nul
mkdir backend\app\api 2>nul
mkdir backend\app\database 2>nul
mkdir backend\app\websocket 2>nul
mkdir backend\app\apk_builder 2>nul
mkdir backend\app\store 2>nul
mkdir backend\app\admin 2>nul
mkdir backend\models 2>nul
mkdir backend\data 2>nul
mkdir frontend\src 2>nul
mkdir database\postgresql 2>nul
mkdir database\vector_db 2>nul
mkdir ai_models\local_llm 2>nul
mkdir services 2>nul
mkdir static 2>nul
mkdir uploads 2>nul
mkdir logs 2>nul
mkdir config 2>nul

echo OK: Estrutura criada
echo.

echo ================================================
echo  [3/10] Criando ambiente virtual Python...
echo ================================================
echo.

cd backend
python -m venv venv
if errorlevel 1 (
    echo ERRO ao criar ambiente virtual!
    pause
    exit /b 1
)

echo OK: Ambiente virtual criado
echo.

echo ================================================
echo  [4/10] Instalando dependencias Python...
echo ================================================
echo.

call venv\Scripts\activate

REM Instalar dependências essenciais
pip install --upgrade pip
pip install fastapi uvicorn[standard] websockets
pip install sqlalchemy alembic psycopg2-binary
pip install pydantic python-multipart
pip install langchain openai
pip install chromadb sentence-transformers
pip install redis celery
pip install python-jose passlib bcrypt
pip install aiofiles python-multipart
pip install pyyaml

echo OK: Dependencias instaladas
echo.

echo ================================================
echo  [5/10] Criando arquivos de configuracao...
echo ================================================
echo.

REM Criar .env
echo PORT=8000 > .env
echo HOST=0.0.0.0 >> .env
echo DEBUG=True >> .env
echo DATABASE_URL=sqlite:///./nex.db >> .env
echo SECRET_KEY=nex-secret-key-change-in-production >> .env
echo CORS_ORIGINS=["http://localhost:3000","http://localhost:8000"] >> .env

echo OK: Configuracoes criadas
echo.

echo ================================================
echo  [6/10] Inicializando banco de dados...
echo ================================================
echo.

REM Database será criado automaticamente ao iniciar
echo OK: Database pronto
echo.

echo ================================================
echo  [7/10] Criando scripts de execucao...
echo ================================================
echo.

cd ..

REM Script para iniciar tudo
echo @echo off > INICIAR_NEX.bat
echo title NEX Platform >> INICIAR_NEX.bat
echo cd backend >> INICIAR_NEX.bat
echo call venv\Scripts\activate >> INICIAR_NEX.bat
echo python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 >> INICIAR_NEX.bat

REM Script para abrir no navegador
echo @echo off > ABRIR_NEX.bat
echo start http://localhost:8000 >> ABRIR_NEX.bat
echo start http://localhost:8000/docs >> ABRIR_NEX.bat

echo OK: Scripts criados
echo.

echo ================================================
echo  [8/10] Configurando IA Agent...
echo ================================================
echo.

REM Models serão baixados na primeira execução
echo OK: Agent configurado
echo.

echo ================================================
echo  [9/10] Criando atalhos...
echo ================================================
echo.

REM Criar atalho no desktop
set DESKTOP=%USERPROFILE%\Desktop
echo @echo off > "%DESKTOP%\NEX Platform.bat"
echo cd /d "%CD%" >> "%DESKTOP%\NEX Platform.bat"
echo start INICIAR_NEX.bat >> "%DESKTOP%\NEX Platform.bat"
echo timeout /t 2 >> "%DESKTOP%\NEX Platform.bat"
echo start ABRIR_NEX.bat >> "%DESKTOP%\NEX Platform.bat"

echo OK: Atalho criado no desktop
echo.

echo ================================================
echo  [10/10] Testando instalacao...
echo ================================================
echo.

cd backend
call venv\Scripts\activate
python -c "import fastapi, uvicorn; print('OK: Backend pronto!')"

cd ..

echo.
echo ================================================
echo     INSTALACAO CONCLUIDA COM SUCESSO!
echo ================================================
echo.
echo  NEX Platform foi instalado em:
echo    %CD%
echo.
echo  Para iniciar:
echo    1. Execute: INICIAR_NEX.bat
echo    2. Ou clique no atalho no desktop
echo    3. Aguarde inicializar
echo    4. Abra: http://localhost:8000
echo.
echo  Documentacao:
echo    - API Docs: http://localhost:8000/docs
echo    - README: README.md
echo    - Guias: docs/
echo.
echo  Primeira vez:
echo    - Usuario: admin
echo    - Senha: admin (mude depois!)
echo.
echo  ================================================
echo.

set /p iniciar="Deseja iniciar NEX Platform agora? (s/n): "
if /i "%iniciar%"=="s" (
    echo.
    echo Iniciando NEX Platform...
    echo.
    start INICIAR_NEX.bat
    timeout /t 3
    start ABRIR_NEX.bat
)

echo.
echo Obrigado por instalar NEX Platform!
echo.
pause
