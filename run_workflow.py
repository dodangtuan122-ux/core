#!/usr/bin/env python3
"""DevForge AI — Multi-Agent Development Platform CLI"""
import sys
import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from src.orchestrator.workflow import DevForgeWorkflow

console = Console()

@click.command()
@click.option("--spec", "-s", required=True, help="Project specification in natural language")
@click.option("--target", "-t", default="production")
@click.option("--stack", default="fastapi+react+postgres")
def main(spec: str, target: str, stack: str):
    console.print(Panel.fit("[bold cyan]🚀 DevForge AI[/bold cyan]\n[dim]Architect → Developer → Reviewer → Tester → DevOps[/dim]", border_style="cyan"))
    result = DevForgeWorkflow(spec=spec, target=target, stack=stack).execute()
    table = Table(title="Workflow Summary")
    table.add_column("Metric", style="cyan"); table.add_column("Value", style="green")
    table.add_row("Duration", f"{result.duration_seconds:.1f}s")
    table.add_row("Files", str(len(result.files_generated)))
    table.add_row("Tests", f"{result.test_coverage:.0f}% coverage")
    table.add_row("Tokens", f"{result.tokens_used:,}")
    table.add_row("Status", "✅ PASS" if result.success else "⚠️ NEEDS FIXES")
    console.print(table)
    return 0 if result.success else 1

if __name__ == "__main__":
    sys.exit(main())