#include <stdio.h>
#include <stdlib.h>

void merge_halves(int number_array[], int left_index, int middle_index, int right_index) {
    int left_size = middle_index - left_index + 1;
    int right_size = right_index - middle_index;
    int left_position, right_position, merged_position;

    int *left_temp = (int *)malloc(left_size * sizeof(int));
    int *right_temp = (int *)malloc(right_size * sizeof(int));

    /* Copy data into temporary arrays */
    for (left_position = 0; left_position < left_size; left_position++)
        left_temp[left_position] = number_array[left_index + left_position];
    for (right_position = 0; right_position < right_size; right_position++)
        right_temp[right_position] = number_array[middle_index + 1 + right_position];

    left_position = 0;
    right_position = 0;
    merged_position = left_index;

    /* Merge the two halves back into the original array */
    while (left_position < left_size && right_position < right_size) {
        if (left_temp[left_position] <= right_temp[right_position]) {
            number_array[merged_position] = left_temp[left_position];
            left_position++;
        } else {
            number_array[merged_position] = right_temp[right_position];
            right_position++;
        }
        merged_position++;
    }

    while (left_position < left_size) {
        number_array[merged_position] = left_temp[left_position];
        left_position++;
        merged_position++;
    }
    while (right_position < right_size) {
        number_array[merged_position] = right_temp[right_position];
        right_position++;
        merged_position++;
    }

    free(left_temp);
    free(right_temp);
}

void merge_sort(int number_array[], int left_index, int right_index) {
    if (left_index < right_index) {
        int middle_index = left_index + (right_index - left_index) / 2;
        merge_sort(number_array, left_index, middle_index);
        merge_sort(number_array, middle_index + 1, right_index);
        merge_halves(number_array, left_index, middle_index, right_index);
    }
}

int main() {
    int numbers[] = {38, 27, 43, 3, 9, 82, 10};
    int array_length = 7;
    int index;

    merge_sort(numbers, 0, array_length - 1);

    printf("Sorted array: ");
    for (index = 0; index < array_length; index++)
        printf("%d ", numbers[index]);
    printf("\n");
    return 0;
}
