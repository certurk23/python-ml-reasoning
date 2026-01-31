from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Score:
    correctness: float  # 0.0 - 1.0
    explanation: str


def normalize(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"\s+", " ", text)
    return text


def exact_match(expected: str, answer: str) -> Score:
    e = normalize(expected)
    a = normalize(answer)
    if a == e:
        return Score(1.0, "Exact match.")
    return Score(0.0, "Not an exact match.")


def contains_expected(expected: str, answer: str) -> Score:
    e = normalize(expected)
    a = normalize(answer)
    if e in a:
        return Score(1.0, "Answer contains the expected key phrase.")
    return Score(0.0, "Answer does not contain the expected key phrase.")


def simple_numeric_check(expected: str, answer: str) -> Score:
    # Good for basic arithmetic / numeric targets (e.g., "4", "3.14")
    e = normalize(expected)
    a = normalize(answer)
    if re.fullmatch(r"-?\d+(\.\d+)?", e) and re.fullmatch(r"-?\d+(\.\d+)?", a):
        return Score(1.0 if a == e else 0.0, "Numeric exact match check.")
    return Score(0.0, "Expected/answer are not purely numeric.")
