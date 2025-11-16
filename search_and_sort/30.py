"""
PROBLEM: Count Inversions
Given an array of integers, find the Inversion Count.
Inversion Count indicates how far (or close) the array is from being sorted.

An inversion is a pair (i, j) where i < j but arr[i] > arr[j].

WHY THIS SOLUTION:
Naive: Check all pairs - O(n^2)
We use MODIFIED MERGE SORT to count in O(n log n)!

KEY INSIGHT:
During merge sort, when we merge two sorted halves:
- If arr[i] > arr[j] where i is from left half, j from right half
- Then arr[i] forms inversions with ALL remaining elements in left half
- Count of inversions = (mid - i + 1)

Why? Because left half is sorted, if arr[i] > arr[j], then all elements
from i to mid are also > arr[j].

APPROACH:
1. Use merge sort to recursively sort array
2. During merge step:
   - If left[i] <= right[j]: No inversion, take left[i]
   - If left[i] > right[j]: Inversion found!
     - Count inversions: (mid - i + 1)
     - Take right[j]
3. Total inversions = inversions in left half + inversions in right half +
                       inversions during merge

TIME COMPLEXITY: O(n log n)
- Same as merge sort
- Each merge operation: O(n)
- log n levels
- Total: O(n log n)

SPACE COMPLEXITY: O(n) - for temporary array

EXAMPLE: arr = [2, 4, 1, 3, 5]
Split: [2, 4] and [1, 3, 5]

Left half [2, 4]: 0 inversions
Right half [1, 3, 5]: 0 inversions

Merge [2, 4] and [1, 3, 5]:
- Compare 2 vs 1: 2 > 1, inversions = (1-0+1) = 2 (pairs: (2,1), (4,1))
- Compare 2 vs 3: 2 < 3, no inversion
- Compare 4 vs 3: 4 > 3, inversions = (1-0+1) = 1 (pair: (4,3))

Total: 3 inversions

WHY INTERVIEWER WILL ACCEPT:
1. Shows modification of classic algorithm
2. O(n log n) vs naive O(n^2)
3. Understanding of divide and conquer
4. Counting during merge - creative insight
"""

# Count Inversions

def merge(arr, temp, left, mid, right):
    """
    Merge two sorted halves and count inversions.

    Args:
        arr: Original array
        temp: Temporary array for merging
        left: Start of left half
        mid: End of left half
        right: End of right half

    Returns:
        Count of inversions during merge
    """
    i = left      # Pointer for left subarray
    j = mid + 1   # Pointer for right subarray
    k = left      # Pointer for merged array
    inv = 0       # Inversion count

    # Merge the two sorted subarrays
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            # No inversion, take from left
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            # Inversion found!
            # All elements from i to mid are greater than arr[j]
            inv += mid - i + 1
            temp[k] = arr[j]
            j += 1
            k += 1

    # Copy remaining elements from left subarray
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Copy remaining elements from right subarray
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy merged elements back to original array
    for i in range(left, right + 1):
        arr[i] = temp[i]

    return inv

def merge_sort(arr, temp, left, right):
    """
    Perform merge sort and count inversions.

    Args:
        arr: Array to sort
        temp: Temporary array
        left: Left boundary
        right: Right boundary

    Returns:
        Total inversion count
    """
    inv = 0

    if left < right:
        mid = (left + right) // 2

        # Count inversions in left half
        inv += merge_sort(arr, temp, left, mid)

        # Count inversions in right half
        inv += merge_sort(arr, temp, mid + 1, right)

        # Count inversions during merge
        inv += merge(arr, temp, left, mid, right)

    return inv

def inv_count(arr):
    """
    Count inversions in array using merge sort.

    Args:
        arr: Input array

    Returns:
        Total inversion count
    """
    n = len(arr)
    temp = [0] * n
    result = merge_sort(arr, temp, 0, n - 1)
    return result

# Test
# arr = [2, 4, 1, 3, 5]
# print(f"Inversion count: {inv_count(arr)}")