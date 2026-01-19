"""
MyLLM Studio - Visual Studio Code-like Web Interface
Modern web interface for MyLLM with real-time sync
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any
import json
import asyncio
from pathlib import Path
import os

app = FastAPI(title="MyLLM Studio", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# WebSocket connections for real-time sync
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.chat_history: List[Dict[str, str]] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        # Send existing chat history
        await websocket.send_json({
            "type": "history",
            "data": self.chat_history
        })

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        """Broadcast to all connected clients"""
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except:
                pass

    async def send_personal(self, message: dict, websocket: WebSocket):
        """Send to specific client"""
        await websocket.send_json(message)

manager = ConnectionManager()

# Serve static files (frontend)
static_dir = Path(__file__).parent / "studio" / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

@app.get("/")
async def root():
    """Serve the main UI"""
    html_file = Path(__file__).parent / "studio" / "index.html"
    if html_file.exists():
        return FileResponse(html_file)
    return HTMLResponse(content=get_embedded_html())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket for real-time communication"""
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()

            # Handle different message types
            if data.get("type") == "chat":
                # Process chat message
                message = data.get("message", "")
                response = await process_chat(message)

                # Add to history
                manager.chat_history.append({
                    "role": "user",
                    "content": message
                })
                manager.chat_history.append({
                    "role": "assistant",
                    "content": response
                })

                # Broadcast to all clients
                await manager.broadcast({
                    "type": "chat_response",
                    "data": {
                        "user": message,
                        "assistant": response
                    }
                })

            elif data.get("type") == "command":
                # Execute CLI command
                command = data.get("command", "")
                result = await execute_command(command)
                await manager.send_personal({
                    "type": "command_result",
                    "data": result
                }, websocket)

            elif data.get("type") == "sync":
                # Sync request
                await manager.broadcast({
                    "type": "sync_update",
                    "data": data.get("data", {})
                })

    except WebSocketDisconnect:
        manager.disconnect(websocket)

async def process_chat(message: str) -> str:
    """Process chat message using loaded model"""
    try:
        from ..models import model_manager

        # Get first loaded model
        loaded = model_manager.get_loaded_models()
        if not loaded:
            return "❌ No model loaded. Please load a model first."

        model = model_manager.get_model(loaded[0]["identifier"])
        if not model:
            return "❌ Model not available."

        # Generate response
        response = model(
            f"User: {message}\nAssistant:",
            max_tokens=512,
            temperature=0.7,
            echo=False
        )

        return response["choices"][0]["text"].strip()

    except Exception as e:
        return f"❌ Error: {str(e)}"

async def execute_command(command: str) -> Dict[str, Any]:
    """Execute MyLLM CLI command"""
    try:
        from ..models import model_manager
        from ..config import config

        parts = command.split()
        cmd = parts[0] if parts else ""

        if cmd == "ls":
            models = model_manager.list_models()
            return {"success": True, "data": models}

        elif cmd == "ps":
            loaded = model_manager.get_loaded_models()
            return {"success": True, "data": loaded}

        elif cmd == "config":
            if len(parts) > 1 and parts[1] == "show":
                return {
                    "success": True,
                    "data": {
                        "models_directory": config.get("models_directory"),
                        "server": config.config.get("server", {}),
                        "default_params": config.config.get("default_model_params", {})
                    }
                }

        return {"success": False, "error": "Command not supported in UI"}

    except Exception as e:
        return {"success": False, "error": str(e)}

def get_embedded_html() -> str:
    """Embedded HTML for the UI"""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MyLLM Studio</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --bg-primary: #1e1e1e;
            --bg-secondary: #252526;
            --bg-tertiary: #2d2d30;
            --border-color: #3e3e42;
            --text-primary: #cccccc;
            --text-secondary: #858585;
            --accent-blue: #007acc;
            --accent-green: #4ec9b0;
            --accent-yellow: #dcdcaa;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            height: 100vh;
            overflow: hidden;
        }

        .container {
            display: flex;
            height: 100vh;
            flex-direction: column;
        }

        /* Header */
        .header {
            background: var(--bg-tertiary);
            padding: 8px 16px;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .header h1 {
            font-size: 14px;
            font-weight: 400;
            color: var(--text-primary);
        }

        .header-actions {
            display: flex;
            gap: 8px;
        }

        .header-btn {
            background: var(--accent-blue);
            color: white;
            border: none;
            padding: 6px 12px;
            border-radius: 2px;
            cursor: pointer;
            font-size: 12px;
            transition: opacity 0.2s;
        }

        .header-btn:hover {
            opacity: 0.8;
        }

        .header-btn.secondary {
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
        }

        /* Main Layout */
        .main-layout {
            display: flex;
            flex: 1;
            overflow: hidden;
        }

        /* Sidebar */
        .sidebar {
            width: 250px;
            background: var(--bg-secondary);
            border-right: 1px solid var(--border-color);
            display: flex;
            flex-direction: column;
        }

        .sidebar-section {
            padding: 16px;
            border-bottom: 1px solid var(--border-color);
        }

        .sidebar-title {
            font-size: 11px;
            text-transform: uppercase;
            color: var(--text-secondary);
            margin-bottom: 8px;
            font-weight: 600;
        }

        .sidebar-item {
            padding: 6px 8px;
            margin: 2px 0;
            border-radius: 2px;
            cursor: pointer;
            font-size: 13px;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: background 0.2s;
        }

        .sidebar-item:hover {
            background: var(--bg-tertiary);
        }

        .sidebar-item.active {
            background: var(--bg-tertiary);
        }

        .status-indicator {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--accent-green);
        }

        .status-indicator.offline {
            background: var(--text-secondary);
        }

        /* Content Area */
        .content {
            flex: 1;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        .tabs {
            display: flex;
            background: var(--bg-secondary);
            border-bottom: 1px solid var(--border-color);
            overflow-x: auto;
        }

        .tab {
            padding: 8px 16px;
            font-size: 13px;
            border-right: 1px solid var(--border-color);
            cursor: pointer;
            background: transparent;
            transition: background 0.2s;
            white-space: nowrap;
        }

        .tab:hover {
            background: var(--bg-tertiary);
        }

        .tab.active {
            background: var(--bg-primary);
        }

        .content-panel {
            flex: 1;
            padding: 16px;
            overflow-y: auto;
        }

        /* Chat Interface */
        .chat-container {
            display: flex;
            flex-direction: column;
            height: 100%;
        }

        .chat-messages {
            flex: 1;
            overflow-y: auto;
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .message {
            display: flex;
            gap: 12px;
            animation: slideIn 0.3s ease;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .message-avatar {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: var(--accent-blue);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
            font-weight: 600;
            flex-shrink: 0;
        }

        .message.assistant .message-avatar {
            background: var(--accent-green);
        }

        .message-content {
            flex: 1;
        }

        .message-role {
            font-size: 12px;
            color: var(--text-secondary);
            margin-bottom: 4px;
        }

        .message-text {
            font-size: 14px;
            line-height: 1.6;
            color: var(--text-primary);
        }

        .chat-input-container {
            padding: 16px;
            border-top: 1px solid var(--border-color);
            background: var(--bg-secondary);
        }

        .chat-input-wrapper {
            display: flex;
            gap: 8px;
        }

        .chat-input {
            flex: 1;
            background: var(--bg-primary);
            border: 1px solid var(--border-color);
            color: var(--text-primary);
            padding: 12px;
            border-radius: 4px;
            font-size: 14px;
            font-family: inherit;
            resize: none;
            min-height: 44px;
            max-height: 200px;
        }

        .chat-input:focus {
            outline: none;
            border-color: var(--accent-blue);
        }

        .send-btn {
            background: var(--accent-blue);
            color: white;
            border: none;
            padding: 0 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            transition: opacity 0.2s;
        }

        .send-btn:hover:not(:disabled) {
            opacity: 0.8;
        }

        .send-btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }

        /* Panel */
        .panel {
            background: var(--bg-secondary);
            border-radius: 4px;
            padding: 16px;
            margin-bottom: 16px;
        }

        .panel-title {
            font-size: 14px;
            margin-bottom: 12px;
            color: var(--accent-yellow);
        }

        .panel-content {
            font-size: 13px;
            line-height: 1.6;
        }

        /* Forms */
        .form-group {
            margin-bottom: 16px;
        }

        .form-label {
            display: block;
            font-size: 13px;
            margin-bottom: 6px;
            color: var(--text-secondary);
        }

        .form-input {
            width: 100%;
            background: var(--bg-primary);
            border: 1px solid var(--border-color);
            color: var(--text-primary);
            padding: 8px 12px;
            border-radius: 2px;
            font-size: 13px;
            font-family: inherit;
        }

        .form-input:focus {
            outline: none;
            border-color: var(--accent-blue);
        }

        .btn {
            background: var(--accent-blue);
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 2px;
            cursor: pointer;
            font-size: 13px;
            transition: opacity 0.2s;
        }

        .btn:hover {
            opacity: 0.8;
        }

        /* Status Bar */
        .status-bar {
            background: var(--accent-blue);
            padding: 4px 16px;
            font-size: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .status-item {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
            height: 10px;
        }

        ::-webkit-scrollbar-track {
            background: var(--bg-secondary);
        }

        ::-webkit-scrollbar-thumb {
            background: var(--border-color);
            border-radius: 5px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #4e4e52;
        }

        /* Utility */
        .text-success {
            color: var(--accent-green);
        }

        .text-error {
            color: #f48771;
        }

        .text-warning {
            color: var(--accent-yellow);
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <div class="header">
            <h1>🚀 MyLLM Studio</h1>
            <div class="header-actions">
                <button class="header-btn secondary" onclick="showConfigPanel()">⚙️ Config</button>
                <button class="header-btn" onclick="connectWebSocket()">🔌 Connect</button>
            </div>
        </div>

        <!-- Main Layout -->
        <div class="main-layout">
            <!-- Sidebar -->
            <div class="sidebar">
                <div class="sidebar-section">
                    <div class="sidebar-title">Models</div>
                    <div id="models-list">
                        <div class="sidebar-item">
                            <div class="status-indicator offline"></div>
                            <span>No models loaded</span>
                        </div>
                    </div>
                </div>

                <div class="sidebar-section">
                    <div class="sidebar-title">Views</div>
                    <div class="sidebar-item active" onclick="showTab('chat')">
                        💬 Chat
                    </div>
                    <div class="sidebar-item" onclick="showTab('console')">
                        🖥️ Console
                    </div>
                    <div class="sidebar-item" onclick="showTab('settings')">
                        ⚙️ Settings
                    </div>
                </div>
            </div>

            <!-- Content -->
            <div class="content">
                <div class="tabs">
                    <div class="tab active" id="tab-chat">Chat</div>
                    <div class="tab" id="tab-console">Console</div>
                    <div class="tab" id="tab-settings">Settings</div>
                </div>

                <div class="content-panel" id="content-chat">
                    <div class="chat-container">
                        <div class="chat-messages" id="chat-messages">
                            <div class="message assistant">
                                <div class="message-avatar">AI</div>
                                <div class="message-content">
                                    <div class="message-role">Assistant</div>
                                    <div class="message-text">
                                        Welcome to MyLLM Studio! 🎉<br><br>
                                        Start chatting with your local LLM models. Make sure a model is loaded first.
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="chat-input-container">
                            <div class="chat-input-wrapper">
                                <textarea
                                    class="chat-input"
                                    id="chat-input"
                                    placeholder="Type your message... (Shift+Enter for new line)"
                                    rows="1"
                                ></textarea>
                                <button class="send-btn" onclick="sendMessage()" id="send-btn">
                                    Send
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="content-panel" id="content-console" style="display: none;">
                    <div class="panel">
                        <div class="panel-title">Command Console</div>
                        <div class="panel-content">
                            <div class="form-group">
                                <label class="form-label">Execute Command</label>
                                <input
                                    type="text"
                                    class="form-input"
                                    id="command-input"
                                    placeholder="ls, ps, config show..."
                                    onkeypress="if(event.key === 'Enter') executeCommand()"
                                />
                            </div>
                            <button class="btn" onclick="executeCommand()">Execute</button>

                            <div id="command-output" style="margin-top: 16px; font-family: 'Courier New', monospace; font-size: 12px;">
                            </div>
                        </div>
                    </div>
                </div>

                <div class="content-panel" id="content-settings" style="display: none;">
                    <div class="panel">
                        <div class="panel-title">Configuration</div>
                        <div class="panel-content">
                            <div class="form-group">
                                <label class="form-label">Models Directory</label>
                                <input type="text" class="form-input" id="models-dir" placeholder="C:\models" />
                            </div>

                            <div class="form-group">
                                <label class="form-label">Server Port</label>
                                <input type="number" class="form-input" id="server-port" value="8080" />
                            </div>

                            <div class="form-group">
                                <label class="form-label">Temperature</label>
                                <input type="number" class="form-input" id="temperature" value="0.7" step="0.1" min="0" max="2" />
                            </div>

                            <div class="form-group">
                                <label class="form-label">Max Tokens</label>
                                <input type="number" class="form-input" id="max-tokens" value="512" />
                            </div>

                            <button class="btn" onclick="saveConfig()">Save Configuration</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Status Bar -->
        <div class="status-bar">
            <div class="status-item">
                <span id="connection-status">🔴 Disconnected</span>
            </div>
            <div class="status-item">
                <span id="model-status">No model loaded</span>
            </div>
        </div>
    </div>

    <script>
        let ws = null;
        let currentTab = 'chat';

        // WebSocket Connection
        function connectWebSocket() {
            const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
            const wsUrl = `${protocol}//${window.location.host}/ws`;

            ws = new WebSocket(wsUrl);

            ws.onopen = () => {
                document.getElementById('connection-status').innerHTML = '🟢 Connected';
                console.log('WebSocket connected');
            };

            ws.onmessage = (event) => {
                const data = JSON.parse(event.data);
                handleWebSocketMessage(data);
            };

            ws.onclose = () => {
                document.getElementById('connection-status').innerHTML = '🔴 Disconnected';
                console.log('WebSocket disconnected');
                // Auto reconnect after 3 seconds
                setTimeout(connectWebSocket, 3000);
            };

            ws.onerror = (error) => {
                console.error('WebSocket error:', error);
            };
        }

        function handleWebSocketMessage(data) {
            if (data.type === 'chat_response') {
                addMessageToChat('assistant', data.data.assistant);
            } else if (data.type === 'command_result') {
                displayCommandResult(data.data);
            } else if (data.type === 'history') {
                // Load chat history
                data.data.forEach(msg => {
                    if (msg.role !== 'system') {
                        addMessageToChat(msg.role, msg.content, false);
                    }
                });
            }
        }

        // Chat Functions
        function sendMessage() {
            const input = document.getElementById('chat-input');
            const message = input.value.trim();

            if (!message || !ws || ws.readyState !== WebSocket.OPEN) {
                return;
            }

            // Add user message to UI
            addMessageToChat('user', message);

            // Send to server
            ws.send(JSON.stringify({
                type: 'chat',
                message: message
            }));

            // Clear input
            input.value = '';
            input.style.height = 'auto';

            // Disable send button temporarily
            const sendBtn = document.getElementById('send-btn');
            sendBtn.disabled = true;
            setTimeout(() => sendBtn.disabled = false, 1000);
        }

        function addMessageToChat(role, content, scroll = true) {
            const messagesDiv = document.getElementById('chat-messages');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${role}`;

            const avatar = role === 'user' ? 'U' : 'AI';
            const roleName = role === 'user' ? 'You' : 'Assistant';

            messageDiv.innerHTML = `
                <div class="message-avatar">${avatar}</div>
                <div class="message-content">
                    <div class="message-role">${roleName}</div>
                    <div class="message-text">${escapeHtml(content)}</div>
                </div>
            `;

            messagesDiv.appendChild(messageDiv);

            if (scroll) {
                messagesDiv.scrollTop = messagesDiv.scrollHeight;
            }
        }

        // Command Functions
        function executeCommand() {
            const input = document.getElementById('command-input');
            const command = input.value.trim();

            if (!command || !ws || ws.readyState !== WebSocket.OPEN) {
                return;
            }

            ws.send(JSON.stringify({
                type: 'command',
                command: command
            }));

            input.value = '';
        }

        function displayCommandResult(result) {
            const output = document.getElementById('command-output');

            if (result.success) {
                output.innerHTML = `<div class="text-success">✓ Success</div><pre>${JSON.stringify(result.data, null, 2)}</pre>`;
            } else {
                output.innerHTML = `<div class="text-error">✗ Error: ${result.error}</div>`;
            }
        }

        // Tab Functions
        function showTab(tabName) {
            // Hide all content panels
            document.querySelectorAll('.content-panel').forEach(panel => {
                panel.style.display = 'none';
            });

            // Remove active class from all tabs
            document.querySelectorAll('.tab').forEach(tab => {
                tab.classList.remove('active');
            });

            document.querySelectorAll('.sidebar-item').forEach(item => {
                item.classList.remove('active');
            });

            // Show selected content
            document.getElementById(`content-${tabName}`).style.display = 'block';
            document.getElementById(`tab-${tabName}`).classList.add('active');

            currentTab = tabName;
        }

        // Config Functions
        function saveConfig() {
            alert('Configuration saved! (Feature coming soon)');
        }

        function showConfigPanel() {
            showTab('settings');
        }

        // Utility Functions
        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML.replace(/\n/g, '<br>');
        }

        // Event Listeners
        document.getElementById('chat-input').addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });

        // Auto-resize textarea
        document.getElementById('chat-input').addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
        });

        // Initialize
        window.onload = () => {
            connectWebSocket();
        };
    </script>
</body>
</html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8090)
