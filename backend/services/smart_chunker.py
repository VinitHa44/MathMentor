"""
Smart Chunking Service for Math Documents
Implements document-type-aware chunking strategies for RAG
"""

import re
from typing import List, Dict, Any, Tuple
from pathlib import Path
from enum import Enum


class ChunkType(Enum):
    """Types of chunks for different content"""
    FORMULA = "formula"
    DEFINITION = "definition"
    EXAMPLE = "example"
    PROCEDURE = "procedure"
    PITFALL = "pitfall"
    CONCEPT = "concept"


class SmartChunker:
    """Intelligent chunking for math documents based on content type"""
    
    def __init__(self):
        """Initialize chunker with patterns for different content types"""
        
        # Pattern matchers
        self.formula_patterns = [
            r'(?:Formula|Equation|Identity):\s*([^\n]+)',
            r'\$\$(.+?)\$\$',  # LaTeX display math
            r'(?:^|\n)([A-Za-z]\'?\(.*?\)\s*=.+?)(?:\n|$)',  # f(x) = ...
        ]
        
        self.definition_patterns = [
            r'(?:Definition|Concept):\s*([^\n]+)',
            r'(?:^|\n)(.*?)\s+is defined as',
        ]
        
        self.example_patterns = [
            r'##\s*Example\s+\d+:',
            r'\*\*Problem:\*\*',
        ]
        
        self.procedure_patterns = [
            r'(?:Procedure|Steps|Method|Algorithm):',
            r'(?:^|\n)\d+\.\s+',  # Numbered steps
        ]
        
        self.pitfall_patterns = [
            r'(?:Common\s+(?:Mistake|Error|Pitfall))s?:',
            r'(?:Wrong|Incorrect|❌):',
        ]
    
    def chunk_markdown_file(self, file_path: Path, topic: str) -> List[Dict[str, Any]]:
        """
        Chunk a markdown file intelligently based on content structure
        
        Args:
            file_path: Path to markdown file
            topic: Topic name (calculus, algebra, etc.)
        
        Returns:
            List of chunks with metadata
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        chunks = []
        
        # First extract examples (most important) - this captures full examples
        chunks.extend(self._extract_examples(content, topic, file_path.stem))
        
        # Get example boundaries to exclude them from formula extraction
        example_ranges = self._get_example_ranges(content)
        
        # Extract formulas (but not from within examples)
        chunks.extend(self._extract_formulas(content, topic, file_path.stem, example_ranges))
        
        # Extract definition chunks
        chunks.extend(self._extract_definitions(content, topic, file_path.stem))
        
        # Extract procedure chunks
        chunks.extend(self._extract_procedures(content, topic, file_path.stem))
        
        # Extract pitfall chunks
        chunks.extend(self._extract_pitfalls(content, topic, file_path.stem))
        
        # Extract key formulas section
        chunks.extend(self._extract_key_formulas_section(content, topic, file_path.stem))
        
        # Extract reference-style content (for textbook-formatted files)
        if len(chunks) == 0:  # Only if no examples found
            chunks.extend(self._extract_reference_sections(content, topic, file_path.stem))
        
        return chunks
    
    def _get_example_ranges(self, content: str) -> List[Tuple[int, int]]:
        """
        Get start and end positions of all example sections
        
        Returns:
            List of (start, end) tuples for example sections
        """
        ranges = []
        pattern = r'##\s*Example\s+\d+:.*?(?=\n##\s*(?:Example|\w+\s+Formulas?)|---\n\n##|$)'
        matches = re.finditer(pattern, content, re.DOTALL)
        
        for match in matches:
            ranges.append((match.start(), match.end()))
        
        return ranges
    
    def _is_in_example_range(self, position: int, example_ranges: List[Tuple[int, int]]) -> bool:
        """Check if a position is within any example range"""
        for start, end in example_ranges:
            if start <= position <= end:
                return True
        return False
    
    def _extract_formulas(self, content: str, topic: str, source: str, 
                          example_ranges: List[Tuple[int, int]] = None) -> List[Dict[str, Any]]:
        """
        Extract individual formulas as chunks (excluding those inside examples)
        
        Args:
            content: File content
            topic: Topic name
            source: Source filename
            example_ranges: List of (start, end) positions for examples to exclude
        
        Returns:
            List of formula chunks
        """
        if example_ranges is None:
            example_ranges = []
        
        chunks = []
        
        # Pattern 1: Explicit formula labels (not typically in examples, but check anyway)
        pattern = r'(?:^|\n)(?:\*\*)?(?:Formula|Equation|Identity):?\s*(.+?)(?:\n\n|\n(?=[#*])|$)'
        matches = re.finditer(pattern, content, re.MULTILINE | re.DOTALL)
        
        for match in matches:
            # Skip if inside example section
            if self._is_in_example_range(match.start(), example_ranges):
                continue
            
            formula_text = match.group(1).strip()
            
            # Clean and format
            if len(formula_text) > 10 and len(formula_text) < 500:  # Reasonable formula size
                chunk = self._create_formula_chunk(formula_text, topic, source)
                if chunk:
                    chunks.append(chunk)
        
        # Pattern 2: Skip LaTeX display equations - they're mostly in examples
        # Only extract from "Key Formulas" section (handled by _extract_key_formulas_section)
        
        return chunks
    
    def _create_formula_chunk(self, text: str, topic: str, source: str) -> Dict[str, Any]:
        """Create a well-formatted formula chunk"""
        # Extract formula name if present
        lines = text.split('\n')
        formula_name = None
        
        if ':' in lines[0]:
            parts = lines[0].split(':', 1)
            formula_name = parts[0].strip()
            text = parts[1].strip() + '\n' + '\n'.join(lines[1:])
        
        return {
            "text": text.strip(),
            "type": ChunkType.FORMULA.value,
            "topic": topic,
            "subtopic": formula_name or "general",
            "source": source,
            "difficulty": "basic"
        }
    
    def _extract_definitions(self, content: str, topic: str, source: str) -> List[Dict[str, Any]]:
        """Extract definitions with their formulas"""
        chunks = []
        
        # Pattern: Definition/Concept sections
        pattern = r'(?:^|\n)(?:\*\*)?(?:Definition|Concept):?\s*(.+?)(?:\n\n##|\n\n---|\Z)'
        matches = re.finditer(pattern, content, re.MULTILINE | re.DOTALL)
        
        for match in matches:
            def_text = match.group(1).strip()
            
            # Ensure it includes both definition and formula
            if len(def_text) > 20 and len(def_text) < 800:
                chunks.append({
                    "text": def_text,
                    "type": ChunkType.DEFINITION.value,
                    "topic": topic,
                    "subtopic": self._infer_subtopic(content, match.start()),
                    "source": source,
                    "difficulty": "basic"
                })
        
        return chunks
    
    def _extract_examples(self, content: str, topic: str, source: str) -> List[Dict[str, Any]]:
        """
        Extract complete examples (Problem + Solution together)
        This is the MOST IMPORTANT chunking strategy
        Handles both "Example N:" and "Problem N:" formats
        """
        chunks = []
        
        # Pattern 1: Extract full examples with "Example N:" format
        pattern1 = r'##\s*Example\s+(\d+):?\s*(.+?)(?=\n##\s*(?:Example|\w+\s+Formulas?)|---\n\n##|$)'
        matches1 = re.finditer(pattern1, content, re.DOTALL)
        
        for match in matches1:
            example_num = match.group(1)
            example_content = match.group(2).strip()
            
            # Parse example structure
            example_data = self._parse_example(example_content)
            
            if example_data:
                # Create full chunk with problem + solution
                chunk_text = self._format_example_chunk(example_num, example_data)
                
                # Determine difficulty
                difficulty = self._infer_difficulty(example_content, topic)
                
                # Extract pattern/concept
                pattern_type = self._infer_pattern(example_data['title'])
                
                chunks.append({
                    "text": chunk_text,
                    "type": ChunkType.EXAMPLE.value,
                    "topic": topic,
                    "subtopic": example_data['title'],
                    "pattern": pattern_type,
                    "source": source,
                    "difficulty": difficulty
                })
        
        # Pattern 2: Extract problems with "Problem N:" format
        pattern2 = r'##\s*Problem\s+(\d+):?\s*(.+?)(?=\n##\s*(?:Problem|\w+\s+Formulas?)|---\n\n##|$)'
        matches2 = re.finditer(pattern2, content, re.DOTALL)
        
        for match in matches2:
            problem_num = match.group(1)
            problem_content = match.group(2).strip()
            
            # Parse problem structure (similar to examples)
            problem_data = self._parse_problem(problem_content)
            
            if problem_data:
                # Create full chunk with question + solution
                chunk_text = self._format_problem_chunk(problem_num, problem_data)
                
                # Determine difficulty
                difficulty = self._infer_difficulty(problem_content, topic)
                
                # Extract pattern/concept
                pattern_type = self._infer_pattern(problem_data['title'])
                
                chunks.append({
                    "text": chunk_text,
                    "type": ChunkType.EXAMPLE.value,
                    "topic": topic,
                    "subtopic": problem_data['title'],
                    "pattern": pattern_type,
                    "source": source,
                    "difficulty": difficulty
                })
        
        return chunks
    
    def _parse_example(self, example_text: str) -> Dict[str, Any]:
        """Parse example into structured components"""
        # Extract title
        title_match = re.match(r'(.+?)(?:\n|$)', example_text)
        title = title_match.group(1).strip() if title_match else "Untitled"
        
        # Extract problem
        problem_match = re.search(r'\*\*Problem:\*\*\s*(.*?)(?=\*\*Solution:\*\*|\*\*Answer:\*\*|$)', 
                                   example_text, re.DOTALL)
        problem = problem_match.group(1).strip() if problem_match else ""
        
        # Extract solution
        solution_match = re.search(r'\*\*Solution:\*\*\s*(.*?)(?=\*\*Answer:\*\*|\*\*Verification:\*\*|---|\n\n##|$)', 
                                    example_text, re.DOTALL)
        solution = solution_match.group(1).strip() if solution_match else ""
        
        # Extract answer
        answer_match = re.search(r'\*\*Answer:\*\*\s*(.*?)(?=\*\*Verification:\*\*|---|\n\n##|$)', 
                                  example_text, re.DOTALL)
        answer = answer_match.group(1).strip() if answer_match else ""
        
        # Extract verification if present
        verification_match = re.search(r'\*\*Verification:\*\*\s*(.*?)(?=---|\n\n##|$)', 
                                        example_text, re.DOTALL)
        verification = verification_match.group(1).strip() if verification_match else ""
        
        if not problem and not solution:
            return None
        
        return {
            "title": title,
            "problem": problem,
            "solution": solution,
            "answer": answer,
            "verification": verification
        }
    
    def _format_example_chunk(self, example_num: str, data: Dict[str, Any]) -> str:
        """Format example as a clean chunk"""
        chunk = f"Example {example_num}: {data['title']}\n\n"
        
        if data['problem']:
            chunk += f"Problem:\n{data['problem']}\n\n"
        
        if data['solution']:
            chunk += f"Solution:\n{data['solution']}\n\n"
        
        if data['answer']:
            chunk += f"Answer: {data['answer']}\n"
        
        if data['verification']:
            chunk += f"\nVerification:\n{data['verification']}"
        
        return chunk.strip()
    
    def _parse_problem(self, problem_text: str) -> Dict[str, Any]:
        """Parse problem (similar to example) into structured components"""
        # Extract title
        title_match = re.match(r'(.+?)(?:\n|$)', problem_text)
        title = title_match.group(1).strip() if title_match else "Untitled"
        
        # Extract question
        question_match = re.search(r'\*\*Question:\*\*\s*(.*?)(?=\*\*Solution:\*\*|\*\*Answer:\*\*|$)', 
                                   problem_text, re.DOTALL)
        question = question_match.group(1).strip() if question_match else ""
        
        # Extract solution
        solution_match = re.search(r'\*\*Solution:\*\*\s*(.*?)(?=\*\*Answer:\*\*|---|\n\n##|$)', 
                                    problem_text, re.DOTALL)
        solution = solution_match.group(1).strip() if solution_match else ""
        
        # Extract answer
        answer_match = re.search(r'\*\*Answer:\*\*\s*(.*?)(?=---|\n\n##|$)', 
                                  problem_text, re.DOTALL)
        answer = answer_match.group(1).strip() if answer_match else ""
        
        if not question and not solution:
            return None
        
        return {
            "title": title,
            "problem": question,
            "solution": solution,
            "answer": answer,
            "verification": ""
        }
    
    def _format_problem_chunk(self, problem_num: str, data: Dict[str, Any]) -> str:
        """Format problem as a clean chunk"""
        chunk = f"Problem {problem_num}: {data['title']}\n\n"
        
        if data['problem']:
            chunk += f"Question:\n{data['problem']}\n\n"
        
        if data['solution']:
            chunk += f"Solution:\n{data['solution']}\n\n"
        
        if data['answer']:
            chunk += f"Answer: {data['answer']}\n"
        
        return chunk.strip()
    
    def _extract_procedures(self, content: str, topic: str, source: str) -> List[Dict[str, Any]]:
        """Extract step-by-step procedures"""
        chunks = []
        
        # Pattern: Procedure sections
        pattern = r'(?:Procedure|Steps?|Method|Algorithm):\s*(.+?)(?:\n\n##|\n\n\*\*|---|\Z)'
        matches = re.finditer(pattern, content, re.MULTILINE | re.DOTALL)
        
        for match in matches:
            procedure_text = match.group(0).strip()
            
            if len(procedure_text) > 30 and len(procedure_text) < 1000:
                chunks.append({
                    "text": procedure_text,
                    "type": ChunkType.PROCEDURE.value,
                    "topic": topic,
                    "subtopic": self._infer_subtopic(content, match.start()),
                    "source": source,
                    "difficulty": "basic"
                })
        
        return chunks
    
    def _extract_pitfalls(self, content: str, topic: str, source: str) -> List[Dict[str, Any]]:
        """Extract common mistakes/pitfalls"""
        chunks = []
        
        # Pattern: Common mistakes sections
        pattern = r'(?:Common\s+(?:Mistake|Error|Pitfall))s?:(.+?)(?:\n\n##|\n\n\*\*|---|\Z)'
        matches = re.finditer(pattern, content, re.MULTILINE | re.DOTALL)
        
        for match in matches:
            pitfall_text = match.group(0).strip()
            
            # Split individual mistakes
            individual_mistakes = re.split(r'\n(?=(?:Wrong|Incorrect|❌|✅|Correct):)', pitfall_text)
            
            for mistake in individual_mistakes:
                mistake = mistake.strip()
                if len(mistake) > 20 and len(mistake) < 500:
                    chunks.append({
                        "text": mistake,
                        "type": ChunkType.PITFALL.value,
                        "topic": topic,
                        "subtopic": self._infer_subtopic(content, 0),
                        "source": source,
                        "difficulty": "basic"
                    })
        
        return chunks
    
    def _extract_key_formulas_section(self, content: str, topic: str, source: str) -> List[Dict[str, Any]]:
        """Extract formulas from 'Key Formulas' section"""
        chunks = []
        
        # Find Key Formulas section
        pattern = r'##\s*Key Formulas?(?:\s+[&\w\s]+)?\s*\n(.*?)(?=\n##|\Z)'
        match = re.search(pattern, content, re.DOTALL)
        
        if not match:
            return chunks
        
        formulas_section = match.group(1)
        
        # Split by subsections or bullet points
        formula_groups = re.split(r'\n###\s+|\n\*\*[A-Z]', formulas_section)
        
        for group in formula_groups:
            group = group.strip()
            if not group:
                continue
            
            # Split individual formulas (by bullet points or blank lines)
            individual_formulas = re.split(r'\n-\s+|\n\*\s+|\n\n', group)
            
            for formula in individual_formulas:
                formula = formula.strip()
                
                # Valid formula criteria
                if (len(formula) > 15 and len(formula) < 300 and 
                    ('=' in formula or '$' in formula)):
                    
                    chunks.append({
                        "text": formula,
                        "type": ChunkType.FORMULA.value,
                        "topic": topic,
                        "subtopic": "key_formulas",
                        "source": source,
                        "difficulty": "reference"
                    })
        
        return chunks
    
    def _infer_subtopic(self, content: str, position: int) -> str:
        """Infer subtopic from nearby headings"""
        # Find nearest heading before position
        text_before = content[:position]
        heading_match = re.findall(r'##\s+(.+?)(?:\n|$)', text_before)
        
        if heading_match:
            return heading_match[-1].strip()
        
        return "general"
    
    def _infer_difficulty(self, text: str, topic: str) -> str:
        """Infer difficulty level from content"""
        text_lower = text.lower()
        
        # Keywords for difficulty
        if any(word in text_lower for word in ['basic', 'simple', 'introduction', 'fundamental']):
            return "basic"
        elif any(word in text_lower for word in ['jee', 'advanced', 'olympiad', 'competitive']):
            return "jee_advanced"
        elif any(word in text_lower for word in ['intermediate', 'medium']):
            return "intermediate"
        else:
            return "jee_basic"
    
    def _infer_pattern(self, title: str) -> str:
        """Infer problem pattern from title"""
        title_lower = title.lower()
        
        patterns = {
            "limit": ["limit", "lim"],
            "derivative": ["derivative", "differentiation", "tangent"],
            "integration": ["integral", "integration"],
            "probability": ["probability", "chance"],
            "conditional_probability": ["conditional", "given"],
            "permutation": ["permutation", "arrangement"],
            "combination": ["combination", "selection"],
            "matrix": ["matrix", "matrices", "determinant"],
            "vector": ["vector", "dot product", "cross product"],
            "linear_equations": ["linear", "system", "equation"],
            "quadratic": ["quadratic", "parabola"],
            "trigonometry": ["sin", "cos", "tan", "trigonometric"],
        }
        
        for pattern_name, keywords in patterns.items():
            if any(keyword in title_lower for keyword in keywords):
                return pattern_name
        
        return "general"
    
    def create_hybrid_chunks(self, chunks: List[Dict[str, Any]]) -> Tuple[List[Dict], List[Dict]]:
        """
        Separate chunks into knowledge and example sets for hybrid retrieval
        
        Args:
            chunks: All chunks
        
        Returns:
            Tuple of (knowledge_chunks, example_chunks)
        """
        knowledge_chunks = []
        example_chunks = []
        
        for chunk in chunks:
            if chunk['type'] in [ChunkType.FORMULA.value, ChunkType.DEFINITION.value, 
                                  ChunkType.PROCEDURE.value]:
                knowledge_chunks.append(chunk)
            elif chunk['type'] in [ChunkType.EXAMPLE.value, ChunkType.PITFALL.value]:
                example_chunks.append(chunk)
            else:
                # Default to knowledge
                knowledge_chunks.append(chunk)
        
        return knowledge_chunks, example_chunks
    
    def _extract_reference_sections(self, content: str, topic: str, source: str) -> List[Dict[str, Any]]:
        """
        Extract content from reference-style markdown files
        Handles files with ### headings like Definition, Formula, Properties, etc.
        
        Args:
            content: File content
            topic: Topic name
            source: Source filename
        
        Returns:
            List of chunks
        """
        chunks = []
        
        # Pattern: Extract ### sections with their content
        pattern = r'###\s+(.+?)\n(.*?)(?=\n###|\n##|$)'
        matches = re.finditer(pattern, content, re.DOTALL)
        
        for match in matches:
            section_title = match.group(1).strip()
            section_content = match.group(2).strip()
            
            # Skip if too short or too long
            if len(section_content) < 20 or len(section_content) > 2000:
                continue
            
            # Combine title and content
            full_text = f"{section_title}\n\n{section_content}"
            
            # Determine chunk type based on section title
            chunk_type = "definition"
            if any(word in section_title.lower() for word in ['formula', 'equation']):
                chunk_type = "formula"
            elif any(word in section_title.lower() for word in ['definition', 'concept']):
                chunk_type = "definition"
            elif any(word in section_title.lower() for word in ['property', 'properties', 'rule']):
                chunk_type = "concept"
            elif any(word in section_title.lower() for word in ['example', 'case']):
                chunk_type = "example"
            
            chunks.append({
                "text": full_text,
                "type": chunk_type,
                "topic": topic,
                "subtopic": section_title,
                "source": source,
                "difficulty": "basic"
            })
        
        return chunks
    
    def get_chunk_stats(self, chunks: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Get statistics about chunks"""
        stats = {
            "total": len(chunks),
            "by_type": {},
            "by_topic": {},
            "by_difficulty": {},
            "avg_length": 0
        }
        
        total_length = 0
        
        for chunk in chunks:
            # By type
            chunk_type = chunk.get('type', 'unknown')
            stats['by_type'][chunk_type] = stats['by_type'].get(chunk_type, 0) + 1
            
            # By topic
            topic = chunk.get('topic', 'unknown')
            stats['by_topic'][topic] = stats['by_topic'].get(topic, 0) + 1
            
            # By difficulty
            difficulty = chunk.get('difficulty', 'unknown')
            stats['by_difficulty'][difficulty] = stats['by_difficulty'].get(difficulty, 0) + 1
            
            # Length
            total_length += len(chunk.get('text', ''))
        
        if chunks:
            stats['avg_length'] = total_length // len(chunks)
        
        return stats
