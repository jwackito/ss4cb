#include <stdio.h>

void bubble_sort(int number_array[], int array_length) {
    /* Sort number_array in ascending order using bubble sort */
    int outer_pass;
    int inner_pass;
    int temp_value;
    int swapped;

    for (outer_pass = 0; outer_pass < array_length - 1; outer_pass++) {
        swapped = 0;
        for (inner_pass = 0; inner_pass < array_length - outer_pass - 1; inner_pass++) {
            if (number_array[inner_pass] > number_array[inner_pass + 1]) {
                /* Swap adjacent elements */
                temp_value = number_array[inner_pass];
                number_array[inner_pass] = number_array[inner_pass + 1];
                number_array[inner_pass + 1] = temp_value;
                swapped = 1;
            }
        }
        /* If no swap occurred in this pass, array is already sorted */
        if (swapped == 0) break;
    }
}

int main() {
    int numbers[] = {64, 34, 25, 12, 22, 11, 90};
    int array_length = 7;
    int index;

    bubble_sort(numbers, array_length);

    printf("Sorted array: ");
    for (index = 0; index < array_length; index++) {
        printf("%d ", numbers[index]);
    }
    printf("\n");
    return 0;
}
