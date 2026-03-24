def linear_search(item_list, target_value):
    """
    Searches for target_value in item_list by checking each element sequentially.
    Returns the index of target_value if found, or -1 if not present.
    """
    current_index = 0
    while current_index < len(item_list):
        current_element = item_list[current_index]
        if current_element == target_value:
            return current_index
        current_index += 1
    return -1


if __name__ == "__main__":
    numbers = [34, 7, 23, 32, 5, 62, 14, 89]
    target = 32
    index = linear_search(numbers, target)
    if index != -1:
        print(f"Value {target} found at index {index}")
    else:
        print(f"Value {target} not found")
