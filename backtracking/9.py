"""
TUG OF WAR
==========

Problem Statement:
-----------------
Given a set of N integers, divide the set into two subsets of N/2 elements each
(or as close as possible if N is odd) such that the absolute difference of their
sums is minimized.

This is called the "Tug of War" problem because we want to form two teams that
are as balanced as possible.

Example:
--------
Input: arr[] = {23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4}
Output:
Set 1: 45 -34 12 98 -1
Set 2: 23 0 -99 4 189 4
Explanation: Sum of set 1 = 120, Sum of set 2 = 121, Difference = 1

Input: arr[] = {1, 2, 3, 4, 5, 6}
Output:
Set 1: 1 2 6
Set 2: 3 4 5
Explanation: Sum of set 1 = 9, Sum of set 2 = 12, Difference = 3

Approach:
---------
1. Use Backtracking to explore all possible ways to partition the array
2. Divide array into two sets such that:
   - Each set has approximately N/2 elements (differs by at most 1 if N is odd)
   - The absolute difference between sums is minimized
3. For each element, try adding it to set1 or set2
4. Only add to a set if it doesn't exceed the size constraint (N+1)//2
5. Track the minimum difference found and corresponding partition
6. Backtrack by removing elements to try other partitions

Time Complexity: O(2^N) - Each element can go to either set
Space Complexity: O(N) - Recursion depth + set storage

Flowchart:
----------
```mermaid
graph TD
    A[Start: idx=0, both sets empty] --> B{idx == N?}
    B -->|Yes| C{Is |s1-s2| < min?}
    C -->|Yes| D[Update min and best partition]
    D --> E[Return]
    C -->|No| E
    B -->|No| F{Can add to set1?}
    F -->|Yes| G[Add element to set1]
    G --> H[Recurse: idx+1]
    H --> I[Backtrack: Remove from set1]
    I --> J{Can add to set2?}
    F -->|No| J
    J -->|Yes| K[Add element to set2]
    K --> L[Recurse: idx+1]
    L --> M[Backtrack: Remove from set2]
    M --> E
    J -->|No| E
```
"""


class Solution:

    def solve(self, idx, s1, s2, set1, set2, arr):
        """
        Recursive backtracking function to find optimal partition

        Args:
            idx (int): Current index in array
            s1 (int): Sum of elements in set1
            s2 (int): Sum of elements in set2
            set1 (list): Current elements in set1
            set2 (list): Current elements in set2
            arr (list): Input array
        """
        # Base Case: Processed all elements
        if idx == self.n:
            # Check if current partition has smaller difference
            if self.min > abs(s1 - s2):
                self.min = abs(s1 - s2)
                # Store the best partition found so far
                self.set1 = set1[:]  # Deep copy
                self.set2 = set2[:]  # Deep copy
            return

        # Try adding current element to set1
        # Constraint: set1 size should not exceed (N+1)//2
        if len(set1) < (self.n + 1) // 2:
            # Include current element in set1
            set1.append(arr[idx])

            # Recursively partition remaining elements
            self.solve(idx + 1, s1 + arr[idx], s2, set1, set2, arr)

            # Backtracking: Remove element from set1
            set1.pop()

        # Try adding current element to set2
        # Constraint: set2 size should not exceed (N+1)//2
        if len(set2) < (self.n + 1) // 2:
            # Include current element in set2
            set2.append(arr[idx])

            # Recursively partition remaining elements
            self.solve(idx + 1, s1, s2 + arr[idx], set1, set2, arr)

            # Backtracking: Remove element from set2
            set2.pop()

    def tugOfWar(self, arr, n):
        """
        Main function to solve Tug of War problem

        Args:
            arr (list): Input array of integers
            n (int): Size of array
        """
        self.n = n

        # Initialize minimum difference to infinity
        self.min = float('inf')

        # Initialize the two sets
        self.set1 = []
        self.set2 = []

        # Start backtracking from index 0
        # Parameters: idx, sum_of_set1, sum_of_set2, set1, set2, arr
        self.solve(0, 0, 0, [], [], arr)

        # Print the results
        print("Set 1:", *self.set1)
        print("Set 2:", *self.set2)
        print(f"Sum of Set 1: {sum(self.set1)}")
        print(f"Sum of Set 2: {sum(self.set2)}")
        print(f"Minimum Difference: {self.min}")


# Example Usage and Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Array with mix of positive and negative numbers
    print("Test Case 1:")
    arr1 = [23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]
    n1 = len(arr1)
    sol.tugOfWar(arr1, n1)

    # Test Case 2: Simple array
    print("\n\nTest Case 2:")
    arr2 = [1, 2, 3, 4, 5, 6]
    n2 = len(arr2)
    sol.tugOfWar(arr2, n2)

    # Test Case 3: Array with all positive numbers
    print("\n\nTest Case 3:")
    arr3 = [3, 4, 5, -3, 100, 1, 89, 54, 23, 20]
    n3 = len(arr3)
    sol.tugOfWar(arr3, n3)

    # Test Case 4: Small array
    print("\n\nTest Case 4:")
    arr4 = [10, 20, 30, 40]
    n4 = len(arr4)
    sol.tugOfWar(arr4, n4)

    # Test Case 5: Odd number of elements
    print("\n\nTest Case 5:")
    arr5 = [5, 10, 15, 20, 25]
    n5 = len(arr5)
    sol.tugOfWar(arr5, n5)
