def moving_average(numbers, window_size):
    if window_size <= 0:
        raise ValueError("Window size must be positive")
    if window_size > len(numbers):
        return []

    result = []
    for i in range(len(numbers) - window_size + 1):
        window = numbers[i:i + window_size]
        result.append(sum(window) / window_size)
    return result


def count_word_frequencies(text):
    frequencies = {}
    for word in text.lower().split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies
