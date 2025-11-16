"""
PROBLEM: Reverse the Array
=============================
Given an array, reverse it in-place.

Example:
    Input:  [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]

APPROACH: Two Pointer Technique
================================
WHY THIS APPROACH?
- We need to reverse the array in-place (without using extra space)
- Two pointer technique is the most efficient way: O(n) time, O(1) space
- We swap elements from both ends moving towards the center

HOW IT WORKS:
- Initialize two pointers: start (s) at beginning, end (e) at last index
- Swap elements at these positions
- Move start forward and end backward
- Continue until pointers meet in the middle

FLOW EXAMPLE:
=============
Array: [1, 2, 3, 4, 5]

Step 1: s=0, e=4
    Swap arr[0] and arr[4]: [5, 2, 3, 4, 1]

Step 2: s=1, e=3
    Swap arr[1] and arr[3]: [5, 4, 3, 2, 1]

Step 3: s=2, e=2
    Pointers meet at middle, stop

Final: [5, 4, 3, 2, 1]

TIME COMPLEXITY:  O(n) - We traverse half the array
SPACE COMPLEXITY: O(1) - No extra space used, in-place reversal
"""

# Test array
# arr = [int(x) for x in input("Enter the array : ").split()]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def arr_rev(arr):
    """
    Reverse an array in-place using two pointer technique.

    Args:
        arr: List of elements to reverse

    Returns:
        The reversed array (modified in-place)
    """
    # Initialize start pointer at the beginning
    s = 0

    # Initialize end pointer at the last index
    e = len(arr) - 1

    # Continue swapping until pointers meet in the middle
    while s <= e:
        # Swap elements at start and end positions
        arr[s], arr[e] = arr[e], arr[s]

        # Move start pointer forward (towards right)
        s += 1

        # Move end pointer backward (towards left)
        e -= 1

    return arr

# Test the function
# Expected output: [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(arr_rev(arr))