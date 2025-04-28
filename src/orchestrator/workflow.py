"""
Multi-Agent Workflow Orchestrator
Coordinates the 5-agent pipeline: Architect → Developer → Reviewer → Tester → DevOps
"""

import asyncio, json, time
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from collections import defaultdict

from src.agents.architect import ArchitectAgent
from src.agents.developer import DeveloperAgent
from src.agents.reviewer import ReviewerAgent
from src.agents.tester import TesterAgent
from src.agents.devops import DevOpsAgent
from src.models.deepseek import DeepSeekClient
from src.models.mimo import MiMoClient
from src.utils.metrics import MetricsTracker


@dataclass
class WorkflowSpec:
    description: str
    target: str = "production"
    stack: str = "fastapi+react+postgres"
    constraints: Dict[str, Any] = field(default_factory=dict)
    max_files: int = 50


@dataclass
class WorkflowResult:
    success: bool
    architecture: Dict[str, Any]
    files_generated: List[str]
    review_findings: List[Dict]
    test_coverage: float
    deployment_manifest: Dict[str, Any]
    duration_seconds: float
    tokens_used: int
    agent_stats: Dict[str, Dict]


class DevForgeWorkflow:
    """Main workflow orchestrator that chains 5 specialized AI agents."""

    def __init__(self, spec: str, target: str = "production",
                 stack: str = "fastapi+react+postgres",
                 deepseek_api_key: Optional[str] = None,
                 mimo_api_key: Optional[str] = None):
        self.spec = WorkflowSpec(description=spec, target=target, stack=stack)
        self.deepseek = DeepSeekClient(api_key=deepseek_api_key)
        self.mimo = MiMoClient(api_key=mimo_api_key)
        self.metrics = MetricsTracker()
        self.architect = ArchitectAgent(model=self.deepseek)
        self.developer = DeveloperAgent(primary_model=self.deepseek, secondary_model=self.mimo)
        self.reviewer = ReviewerAgent(model=self.deepseek)
        self.tester = TesterAgent(model=self.mimo)
        self.devops = DevOpsAgent(model=self.deepseek)

    def execute(self) -> WorkflowResult:
        start_time = time.time()
        agent_stats = defaultdict(dict)

        # Phase 1: Architecture Design
        architecture = self.architect.design(
            spec=self.spec.description, target=self.spec.target, stack=self.spec.stack)
        agent_stats["architect"] = {"duration": time.time() - start_time, "model": "DeepSeek V3",
                                     "output": f"{len(architecture.get('components', []))} components"}
        self.metrics.log_agent_call("architect", "deepseek-v3", 12500)

        # Phase 2: Code Generation
        dev_start = time.time()
        files_generated = self.developer.generate(architecture=architecture, stack=self.spec.stack)
        agent_stats["developer"] = {"duration": time.time() - dev_start,
                                     "model": "DeepSeek V3 + MiMo V2.5 Pro",
                                     "output": f"{len(files_generated)} files"}
        self.metrics.log_agent_call("developer", "deepseek-v3+mimo-v2.5", 45000)

        # Phase 3: Review
        review_start = time.time()
        review_findings = self.reviewer.review(files=files_generated, architecture=architecture)
        critical = sum(1 for f in review_findings if f.get("severity") == "critical")
        agent_stats["reviewer"] = {"duration": time.time() - review_start, "model": "DeepSeek V3",
                                    "output": f"{len(review_findings)} findings ({critical} critical)"}
        self.metrics.log_agent_call("reviewer", "deepseek-v3", 18000)

        # Phase 4: Testing
        test_start = time.time()
        test_result = self.tester.generate_tests(files=files_generated, architecture=architecture)
        coverage = test_result.get("coverage_pct", 0)
        agent_stats["tester"] = {"duration": time.time() - test_start, "model": "MiMo V2.5 Pro",
                                  "output": f"{test_result.get('test_count', 0)} tests, {coverage:.0f}% coverage"}
        self.metrics.log_agent_call("tester", "mimo-v2.5-pro", 22000)

        # Phase 5: Deployment
        deploy_start = time.time()
        deployment = self.devops.deploy(architecture=architecture, files=files_generated, target=self.spec.target)
        agent_stats["devops"] = {"duration": time.time() - deploy_start, "model": "DeepSeek V3",
                                  "output": f"Docker + {deployment.get('k8s_manifests', 0)} K8s manifests"}
        self.metrics.log_agent_call("devops", "deepseek-v3", 15000)

        total_time = time.time() - start_time
        return WorkflowResult(success=critical == 0, architecture=architecture,
                              files_generated=files_generated, review_findings=review_findings,
                              test_coverage=coverage, deployment_manifest=deployment,
                              duration_seconds=total_time, tokens_used=self.metrics.get_total_tokens(),
                              agent_stats=dict(agent_stats))