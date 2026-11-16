def bubble_sort(arr):
    comparisons = swaps = 0
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        # After pass i, the largest i+1 elements are in their final place
        for j in range(n - 1 - i):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:  # early exit: a full pass with no swaps means sorted
            break
    return comparisons, swaps


def selection_sort(arr):
    comparisons = swaps = 0
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        # Find the minimum of the unsorted portion arr[i..n-1]
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:  # only swap when needed
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return comparisons, swaps


def insertion_sort(arr):
    comparisons = shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift larger elements one slot right (no repeated swapping)
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break
        arr[j + 1] = key  # drop the key into its gap
    return comparisons, shifts


def main():
    cases = {
        "A. Random": [29, 10, 14, 37, 13, 5, 22],
        "B. Sorted": [1, 2, 3, 4, 5, 6, 7],
        "C. Reverse": [7, 6, 5, 4, 3, 2, 1],
        "D. Duplicates": [4, 2, 4, 1, 2, 3, 1],
        "E1. Empty": [],
        "E2. Single": [42],
        "E3. Two items": [2, 1],
    }
    algos = [("Bubble", bubble_sort), ("Selection", selection_sort),
             ("Insertion", insertion_sort)]

    for name, data in cases.items():
        print(f"\n{name}: input = {data}")
        for algo_name, fn in algos:
            arr = data.copy()  # fresh copy so each algorithm sees the original
            c, w = fn(arr)
            print(f"  {algo_name:<10} -> {arr}  comparisons={c}, swaps/shifts={w}")


if __name__ == "__main__":
    main()