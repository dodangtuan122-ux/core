"""Workflow engine — orchestrates agent pipeline."""

class WorkflowEngine:
    def __init__(self):
        self.agents = []
    
    def register(self, agent):
        self.agents.append(agent)
    
    def execute(self, spec):
        context = {}
        for agent in self.agents:
            context = agent.process(context, spec)
        return context

# Updated: 2025-03-20T11:30:00