# Elementary Sorting Algorithms

Implementation of Bubble Sort, Selection Sort, and Insertion Sort in Python.
Activity for Data Structures and Algorithms.

**Name:** Ambrichie Rose M. Encio
**Section:** BSCS2A

## Files
- `sorting.py`: the three sorting functions and a driver program

## Features
- Sorts integer arrays in ascending order, in place
- No built-in sort functions are used
- Bubble Sort has an early-exit optimization (stops if a pass makes no swaps)
- Selection Sort finds the minimum of the unsorted portion on each pass
- Insertion Sort uses shifting instead of repeated swapping
- Each function returns the number of comparisons and swaps/shifts

## How to Run
Requires Python 3.

    python sorting.py

## Test Cases
The driver runs all three algorithms on:
- Random: [29, 10, 14, 37, 13, 5, 22]
- Already sorted: [1, 2, 3, 4, 5, 6, 7]
- Reverse sorted: [7, 6, 5, 4, 3, 2, 1]
- Duplicates: [4, 2, 4, 1, 2, 3, 1]
- Edge cases: [], [42], [2, 1]

## Counting Convention
- A comparison is one test between two array elements.
- Selection Sort counts a swap only when the minimum is not already in place.
- Insertion Sort counts each element moved one slot to the right as a shift.
