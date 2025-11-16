"""
PROBLEM: Move Negative Numbers to Beginning and Positive to End
=================================================================
Rearrange an array so that all negative numbers appear before positive numbers.
The relative order of elements doesn't need to be maintained.

Example:
    Input:  [1, -2, 3, -4, 5, -6, 7, -8, 9]
    Output: [-2, -4, -6, -8, 1, 3, 5, 7, 9] (one possible output)

Note: Order within negative or positive elements doesn't matter.

APPROACH: Two Pointer Technique (Partition Method)
===================================================
WHY THIS APPROACH?
- Uses constant extra space O(1)
- Single pass through array O(n)
- Similar to partition step in QuickSort
- Two pointers converge from both ends

HOW IT WORKS:
1. Use two pointers: left at start, right at end
2. Move left pointer forward if element is negative (already in correct position)
3. Move right pointer backward if element is positive (already in correct position)
4. If left is positive and right is negative, swap them
5. Continue until pointers meet

FLOW EXAMPLE:
=============
Array: [1, -2, 3, -4, 5]
Goal: Move negatives to left, positives to right

Initial: left=0, right=4
    [1, -2, 3, -4, 5]
     L           R

Step 1: arr[0]=1 is positive, arr[4]=5 is positive
    arr[right] >= 0, so move right pointer left
    left=0, right=3
    [1, -2, 3, -4, 5]
     L        R

Step 2: arr[0]=1 is positive, arr[3]=-4 is negative
    left is positive, right is negative → SWAP
    [−4, -2, 3, 1, 5]
        L     R
    left=1, right=2

Step 3: arr[1]=-2 is negative
    arr[left] < 0, so move left pointer right
    left=2, right=2
    [−4, -2, 3, 1, 5]
           LR

Step 4: arr[2]=3 is positive
    arr[right] >= 0, so move right pointer left
    left=2, right=1
    left > right, STOP

Final: [-4, -2, 3, 1, 5]
    All negatives [-4, -2] are before positives [3, 1, 5]

TIME COMPLEXITY:  O(n) - Single pass through array
SPACE COMPLEXITY: O(1) - No extra space, in-place swapping
"""

# Test array
# arr = [int(x) for x in input("Enter the array : ").split()]
arr = [1, -2, 3, -4, 5, -6, 7, -8, 9]

def move(arr):
    """
    Move all negative numbers to the beginning and positive to the end.

    Args:
        arr: Array of integers (positive and negative)

    Returns:
        Rearranged array with negatives first, then positives
    """
    n = len(arr)

    # Initialize two pointers
    left = 0        # Points to leftmost element
    right = n - 1   # Points to rightmost element

    # Continue until pointers meet
    while left <= right:
        # If left element is negative, it's already in correct position
        # Move left pointer forward
        if arr[left] < 0:
            left += 1

        # If right element is positive or zero, it's already in correct position
        # Move right pointer backward
        elif arr[right] >= 0:
            right -= 1

        # If left is positive and right is negative, they're in wrong positions
        # Swap them and move both pointers
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

# Test the function
# Expected output: All negatives first, then all positives (order within may vary)
# Example: [-2, -4, -6, -8, 9, 7, 5, 3, 1] or [-8, -6, -4, -2, 1, 3, 5, 7, 9]
print(move(arr))