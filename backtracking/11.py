"""
COMBINATION SUM II
==================

Problem Statement:
-----------------
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used ONCE in the combination.

Note: The solution set must not contain duplicate combinations.

Example:
--------
Input: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

Input: candidates = [2, 5, 2, 1, 2], target = 5
Output: [[1, 2, 2], [5]]

Approach:
---------
1. Sort the array to handle duplicates and enable early termination
2. Use Backtracking to explore all combinations
3. For each element at index i:
   - Skip duplicates: if arr[i] == arr[i-1], skip (already processed)
   - If arr[i] > target, break (no point checking larger elements)
   - Include arr[i] in path and recurse with target - arr[i]
   - Start next recursion from i+1 (not i) to avoid reusing same element
4. When target becomes 0, we found a valid combination
5. Backtrack by removing last element to try other combinations

Key Differences from Combination Sum I:
- Each element can be used only once (not unlimited times)
- Need to handle duplicate elements in input array
- Move to next index (i+1) instead of same index

Time Complexity: O(2^N) - Each element can be included or excluded
Space Complexity: O(N) - Recursion depth + path storage

Flowchart:
----------
```mermaid
graph TD
    A[Start: Sort array] --> B[solve idx=0, target]
    B --> C{target == 0?}
    C -->|Yes| D[Found combination - Add to result]
    D --> E[Return]
    C -->|No| F[For i from idx to n]
    F --> G{i > idx AND arr[i] == arr[i-1]?}
    G -->|Yes| H[Skip duplicate]
    H --> F
    G -->|No| I{arr[i] > target?}
    I -->|Yes| J[Break - remaining too large]
    I -->|No| K[Add arr[i] to path]
    K --> L[Recurse: i+1, target-arr[i]]
    L --> M[Backtrack: Remove arr[i]]
    M --> F
    F -->|All tried| E
    J --> E
```
"""


class Solution:

    def solve(self, idx, path, target):
        """
        Recursive backtracking function to find combinations

        Args:
            idx (int): Current starting index in array
            path (list): Current combination being built
            target (int): Remaining target sum
        """
        # Base Case: Found a valid combination
        if target == 0:
            # Add copy of current path to result
            self.res.append(path[:])
            return

        # Try including elements from idx onwards
        for i in range(idx, self.n):
            # Skip duplicates: If current element same as previous,
            # skip it to avoid duplicate combinations
            # (i > idx ensures we don't skip the first element in this level)
            if i > idx and self.arr[i] == self.arr[i - 1]:
                continue

            # Early termination: If current element exceeds target,
            # all remaining elements (being sorted) will also exceed
            if self.arr[i] > target:
                break  # No need to check further

            # Include current element in path
            path.append(self.arr[i])

            # Recursively find combinations with remaining elements
            # BUG FIX: Use i+1 instead of i to avoid reusing same element
            self.solve(i + 1, path, target - self.arr[i])

            # Backtracking: Remove current element to try other combinations
            path.pop()

    def combinationSum2(self, arr, target):
        """
        Main function to find all unique combinations that sum to target

        Args:
            arr (list): Array of candidate numbers
            target (int): Target sum

        Returns:
            list: List of all unique combinations
        """
        # Sort array to handle duplicates and enable early termination
        arr.sort()

        self.arr = arr
        self.n = len(arr)

        # Initialize result list
        self.res = []

        # Start backtracking from index 0
        self.solve(0, [], target)

        return self.res


# Example Usage and Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Array with duplicates
    print("Test Case 1:")
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    result1 = sol.combinationSum2(candidates1, target1)
    print(f"Input: candidates = {candidates1}, target = {target1}")
    print(f"Output: {result1}")
    print(f"Explanation: Unique combinations that sum to {target1}")

    # Test Case 2: Multiple duplicates
    print("\n\nTest Case 2:")
    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    result2 = sol.combinationSum2(candidates2, target2)
    print(f"Input: candidates = {candidates2}, target = {target2}")
    print(f"Output: {result2}")

    # Test Case 3: No valid combination
    print("\n\nTest Case 3:")
    candidates3 = [2, 3, 5]
    target3 = 1
    result3 = sol.combinationSum2(candidates3, target3)
    print(f"Input: candidates = {candidates3}, target = {target3}")
    print(f"Output: {result3}")
    print("Explanation: No combination can sum to 1")

    # Test Case 4: Single element solution
    print("\n\nTest Case 4:")
    candidates4 = [1, 2, 3, 4, 5]
    target4 = 5
    result4 = sol.combinationSum2(candidates4, target4)
    print(f"Input: candidates = {candidates4}, target = {target4}")
    print(f"Output: {result4}")

    # Test Case 5: All elements needed
    print("\n\nTest Case 5:")
    candidates5 = [1, 1, 1, 1]
    target5 = 4
    result5 = sol.combinationSum2(candidates5, target5)
    print(f"Input: candidates = {candidates5}, target = {target5}")
    print(f"Output: {result5}")
    print("Explanation: Only one way - use all four 1's")
