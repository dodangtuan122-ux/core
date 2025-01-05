"""Reviewer Agent — code quality & security analysis."""

class ReviewerAgent:
    def __init__(self, model="deepseek"):
        self.model = model
    
    def process(self, context, spec):
        files = context.get("files", [])
        findings = []
        for f in files:
            findings.append({"file": f, "severity": "low", "message": "Review pending"})
        return {"review_findings": findings}
