"""
PROBLEM: Maximum Subarray Sum (Kadane's Algorithm)
===================================================
Given an array arr of N integers, find the contiguous subarray (containing at least one number)
which has the maximum sum and return its sum.

Example:
    Input:  arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    Output: 7
    Explanation: The subarray [4, -1, -2, 1, 5] has the maximum sum of 7

    Input:  arr = [1, 2, 3, -2, 5]
    Output: 9
    Explanation: The subarray [1, 2, 3, -2, 5] has the maximum sum of 9

    Input:  arr = [-1, -2, -3, -4]
    Output: -1
    Explanation: The subarray [-1] has the maximum sum of -1

APPROACH: Kadane's Algorithm
==============================
WHY THIS APPROACH?
- Kadane's Algorithm is the most efficient solution for this problem
- Linear Time Complexity: O(n) - Single pass through array
- Constant Space Complexity: O(1) - No extra space needed
- Dynamic Programming approach without extra space
- Handles all negative numbers correctly
- Elegant and simple to implement

ALTERNATIVE APPROACHES:
1. Brute Force: Check all possible subarrays - O(n²) or O(n³) time
2. Divide and Conquer: Split array recursively - O(n log n) time
3. Kadane's Algorithm: Optimal solution - O(n) time

HOW IT WORKS:
The key insight of Kadane's algorithm is:
- At each position, we have two choices:
  1. Extend the current subarray by including current element
  2. Start a new subarray from current element
- We choose the option that gives us maximum sum
- We track the maximum sum seen so far globally

Algorithm Steps:
1. Initialize max_int (global maximum) to -infinity (handles all negative arrays)
2. Initialize max_till_here (current subarray sum) to 0
3. For each element in array:
   a. Add current element to max_till_here (extend current subarray)
   b. If max_till_here > max_int, update max_int (found better sum)
   c. If max_till_here < 0, reset to 0 (start fresh from next element)
4. Return max_int

WHY RESET TO 0 WHEN SUM BECOMES NEGATIVE?
===========================================
If the current subarray sum becomes negative, it will only decrease
the sum of any future subarray. Therefore, it's better to discard
the current subarray and start fresh from the next element.

Example: arr = [5, -10, 6]
- After processing 5: max_till_here = 5
- After adding -10: max_till_here = -5
- Reset to 0 (discard [5, -10])
- Start fresh with 6: max_till_here = 6
- Result: 6 (better than 5 + (-10) + 6 = 1)

FLOW EXAMPLE:
=============
Array: [-2, -3, 4, -1, -2, 1, 5, -3]
Goal: Find maximum sum of contiguous subarray

Initial State:
    max_int = -∞ (negative infinity)
    max_till_here = 0

Step 1: Process arr[0] = -2
    max_till_here = 0 + (-2) = -2
    max_int = max(-∞, -2) = -2
    max_till_here < 0, reset to 0
    Current state: max_int = -2, max_till_here = 0

Step 2: Process arr[1] = -3
    max_till_here = 0 + (-3) = -3
    max_int = max(-2, -3) = -2
    max_till_here < 0, reset to 0
    Current state: max_int = -2, max_till_here = 0

Step 3: Process arr[2] = 4
    max_till_here = 0 + 4 = 4
    max_int = max(-2, 4) = 4
    max_till_here >= 0, keep it
    Current state: max_int = 4, max_till_here = 4
    [Subarray starts here: [4]]

Step 4: Process arr[3] = -1
    max_till_here = 4 + (-1) = 3
    max_int = max(4, 3) = 4
    max_till_here >= 0, keep it
    Current state: max_int = 4, max_till_here = 3
    [Current subarray: [4, -1]]

Step 5: Process arr[4] = -2
    max_till_here = 3 + (-2) = 1
    max_int = max(4, 1) = 4
    max_till_here >= 0, keep it
    Current state: max_int = 4, max_till_here = 1
    [Current subarray: [4, -1, -2]]

Step 6: Process arr[5] = 1
    max_till_here = 1 + 1 = 2
    max_int = max(4, 2) = 4
    max_till_here >= 0, keep it
    Current state: max_int = 4, max_till_here = 2
    [Current subarray: [4, -1, -2, 1]]

Step 7: Process arr[6] = 5
    max_till_here = 2 + 5 = 7
    max_int = max(4, 7) = 7
    max_till_here >= 0, keep it
    Current state: max_int = 7, max_till_here = 7
    [Current subarray: [4, -1, -2, 1, 5]]

Step 8: Process arr[7] = -3
    max_till_here = 7 + (-3) = 4
    max_int = max(7, 4) = 7
    max_till_here >= 0, keep it
    Current state: max_int = 7, max_till_here = 4
    [Current subarray: [4, -1, -2, 1, 5, -3]]

Final Result: max_int = 7
Maximum sum subarray: [4, -1, -2, 1, 5]

FLOWCHART:
==========
    ┌──────────────────────────────────┐
    │ Start: max_subarray_sum(arr)     │
    └────────────┬─────────────────────┘
                 │
                 ▼
    ┌──────────────────────────────────┐
    │ Initialize:                      │
    │ max_int = -∞                     │
    │ max_till_here = 0                │
    └────────────┬─────────────────────┘
                 │
                 ▼
    ┌──────────────────────────────────┐
    │ For i = 0 to len(arr) - 1        │
    └────────────┬─────────────────────┘
                 │
                 ▼
    ┌──────────────────────────────────┐
    │ max_till_here += arr[i]          │
    │ (extend current subarray)        │
    └────────────┬─────────────────────┘
                 │
                 ▼
    ┌──────────────────────────────────┐
    │ Is max_till_here > max_int?      │
    └────┬───────────────────────┬─────┘
         │ Yes                   │ No
         │                       │
         ▼                       │
    ┌────────────────┐           │
    │ max_int =      │           │
    │ max_till_here  │           │
    │ (new best sum) │           │
    └────┬───────────┘           │
         │                       │
         └───────────┬───────────┘
                     │
                     ▼
    ┌──────────────────────────────────┐
    │ Is max_till_here < 0?            │
    └────┬───────────────────────┬─────┘
         │ Yes                   │ No
         │                       │
         ▼                       │
    ┌────────────────┐           │
    │ max_till_here  │           │
    │ = 0            │           │
    │ (reset/start   │           │
    │  fresh)        │           │
    └────┬───────────┘           │
         │                       │
         └───────────┬───────────┘
                     │
                     ▼
    ┌──────────────────────────────────┐
    │ More elements in array?          │
    └────┬────────────────────────┬────┘
         │ Yes                    │ No
         │                        │
         │ (loop back)            ▼
         │              ┌──────────────────┐
         └─────────────►│ Return max_int   │
                        └──────────────────┘

SPECIAL CASE: All Negative Numbers
====================================
Why we initialize max_int to -∞ instead of 0:

If array has all negative numbers (e.g., [-5, -2, -8, -1]):
- We must pick at least one element
- The best choice is the least negative number (-1)
- If we initialized max_int to 0, we'd incorrectly return 0

With max_int = -∞:
- First element: max_int = -5
- Second element: max_int = -2
- Third element: max_int = -2 (no change)
- Fourth element: max_int = -1
- Result: -1 (correct!)

TIME COMPLEXITY:  O(n) - Single pass through array
SPACE COMPLEXITY: O(1) - Only two variables used regardless of input size
"""


class Solution:
    """
    Solution class for finding maximum sum of a contiguous subarray.

    This class implements Kadane's Algorithm, which is an efficient dynamic
    programming approach to solve the maximum subarray sum problem in linear time.

    The algorithm maintains two values:
    1. max_int: The maximum sum found so far (global maximum)
    2. max_till_here: The maximum sum ending at current position (local maximum)
    """

    def max_subarray_sum(self, arr):
        """
        Find the maximum sum of any contiguous subarray using Kadane's Algorithm.

        This method efficiently finds the maximum sum by maintaining a running sum
        and resetting when the running sum becomes negative.

        Args:
            arr (list): List of integers (can contain positive, negative, or both)

        Returns:
            int: Maximum sum of contiguous subarray

        Time Complexity: O(n) - Single pass through the array
        Space Complexity: O(1) - Constant extra space

        Example:
            >>> solution = Solution()
            >>> solution.max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3])
            7
        """
        # Initialize max_int to negative infinity to handle arrays with all negative numbers
        # This ensures we pick at least one element even if all are negative
        max_int = float('-inf')

        # Initialize max_till_here to track the maximum sum ending at current position
        # Start with 0 as we haven't processed any elements yet
        max_till_here = 0

        # Iterate through each element in the array
        for i in range(len(arr)):
            # Add current element to running sum (extend current subarray)
            # This represents the choice: "include current element in existing subarray"
            max_till_here += arr[i]

            # Update global maximum if current sum is better
            # This keeps track of the best subarray sum we've seen so far
            if max_till_here > max_int:
                max_int = max_till_here

            # Key insight of Kadane's algorithm:
            # If running sum becomes negative, it will only hurt future subarrays
            # Better to discard current subarray and start fresh from next element
            if max_till_here < 0:
                max_till_here = 0  # Reset to start new subarray from next element

        # Return the maximum subarray sum found
        return max_int


# Test cases
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Test 1: Mixed positive and negative numbers (classic example)
    arr1 = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(f"Array: {arr1}")
    print(f"Maximum subarray sum: {solution.max_subarray_sum(arr1)}")  # Expected: 7
    print("Explanation: Subarray [4, -1, -2, 1, 5] has sum = 7\n")

    # Test 2: All positive numbers
    arr2 = [1, 2, 3, -2, 5]
    print(f"Array: {arr2}")
    print(f"Maximum subarray sum: {solution.max_subarray_sum(arr2)}")  # Expected: 9
    print("Explanation: Entire array [1, 2, 3, -2, 5] has sum = 9\n")

    # Test 3: All negative numbers
    arr3 = [-1, -2, -3, -4]
    print(f"Array: {arr3}")
    print(f"Maximum subarray sum: {solution.max_subarray_sum(arr3)}")  # Expected: -1
    print("Explanation: Best single element subarray [-1] has sum = -1\n")

    # Test 4: Single element
    arr4 = [5]
    print(f"Array: {arr4}")
    print(f"Maximum subarray sum: {solution.max_subarray_sum(arr4)}")  # Expected: 5
    print("Explanation: Single element [5] has sum = 5\n")

    # Test 5: Large negative followed by large positive
    arr5 = [-10, 20, -5, 10]
    print(f"Array: {arr5}")
    print(f"Maximum subarray sum: {solution.max_subarray_sum(arr5)}")  # Expected: 25
    print("Explanation: Subarray [20, -5, 10] has sum = 25\n")
