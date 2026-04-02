# Radix Sort

## Author
Luca Giordano (2026-04-01)

## Algorithm Description
Radix sort is a non-comparative integer sorting algorithm that sorts elements digit by digit, from the least significant to the most significant digit. At each digit position, it uses a stable subroutine — typically counting sort — to arrange the elements according to that digit without disturbing the relative order established by previous passes. Because it does not rely on comparisons between elements, it can achieve O(nk) time complexity, where n is the number of elements and k is the number of digits in the maximum value.

## Model Used to Create the Base Code
claude-sonnet-4-6

### Prompt
```
Write a Python function called `radix_sort` that receives a list of non-negative integers called `array` and returns it sorted in ascending order using the radix sort algorithm with counting sort as the stable subroutine. Use descriptive English names for all variables.
```

## Obfuscated Version
Manually obfuscated