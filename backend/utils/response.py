"""
Response utilities for consistent API responses
"""

from typing import Any, Dict, List, Optional


def success_response(
    data: Any,
    message: str = "Success",
    status: str = "success"
) -> Dict[str, Any]:
    """
    Create a success response
    
    Args:
        data: Response data
        message: Success message
        status: Response status
    
    Returns:
        Formatted success response
    """
    return {
        "status": status,
        "message": message,
        "data": data
    }


def error_response(
    message: str,
    error: str = "",
    status: str = "error"
) -> Dict[str, Any]:
    """
    Create an error response
    
    Args:
        message: Error message
        error: Detailed error information
        status: Response status
    
    Returns:
        Formatted error response
    """
    return {
        "status": status,
        "message": message,
        "error": error
    }


def clarification_response(
    parsed_problem: Dict[str, Any],
    reason: str,
    agent_trace: List[Dict[str, Any]],
    needs_human_review: bool = False,
    hitl_reason: List[str] = None
) -> Dict[str, Any]:
    """
    Create a clarification response
    
    Args:
        parsed_problem: Parsed problem data
        reason: Reason for clarification
        agent_trace: Agent execution trace
        needs_human_review: Whether human review is needed
        hitl_reason: HITL reasons
    
    Returns:
        Formatted clarification response
    """
    return {
        "status": "needs_clarification",
        "parsed_problem": parsed_problem,
        "clarification_reason": reason,
        "agent_trace": agent_trace,
        "needs_human_review": needs_human_review,
        "hitl_reason": hitl_reason or []
    }


def hitl_response(
    problem_id: str,
    hitl_reason: List[str],
    parsed_problem: Dict[str, Any],
    solution: Dict[str, Any],
    verification: Dict[str, Any],
    agent_trace: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Create a HITL (Human-in-the-Loop) response
    
    Args:
        problem_id: Problem ID
        hitl_reason: List of HITL reasons
        parsed_problem: Parsed problem data
        solution: Solution data
        verification: Verification data
        agent_trace: Agent execution trace
    
    Returns:
        Formatted HITL response
    """
    return {
        "status": "needs_human_review",
        "problem_id": problem_id,
        "needs_human_review": True,
        "hitl_reason": hitl_reason,
        "parsed_problem": parsed_problem,
        "solution": solution,
        "verification": verification,
        "agent_trace": agent_trace
    }
