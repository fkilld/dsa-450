"""
PERMUTATIONS OF A GIVEN STRING
===============================

Problem Statement:
-----------------
Given a string S, find all permutations of the string. A permutation is a
rearrangement of all the characters of the string.

Example:
--------
Input: S = "ABC"
Output: ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]

Input: S = "AB"
Output: ["AB", "BA"]

Input: S = "AAB"
Output: ["AAB", "ABA", "BAA"]
Note: May contain duplicates if input has duplicate characters

Approach:
---------
1. Use Backtracking with swapping technique
2. Fix each character at current position (idx) one by one
3. For each character from idx to end:
   - Swap current character with character at idx
   - Recursively generate permutations for remaining characters (idx+1)
   - Backtrack by swapping back to restore original state
4. When idx reaches end of string, we have a complete permutation

Key Insight: By swapping each character to the front and recursing,
we explore all possible orderings.

Time Complexity: O(N! * N) - N! permutations, each taking O(N) to create
Space Complexity: O(N) - Recursion depth + string storage

Flowchart:
----------
```mermaid
graph TD
    A[Start: idx=0] --> B{idx == n?}
    B -->|Yes| C[Found permutation - Add to result]
    C --> D[Return]
    B -->|No| E[For i from idx to n-1]
    E --> F[Swap s[idx] with s[i]]
    F --> G[Recurse: solve idx+1]
    G --> H[Backtrack: Swap s[idx] with s[i]]
    H --> I{More positions to try?}
    I -->|Yes| E
    I -->|No| D
```
"""


class Solution:

    def solve(self, idx, s):
        """
        Recursive backtracking function to generate permutations

        Args:
            idx (int): Current position being fixed
            s (list): List of characters (mutable for swapping)
        """
        # Base Case: Reached end of string - found a permutation
        if idx == self.n:
            # Join characters and add to result
            self.res.append("".join(s))
            return

        # Try fixing each character from idx to end at position idx
        for i in range(idx, self.n):
            # Swap character at i with character at idx
            # This fixes s[i] at position idx
            s[idx], s[i] = s[i], s[idx]

            # Recursively generate permutations for remaining positions
            self.solve(idx + 1, s)

            # Backtracking: Restore original order
            # Swap back to try other characters at this position
            s[idx], s[i] = s[idx], s[i]

    def find_permutations(self, S):
        """
        Main function to find all permutations of string

        Args:
            S (str): Input string

        Returns:
            list: List of all permutations
        """
        # Convert string to list for easier swapping
        s = list(S)

        # Initialize result list
        self.res = []

        # Store string length
        self.n = len(s)

        # Start backtracking from position 0
        self.solve(0, s)

        return self.res


# Example Usage and Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Three distinct characters
    print("Test Case 1:")
    s1 = "ABC"
    result1 = sol.find_permutations(s1)
    print(f"Input: S = '{s1}'")
    print(f"Output: {result1}")
    print(f"Total permutations: {len(result1)}")
    print("Explanation: 3! = 6 permutations for 3 distinct characters")

    # Test Case 2: Two characters
    print("\n\nTest Case 2:")
    s2 = "AB"
    result2 = sol.find_permutations(s2)
    print(f"Input: S = '{s2}'")
    print(f"Output: {result2}")
    print(f"Total permutations: {len(result2)}")

    # Test Case 3: String with duplicates
    print("\n\nTest Case 3:")
    s3 = "AAB"
    result3 = sol.find_permutations(s3)
    print(f"Input: S = '{s3}'")
    print(f"Output: {result3}")
    print(f"Total permutations: {len(result3)}")
    print("Note: Contains duplicates because input has duplicate 'A's")

    # Test Case 4: Single character
    print("\n\nTest Case 4:")
    s4 = "A"
    result4 = sol.find_permutations(s4)
    print(f"Input: S = '{s4}'")
    print(f"Output: {result4}")
    print(f"Total permutations: {len(result4)}")

    # Test Case 5: Four characters
    print("\n\nTest Case 5:")
    s5 = "ABCD"
    result5 = sol.find_permutations(s5)
    print(f"Input: S = '{s5}'")
    print(f"Total permutations: {len(result5)}")
    print("Explanation: 4! = 24 permutations")
    print("First few:", result5[:5])

    # Test Case 6: All same characters
    print("\n\nTest Case 6:")
    s6 = "AAA"
    result6 = sol.find_permutations(s6)
    print(f"Input: S = '{s6}'")
    print(f"Output: {result6}")
    print(f"Total permutations: {len(result6)}")
    print("Note: All permutations are same due to duplicate characters")
