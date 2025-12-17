"""
Memory Service - Stores problem history, solutions, feedback for learning
"""

import json
import os
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path

class MemoryService:
    """Service for storing and retrieving problem-solving history"""
    
    def __init__(self, storage_dir: str = "memory_store"):
        """
        Initialize Memory Service
        
        Args:
            storage_dir: Directory to store memory files
        """
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(exist_ok=True)
        
        # Storage files
        self.problems_file = self.storage_dir / "problems.jsonl"
        self.feedback_file = self.storage_dir / "feedback.jsonl"
        self.patterns_file = self.storage_dir / "patterns.json"
        
        # Ensure files exist
        for file in [self.problems_file, self.feedback_file]:
            if not file.exists():
                file.touch()
        
        if not self.patterns_file.exists():
            self._save_patterns({})
    
    def store_problem(
        self,
        problem_text: str,
        parsed_data: Dict[str, Any],
        solution: Dict[str, Any],
        verification: Dict[str, Any],
        retrieved_context: List[Dict[str, Any]],
        agent_trace: List[Dict[str, Any]]
    ) -> str:
        """
        Store a solved problem in memory
        
        Args:
            problem_text: Original problem
            parsed_data: Parsed problem data
            solution: Solution data
            verification: Verification result
            retrieved_context: RAG retrieved chunks
            agent_trace: Agent execution trace
        
        Returns:
            Problem ID
        """
        problem_id = self._generate_id()
        
        record = {
            "id": problem_id,
            "timestamp": datetime.now().isoformat(),
            "problem_text": problem_text,
            "topic": parsed_data.get('topic', 'general'),
            "variables": parsed_data.get('variables', {}),
            "constraints": parsed_data.get('constraints', {}),
            "solution": {
                "final_answer": solution.get('final_answer', ''),
                "steps": solution.get('steps', []),
                "confidence": solution.get('confidence', 0)
            },
            "verification": {
                "is_correct": verification.get('is_correct', False),
                "confidence": verification.get('confidence', 0),
                "issues": verification.get('issues', [])
            },
            "retrieved_context": [
                {
                    "source": ctx['source'],
                    "topic": ctx['topic'],
                    "score": ctx['score']
                }
                for ctx in retrieved_context
            ],
            "agent_trace": agent_trace,
            "feedback": None  # To be updated later
        }
        
        # Append to problems file (JSONL format)
        with open(self.problems_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(record) + '\n')
        
        return problem_id
    
    def store_feedback(
        self,
        problem_id: str,
        feedback_type: str,  # 'approve', 'edit', 'reject'
        user_comment: Optional[str] = None,
        corrected_solution: Optional[str] = None
    ):
        """
        Store user feedback for a problem
        
        Args:
            problem_id: Problem ID
            feedback_type: Type of feedback
            user_comment: Optional user comment
            corrected_solution: Optional corrected solution
        """
        feedback_record = {
            "problem_id": problem_id,
            "timestamp": datetime.now().isoformat(),
            "feedback_type": feedback_type,
            "user_comment": user_comment,
            "corrected_solution": corrected_solution
        }
        
        # Append to feedback file
        with open(self.feedback_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(feedback_record) + '\n')
        
        # Update patterns if feedback is negative
        if feedback_type in ['edit', 'reject']:
            self._update_mistake_patterns(problem_id, feedback_record)
    
    def get_problem_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Get recent problem history
        
        Args:
            limit: Number of recent problems to return
        
        Returns:
            List of problem records
        """
        problems = []
        
        if not self.problems_file.exists():
            return problems
        
        with open(self.problems_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    problems.append(json.loads(line))
        
        # Return most recent
        return problems[-limit:][::-1]  # Reverse to show newest first
    
    def find_similar_problems(
        self,
        topic: str,
        variables: Dict[str, Any],
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """
        Find similar problems from history
        
        Args:
            topic: Problem topic
            variables: Problem variables
            limit: Number of similar problems to return
        
        Returns:
            List of similar problem records
        """
        similar = []
        
        if not self.problems_file.exists():
            return similar
        
        with open(self.problems_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    record = json.loads(line)
                    
                    # Check topic match
                    if record.get('topic') == topic:
                        # Check variable similarity
                        similarity = self._calculate_similarity(
                            variables,
                            record.get('variables', {})
                        )
                        
                        if similarity > 0.5:  # Threshold
                            record['similarity'] = similarity
                            similar.append(record)
        
        # Sort by similarity and return top N
        similar.sort(key=lambda x: x.get('similarity', 0), reverse=True)
        return similar[:limit]
    
    def get_mistake_patterns(self, topic: Optional[str] = None) -> Dict[str, Any]:
        """
        Get common mistake patterns
        
        Args:
            topic: Optional topic filter
        
        Returns:
            Mistake patterns
        """
        patterns = self._load_patterns()
        
        if topic:
            return patterns.get(topic, {})
        
        return patterns
    
    def _generate_id(self) -> str:
        """Generate unique problem ID"""
        import uuid
        return str(uuid.uuid4())[:8]
    
    def _calculate_similarity(self, vars1: Dict, vars2: Dict) -> float:
        """Calculate similarity between two variable sets"""
        if not vars1 or not vars2:
            return 0.0
        
        # Simple Jaccard similarity
        keys1 = set(vars1.keys())
        keys2 = set(vars2.keys())
        
        if not keys1 or not keys2:
            return 0.0
        
        intersection = len(keys1 & keys2)
        union = len(keys1 | keys2)
        
        return intersection / union if union > 0 else 0.0
    
    def _update_mistake_patterns(self, problem_id: str, feedback: Dict[str, Any]):
        """Update mistake patterns based on feedback"""
        # Load current patterns
        patterns = self._load_patterns()
        
        # Find the problem
        problem = None
        with open(self.problems_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    record = json.loads(line)
                    if record['id'] == problem_id:
                        problem = record
                        break
        
        if not problem:
            return
        
        topic = problem.get('topic', 'general')
        
        # Initialize topic patterns if needed
        if topic not in patterns:
            patterns[topic] = {
                "common_mistakes": [],
                "correction_count": 0
            }
        
        # Increment correction count
        patterns[topic]["correction_count"] += 1
        
        # Add mistake if user provided comment
        if feedback.get('user_comment'):
            patterns[topic]["common_mistakes"].append({
                "timestamp": feedback['timestamp'],
                "problem_snippet": problem['problem_text'][:100],
                "user_comment": feedback['user_comment']
            })
            
            # Keep only last 50 mistakes
            patterns[topic]["common_mistakes"] = patterns[topic]["common_mistakes"][-50:]
        
        # Save patterns
        self._save_patterns(patterns)
    
    def _load_patterns(self) -> Dict[str, Any]:
        """Load mistake patterns from file"""
        if not self.patterns_file.exists():
            return {}
        
        with open(self.patterns_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _save_patterns(self, patterns: Dict[str, Any]):
        """Save mistake patterns to file"""
        with open(self.patterns_file, 'w', encoding='utf-8') as f:
            json.dump(patterns, f, indent=2, ensure_ascii=False)
