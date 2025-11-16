"""
Problem: Word Wrap (Text Justification with Minimum Cost)
----------------------------------------------------------
Given an array of word lengths and a maximum line width k, arrange the words
into lines such that the total cost is minimized. The cost of a line is the
square of the number of extra spaces at the end of the line (last line has 0 cost).

APPROACH: Dynamic Programming (Right-to-Left)
----------------------------------------------
WHY THIS APPROACH?
- We use DP working backwards from the last word because the last line has
  special treatment (0 cost regardless of spaces)
- Right-to-left DP allows us to know the optimal cost for all suffixes, making
  it easy to compute the cost for each prefix
- For each position i, we try all possible last words that fit on the line
  starting at i, and choose the one with minimum total cost
- Bottom-up DP avoids recalculating subproblems (memoization automatically handled)
- Alternative: Top-down would require special handling for the last line case

ALGORITHM:
1. Create dp[i] = minimum cost to arrange words from index i to end
2. Create ans[i] = the last word index on the line starting with word i
3. Base case: dp[n-1] = 0 (single last word has no cost)
4. For each position i from n-2 down to 0:
   a. Try placing words i, i+1, ..., j on the same line
   b. Track current line length (sum of word lengths + spaces)
   c. If line length exceeds k, break
   d. If j is the last word (j==n-1), cost is 0
   e. Otherwise, cost = (k - curr_len)² + dp[j+1]
   f. Choose j that gives minimum cost
5. Return dp[0] for the minimum cost starting from word 0

TIME COMPLEXITY: O(n²) where n is number of words
- Outer loop runs n times, inner loop runs up to n times

SPACE COMPLEXITY: O(n)
- Two arrays of size n for dp and ans

EDGE CASES:
- Single word: cost is 0
- All words fit on one line: cost is (k - total_length)² if not last line
- Word length > k: would cause infinite cost (problem assumes valid input)
- Empty array: not applicable

EXAMPLE:
Input: arr = [3, 2, 2, 5], k = 6
Words: "aaa bb cc ddddd"
Optimal arrangement:
Line 1: "aaa bb" (length=6, no extra spaces, cost=0²=0)
Line 2: "cc" (length=2, extra=4, but last line so cost=0)
Line 3: "ddddd" (length=5, last line, cost=0)
OR better:
Line 1: "aaa" (length=3, extra=3, cost=9)
Line 2: "bb cc" (length=5, extra=1, cost=1)
Line 3: "ddddd" (length=5, last line, cost=0)
Total cost: depends on optimal arrangement
"""

class Solution:
    def wordWrap(self, arr, k):
        n = len(arr)
        dp = [0]*n # stores the min line cost for arr[i] as start index
        ans = [0]*n # stores the last index with arr[i] as start

        # Base case: if only one word is present (the last word)
        # Last line has no cost regardless of extra spaces
        dp[n - 1] = 0
        ans[n - 1] = n - 1

        # Work backwards from second-to-last word to first word
        # For each position, we determine the optimal line arrangement
        for i in range(n -2, -1, -1):
            curr_len = -1 # Start at -1 because we add +1 for space before each word
            dp[i] = float('inf') # Initialize to infinity (will be minimized)

            # Try placing words from i to j on the same line
            for j in range(i, n):
                # Add current word length plus one space
                # (first word on line won't have space due to -1 initialization)
                curr_len += arr[j] + 1

                # If line exceeds max width, can't fit more words
                if curr_len > k:
                    break

                # Calculate cost of this line arrangement
                # If j is the last word, we're on the last line (cost = 0)
                if j == n - 1:
                    cost = 0
                else:
                    # Cost = (extra spaces)² + optimal cost for remaining words
                    # k - curr_len gives extra spaces on this line
                    cost = (k - curr_len) * (k - curr_len) + dp[j + 1]

                # Update dp[i] if this arrangement gives a better (lower) cost
                if cost < dp[i]:
                    dp[i] = cost
                    ans[i] = j  # Remember where this line ends

        # Return the minimum cost starting from the first word
        return dp[0]