#!/usr/bin/env python3
"""DevForge AI CLI — run workflows from command line."""
import sys
from src.orchestrator.workflow import WorkflowEngine
from src.agents.architect import ArchitectAgent
from src.agents.developer import DeveloperAgent

def main():
    spec = sys.argv[1] if len(sys.argv) > 1 else "Build a REST API"
    engine = WorkflowEngine()
    engine.register(ArchitectAgent())
    engine.register(DeveloperAgent())
    result = engine.execute(spec)
    print(f"Done: {len(result.get('files', []))} files generated")

if __name__ == "__main__":
    main()

# Updated: 2025-01-25T11:00:00