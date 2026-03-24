def binary_search(sorted_list, target_value):
    """
    Searches for target_value in sorted_list using binary search.
    Returns the index of target_value if found, or -1 if not present.
    """
    left_index = 0
    right_index = len(sorted_list) - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_value = sorted_list[middle_index]

        if middle_value == target_value:
            return middle_index
        elif middle_value < target_value:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1

    return -1


if __name__ == "__main__":
    numbers = [2, 5, 8, 12, 16, 23, 38, 45, 67, 90]
    target = 23
    index = binary_search(numbers, target)
    if index != -1:
        print(f"Value {target} found at index {index}")
    else:
        print(f"Value {target} not found")
