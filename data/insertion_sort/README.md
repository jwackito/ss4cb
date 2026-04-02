# Insertion Sort

## Author
Luca Giordano (2026-04-01)

## Algorithm Description
Insertion sort is a simple comparison-based sorting algorithm that builds the final sorted array one element at a time. It iterates through the input, and for each element, finds its correct position within the already-sorted portion of the array by shifting larger elements one position to the right. It is efficient for small datasets and nearly-sorted arrays, with a worst-case and average time complexity of O(n²) and a best-case of O(n).

## Model Used to Create the Base Code
claude-sonnet-4-6

### Prompt
```
Write a Python function called `insertion_sort` that receives a list called `array` and returns it sorted in ascending order using the insertion sort algorithm. Use descriptive English names for all variables.
```

## Obfuscated Version
manually obfuscated