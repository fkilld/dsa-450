"""
Problem: Longest Palindromic Substring
---------------------------------------
Given a string, find the longest substring that is a palindrome.

APPROACH: Expand Around Center (Two Pointers)
---------------------------------------------
WHY THIS APPROACH?
- Expand-around-center is optimal for this problem because:
  * O(n²) time is best we can do for general case
  * O(1) space - no extra data structures needed
  * Intuitive: every palindrome has a center we can expand from
  * Handles both even and odd length palindromes naturally
- Alternative: Manacher's algorithm is O(n) but complex to implement
- Alternative: DP is O(n²) time but O(n²) space - wasteful

KEY INSIGHT:
Every palindrome can be found by starting from its CENTER and expanding outward.
But centers come in TWO types:
1. ODD length palindromes: center is a single character (e.g., "racecar")
2. EVEN length palindromes: center is between two characters (e.g., "abba")

ALGORITHM:
For each possible center position in the string:
1. Try expanding around EVEN-length center (between chars i-1 and i)
   - Start with low=i-1, high=i
   - Expand while characters match
   - Track longest palindrome found
2. Try expanding around ODD-length center (at char i)
   - Start with low=i-1, high=i+1
   - Expand while characters match
   - Track longest palindrome found
3. Return the longest palindrome found

TIME COMPLEXITY: O(n²)
- Outer loop: n iterations (one per potential center)
- Inner while loops: O(n) expansion in worst case (all same character)
- Total: O(n × n) = O(n²)

SPACE COMPLEXITY: O(1)
- Only using fixed variables (start, end, low, high)
- Return value doesn't count toward space complexity

WHY TWO SEPARATE CHECKS?
We need to check both even and odd length palindromes because:
- "abba" has center between b's (even length)
- "aba" has center at 'b' (odd length)
Missing either check would miss valid palindromes!

EDGE CASES:
- Single character: return that character (length 1)
- No palindrome > 1: return first character
- Entire string is palindrome: return entire string

EXAMPLE TRACE: s = "babad"
i=1 (char 'a'):
  Even: low=0, high=1 → "ba" not palindrome
  Odd: low=0, high=2 → "bab" palindrome! start=0, end=3
i=2 (char 'b'):
  Even: low=1, high=2 → "ab" not palindrome
  Odd: low=1, high=3 → "aba" palindrome! (same length as "bab")
Result: "bab" (or "aba", both length 3)
"""

class Solution:
    def longestPalin(self, s):
        start = 0  # Starting index of the longest palindrome found
        end = 1    # Length of the longest palindrome found (initialized to 1 for single char)

        # Try every position as a potential palindrome center
        for i in range(1, len(s)):
            # CASE 1: Check for EVEN-length palindromes
            # Center is BETWEEN characters i-1 and i
            # Example: "abba" - center between the two b's
            low = i - 1   # Start just left of center
            high = i      # Start just right of center

            # Expand outward while characters match and we're in bounds
            while low >= 0 and high < len(s) and s[low] == s[high]:
                # Check if this palindrome is longer than current best
                if high - low + 1 > end:
                    start = low                # Update starting position
                    end = high - low + 1       # Update length
                # Expand further outward
                low -= 1
                high += 1

            # CASE 2: Check for ODD-length palindromes
            # Center is AT character i
            # Example: "racecar" - center is 'e'
            low = i - 1     # Start left of center
            high = i + 1    # Start right of center

            # Expand outward while characters match and we're in bounds
            while low >= 0 and high < len(s) and s[low] == s[high]:
                # Check if this palindrome is longer than current best
                if high - low + 1 > end:
                    start = low                # Update starting position
                    end = high - low + 1       # Update length
                # Expand further outward
                low -= 1
                high += 1

        # Return the longest palindrome substring
        # start = beginning index, end = length
        return s[start:start + end]
            