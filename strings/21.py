"""
Count Palindromic Subsequences

PROBLEM:
Given a string, count the number of palindromic subsequences in it. A palindromic
subsequence is a sequence that reads the same backward as forward (not necessarily contiguous).
For example, "aba" has 4 palindromic subsequences: "a", "b", "a", "aba".

WHY THIS APPROACH:
We use Dynamic Programming because:
1. The problem has overlapping subproblems - counting palindromes in substring [i, j]
   depends on results from smaller substrings
2. It has optimal substructure - the solution for [i, j] can be built from solutions
   of [i+1, j], [i, j-1], and [i+1, j-1]
3. Two implementations shown: recursive with memoization (top-down) and
   tabulation (bottom-up) for comparison

ALGORITHM:
Method 1 - Recursive with Memoization (countPs):
1. Base cases:
   - If i > j: return 0 (invalid range)
   - If i == j: return 1 (single character is palindrome)
2. If characters at i and j match:
   - Count all palindromes in [i+1, j] (excluding first char)
   - Count all palindromes in [i, j-1] (excluding last char)
   - Add 1 for the new palindrome formed by string[i] and string[j]
3. If characters don't match:
   - Add palindromes from [i+1, j] and [i, j-1]
   - Subtract [i+1, j-1] to avoid double counting

Method 2 - Tabulation (countPs_2):
1. Initialize: Each single character is a palindrome (cps[i][i] = 1)
2. Build table for increasing substring lengths
3. For each substring, apply same logic as recursive approach
4. Return cps[0][n-1] modulo 10^9 + 7

TIME COMPLEXITY: O(n²) for both methods
- We fill an n×n DP table, each cell computed in O(1)

SPACE COMPLEXITY:
- Recursive: O(n²) for DP table + O(n) for recursion stack
- Tabulation: O(n²) for DP table only

EDGE CASES:
1. Single character: Returns 1
2. All same characters: Returns n*(n+1)/2
3. No repeating characters: Returns n (each character individually)
4. Empty string: Returns 0

EXAMPLE:
Input: "abcd"
Output: 4 (palindromes: "a", "b", "c", "d")

Input: "aab"
Output: 4 (palindromes: "a", "a", "b", "aa")
"""

class Solution:
    def func(self, i, j):
        """Helper function to count palindromic subsequences in substring [i, j]"""
        # Base case: invalid range
        if i > j: return 0

        # Return memoized result if already calculated
        if self.dp[i][j] != -1:
            return self.dp[i][j]

        # Base case: single character is always a palindrome
        if i == j:
            self.dp[i][j] = 1
            return 1

        # Case 1: When boundary characters match (e.g., "aba")
        # We can form new palindromes by adding these matching chars to inner subsequences
        elif self.string[i] == self.string[j]:
            # Count palindromes without first char + without last char + 1 (the pair itself)
            self.dp[i][j] = self.func(i+ 1, j) + self.func(i, j-1) + 1
            return self.dp[i][j]

        # Case 2: When boundary characters don't match
        else:
            # Include palindromes from both substrings but subtract overlap to avoid double counting
            self.dp[i][j] = self.func(i+1, j) + self.func(i, j-1) - self.func(i+1, j-1)
            return self.dp[i][j]

    def countPs(self, string):
        """
        Method 1: Count palindromic subsequences using recursive approach with memoization
        Initializes DP table and calls helper function
        """
        n = len(string)
        # Initialize DP table with -1 (uncalculated state)
        self.dp =[[-1 for x in range(n)] for y in range(n)]
        self.string = string
        # Start counting from entire string [0, n-1]
        return self.func(0, n -1)

    def countPs_2(self, string):
        """
        Method 2: Count palindromic subsequences using iterative tabulation (bottom-up DP)
        More space-efficient as it avoids recursion stack
        """
        n = len(string)

        # DP table: cps[i][j] stores count of palindromic subsequences in substring [i, j]
        cps = [[0 for i in range(n + 2)] for y in range(n + 2)]

        # Base case: each single character is a palindrome
        for i in range(n):
            cps[i][i] = 1

        # Build table for increasing substring lengths (2 to n)
        for l in range(2, n + 1):
            for i in range(n):
                # k is the ending index of substring of length l starting at i
                k = l + i - 1
                if k < n:
                    # Same logic as recursive approach
                    if string[i] == string[k]:
                        # Matching boundary chars: sum both substrings + 1 for the pair
                        cps[i][k] = cps[i + 1][k] + cps[i][k -1] + 1
                    else:
                        # Non-matching chars: subtract overlap to avoid double counting
                        cps[i][k] = cps[i + 1][k] + cps[i][k -1] - cps[i + 1][k - 1]

        # Return result modulo 10^9 + 7 to handle large numbers
        return cps[0][n-1] % (10**9 + 7)

ans = Solution()
print(ans.countPs('abcd'))