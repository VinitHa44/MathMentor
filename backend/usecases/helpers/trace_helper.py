"""
Agent trace helpers
"""

from typing import Dict, Any, List
from datetime import datetime


def add_agent_trace(
    agent_trace: List[Dict[str, Any]],
    agent_name: str,
    status: str,
    output: Dict[str, Any]
) -> None:
    """
    Add entry to agent trace
    
    Args:
        agent_trace: Agent trace list
        agent_name: Name of the agent
        status: Status (completed, failed, skipped)
        output: Agent output data
    """
    agent_trace.append({
        "agent": agent_name,
        "status": status,
        "output": output,
        "timestamp": datetime.now().isoformat()
    })
