"""Shared context between agents."""

class AgentContext:
    def __init__(self):
        self.data = {}
    
    def set(self, key, value):
        self.data[key] = value
    
    def get(self, key, default=None):
        return self.data.get(key, default)

# Updated: 2025-03-25T16:00:00