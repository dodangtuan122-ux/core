"""Xiaomi MiMo API client."""
import os

class MiMoClient:
    BASE_URL = "https://api.xiaomimimo.com/v1"
    
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("MIMO_API_KEY", "")
    
    def generate(self, prompt, max_tokens=8192):
        return "Generated via MiMo V2.5 Pro"
