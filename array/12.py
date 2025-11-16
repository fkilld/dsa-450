"""
PROBLEM: Maximum Subarray Sum (Kadane's Algorithm)
====================================================
Find the contiguous subarray (containing at least one number) which has the largest sum.

Example:
    Input:  arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6
    Explanation: Subarray [4, -1, 2, 1] has the largest sum = 6

    Input:  arr = [1, 2, 3, -2, 5]
    Output: 9
    Explanation: Subarray [1, 2, 3, -2, 5] (entire array) has sum = 9

APPROACH: Kadane's Algorithm (Dynamic Programming)
===================================================
WHY THIS APPROACH?
- Brute force would check all subarrays: O(n²) or O(n³)
- Kadane's algorithm solves it in O(n) time with O(1) space
- Key insight: At each position, decide whether to extend current subarray or start new one
- If current sum becomes negative, it's better to start fresh from next element

CORE IDEA:
- max_till_here: Maximum sum of subarray ending at current position
- max_int: Overall maximum sum found so far
- At each element: max_till_here = max(arr[i], max_till_here + arr[i])
- If max_till_here < 0, reset to 0 (start fresh)

HOW IT WORKS:
1. Initialize max_int = -infinity (to handle all negative arrays)
2. Initialize max_till_here = 0
3. For each element:
   a. Add element to max_till_here
   b. Update max_int if max_till_here is greater
   c. If max_till_here becomes negative, reset to 0 (start new subarray)

FLOW EXAMPLE:
=============
Array: [-2, 1, -3, 4, -1, 2, 1, -5, 4]

i=0: arr[0]=-2
    max_till_here = 0 + (-2) = -2
    max_int = max(-inf, -2) = -2
    max_till_here < 0, reset to 0

i=1: arr[1]=1
    max_till_here = 0 + 1 = 1
    max_int = max(-2, 1) = 1

i=2: arr[2]=-3
    max_till_here = 1 + (-3) = -2
    max_int = max(1, -2) = 1
    max_till_here < 0, reset to 0

i=3: arr[3]=4
    max_till_here = 0 + 4 = 4
    max_int = max(1, 4) = 4

i=4: arr[4]=-1
    max_till_here = 4 + (-1) = 3
    max_int = max(4, 3) = 4

i=5: arr[5]=2
    max_till_here = 3 + 2 = 5
    max_int = max(4, 5) = 5

i=6: arr[6]=1
    max_till_here = 5 + 1 = 6
    max_int = max(5, 6) = 6

i=7: arr[7]=-5
    max_till_here = 6 + (-5) = 1
    max_int = max(6, 1) = 6

i=8: arr[8]=4
    max_till_here = 1 + 4 = 5
    max_int = max(6, 5) = 6

Final: max_int = 6 (subarray [4, -1, 2, 1])

WHY RESET TO 0?
If sum becomes negative, any future subarray would benefit from NOT including
the negative sum. Better to start fresh from the next element.

TIME COMPLEXITY:  O(n) - Single pass through array
SPACE COMPLEXITY: O(1) - Only using two variables
"""

class Solution:
    def kadanes_algo(self, arr):
        """
        Find maximum sum of contiguous subarray using Kadane's Algorithm.

        Args:
            arr: Array of integers (can contain negative numbers)

        Returns:
            Maximum sum of any contiguous subarray
        """
        # Initialize to negative infinity to handle all-negative arrays
        max_int = float('-inf')

        # Tracks maximum sum of subarray ending at current position
        max_till_here = 0

        # Traverse through the array
        for i in range(len(arr)):
            # Add current element to the running sum
            max_till_here += arr[i]

            # Update global maximum if current sum is larger
            if max_till_here > max_int:
                max_int = max_till_here

            # If sum becomes negative, reset to 0
            # (starting a new subarray from next element would be better)
            if max_till_here < 0:
                max_till_here = 0

        return max_int