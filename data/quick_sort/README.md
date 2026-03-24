# Quick Sort

Victor Manuel Montini (2026-03-22)

## Algorithm name

Quick Sort

## Author

Victor Manuel Montini (2026-03-22)

## Algorithm description

Quick sort is a highly efficient divide-and-conquer sorting algorithm. It works by selecting a pivot element and partitioning the array into two sub-arrays: elements less than or equal to the pivot and elements greater than the pivot. It then recursively sorts the sub-arrays. The choice of pivot affects performance; this implementation uses the last element as the pivot. Average time complexity is O(n log n), worst case O(n²).

## Model used to create the base code

claude-sonnet-4-6

### Prompt

```
Write a C implementation of quick sort with a function called quick_sort that receives an integer array `number_array`, a `low_index` and a `high_index`, and sorts the array in ascending order recursively using the last element as pivot. Include helper functions swap_elements and partition_array. Use descriptive English variable names.
```

## Obfuscated version

manually obfuscated
