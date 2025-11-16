"""
Problem: Count and Say Sequence
--------------------------------
Generate the nth term of the count-and-say sequence.

The sequence goes:
1st term: "1"
2nd term: "11" (one 1)
3rd term: "21" (two 1s)
4th term: "1211" (one 2, one 1)
5th term: "111221" (one 1, one 2, two 1s)

APPROACH: Iterative String Building with Run-Length Encoding
------------------------------------------------------------
WHY THIS APPROACH?
- We use iterative building because each term depends ONLY on the previous term
- Run-length encoding is the natural way to "say" what we "count"
- Adding sentinel character ('$') is a clever trick to handle the last group
- Building string term-by-term is more intuitive than trying to find a formula
- No mathematical formula exists - must simulate the process

WHY NOT RECURSION?
- Recursion would be inefficient (redundant recalculations without memoization)
- Iteration uses O(1) space (excluding output), recursion uses O(n) call stack
- Each term only needs the previous term, not earlier ones

THE SENTINEL TRICK:
We append '$' to ensure the last group of digits gets counted.
Without it, the inner loop wouldn't detect the end of the last group.

ALGORITHM:
1. Handle base cases: n=1 returns "1", n=2 returns "11"
2. Initialize s = "11" (starting from term 2)
3. For each term from 3 to n:
   a. Add sentinel '$' to mark end
   b. Create empty result string (temp)
   c. Scan through string counting consecutive identical digits
   d. When digit changes: append (count + digit) to result
   e. Replace s with newly built string
4. Return final string

TIME COMPLEXITY: O(n * m) where n = term number, m = average length of term
- Outer loop runs n times
- Inner loop processes each character in current term
- Term length grows exponentially in practice (roughly 1.3x per term)

SPACE COMPLEXITY: O(m) where m = length of nth term
- Only storing current and next term strings
- No recursion stack

EDGE CASES:
- n = 1: returns "1" (base case)
- n = 2: returns "11" (base case)
- Large n: string length grows exponentially

EXAMPLE TRACE (n=4):
Start: s = "11"
i=3:
  s = "11$"
  j=1: '1'!='1' ✗, c=2
  j=2: '$'!='1' ✓, temp="21", c=1
  s = "21"
i=4:
  s = "21$"
  j=1: '1'!='2' ✓, temp="12", c=1
  j=2: '$'!='1' ✓, temp="1211", c=1
  s = "1211"
Return "1211"
"""

class Solution:
    def countAndSay(self, n):
        # Base cases: first two terms are fixed
        if n == 1: return "1"
        if n == 2: return "11"

        # Start from the 2nd term
        s = "11"

        # Build each subsequent term iteratively
        for i in range(3, n + 1):
            # KEY TRICK: Add sentinel character to handle last group
            # Without this, we wouldn't process the final group of digits
            s += "$"

            temp = ""  # Stores the newly constructed string for this term
            c = 1      # Counter for consecutive identical characters

            # Scan through string, comparing each char with previous
            for j in range(1, len(s)):
                if s[j] != s[j - 1]:
                    # Different character found - "say" the previous group
                    temp += str(c)        # Add the count
                    temp += s[j - 1]      # Add the digit itself
                    c = 1                 # Reset counter for new group
                else:
                    # Same character continues - increment counter
                    c += 1

            # Current term becomes the next term's input
            s = temp

        return s