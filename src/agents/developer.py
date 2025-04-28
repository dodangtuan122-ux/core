"""Developer Agent — Multi-file code generation"""
from typing import Dict, Any, List

class DeveloperAgent:
    def __init__(self, primary_model, secondary_model):
        self.primary = primary_model
        self.secondary = secondary_model

    def generate(self, architecture: Dict[str, Any], stack: str, max_files: int = 50) -> List[str]:
        generated = []
        for component in architecture.get("components", []):
            name = component.get("name", "module")
            ctype = component.get("type", "")
            slug = name.lower().replace(" ", "_")
            if ctype in ("gateway", "service"):
                generated.extend([f"src/services/{slug}/__init__.py", f"src/services/{slug}/routes.py",
                                  f"src/services/{slug}/models.py", f"src/services/{slug}/service.py"])
            elif ctype == "frontend":
                generated.extend([f"frontend/src/pages/{slug}.tsx", f"frontend/src/components/{slug}/index.tsx"])
            elif ctype == "database":
                generated.extend(["migrations/001_initial_schema.sql", "src/database/connection.py"])
        generated.extend(["src/main.py", "src/config.py", "docker-compose.yml", "Dockerfile",
                          ".env.example", "requirements.txt"])
        return generated[:max_files]