"""Task queue for batch processing."""
from collections import deque

class TaskQueue:
    def __init__(self, max_concurrent=3):
        self.queue = deque()
        self.max_concurrent = max_concurrent
    
    def enqueue(self, task):
        self.queue.append(task)
    
    def stats(self):
        return {"queued": len(self.queue)}
