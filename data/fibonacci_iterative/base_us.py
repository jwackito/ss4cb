def fibonacci_iterative(term_count):
    """
    Returns a list containing the first term_count numbers
    of the Fibonacci sequence using an iterative approach.
    """
    if term_count <= 0:
        return []
    if term_count == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < term_count:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence


if __name__ == "__main__":
    count = 10
    result = fibonacci_iterative(count)
    print(f"First {count} Fibonacci numbers: {result}")
