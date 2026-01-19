"""
NEX Platform - Main Application
FastAPI backend with AI Agent, WebSocket, Store, and Admin
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
import uvicorn

from app.ai_agent.agent_core import AgentCore
from app.database.core import engine, Base, get_db
from app.api import auth, users, apps, chat, admin, store
from app.websocket.manager import ConnectionManager
from app.config import settings

# Lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events"""
    # Startup
    print("🚀 Starting NEX Platform...")

    # Create database tables
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized")

    # Initialize AI Agent
    app.state.agent = AgentCore()
    await app.state.agent.initialize()
    print("✅ AI Agent initialized")

    # Initialize WebSocket manager
    app.state.ws_manager = ConnectionManager()
    print("✅ WebSocket manager initialized")

    print("🎉 NEX Platform ready!")

    yield

    # Shutdown
    print("👋 Shutting down NEX Platform...")
    await app.state.agent.shutdown()
    print("✅ Graceful shutdown complete")


# Create FastAPI app
app = FastAPI(
    title="NEX Platform",
    description="Plataforma Completa de IA Autônoma com Store de Apps",
    version="1.0.0",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(apps.router, prefix="/api/apps", tags=["Apps"])
app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])
app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])
app.include_router(store.router, prefix="/api/store", tags=["Store"])

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "NEX Platform API",
        "version": "1.0.0",
        "status": "running",
        "agent_status": app.state.agent.status,
        "docs": "/docs",
        "endpoints": {
            "auth": "/api/auth",
            "users": "/api/users",
            "apps": "/api/apps",
            "chat": "/api/chat",
            "admin": "/api/admin",
            "store": "/api/store",
            "websocket": "/ws"
        }
    }


@app.get("/health")
async def health():
    """Health check"""
    return {
        "status": "healthy",
        "agent": app.state.agent.is_healthy(),
        "database": "connected",
        "websocket": app.state.ws_manager.active_connections_count()
    }


@app.get("/api/agent/status")
async def agent_status():
    """Get AI Agent status"""
    return {
        "status": app.state.agent.status,
        "capabilities": app.state.agent.get_capabilities(),
        "memory_size": app.state.agent.get_memory_size(),
        "learning_progress": app.state.agent.get_learning_progress(),
        "improvements": app.state.agent.get_recent_improvements()
    }


# WebSocket endpoint
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    """WebSocket connection for real-time communication"""
    manager = app.state.ws_manager
    agent = app.state.agent

    await manager.connect(websocket, client_id)

    try:
        # Send welcome message
        await manager.send_personal({
            "type": "connected",
            "message": "Connected to NEX Platform",
            "agent_status": agent.status
        }, websocket)

        while True:
            # Receive message
            data = await websocket.receive_json()

            # Handle different message types
            message_type = data.get("type")

            if message_type == "chat":
                # Process chat message with AI
                user_message = data.get("message", "")

                # Send typing indicator
                await manager.broadcast({
                    "type": "typing",
                    "user": "Agent",
                    "status": True
                })

                # Get AI response
                response = await agent.process_message(user_message, client_id)

                # Send response
                await manager.broadcast({
                    "type": "chat_response",
                    "message": response,
                    "metadata": {
                        "model": agent.current_model,
                        "confidence": response.get("confidence", 0.9)
                    }
                })

            elif message_type == "command":
                # Execute command
                command = data.get("command", "")
                result = await agent.execute_command(command)

                await manager.send_personal({
                    "type": "command_result",
                    "command": command,
                    "result": result
                }, websocket)

            elif message_type == "build":
                # Build APK
                project_data = data.get("project", {})

                # Start build process
                build_id = await app.state.apk_builder.start_build(project_data)

                await manager.send_personal({
                    "type": "build_started",
                    "build_id": build_id
                }, websocket)

            elif message_type == "agent_improve":
                # Trigger agent self-improvement
                await agent.trigger_self_improvement()

                await manager.broadcast({
                    "type": "agent_improving",
                    "status": "started"
                })

            elif message_type == "sync":
                # Sync data
                sync_data = data.get("data", {})
                await manager.broadcast({
                    "type": "sync_update",
                    "data": sync_data
                })

    except WebSocketDisconnect:
        manager.disconnect(websocket, client_id)
        await manager.broadcast({
            "type": "user_disconnected",
            "client_id": client_id
        })


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info"
    )
