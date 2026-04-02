# Shell Sort

## Author
Luca Giordano (2026-04-01)

## Algorithm Description
Shell sort is a generalization of insertion sort that allows the exchange of elements that are far apart. The algorithm sorts elements at a given gap interval, progressively reducing the gap until it reaches 1, at which point it performs a final insertion sort pass. Because elements are already partially sorted by the time the gap reaches 1, this final pass is significantly cheaper than a plain insertion sort. Time complexity depends on the gap sequence used; with the default halving sequence it is O(n²) in the worst case, but other sequences can achieve O(n log² n).

## Model Used to Create the Base Code
claude-sonnet-4-6

### Prompt
```
Write a Python function called `shell_sort` that receives a list called `array` and returns it sorted in ascending order using the shell sort algorithm with a halving gap sequence. Use descriptive English names for all variables.
```

## Obfuscated Version
Manually obfuscated