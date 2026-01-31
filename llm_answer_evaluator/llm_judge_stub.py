"""
This module simulates how an LLM (e.g. GPT / Claude)
can be used as a judge to score model answers.

In production, this could be replaced with a real API call.
"""

from dataclasses import dataclass


@dataclass
class LLMJudgeResult:
    score: float
    reasoning: str


def llm_judge(question: str, expected: str, answer: str) -> LLMJudgeResult:
    """
    Simulated LLM-based evaluation logic.
    """
    if expected.lower() in answer.lower():
        return LLMJudgeResult(
            score=1.0,
            reasoning="The answer contains the expected key information."
        )

    return LLMJudgeResult(
        score=0.0,
        reasoning="The answer does not sufficiently address the expected result."
    )
