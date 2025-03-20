"""Metrics tracking."""

class MetricsTracker:
    def __init__(self):
        self.total_tokens = 0
        self.total_calls = 0
    
    def log_call(self, tokens):
        self.total_tokens += tokens
        self.total_calls += 1

# Updated: 2025-03-20T11:30:00