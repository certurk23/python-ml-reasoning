def evaluate_answer(expected, generated):
    """
    Simple evaluation function for AI-generated answers.
    Returns a score based on correctness.
    """
    if expected == generated:
        return 1.0
    if expected in generated:
        return 0.5
    return 0.0


expected_answer = "The time complexity is O(n)"
generated_answer = "The algorithm runs in O(n) time"

score = evaluate_answer(expected_answer, generated_answer)
print("Evaluation score:", score)
