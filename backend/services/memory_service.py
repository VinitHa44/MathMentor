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
        
        # Storage files
        self.problems_file = self.storage_dir / "problems.jsonl"
        self.feedback_file = self.storage_dir / "feedback.jsonl"
        self.patterns_file = self.storage_dir / "patterns.json"
        
        # Initialize storage
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self):
        """Ensure storage directory and files exist"""
        # Create directory if it doesn't exist
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        
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
        # Ensure storage exists before writing
        self._ensure_storage_exists()
        
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
                    "source": ctx.get('source', '') if isinstance(ctx, dict) else '',
                    "topic": ctx.get('topic', '') if isinstance(ctx, dict) else '',
                    "score": ctx.get('score', 0) if isinstance(ctx, dict) else 0
                }
                for ctx in retrieved_context
                if isinstance(ctx, dict)
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
        # Ensure storage exists before writing
        self._ensure_storage_exists()
        
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
        # Ensure storage exists
        self._ensure_storage_exists()
        
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
        # Ensure storage exists
        self._ensure_storage_exists()
        
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
                        record_vars = record.get('variables', {})
                        # Ensure both are dicts before comparing
                        if isinstance(variables, dict) and isinstance(record_vars, dict):
                            similarity = self._calculate_similarity(
                                variables,
                                record_vars
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
    def get_solution_patterns(self, topic: str) -> List[Dict[str, Any]]:
        """
        Retrieve known solution patterns for a topic, including user corrections
        
        Args:
            topic: Problem topic
        
        Returns:
            List of solution patterns with steps (prioritizing user corrections)
        """
        patterns = []
        
        # FIRST: Get user corrections from patterns.json (highest priority!)
        correction_patterns = self._load_patterns()
        if topic in correction_patterns:
            topic_corrections = correction_patterns[topic].get('common_mistakes', [])
            for correction in topic_corrections:
                # Parse user comment to extract steps and answer
                user_comment = correction.get('user_comment', '')
                if user_comment:
                    patterns.append({
                        'problem_text': correction.get('problem_snippet', ''),
                        'problem_snippet': correction.get('problem_snippet', ''),
                        'steps': user_comment.split('\n'),  # User's corrected steps
                        'final_answer': self._extract_answer_from_comment(user_comment),
                        'confidence': 1.0,  # User corrections are highest confidence
                        'source': 'user_correction'
                    })
        
        # SECOND: Get verified solutions from problems.jsonl
        if self.problems_file.exists():
            with open(self.problems_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        record = json.loads(line)
                        
                        # Only use verified correct solutions
                        if (record.get('topic') == topic and 
                            record.get('verification', {}).get('is_correct', False)):
                            patterns.append({
                                'problem_text': record['problem_text'],
                                'steps': record.get('solution', {}).get('steps', []),
                                'final_answer': record.get('solution', {}).get('final_answer', ''),
                                'confidence': record.get('verification', {}).get('confidence', 0),
                                'source': 'verified_solution'
                            })
        
        # Sort: user corrections first (confidence=1.0), then by confidence
        patterns.sort(key=lambda x: x['confidence'], reverse=True)
        return patterns[:5]  # Top 5 patterns
    
    def _extract_answer_from_comment(self, comment: str) -> str:
        """Extract final answer from user comment"""
        import re
        # Look for "Answer:" pattern
        match = re.search(r'\*\*Answer:\*\*\s*([^\n]+)', comment)
        if match:
            return match.group(1).strip()
        # Look for last line with a number
        lines = [l.strip() for l in comment.split('\n') if l.strip()]
        for line in reversed(lines):
            if re.search(r'\d+\.?\d*', line):
                return line
        return 'See correction'
    
    def apply_known_corrections(self, text: str) -> str:
        """
        Apply known OCR/ASR corrections to input text
        
        Args:
            text: Input text possibly containing errors
        
        Returns:
            Corrected text
        """
        patterns = self._load_patterns()
        
        # Apply common corrections
        corrections = patterns.get('ocr_corrections', {})
        
        corrected = text
        for wrong, right in corrections.items():
            corrected = corrected.replace(wrong, right)
        
        return corrected
    
    def store_ocr_correction(self, wrong_text: str, corrected_text: str):
        """
        Store OCR/ASR correction for future learning
        
        Args:
            wrong_text: Original incorrect text
            corrected_text: Human-corrected text
        """
        patterns = self._load_patterns()
        
        if 'ocr_corrections' not in patterns:
            patterns['ocr_corrections'] = {}
        
        # Store word-level differences
        wrong_words = wrong_text.split()
        correct_words = corrected_text.split()
        
        for w, c in zip(wrong_words, correct_words):
            if w != c:
                patterns['ocr_corrections'][w] = c
        
        self._save_patterns(patterns)
    
    def search_by_structure(self, problem_structure: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Search memory by problem structure
        
        Args:
            problem_structure: Structured problem data (counts, types, etc.)
        
        Returns:
            List of similar problems
        """
        similar = []
        
        if not self.problems_file.exists():
            return similar
        
        with open(self.problems_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    record = json.loads(line)
                    
                    # Compare structure
                    record_structure = record.get('variables', {})
                    
                    # Check if structures match
                    if self._structures_match(problem_structure, record_structure):
                        similar.append(record)
        
        return similar
    
    def _structures_match(self, struct1: Dict, struct2: Dict) -> bool:
        """Check if two problem structures match"""
        # For probability problems with counts
        if 'counts' in struct1 and 'counts' in struct2:
            keys1 = set(struct1['counts'].keys())
            keys2 = set(struct2['counts'].keys())
            
            # Same categories means similar structure
            return keys1 == keys2
        
        # Generic key comparison
        return set(struct1.keys()) == set(struct2.keys())