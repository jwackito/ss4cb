#include <stdio.h>

void swap_elements(int *first_element, int *second_element) {
    int temporary_value = *first_element;
    *first_element = *second_element;
    *second_element = temporary_value;
}

int partition_array(int number_array[], int low_index, int high_index) {
    int pivot_value = number_array[high_index];
    int smaller_element_index = low_index - 1;
    int current_index;

    for (current_index = low_index; current_index < high_index; current_index++) {
        if (number_array[current_index] <= pivot_value) {
            smaller_element_index++;
            swap_elements(&number_array[smaller_element_index], &number_array[current_index]);
        }
    }
    swap_elements(&number_array[smaller_element_index + 1], &number_array[high_index]);
    return smaller_element_index + 1;
}

void quick_sort(int number_array[], int low_index, int high_index) {
    if (low_index < high_index) {
        int pivot_index = partition_array(number_array, low_index, high_index);
        quick_sort(number_array, low_index, pivot_index - 1);
        quick_sort(number_array, pivot_index + 1, high_index);
    }
}

int main() {
    int numbers[] = {10, 7, 8, 9, 1, 5};
    int array_length = 6;
    int index;

    quick_sort(numbers, 0, array_length - 1);

    printf("Sorted array: ");
    for (index = 0; index < array_length; index++)
        printf("%d ", numbers[index]);
    printf("\n");
    return 0;
}
