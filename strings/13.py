"""
Problem: Edit Distance (Levenshtein Distance)
----------------------------------------------
Given two strings s and t, find the minimum number of operations required to
convert string s to string t. Allowed operations are:
1. Insert a character
2. Delete a character
3. Replace a character

APPROACH: Dynamic Programming with Memoization (Top-Down)
----------------------------------------------------------
WHY THIS APPROACH?
- Memoized recursion naturally represents the decision tree for each character
- At each position, we have 3 choices (insert/delete/replace), and we pick
  the one with minimum cost
- DP table stores solutions to subproblems to avoid recomputation
- Top-down approach is intuitive: for each character, decide what to do
- Alternative bottom-up DP would work too, but this approach is easier to
  understand the recursion structure
- Memoization reduces time from O(3^(n+m)) to O(n*m)

ALGORITHM:
1. Create a 2D DP table dp[n+1][m+1] initialized to -1
2. Base cases:
   - If s is empty (n=0), we need m insertions to get t
   - If t is empty (m=0), we need n deletions to convert s
3. For each position (n, m):
   a. If dp[n][m] already computed, return it
   b. If s[n-1] == t[m-1], characters match:
      - No operation needed, recurse with (n-1, m-1)
   c. If s[n-1] != t[m-1], try all three operations:
      - Delete from s: 1 + operation(n-1, m)
      - Insert into s: 1 + operation(n, m-1)
      - Replace in s: 1 + operation(n-1, m-1)
   d. Store minimum in dp[n][m] and return
4. Return dp[n][m] for the final answer

TIME COMPLEXITY: O(n * m) where n = len(s), m = len(t)
- We fill an n×m DP table, each cell computed once

SPACE COMPLEXITY: O(n * m)
- DP table of size (n+1) × (m+1)
- Recursion stack can go up to O(n+m) depth

EDGE CASES:
- Empty strings: if s="", return len(t); if t="", return len(s)
- Identical strings: return 0
- One character different: return 1
- Completely different strings: return max(len(s), len(t))

EXAMPLE:
Input: s = "horse", t = "ros"
- 'h' -> 'r': replace (1 operation)
- 'o' -> 'o': match (0 operations)
- 'r' -> 's': already have 'r', need 's' after
- Delete 'r', 's' -> 's': match
- Delete 'e'
Total: 3 operations (replace h->r, delete r, delete e)

Video explanation: https://www.youtube.com/watch?v=AuYujVj646Q
"""

class Solution:
    def operation(self, s, t, n, m, dp):
        # Base case 1: If string s is exhausted (n=0)
        # We need m insertions to form string t
        if n == 0: return m

        # Base case 2: If string t is exhausted (m=0)
        # We need n deletions to convert s to empty string
        if m == 0: return n

        # Memoization: Return cached result if already computed
        if dp[n][m] != -1:
            return dp[n][m]

        # Case 1: Characters match (s[n-1] == t[m-1])
        # No operation needed, move both pointers back
        if s[n - 1] == t[m -1]:
            if dp[n - 1][m - 1] == -1:
                # Compute and cache the result
                dp[n][m] = self.operation(s, t, n - 1, m - 1, dp)
                return dp[n][m]
            else:
                # Use already computed result
                dp[n][m] = dp[n -1][m - 1]
                return dp[n][m]
        else:
            # Case 2: Characters don't match - try all 3 operations

            # Operation 1: DELETE - Remove character from s
            # Move s pointer back (n-1), keep t pointer same (m)
            if dp[n - 1][m] != -1:
                m1 = dp[n -1][m]
            else:
                m1 = self.operation(s, t, n -1, m, dp)

            # Operation 2: INSERT - Add character to s to match t[m-1]
            # Keep s pointer same (n), move t pointer back (m-1)
            if dp[n][m - 1] != -1:
                m2 = dp[n][m - 1]
            else:
                m2 = self.operation(s, t, n, m - 1, dp)

            # Operation 3: REPLACE - Replace s[n-1] with t[m-1]
            # Move both pointers back (n-1, m-1)
            if dp[n - 1][m - 1] != -1:
                m3 = dp[n -1][m -1]
            else:
                m3 = self.operation(s, t, n - 1, m -1, dp)

        # Take minimum of all three operations and add 1 for current operation
        dp[n][m] = 1 + min(m1, min(m2, m3))
        return dp[n][m]

    def editDistance(self, s, t):
        n = len(s) # length of string 1
        m = len(t) # length of string 2

        # dp = [[0 for col in columns] for r in rows]
        dp = [[-1 for x in range(n + 1)] for y in range(m + 1)]
        return self.operation(s, t, n, m, dp)