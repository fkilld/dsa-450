"""
LARGEST NUMBER IN K SWAPS
=========================

Problem Statement:
-----------------
Given a number as a string and an integer K, find the maximum number that can be
formed by performing at most K swaps on the digits of the number.

Example:
--------
Input: s = "1234567", k = 4
Output: 7654321
Explanation: Swap 1 with 7, 2 with 6, 3 with 5, 4 with 4 (4 swaps)

Input: s = "3435335", k = 3
Output: 5543333
Explanation: Swap 3 with 5, 4 with 5, 3 with 4 (3 swaps used)

Input: s = "129814999", k = 4
Output: 999984211
Explanation: After optimal swaps to maximize the number

Approach:
---------
1. Use Backtracking to explore all possible swap combinations
2. For each position from left to right:
   - Find the maximum digit to the right of current position
   - If max digit > current digit, we need to use a swap
   - Try swapping current position with all occurrences of max digit
   - This explores different arrangements when multiple max digits exist
3. After each swap, recursively solve for next position with remaining swaps
4. Backtrack by undoing the swap to try other possibilities
5. Track the maximum number found across all swap combinations

Optimization: Only swap if the maximum digit on right is greater than current digit

Time Complexity: O(N^K) - In worst case, K swaps with N choices each
Space Complexity: O(N) - Recursion depth + string storage

Flowchart:
----------
```mermaid
graph TD
    A[Start: idx=0, k swaps] --> B{k==0 OR idx==n?}
    B -->|Yes| C[Return]
    B -->|No| D[Find max digit on right]
    D --> E{max > current digit?}
    E -->|Yes| F[Decrement k by 1]
    E -->|No| F2[k remains same]
    F --> G[For each occurrence of max]
    F2 --> G
    G --> H[Swap current with max position]
    H --> I[Update global max number]
    I --> J[Recurse: idx+1, remaining k]
    J --> K[Backtrack: Undo swap]
    K --> L{More max occurrences?}
    L -->|Yes| G
    L -->|No| C
```
"""


class Solution:

    def solve(self, idx, k, s):
        """
        Recursive backtracking function to find maximum number

        Args:
            idx (int): Current position in string
            k (int): Remaining swaps allowed
            s (list): List of digits (mutable for swapping)
        """
        # Base Case: No swaps left or reached end of string
        if k == 0 or idx == self.n:
            return

        # Find the maximum digit to the right of current position (including current)
        max_el = s[idx]
        for i in range(idx + 1, self.n):
            max_el = max(max_el, s[i])

        # Optimization: Only use a swap if max digit is greater than current
        # If current digit is already the max, no swap needed
        if max_el != s[idx]:
            k -= 1

        # Try swapping with all occurrences of max_el on the right
        # We iterate from right to left to explore all possibilities
        for i in range(self.n - 1, idx - 1, -1):
            # If this position has the max digit
            if s[i] == max_el:
                # Perform the swap
                s[i], s[idx] = s[idx], s[i]

                # Update the global maximum if current number is larger
                current_num = int("".join(s))
                self.max = max(self.max, current_num)

                # Recursively solve for next position with remaining swaps
                self.solve(idx + 1, k, s)

                # Backtracking: Undo the swap to try other possibilities
                s[i], s[idx] = s[idx], s[i]

    def findMaximumNum(self, s, k):
        """
        Main function to find maximum number possible with k swaps

        Args:
            s (str): Input number as string
            k (int): Maximum number of swaps allowed

        Returns:
            int: Maximum number that can be formed
        """
        self.n = len(s)  # Length of number string

        # Initialize max to negative infinity
        self.max = float('-inf')

        # Convert string to list for easier swapping
        num = list(s)

        # Start backtracking from position 0 with k swaps
        self.solve(0, k, num)

        return self.max


# Example Usage and Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Multiple swaps needed
    print("Test Case 1:")
    s1 = "1234567"
    k1 = 4
    result1 = sol.findMaximumNum(s1, k1)
    print(f"Input: s = '{s1}', k = {k1}")
    print(f"Output: {result1}")
    print(f"Explanation: Swap to get largest digits at front")

    # Test Case 2: Some swaps needed
    print("\n\nTest Case 2:")
    s2 = "3435335"
    k2 = 3
    result2 = sol.findMaximumNum(s2, k2)
    print(f"Input: s = '{s2}', k = {k2}")
    print(f"Output: {result2}")

    # Test Case 3: Many swaps with repeated digits
    print("\n\nTest Case 3:")
    s3 = "129814999"
    k3 = 4
    result3 = sol.findMaximumNum(s3, k3)
    print(f"Input: s = '{s3}', k = {k3}")
    print(f"Output: {result3}")

    # Test Case 4: Already maximum (no swaps needed)
    print("\n\nTest Case 4:")
    s4 = "9876543210"
    k4 = 3
    result4 = sol.findMaximumNum(s4, k4)
    print(f"Input: s = '{s4}', k = {k4}")
    print(f"Output: {result4}")
    print("Explanation: Already in descending order, no swaps improve it")

    # Test Case 5: Limited swaps
    print("\n\nTest Case 5:")
    s5 = "12345"
    k5 = 1
    result5 = sol.findMaximumNum(s5, k5)
    print(f"Input: s = '{s5}', k = {k5}")
    print(f"Output: {result5}")
    print("Explanation: With 1 swap, swap 1 with 5")

    # Test Case 6: Zero swaps
    print("\n\nTest Case 6:")
    s6 = "54321"
    k6 = 0
    result6 = sol.findMaximumNum(s6, k6)
    print(f"Input: s = '{s6}', k = {k6}")
    print(f"Output: {result6}")
    print("Explanation: No swaps allowed, return original number")
