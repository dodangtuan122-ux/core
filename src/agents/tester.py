"""Tester Agent — automated test generation."""

class TesterAgent:
    def __init__(self, model="deepseek"):
        self.model = model
    
    def process(self, context, spec):
        return {"tests_generated": 0, "coverage": 0}
