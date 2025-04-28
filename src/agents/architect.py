"""Architect Agent — System design and architecture planning"""
import json
from typing import Dict, Any, List

class ArchitectAgent:
    def __init__(self, model): self.model = model

    def design(self, spec: str, target: str, stack: str) -> Dict[str, Any]:
        components = []
        if "api" in spec.lower() or "backend" in spec.lower():
            components.append({"name": "API Gateway", "type": "gateway", "tech": "FastAPI"})
            components.append({"name": "Auth Service", "type": "service", "tech": "JWT + OAuth2"})
        if "frontend" in spec.lower() or "dashboard" in spec.lower():
            components.append({"name": "Web Frontend", "type": "frontend", "tech": "React + TypeScript"})
        if "database" in spec.lower() or "data" in spec.lower():
            components.append({"name": "Primary Database", "type": "database", "tech": "PostgreSQL"})
        if "real-time" in spec.lower() or "websocket" in spec.lower() or "chat" in spec.lower():
            components.append({"name": "WebSocket Service", "type": "service", "tech": "Socket.IO + Redis"})
        if not components:
            components = [{"name": "API Server", "type": "service", "tech": "FastAPI"},
                          {"name": "Database", "type": "database", "tech": "PostgreSQL"},
                          {"name": "Frontend App", "type": "frontend", "tech": "React"}]
        return {"components": components, "data_flow": "Client → API Gateway → Service → Database",
                "scaling_strategy": "Horizontal with Kubernetes HPA",
                "security": ["JWT Auth", "Rate Limiting", "CORS", "Input Validation"]}