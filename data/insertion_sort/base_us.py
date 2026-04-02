def insertion_sort(array):
    """Sort a list in ascending order using the insertion sort algorithm."""
    for current_index in range(1, len(array)):
        current_value = array[current_index]
        position = current_index - 1

        while position >= 0 and array[position] > current_value:
            array[position + 1] = array[position]
            position -= 1

        array[position + 1] = current_value

    return array