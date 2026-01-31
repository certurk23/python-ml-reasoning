from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List, Tuple

from .dataset import Sample
from .metrics import Score, contains_expected, exact_match, simple_numeric_check


@dataclass
class EvaluationResult:
    sample_id: str
    score: float
    rule: str
    explanation: str


Rule = Tuple[str, Callable[[str, str], Score]]


DEFAULT_RULES: List[Rule] = [
    ("numeric_exact", simple_numeric_check),
    ("exact_match", exact_match),
    ("contains_expected", contains_expected),
]


def evaluate_sample(sample: Sample, rules: List[Rule] | None = None) -> EvaluationResult:
    rules = rules or DEFAULT_RULES

    best = Score(0.0, "No rule matched.")
    best_rule = "none"

    for name, fn in rules:
        s = fn(sample.expected, sample.model_answer)
        if s.correctness > best.correctness:
            best = s
            best_rule = name
        if best.correctness == 1.0:
            break

    return EvaluationResult(
        sample_id=sample.id,
        score=best.correctness,
        rule=best_rule,
        explanation=best.explanation,
    )


def evaluate_all(samples: List[Sample]) -> List[EvaluationResult]:
    return [evaluate_sample(s) for s in samples]
