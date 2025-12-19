"""
Data transformation helpers
"""

from typing import Dict, Any, List


def format_retrieved_context(retrieved_context: List[Any]) -> List[Dict[str, Any]]:
    """
    Format retrieved context for response
    
    Args:
        retrieved_context: Raw retrieved context
    
    Returns:
        Formatted context list
    """
    formatted = []
    
    for item in retrieved_context:
        if isinstance(item, dict):
            formatted.append({
                "text": item.get('text', ''),
                "source": item.get('metadata', {}).get('source', ''),
                "topic": item.get('metadata', {}).get('topic', ''),
                "score": item.get('score', 0)
            })
    
    return formatted


def extract_problem_variables(parsed_problem: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract variables from parsed problem
    
    Args:
        parsed_problem: Parsed problem data
    
    Returns:
        Variables dictionary
    """
    return parsed_problem.get('variables', {})


def extract_problem_constraints(parsed_problem: Dict[str, Any]) -> List[Any]:
    """
    Extract constraints from parsed problem
    
    Args:
        parsed_problem: Parsed problem data
    
    Returns:
        Constraints list
    """
    return parsed_problem.get('constraints', [])


def build_solution_data(
    problem: str,
    topic: str,
    solution_result: Dict[str, Any],
    verification_result: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Build solution data for response
    
    Args:
        problem: Problem text
        topic: Problem topic
        solution_result: Solution from solver agent
        verification_result: Verification from verifier agent
    
    Returns:
        Formatted solution data
    """
    return {
        "problem": problem,
        "topic": topic,
        "final_answer": solution_result['final_answer'],
        "steps": solution_result['steps'],
        "solution_text": solution_result['solution_text'],
        "confidence": verification_result.get('confidence', 50),
        "verification_passed": verification_result.get('is_correct', False),
        "verification_confidence": verification_result.get('confidence', 0)
    }


def build_verification_data(verification_result: Dict[str, Any]) -> Dict[str, Any]:
    """
    Build verification data for response
    
    Args:
        verification_result: Verification from verifier agent
    
    Returns:
        Formatted verification data
    """
    return {
        "is_correct": verification_result.get('is_correct', False),
        "confidence": verification_result.get('confidence', 0),
        "issues": verification_result.get('issues', []),
        "suggestions": verification_result.get('suggestions', []),
        "needs_human_review": verification_result.get('needs_human_review', False)
    }


def build_explanation_details(explanation_result: Dict[str, Any]) -> Dict[str, Any]:
    """
    Build explanation details for response
    
    Args:
        explanation_result: Explanation from explainer agent
    
    Returns:
        Formatted explanation details
    """
    return {
        "key_concept": explanation_result.get('key_concept', ''),
        "analogy": explanation_result.get('analogy', ''),
        "common_mistakes": explanation_result.get('common_mistakes', '')
    }
