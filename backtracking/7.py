"""
PARTITION EQUAL SUBSET SUM
==========================

Problem Statement:
-----------------
Given an array arr[] of size N, check if it can be partitioned into two subsets
such that the sum of elements in both subsets is equal.

Example:
--------
Input: N = 4, arr[] = {1, 5, 11, 5}
Output: True
Explanation: The array can be partitioned as {1, 5, 5} and {11}

Input: N = 3, arr[] = {1, 3, 5}
Output: False
Explanation: The array cannot be partitioned into equal sum subsets

Input: N = 4, arr[] = {1, 2, 3, 4}
Output: True
Explanation: The array can be partitioned as {1, 4} and {2, 3}

Approach:
---------
1. Calculate total sum of all elements
2. If sum is odd, partition is impossible (return False)
3. If sum is even, problem reduces to: Can we find a subset with sum = total_sum/2?
4. Use Recursion with Memoization (Top-down DP):
   - For each element, we have two choices: include it or exclude it
   - If we can make sum = total_sum/2, then remaining elements also sum to total_sum/2
5. Use DP array to store already computed results to avoid recomputation

Time Complexity: O(N * Sum) - We compute each state (idx, sum) at most once
Space Complexity: O(N * Sum) - DP table + O(N) recursion stack

Flowchart:
----------
```mermaid
graph TD
    A[Start: Calculate total sum] --> B{Is sum odd?}
    B -->|Yes| C[Return False - Cannot partition]
    B -->|No| D[Target = sum/2]
    D --> E[Call solve idx=N-1, target]
    E --> F{idx == -1?}
    F -->|Yes| G{target == 0?}
    G -->|Yes| H[Return True]
    G -->|No| I[Return False]
    F -->|No| J{target == 0?}
    J -->|Yes| H
    J -->|No| K{target < 0?}
    K -->|Yes| I
    K -->|No| L{Result in DP?}
    L -->|Yes| M[Return DP value]
    L -->|No| N[Try including element]
    N --> O[Try excluding element]
    O --> P[Store result in DP]
    P --> Q[Return result]
```
"""


class Solution:
    def equalPartition(self, N, arr):
        """
        Main function to check if array can be partitioned into equal sum subsets

        Args:
            N (int): Size of array
            arr (list): Input array

        Returns:
            bool: True if equal partition possible, False otherwise
        """
        self.arr = arr

        # Calculate total sum of all elements
        s = 0
        for el in arr:
            s += el

        # If sum is odd, we cannot divide the array into two equal subsets
        if s % 2 != 0:
            return False

        # Create DP table to store precomputed results
        # dp[i][j] = Can we make sum 'j' using elements from index 0 to i?
        # Initialize with -1 (uncomputed state)
        self.dp = [[-1 for _ in range(s // 2 + 1)] for _ in range(N)]

        # Check if we can find a subset with sum = s/2
        # If yes, remaining elements also have sum = s/2
        return self.solve(N - 1, s // 2)

    def solve(self, idx, s):
        """
        Recursive function with memoization to check if sum 's' can be achieved

        Args:
            idx (int): Current index in array (processing from right to left)
            s (int): Remaining sum to achieve

        Returns:
            bool: True if sum can be achieved, False otherwise
        """
        # Base Case 1: Traversed all elements
        if idx == -1:
            # If remaining sum is 0, we found a valid subset
            if s == 0:
                return True
            # Otherwise, we couldn't find the sum
            return False

        # Base Case 2: Found the required sum
        if s == 0:
            return True

        # Base Case 3: Sum became negative (overshot the target)
        if s < 0:
            return False

        # If this state is already computed, return cached result
        if self.dp[idx][s] != -1:
            return self.dp[idx][s]

        # Recursive Case: Try two options
        # Option 1: Include current element at idx
        include = self.solve(idx - 1, s - self.arr[idx])

        # Option 2: Exclude current element at idx
        exclude = self.solve(idx - 1, s)

        # Store result in DP table: True if either option works
        self.dp[idx][s] = include or exclude

        return self.dp[idx][s]


# Example Usage and Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Equal partition possible
    print("Test Case 1:")
    arr1 = [1, 5, 11, 5]
    N1 = len(arr1)
    result1 = sol.equalPartition(N1, arr1)
    print(f"Input: arr = {arr1}")
    print(f"Output: {result1}")
    print(f"Explanation: Can partition as {{1, 5, 5}} and {{11}}, both sum to 11")

    # Test Case 2: Equal partition not possible
    print("\nTest Case 2:")
    arr2 = [1, 3, 5]
    N2 = len(arr2)
    result2 = sol.equalPartition(N2, arr2)
    print(f"Input: arr = {arr2}")
    print(f"Output: {result2}")
    print(f"Explanation: Total sum is 9 (odd), cannot partition equally")

    # Test Case 3: Equal partition possible
    print("\nTest Case 3:")
    arr3 = [1, 2, 3, 4]
    N3 = len(arr3)
    result3 = sol.equalPartition(N3, arr3)
    print(f"Input: arr = {arr3}")
    print(f"Output: {result3}")
    print(f"Explanation: Can partition as {{1, 4}} and {{2, 3}}, both sum to 5")

    # Test Case 4: Single element (cannot partition)
    print("\nTest Case 4:")
    arr4 = [5]
    N4 = len(arr4)
    result4 = sol.equalPartition(N4, arr4)
    print(f"Input: arr = {arr4}")
    print(f"Output: {result4}")
    print(f"Explanation: Cannot partition single element into two subsets")

    # Test Case 5: All zeros
    print("\nTest Case 5:")
    arr5 = [0, 0, 0, 0]
    N5 = len(arr5)
    result5 = sol.equalPartition(N5, arr5)
    print(f"Input: arr = {arr5}")
    print(f"Output: {result5}")
    print(f"Explanation: Can partition as {{0, 0}} and {{0, 0}}")
