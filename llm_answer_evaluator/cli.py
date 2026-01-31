from __future__ import annotations

import argparse

from .dataset import load_jsonl
from .evaluator import evaluate_all


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate model answers on a JSONL dataset.")
    parser.add_argument("--data", required=True, help="Path to JSONL file")
    args = parser.parse_args()

    samples = load_jsonl(args.data)
    results = evaluate_all(samples)

    total = len(results)
    avg = sum(r.score for r in results) / total if total else 0.0

    print(f"Samples: {total}")
    print(f"Average score: {avg:.3f}\n")

    for r in results:
        print(f"[{r.sample_id}] score={r.score:.1f} rule={r.rule} note={r.explanation}")


if __name__ == "__main__":
    main()
