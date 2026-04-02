def shell_sort(array):
    """Sort a list in ascending order using the shell sort algorithm."""
    gap = len(array) // 2

    while gap > 0:
        for current_index in range(gap, len(array)):
            current_value = array[current_index]
            position = current_index

            while position >= gap and array[position - gap] > current_value:
                array[position] = array[position - gap]
                position -= gap

            array[position] = current_value

        gap //= 2

    return array