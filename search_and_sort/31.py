"""
PROBLEM: In-Place Merge Sort
Implement Merge Sort without using extra memory for merge operation.
Standard merge sort uses O(n) extra space; in-place version uses O(1).

WHY THIS SOLUTION:
Standard merge sort: O(n log n) time, O(n) space
In-place merge sort: O(n^2) worst case time, O(1) space

Trade-off: We sacrifice time complexity for space complexity!

KEY INSIGHT:
Instead of merging into a temporary array, we shift elements in place:
- When right element should come before left elements
- Shift all left elements one position right
- Insert right element at correct position

This is similar to insertion sort for the merge step.

APPROACH:
1. Recursively divide array (same as standard merge sort)
2. For merge step:
   - Check if already sorted (arr[mid] <= arr[mid+1]) - return early
   - Use two pointers for left and right halves
   - If left element is smaller: move left pointer
   - If right element is smaller:
     - Save right element value
     - Shift all elements between start and start2 one position right
     - Place value at start position
     - Update pointers

TIME COMPLEXITY: O(n^2) worst case
- Recursive calls: O(log n) levels
- Merge with shifting: O(n^2) in worst case (when we shift many elements)
- Best case: O(n log n) when array is nearly sorted

SPACE COMPLEXITY: O(1) for merge operation
- Only O(log n) for recursion stack
- No auxiliary array for merging

EXAMPLE: arr = [12, 11, 13, 5, 6, 7]
Split: [12, 11, 13] and [5, 6, 7]

Merge [11, 12, 13] and [5, 6, 7]:
- 11 > 5: shift [11,12,13] right, insert 5 → [5, 11, 12, 13, 6, 7]
- 11 > 6: shift [11,12,13] right, insert 6 → [5, 6, 11, 12, 13, 7]
- 11 > 7: shift [11,12,13] right, insert 7 → [5, 6, 7, 11, 12, 13]

WHY INTERVIEWER WILL ACCEPT:
1. Understanding of space-time trade-offs
2. Shows in-place algorithm design
3. Recognizes when optimization is needed
4. Demonstrates insertion technique for merging
"""

# In-Place Merge Sort

def merge(arr, start, mid, end):
    """
    Merge two sorted subarrays in-place without extra space.

    Args:
        arr: Array to merge
        start: Start of first subarray
        mid: End of first subarray
        end: End of second subarray
    """
    start2 = mid + 1  # Start of second subarray

    # Optimization: If already sorted, no merge needed
    # Last element of left half <= first element of right half
    if arr[mid] <= arr[start2]:
        return

    # Merge process using shifting
    while start <= mid and start2 <= end:
        if arr[start] <= arr[start2]:
            # Left element is smaller, move to next
            start += 1
        else:
            # Right element should come before left element
            value = arr[start2]
            index = start2

            # Shift all elements from start to start2-1 one position right
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            # Place the right element at correct position
            arr[start] = value

            # Update pointers
            # All three pointers move forward
            start += 1
            mid += 1
            start2 += 1

def merge_sort(arr, left, right):
    """
    Perform merge sort recursively with in-place merging.

    Args:
        arr: Array to sort
        left: Left boundary
        right: Right boundary
    """
    if left < right:
        mid = (left + right) // 2

        # Sort left half
        merge_sort(arr, left, mid)

        # Sort right half
        merge_sort(arr, mid + 1, right)

        # Merge both halves in-place
        merge(arr, left, mid, right)

# Test
# arr = [12, 11, 13, 5, 6, 7]
# merge_sort(arr, 0, len(arr) - 1)
# print("Sorted array:", arr)