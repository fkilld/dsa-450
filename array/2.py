"""
PROBLEM: Find Kth Smallest Element in an Array
================================================
Given an array and a number k, find the kth smallest element in the array.

Example:
    Input:  arr = [7, 10, 4, 3, 20, 15], k = 3
    Output: 7
    Explanation: The 3rd smallest element is 7 (sorted: [3, 4, 7, 10, 15, 20])

    Input:  arr = [7, 10, 4, 20, 15], k = 4
    Output: 15

APPROACH: QuickSelect Algorithm
=================================
WHY THIS APPROACH?
- QuickSelect is an optimized version of QuickSort for selection problems
- Average Time Complexity: O(n) - much better than sorting O(n log n)
- Worst Case: O(n²) but can be avoided with random pivot selection
- Space Complexity: O(1) - in-place algorithm
- We don't need to fully sort the array, just partition it to find the kth element

HOW IT WORKS:
1. Choose a pivot element (we use the rightmost element)
2. Partition the array so elements ≤ pivot are on left, elements > pivot are on right
3. If pivot is at position k-1, we found the kth smallest element
4. If k-1 < pivot_index, search in left partition
5. If k-1 > pivot_index, search in right partition

FLOW EXAMPLE:
=============
Array: [7, 10, 4, 3, 20, 15], k = 3 (find 3rd smallest)
Goal: Find element at position k-1 = 2 after sorting

Step 1: Initial call quickSelect(arr, 0, 5, 2)
    Pivot = arr[5] = 15
    Partition array around 15:
    [7, 10, 4, 3, 15, 20]
           ↑
    pivot_index = 4

Step 2: k-1 (2) < pivot_index (4)
    Search left partition: quickSelect(arr, 0, 3, 2)
    Pivot = arr[3] = 3
    Partition array around 3:
    [3, 7, 10, 4, 15, 20]
     ↑
    pivot_index = 0

Step 3: k-1 (2) > pivot_index (0)
    Search right partition: quickSelect(arr, 1, 3, 2)
    Pivot = arr[3] = 4
    Partition array around 4:
    [3, 4, 10, 7, 15, 20]
        ↑
    pivot_index = 1

Step 4: k-1 (2) > pivot_index (1)
    Search right partition: quickSelect(arr, 2, 3, 2)
    Pivot = arr[3] = 7
    Partition array around 7:
    [3, 4, 7, 10, 15, 20]
           ↑
    pivot_index = 2

Step 5: k-1 (2) == pivot_index (2)
    Found! Return arr[2] = 7

FLOWCHART:
==========
    ┌─────────────────────────────────┐
    │   Start: kth_smallest(arr, k)   │
    └───────────────┬─────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────┐
    │ Validate: arr empty or k invalid? │
    └───────────┬───────────────────────┘
                │ Yes
                ├──────► Return -1
                │ No
                ▼
    ┌─────────────────────────────────────┐
    │ Call quick_select(arr, 0, n-1, k-1) │
    └───────────────┬─────────────────────┘
                    │
                    ▼
    ┌─────────────────────────────────┐
    │     Is left == right?           │
    └────────┬────────────────────────┘
             │ Yes
             ├────────► Return arr[left]
             │ No
             ▼
    ┌─────────────────────────────────┐
    │  Partition around pivot (right) │
    │  - Elements ≤ pivot go left     │
    │  - Elements > pivot stay right  │
    └────────┬────────────────────────┘
             │
             ▼
    ┌─────────────────────────────────┐
    │   Compare pivot_index with k-1  │
    └────┬────────────────────────────┘
         │
    ┌────┴─────┬──────────┬─────────┐
    │          │          │         │
    │ ==       │ <        │ >       │
    │          │          │         │
    ▼          ▼          ▼         ▼
 Return    Recurse    Recurse
arr[pivot] left       right
          partition   partition

TIME COMPLEXITY:
- Average Case: O(n) - Each partition reduces problem size by ~half
- Worst Case: O(n²) - When pivot is always smallest/largest
- Best Case: O(n) - When pivot is always median

SPACE COMPLEXITY: O(log n) for recursion stack (average case)
"""

def kth_smallest(arr, k):
    """
    Find the kth smallest element in an array using QuickSelect algorithm.

    Args:
        arr: List of integers
        k: Position of the element to find (1-based index)

    Returns:
        The kth smallest element or -1 if not found

    Time Complexity: Average O(n), worst case O(n²)
    Space Complexity: O(1) for auxiliary space, O(log n) for recursion
    """
    # Validate input: check for empty array or invalid k
    if not arr or k <= 0 or k > len(arr):
        return -1

    def partition(arr, left, right):
        """
        Partition the array around a pivot element (rightmost element).

        After partitioning:
        - All elements ≤ pivot are on the left side
        - Pivot is at its final sorted position
        - All elements > pivot are on the right side

        Args:
            arr: Array to partition
            left: Start index of partition range
            right: End index of partition range (pivot location)

        Returns:
            Final index of the pivot element
        """
        # Choose rightmost element as pivot
        pivot = arr[right]

        # i tracks the position where next element ≤ pivot should go
        # Elements from left to i are ≤ pivot
        i = left - 1

        # Scan through elements from left to right-1
        for j in range(left, right):
            # If current element is smaller than or equal to pivot
            if arr[j] <= pivot:
                i += 1  # Move boundary of smaller elements
                # Swap current element with element at boundary
                arr[i], arr[j] = arr[j], arr[i]

        # Place pivot in its final position (after all smaller elements)
        arr[i + 1], arr[right] = arr[right], arr[i + 1]

        # Return final pivot position
        return i + 1

    def quick_select(arr, left, right, k_index):
        """
        Recursively find the element at k_index position in sorted order.

        Uses QuickSelect algorithm which is similar to QuickSort but
        only recurses into one partition instead of both.

        Args:
            arr: Array to search
            left: Left boundary of current search range
            right: Right boundary of current search range
            k_index: 0-based index of target element in sorted order

        Returns:
            The element at k_index position
        """
        # Base case: only one element in range
        if left == right:
            return arr[left]

        # Partition array and get pivot's final position
        pivot_index = partition(arr, left, right)

        # Check if pivot is at the target position
        if pivot_index == k_index:
            # Found the kth smallest element!
            return arr[pivot_index]

        elif k_index < pivot_index:
            # Target is in left partition (smaller elements)
            # Recurse on left side only
            return quick_select(arr, left, pivot_index - 1, k_index)

        else:
            # Target is in right partition (larger elements)
            # Recurse on right side only
            return quick_select(arr, pivot_index + 1, right, k_index)

    # Convert k from 1-based to 0-based index and find the element
    return quick_select(arr, 0, len(arr) - 1, k - 1)


# Test cases
if __name__ == "__main__":
    # Test 1: Find 3rd smallest in [7, 10, 4, 3, 20, 15]
    arr1 = [7, 10, 4, 3, 20, 15]
    k1 = 3
    print(f"Array: {arr1}")
    print(f"3rd smallest element: {kth_smallest(arr1, k1)}")  # Expected: 7

    # Test 2: Find 4th smallest in [7, 10, 4, 20, 15]
    arr2 = [7, 10, 4, 20, 15]
    k2 = 4
    print(f"\nArray: {arr2}")
    print(f"4th smallest element: {kth_smallest(arr2, k2)}")  # Expected: 15
