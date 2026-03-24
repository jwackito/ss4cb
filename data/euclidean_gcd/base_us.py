def euclidean_gcd(first_number, second_number):
    """
    Returns the greatest common divisor of first_number and second_number
    using the Euclidean algorithm.
    """
    dividend = first_number
    divisor = second_number

    while divisor != 0:
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder

    return dividend


if __name__ == "__main__":
    num_a = 48
    num_b = 18
    result = euclidean_gcd(num_a, num_b)
    print(f"GCD of {num_a} and {num_b} is: {result}")
