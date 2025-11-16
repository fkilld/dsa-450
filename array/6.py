"""
PROBLEM: Cyclically Rotate an Array by One
============================================
Given an array, rotate it by one position in clockwise direction.

Example:
    Input:  [1, 2, 3, 4, 5]
    Output: [5, 1, 2, 3, 4]
    Explanation: Last element moves to front, all others shift right by 1

    Input:  [9, 8, 7, 6, 4, 2]
    Output: [2, 9, 8, 7, 6, 4]

APPROACH: Store Last Element and Shift Right
==============================================
WHY THIS APPROACH?
- Simple and intuitive: Save last element, shift all others right, place last at front
- In-place rotation: O(1) extra space
- Linear time: O(n) - single pass

ALTERNATIVE APPROACHES:
1. Reverse algorithm: Reverse entire array, then reverse first part and second part
2. Store last and shift (current): Simple and direct

HOW IT WORKS:
1. Store the last element in a temporary variable
2. Shift all elements one position to the right (starting from second-last)
3. Place the stored last element at the first position

FLOW EXAMPLE:
=============
Array: [1, 2, 3, 4, 5]
Goal: Rotate clockwise by 1 position

Step 1: Store last element
    last = arr[4] = 5
    [1, 2, 3, 4, 5]

Step 2: Shift elements right (loop from n-2 to 0)
    i=3: arr[4] = arr[3] → [1, 2, 3, 4, 4]
    i=2: arr[3] = arr[2] → [1, 2, 3, 3, 4]
    i=1: arr[2] = arr[1] → [1, 2, 2, 3, 4]
    i=0: arr[1] = arr[0] → [1, 1, 2, 3, 4]

Step 3: Place last element at first position
    arr[0] = last = 5
    [5, 1, 2, 3, 4]

Final: [5, 1, 2, 3, 4]

WHY TRAVERSE IN REVERSE?
If we go forward (left to right), we would overwrite elements before copying them,
losing data. Going reverse ensures we copy each element before it gets overwritten.

Example of WRONG approach (forward):
    i=0: arr[1] = arr[0] → [1, 1, 3, 4, 5]  // Lost 2!
    i=1: arr[2] = arr[1] → [1, 1, 1, 4, 5]  // Lost 3!
    ...all elements become same

TIME COMPLEXITY:  O(n) - Single pass to shift all elements
SPACE COMPLEXITY: O(1) - Only one variable to store last element
"""

def rotate(arr, n):
    """
    Rotate an array by one position in clockwise direction.

    Args:
        arr: Input array to be rotated
        n: Size of the array

    Returns:
        Rotated array (modified in-place)

    Example:
        >>> rotate([1, 2, 3, 4, 5], 5)
        [5, 1, 2, 3, 4]
    """
    # Store the last element of the array
    # This element will be moved to the front
    last = arr[n - 1]

    # Loop from second-last element (n-2) to first element (0) in reverse order
    # We use reverse order to avoid overwriting elements before they're moved
    # range(n-2, -1, -1) means: start at n-2, go to 0 (inclusive), step by -1
    for i in range(n - 2, -1, -1):
        # Move each element one position forward (to the right)
        # arr[i] moves to arr[i+1]
        arr[i + 1] = arr[i]

    # Place the stored last element at the first position (index 0)
    # This completes the cyclic rotation by one position clockwise
    arr[0] = last

    return arr

# Test the function
rotated_array = rotate([1, 2, 3, 4, 5], 5)
# Expected output: [5, 1, 2, 3, 4]
print(rotated_array)