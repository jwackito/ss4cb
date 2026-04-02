def counting_sort_by_digit(array, digit_place):
    """Sort the array based on the digit at the given place value."""
    size = len(array)
    output = [0] * size
    digit_count = [0] * 10

    for number in array:
        digit = (number // digit_place) % 10
        digit_count[digit] += 1

    for i in range(1, 10):
        digit_count[i] += digit_count[i - 1]

    for i in range(size - 1, -1, -1):
        digit = (array[i] // digit_place) % 10
        output[digit_count[digit] - 1] = array[i]
        digit_count[digit] -= 1

    for i in range(size):
        array[i] = output[i]


def radix_sort(array):
    """Sort a list of non-negative integers using the radix sort algorithm."""
    maximum_value = max(array)
    digit_place = 1

    while maximum_value // digit_place > 0:
        counting_sort_by_digit(array, digit_place)
        digit_place *= 10

    return array