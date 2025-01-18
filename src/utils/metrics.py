"""Metrics tracking."""

class MetricsTracker:
    def __init__(self):
        self.total_tokens = 0
        self.total_calls = 0
    
    def log_call(self, tokens):
        self.total_tokens += tokens
        self.total_calls += 1
