"""Developer Agent — generates code from architecture."""

class DeveloperAgent:
    def __init__(self, model="deepseek"):
        self.model = model
    
    def process(self, context, spec):
        arch = context.get("architecture", {})
        return {"files": [], "model_used": self.model}
