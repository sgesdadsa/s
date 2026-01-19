"""
NEX AI Agent Core
Auto-learning, self-improving AI agent with memory and context
"""

import asyncio
from typing import Dict, List, Optional, Any
from datetime import datetime
import json
from pathlib import Path

# LangChain imports
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory, VectorStoreRetrieval