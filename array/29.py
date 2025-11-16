"""
PROBLEM: Chocolate Distribution Problem - Minimize Unfairness
==============================================================
Given an array of N integers where each value represents the number of chocolates
in a packet. There are M students. Distribute exactly one packet to each student
such that the difference between the maximum and minimum chocolates given is minimized.

Goal: Minimize (max_chocolates - min_chocolates) among distributed packets

Example 1:
    Input:  arr = [7, 3, 2, 4, 9, 12, 56], M = 3 students
    Output: 2
    Explanation: If we distribute packets with [3, 2, 4] chocolates,
                 difference = 4 - 2 = 2 (minimum possible)

Example 2:
    Input:  arr = [3, 4, 1, 9, 56, 7, 9, 12], M = 5 students
    Output: 6
    Explanation: If we distribute [3, 4, 7, 9, 9],
                 difference = 9 - 3 = 6 (minimum possible)

Example 3:
    Input:  arr = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50], M = 7
    Output: 10
    Explanation: Distribute [25, 28, 30, 30, 40, 41, 42] (after sorting)
                 difference = 42 - 25 = 17 (Wait, let me recalculate...)
                 Or [40, 41, 42, 43, 44, 48, 50]?
                 difference = 50 - 40 = 10

APPROACH: Sort and Sliding Window
===================================
WHY THIS APPROACH?
- We want to minimize the difference between max and min
- After sorting, consecutive M elements will have the smallest difference
- Any M elements form a window, and we slide this window to find minimum difference
- Sorting brings similar values together, making it easier to find the optimal distribution

KEY INSIGHT:
After sorting, the minimum difference will always be achieved by selecting
M consecutive elements from the sorted array. Why?
- If we skip elements in between, the difference only increases or stays same
- Consecutive elements in sorted array have smallest possible range

ALTERNATIVE APPROACHES:
1. Brute Force: Try all combinations of M packets - O(nCm * M) - too slow
2. Sort + Sliding Window (current): O(n log n) - optimal

HOW IT WORKS:
1. Sort the array
2. Consider every consecutive M elements as a window
3. Calculate difference (max - min) for each window
   - In a window of M elements: max = arr[i+M-1], min = arr[i]
4. Track and return the minimum difference

FLOW EXAMPLE:
=============
Array: arr = [7, 3, 2, 4, 9, 12, 56], M = 3 students

Step 1: Sort the array
    arr = [2, 3, 4, 7, 9, 12, 56]
    N = 7, M = 3

Step 2: Try all windows of size M=3
    min_diff = infinity

Window 1: [2, 3, 4] (i=0 to i+M-1=2)
    difference = arr[2] - arr[0] = 4 - 2 = 2
    min_diff = min(inf, 2) = 2

    [2, 3, 4], 7, 9, 12, 56
     ^     ^
     i   i+M-1

Window 2: [3, 4, 7] (i=1 to i+M-1=3)
    difference = arr[3] - arr[1] = 7 - 3 = 4
    min_diff = min(2, 4) = 2

    2, [3, 4, 7], 9, 12, 56
        ^     ^
        i   i+M-1

Window 3: [4, 7, 9] (i=2 to i+M-1=4)
    difference = arr[4] - arr[2] = 9 - 4 = 5
    min_diff = min(2, 5) = 2

    2, 3, [4, 7, 9], 12, 56
           ^     ^
           i   i+M-1

Window 4: [7, 9, 12] (i=3 to i+M-1=5)
    difference = arr[5] - arr[3] = 12 - 7 = 5
    min_diff = min(2, 5) = 2

    2, 3, 4, [7, 9, 12], 56
              ^      ^
              i    i+M-1

Window 5: [9, 12, 56] (i=4 to i+M-1=6)
    difference = arr[6] - arr[4] = 56 - 9 = 47
    min_diff = min(2, 47) = 2

    2, 3, 4, 7, [9, 12, 56]
                 ^       ^
                 i     i+M-1

Step 3: Return minimum difference
    min_diff = 2

Best distribution: [2, 3, 4] with difference 2

NUMBER OF WINDOWS:
==================
Total windows = N - M + 1

Why? If N=7 and M=3:
- Window starting at i=0 ends at i=2 ✓
- Window starting at i=1 ends at i=3 ✓
- Window starting at i=2 ends at i=4 ✓
- Window starting at i=3 ends at i=5 ✓
- Window starting at i=4 ends at i=6 ✓
- Window starting at i=5 ends at i=7 ✗ (out of bounds)

So we can start from i=0 to i=N-M (inclusive)
Total windows = (N-M) - 0 + 1 = N - M + 1

EDGE CASES:
===========
1. M = 0 or N = 0: No students or no packets → return 0
2. M > N: More students than packets → impossible → return -1
3. M = 1: Only 1 student → difference is 0 (only one packet distributed)
4. M = N: Distribute all packets → difference = max(arr) - min(arr)

TIME COMPLEXITY:  O(n log n) - Dominated by sorting, sliding window is O(n)
SPACE COMPLEXITY: O(1) - Only using variables, in-place sorting (or O(n) for sort space)
"""

def findMinDiff(self, arr, N, M):
    """
    Find minimum difference between max and min chocolates distributed.

    Args:
        arr: Array where arr[i] represents chocolates in packet i
        N: Total number of chocolate packets
        M: Number of students

    Returns:
        Minimum possible difference between max and min chocolates
        Returns -1 if distribution is impossible (M > N)
        Returns 0 if no students or no packets

    Example:
        >>> findMinDiff([7, 3, 2, 4, 9, 12, 56], 7, 3)
        2
        >>> findMinDiff([3, 4, 1, 9, 56, 7, 9, 12], 8, 5)
        6
    """
    # EDGE CASE 1: No students or no packets
    # If there are no students, no distribution needed
    # If there are no packets, no chocolates to distribute
    # In both cases, difference is 0
    if M == 0 or N == 0:
        return 0

    # STEP 1: Sort the array
    # Sorting is crucial because it brings similar values together
    # After sorting, consecutive M elements will have smallest difference
    # Example: [7, 3, 2, 4, 9] becomes [2, 3, 4, 7, 9]
    # Now [2, 3, 4] has smaller diff than [2, 4, 9]
    arr.sort()

    # EDGE CASE 2: More students than packets
    # If we have more students than packets, we cannot distribute
    # one packet to each student (impossible scenario)
    if N < M:
        return -1

    # STEP 2: Initialize minimum difference to infinity
    # We'll update this as we find better distributions
    # Using infinity ensures any actual difference will be smaller
    min_diff = float('inf')

    # STEP 3: Try all possible consecutive windows of size M
    # A window [i, i+M-1] represents selecting M consecutive packets
    # We need to check N-M+1 windows total
    # Example: N=7, M=3 → check windows at i=0,1,2,3,4 (5 windows)
    for i in range(N - M + 1):
        # For current window starting at i:
        # - Minimum chocolates: arr[i] (first element in window)
        # - Maximum chocolates: arr[i+M-1] (last element in window)
        #
        # Example window [2, 3, 4]:
        # - arr[i] = 2 (minimum)
        # - arr[i+M-1] = arr[i+2] = 4 (maximum)
        # - difference = 4 - 2 = 2
        current_diff = arr[i + M - 1] - arr[i]

        # STEP 4: Update minimum difference if current is better
        # Keep track of the smallest difference found so far
        min_diff = min(min_diff, current_diff)

    # STEP 5: Return the minimum difference found
    return min_diff


# Example test cases
if __name__ == "__main__":
    class Solution:
        def findMinDiff(self, arr, N, M):
            """Wrapper for testing"""
            if M == 0 or N == 0:
                return 0
            arr.sort()
            if N < M:
                return -1
            min_diff = float('inf')
            for i in range(N - M + 1):
                current_diff = arr[i + M - 1] - arr[i]
                min_diff = min(min_diff, current_diff)
            return min_diff

    sol = Solution()

    # Test case 1
    arr1 = [7, 3, 2, 4, 9, 12, 56]
    print(sol.findMinDiff(arr1, len(arr1), 3))  # Expected: 2

    # Test case 2
    arr2 = [3, 4, 1, 9, 56, 7, 9, 12]
    print(sol.findMinDiff(arr2, len(arr2), 5))  # Expected: 6

    # Test case 3: Edge case - more students than packets
    arr3 = [1, 2, 3]
    print(sol.findMinDiff(arr3, len(arr3), 5))  # Expected: -1