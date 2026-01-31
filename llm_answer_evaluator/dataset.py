from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List


@dataclass
class Sample:
    id: str
    question: str
    expected: str
    model_answer: str


def load_jsonl(path: str | Path) -> List[Sample]:
    path = Path(path)
    samples: List[Sample] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        obj = json.loads(line)
        samples.append(
            Sample(
                id=str(obj["id"]),
                question=obj["question"],
                expected=obj["expected"],
                model_answer=obj["model_answer"],
            )
        )
    return samples
