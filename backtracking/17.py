"""
PARTITION ARRAY TO K SUBSETS
=============================

Problem Statement:
-----------------
Given an array of integers nums and a positive integer k, check whether it is
possible to divide this array into k non-empty subsets whose sums are all equal.

Example:
--------
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide into 4 subsets (5), (1, 4), (2, 3), (2, 3)
with equal sum = 5

Input: nums = [1, 2, 3, 4], k = 3
Output: False
Explanation: Cannot partition into 3 equal sum subsets

Approach:
---------
1. Calculate total sum of all elements
2. If sum is not divisible by k, return False
3. Target sum for each subset = total_sum / k
4. Use Backtracking to try forming k subsets:
   - Start with first element in first subset
   - For each element, try adding it to current subset
   - If current subset sum equals target, move to next subset
   - If we form k-1 subsets successfully, the last one is automatically valid
5. Use visited array to track which elements are used
6. Backtrack if current assignment doesn't lead to solution

Key Optimization: If we successfully form k-1 equal subsets, the remaining
elements must also form an equal subset (no need to check k-th subset)

Time Complexity: O(k * 2^N) - For each of k subsets, try all element combinations
Space Complexity: O(N) - Visited array + recursion stack

Flowchart:
----------
```mermaid
graph TD
    A[Start: Calculate sum] --> B{sum % k != 0?}
    B -->|Yes| C[Return False]
    B -->|No| D[target = sum/k]
    D --> E[solve s_idx=0]
    E --> F{subSet[s_idx] == target?}
    F -->|Yes| G{s_idx == k-2?}
    G -->|Yes| H[Return True - Found k-1 subsets]
    G -->|No| I[Move to next subset: s_idx+1]
    I --> E
    F -->|No| J[Try adding each unvisited element]
    J --> K{subSet + arr[i] <= target?}
    K -->|Yes| L[Mark visited, add to subset]
    L --> M[Recurse]
    M --> N{Solution found?}
    N -->|Yes| H
    N -->|No| O[Backtrack: Unmark, remove]
    O --> P{More elements?}
    K -->|No| P
    P -->|Yes| J
    P -->|No| Q[Return False]
```
"""


class Solution:

    def solve(self, s_idx):
        """
        Recursive backtracking function to partition array into k equal subsets

        Args:
            s_idx (int): Current subset index being filled (0 to k-1)

        Returns:
            bool: True if partitioning possible, False otherwise
        """
        # Base Case: Current subset has reached target sum
        if self.subSet[s_idx] == self.sum:
            # If we successfully formed k-1 subsets
            # The remaining elements automatically form the k-th subset
            # (comparing with k-2 because of 0-based indexing)
            if s_idx == self.k - 2:
                return True

            # Move to filling next subset
            return self.solve(s_idx + 1)

        # Try adding each element to current subset
        for i in range(self.n):
            # If element not yet used
            if not self.vis[i]:
                # Check if adding this element doesn't exceed target sum
                if self.subSet[s_idx] + self.arr[i] <= self.sum:
                    # Mark element as used
                    self.vis[i] = True

                    # Add element to current subset
                    self.subSet[s_idx] += self.arr[i]

                    # Recursively try to complete partition
                    if self.solve(s_idx):
                        return True

                    # Backtracking: Remove element and mark as unused
                    self.vis[i] = False
                    self.subSet[s_idx] -= self.arr[i]

        # No valid partition found with current configuration
        return False

    def isKPartitionPossible(self, a, k):
        """
        Main function to check if array can be partitioned into k equal subsets

        Args:
            a (list): Array of integers
            k (int): Number of subsets required

        Returns:
            bool: True if k equal partitions possible, False otherwise
        """
        # Edge Case 1: If only 1 subset needed, always possible
        if k == 1:
            return True

        self.n = len(a)

        # Edge Case 2: Cannot partition N elements into more than N subsets
        if k > self.n:
            return False

        # Calculate total sum
        s = 0
        for el in a:
            s += el

        # If sum not divisible by k, equal partition impossible
        if s % k != 0:
            return False

        # Target sum for each subset
        self.sum = s // k

        self.arr = a  # Store array
        self.k = k    # Store number of subsets

        # Visited array to track which elements are used
        self.vis = [False] * self.n

        # Array to store current sum of each subset
        self.subSet = [0] * k

        # Optimization: Initialize first subset with first element
        # This reduces redundant computations
        self.vis[0] = True
        self.subSet[0] = self.arr[0]

        # Start backtracking from subset 0
        return self.solve(0)


# Example Usage and Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Possible partition
    print("Test Case 1:")
    arr1 = [4, 3, 2, 3, 5, 2, 1]
    k1 = 4
    result1 = sol.isKPartitionPossible(arr1, k1)
    print(f"Input: arr = {arr1}, k = {k1}")
    print(f"Output: {result1}")
    print(f"Explanation: Can partition into {k1} subsets: (5), (1,4), (2,3), (2,3)")
    print(f"Each subset sum = {sum(arr1)//k1}")

    # Test Case 2: Not possible
    print("\n\nTest Case 2:")
    arr2 = [1, 2, 3, 4]
    k2 = 3
    result2 = sol.isKPartitionPossible(arr2, k2)
    print(f"Input: arr = {arr2}, k = {k2}")
    print(f"Output: {result2}")
    print(f"Explanation: Sum = 10, not divisible by 3")

    # Test Case 3: k = 1 (always possible)
    print("\n\nTest Case 3:")
    arr3 = [1, 2, 3, 4, 5]
    k3 = 1
    result3 = sol.isKPartitionPossible(arr3, k3)
    print(f"Input: arr = {arr3}, k = {k3}")
    print(f"Output: {result3}")
    print("Explanation: k=1 means entire array is one subset")

    # Test Case 4: k = n (each element is a subset)
    print("\n\nTest Case 4:")
    arr4 = [5, 5, 5, 5]
    k4 = 4
    result4 = sol.isKPartitionPossible(arr4, k4)
    print(f"Input: arr = {arr4}, k = {k4}")
    print(f"Output: {result4}")
    print("Explanation: Each element forms a subset of sum 5")

    # Test Case 5: Complex partition
    print("\n\nTest Case 5:")
    arr5 = [2, 2, 2, 2, 3, 4, 5]
    k5 = 4
    result5 = sol.isKPartitionPossible(arr5, k5)
    print(f"Input: arr = {arr5}, k = {k5}")
    print(f"Output: {result5}")
    print(f"Sum = {sum(arr5)}, Target per subset = {sum(arr5)//k5}")

    # Test Case 6: k > n (not possible)
    print("\n\nTest Case 6:")
    arr6 = [1, 2, 3]
    k6 = 5
    result6 = sol.isKPartitionPossible(arr6, k6)
    print(f"Input: arr = {arr6}, k = {k6}")
    print(f"Output: {result6}")
    print("Explanation: Cannot create 5 subsets from 3 elements")

    # Test Case 7: Array with zeros
    print("\n\nTest Case 7:")
    arr7 = [0, 0, 0, 0]
    k7 = 2
    result7 = sol.isKPartitionPossible(arr7, k7)
    print(f"Input: arr = {arr7}, k = {k7}")
    print(f"Output: {result7}")
    print("Explanation: Can partition into (0,0) and (0,0)")
