"""
Longest Common Subsequence (LCS)

PROBLEM:
Given two strings s1 and s2, find the length of their longest common subsequence.
A subsequence is a sequence that can be derived from another sequence by deleting
some or no elements without changing the order of remaining elements.

For example:
- LCS of "ABCDGH" and "AEDFHR" is "ADH" (length 3)
- LCS of "AGGTAB" and "GXTXAYB" is "GTAB" (length 4)

WHY THIS APPROACH:
We use Dynamic Programming because:
1. The problem has overlapping subproblems - LCS(i, j) is used multiple times
2. It has optimal substructure - LCS of larger strings built from LCS of substrings
3. Two methods shown: Memoized Recursion (top-down) and Tabulation (bottom-up)
4. Memoization is intuitive (recursive thinking with caching)
5. Tabulation eliminates recursion overhead and is slightly more efficient

ALGORITHM:

Base Cases:
- If either string is empty (index -1), LCS length is 0

Recursive Relation:
- If s1[i] == s2[j]: LCS(i,j) = 1 + LCS(i-1, j-1)  [characters match, include them]
- Else: LCS(i,j) = max(LCS(i-1, j), LCS(i, j-1))  [skip one character from either string]

Method 1 - Memoized Recursion (lcs):
1. Initialize DP table with -1 (uncalculated state)
2. Use recursive function with base cases:
   - If x == -1 or y == -1: return 0
   - If already calculated: return cached value
3. If characters match: recursively solve for remaining substrings + 1
4. If characters don't match: take max of two options (skip from s1 or s2)
5. Cache and return result

Method 2 - Tabulation (lcs_2):
1. Create DP table of size (x+1) × (y+1)
2. Initialize first row and column to 0 (base case: empty strings)
3. Fill table bottom-up:
   - If characters match: dp[i][j] = dp[i-1][j-1] + 1
   - Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
4. Return dp[x][y] (LCS of full strings)

TIME COMPLEXITY: O(x * y) where x, y are lengths of strings
- We fill an x×y DP table
- Each cell computed in O(1) time

SPACE COMPLEXITY:
- Memoization: O(x * y) for DP table + O(x + y) for recursion stack
- Tabulation: O(x * y) for DP table only

EDGE CASES:
1. Empty strings: Returns 0
2. No common subsequence: Returns 0
3. One string is subsequence of other: Returns length of smaller string
4. Identical strings: Returns length of the string

EXAMPLES:
Input: s1 = "ABCDGH", s2 = "AEDFHR"
DP table visualization:
    ""  A  E  D  F  H  R
""   0  0  0  0  0  0  0
A    0  1  1  1  1  1  1
B    0  1  1  1  1  1  1
C    0  1  1  1  1  1  1
D    0  1  1  2  2  2  2
G    0  1  1  2  2  2  2
H    0  1  1  2  2  3  3
Output: 3 (LCS = "ADH")

Input: s1 = "ABC", s2 = "AC"
Output: 2 (LCS = "AC")

Input: s1 = "ABC", s2 = "DEF"
Output: 0 (no common subsequence)
"""

class Solution:
    def func(self, x, y, s1, s2):
        """
        Recursive helper function to compute LCS with memoization

        Args:
            x: Current index in s1 (0-indexed)
            y: Current index in s2 (0-indexed)
            s1: First string
            s2: Second string

        Returns:
            Length of LCS for s1[0..x] and s2[0..y]
        """
        # Base case: if either string is exhausted, LCS length is 0
        if x == -1 or y == -1:
            return 0

        # Return cached result if already computed
        if self.dp[x][y] != -1:
            return self.dp[x][y]

        # Case 1: Characters match - include this character in LCS
        if s1[x] == s2[y]:
            self.dp[x][y] = 1 + self.func(x-1, y-1, s1, s2)
            return self.dp[x][y]

        # Case 2: Characters don't match - try both options
        # Option a: Skip character from s1
        a = self.func(x-1, y, s1, s2)
        # Option b: Skip character from s2
        b = self.func(x, y-1, s1, s2)

        # Take maximum of both options
        self.dp[x][y] = max(a, b)
        return self.dp[x][y]

    def lcs(self, x, y, s1, s2):
        """
        Method 1: Find LCS length using memoized recursion (top-down DP)

        Args:
            x: Length of first string
            y: Length of second string
            s1: First string
            s2: Second string

        Returns:
            Length of longest common subsequence
        """
        # Initialize DP table with -1 (uncalculated state)
        self.dp = [[-1 for i in range(y + 1)] for j in range(x + 1)]
        # Start recursion from last indices (x-1, y-1)
        return self.func(x-1, y-1, s1, s2)
    
    def lcs_2(self, x, y, s1, s2):
        """
        Method 2: Find LCS length using tabulation (bottom-up DP)
        More efficient than recursion as it avoids function call overhead

        Args:
            x: Length of first string
            y: Length of second string
            s1: First string
            s2: Second string

        Returns:
            Length of longest common subsequence
        """
        # Create DP table: dp[i][j] = LCS length of s1[0..i-1] and s2[0..j-1]
        dp = [[-1 for i in range(y + 1)] for j in range(x + 1)]

        # Fill the DP table bottom-up
        for i in range(x + 1):
            for j in range(y + 1):
                # Base case: empty string has LCS length 0
                if i == 0 or j == 0:
                    dp[i][j] = 0

                # Characters match: add 1 to LCS of remaining substrings
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1

                # Characters don't match: take max of two options
                else:
                    # Option 1: Exclude current char from s1
                    # Option 2: Exclude current char from s2
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # Return LCS length for complete strings
        return dp[x][y]