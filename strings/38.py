"""
Wildcard Pattern Matching

PROBLEM DESCRIPTION:
Given a string and a wildcard pattern, determine if they match.
The wildcard pattern can include:
- '?' : Matches exactly one character
- '*' : Matches zero or more characters (any sequence)
- Regular characters: Must match exactly

Example: pattern = "a*b?c", string = "aXYbZc" -> True
         (a matches a, * matches XY, b matches b, ? matches Z, c matches c)
Example: pattern = "a?b", string = "acb" -> True
         (a matches a, ? matches c, b matches b)
Example: pattern = "a*b", string = "a" -> False
         (* can match empty, but 'b' is missing)

WHY THIS APPROACH (Dynamic Programming):
We use DYNAMIC PROGRAMMING with a 2D table because:
1. Optimal substructure: match(s[0..i], p[0..j]) depends on smaller subproblems
2. Overlapping subproblems: same substrings are checked multiple times
3. '*' creates branching: it can match 0, 1, 2, ... characters
   - Without DP, recursive solution would recompute same states many times
4. DP table dp[i][j] = "does string[0..i-1] match pattern[0..j-1]?"
5. Build solution bottom-up from empty strings to full strings

ALTERNATIVE APPROACHES (Not Used):
1. Recursion without memoization: O(2^n) - too slow, many redundant computations
2. Greedy matching: Doesn't work because '*' can match variable lengths
3. Regular expression engines: Overkill for simple '?' and '*' wildcards

ALGORITHM:
Step 1: Handle Empty Pattern
   - If pattern is empty, only empty string matches

Step 2: Create DP Table
   - dp[i][j] = True if string[0..i-1] matches pattern[0..j-1]
   - Dimensions: (n+1) x (m+1) where n = len(string), m = len(pattern)

Step 3: Initialize Base Cases
   - dp[0][0] = True (empty string matches empty pattern)
   - dp[0][j] = True if pattern[0..j-1] contains only '*'
     (because '*' can match empty string)
   - dp[i][0] = False for i > 0 (non-empty string can't match empty pattern)

Step 4: Fill DP Table
   For each position (i, j):

   Case A: pattern[j-1] == '*'
     - '*' matches zero chars: dp[i][j] = dp[i][j-1]
     - '*' matches one or more chars: dp[i][j] = dp[i-1][j]
     - Combined: dp[i][j] = dp[i][j-1] OR dp[i-1][j]

   Case B: pattern[j-1] == '?' OR pattern[j-1] == string[i-1]
     - Characters match (either exact or wildcard '?')
     - dp[i][j] = dp[i-1][j-1]

   Case C: Characters don't match
     - dp[i][j] = False

Step 5: Return Result
   - Return dp[n][m] (does full string match full pattern?)

EDGE CASES:
1. Empty pattern and empty string -> True
2. Empty pattern and non-empty string -> False
3. Pattern with only '*' -> matches any string (including empty)
4. String with no wildcards -> exact match required
5. Multiple consecutive '*' -> same as single '*'
6. Pattern longer than string but still matches (e.g., "***" matches "a")

TIME COMPLEXITY: O(n * m)
- n = length of string, m = length of pattern
- We fill a table of size (n+1) x (m+1)
- Each cell takes O(1) time to compute
- Overall: O(n * m)

SPACE COMPLEXITY: O(n * m)
- DP table of size (n+1) x (m+1)
- Can be optimized to O(m) using rolling array, but current implementation uses O(n*m)

EXAMPLE WALKTHROUGH:
Input: string = "abc", pattern = "a?c"

Step 1: Create dp table (4 x 4):
        ""  a   ?   c
    ""  T   F   F   F
    a   F   ?   ?   ?
    b   F   ?   ?   ?
    c   F   ?   ?   ?

Step 2: Initialize base cases:
        ""  a   ?   c
    ""  T   F   F   F
    a   F
    b   F
    c   F

Step 3: Fill table:
  dp[1][1]: 'a' vs 'a' -> match -> dp[0][0] = T -> T
  dp[1][2]: 'a' vs '?' -> need 'aa' match 'a?' -> F
  ...
  dp[2][2]: 'ab' vs 'a?' -> 'b' vs '?' -> match -> dp[1][1] = T -> T
  dp[3][3]: 'abc' vs 'a?c' -> 'c' vs 'c' -> match -> dp[2][2] = T -> T

Final table:
        ""  a   ?   c
    ""  T   F   F   F
    a   F   T   F   F
    b   F   F   T   F
    c   F   F   F   T

Output: dp[3][3] = True
"""

# Wildcard Pattern Matching

def match(pattern, string):
    """
    Check if string matches wildcard pattern using dynamic programming.

    Args:
        pattern: Wildcard pattern with '*' (0+ chars) and '?' (1 char)
        string: String to match against pattern

    Returns:
        True if string matches pattern, False otherwise
    """
    # n = length of string, m = length of pattern
    n = len(string)
    m = len(pattern)

    # Step 1: Handle empty pattern edge case
    if m == 0:
        return n == 0  # Empty pattern matches only empty string

    # Step 2: Create DP table
    # dp[i][j] = True if string[0..i-1] matches pattern[0..j-1]
    dp = [[False for i in range(m + 1)] for j in range(n + 1)]

    # Step 3: Initialize base cases
    # Base case: empty string matches empty pattern
    dp[0][0] = True

    # Base case: empty string can match pattern with only '*'
    # '*' can match zero characters, so propagate True along first row
    for j in range(1, m + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]  # Inherits from previous pattern char

    # Step 4: Fill the DP table bottom-up
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Note: i, j represent lengths (1-indexed)
            # pattern[j-1] and string[i-1] are actual characters (0-indexed)

            # Case A: Pattern has '*' wildcard
            if pattern[j - 1] == '*':
                # Two choices for '*':
                # 1. Match zero characters: dp[i][j-1] (ignore '*')
                # 2. Match one or more characters: dp[i-1][j] (use '*' again)
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

            # Case B: Pattern has '?' wildcard or exact character match
            elif pattern[j - 1] == '?' or pattern[j - 1] == string[i - 1]:
                # '?' matches any single character
                # Or characters match exactly
                # Result depends on whether prefixes matched
                dp[i][j] = dp[i - 1][j - 1]

            # Case C: Characters don't match and no wildcard
            else:
                dp[i][j] = False

    # Step 5: Return final result
    # Does full string match full pattern?
    return dp[n][m]