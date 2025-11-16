"""
Problem: Longest Prefix Suffix (LPS Array for KMP Algorithm)
-------------------------------------------------------------
Compute the Longest Proper Prefix which is also Suffix for each position in string.
This is the preprocessing step for the KMP (Knuth-Morris-Pratt) pattern matching algorithm.

APPROACH: Two Pointer with Previously Computed LPS Values
---------------------------------------------------------
WHY THIS APPROACH?
- We use dynamic programming principle: previously computed LPS values help compute current
- Avoids naive O(n³) approach of checking all prefix-suffix pairs explicitly
- The key insight: if we have a mismatch, we can "fall back" to a shorter prefix using lps[l-1]
- This leverages the fact that if a prefix p matches, we already know lps values within p
- Achieves O(n) time despite seemingly nested structure (amortized analysis)

WHAT IS LPS?
LPS[i] = length of longest PROPER prefix of substring s[0...i] that is also a suffix
- "Proper" means prefix ≠ entire substring

Example: s = "AAACAAAA"
Position:  0 1 2 3 4 5 6 7
String:    A A A C A A A A
LPS:       0 1 2 0 1 2 3 3

At index 6: "AAACAAA" has prefix "AAA" which is also suffix → LPS[6] = 3

WHY IS THIS USEFUL?
- KMP pattern matching uses this to avoid re-examining characters after a mismatch
- Helps find repeating patterns in strings
- Used in string compression and periodicity detection

ALGORITHM:
1. Initialize lps array with all zeros, size n
2. Set l = 0 (length of previous match), i = 1 (current position)
3. For each position i:
   a. If s[i] == s[l]: We extend the current match
      - Set lps[i] = l + 1
      - Increment both l and i
   b. If s[i] != s[l]: Mismatch occurred
      - If l > 0: "Fall back" to shorter prefix using l = lps[l-1]
        (Try to match using a shorter previously computed prefix)
      - If l == 0: No match possible, set lps[i] = 0, move to next position
4. Return lps[n-1] (LPS value of last position)

WHY THE FALLBACK WORKS?
When we have a mismatch at position i with length l:
- We know s[0...l-1] matches s[i-l...i-1] (by definition of l)
- lps[l-1] gives us a shorter prefix that also matches within s[0...l-1]
- This shorter prefix might match at current position i

TIME COMPLEXITY: O(n)
- Each character is processed at most twice
- 'i' only moves forward (n iterations)
- 'l' increases at most n times, decreases at most n times
- Amortized: O(2n) = O(n)

SPACE COMPLEXITY: O(n)
- LPS array of size n

EDGE CASES:
- Empty string: n=0, return 0
- Single character: lps = [0], return 0
- All same characters "AAAA": lps = [0,1,2,3]
- No repeating pattern "ABCD": lps = [0,0,0,0]

EXAMPLE TRACE: s = "ABABC"
i=1: s[1]='B' != s[0]='A' → lps[1]=0, i=2
i=2: s[2]='A' == s[0]='A' → lps[2]=1, l=1, i=3
i=3: s[3]='B' == s[1]='B' → lps[3]=2, l=2, i=4
i=4: s[4]='C' != s[2]='A' → fallback l=lps[1]=0
     s[4]='C' != s[0]='A' → lps[4]=0, i=5
Result: lps = [0,0,1,2,0], return lps[4] = 0
"""

class Solution:
	def lps(self, s):
		n = len(s)

		# LPS array: lps[i] = length of longest proper prefix of s[0..i]
		# that is also a suffix
		lps = [0] * n

		# l = length of the previous longest matching prefix-suffix
		# Also acts as index in the string we're comparing against
		l = 0

		# Start from index 1 (index 0 is always 0 by definition)
		i = 1

		# Process each character
		while i < len(s):
			if s[i] == s[l]:
				# MATCH: Current character extends the previous match
				# The longest prefix-suffix length increases by 1
				lps[i] = l + 1
				l += 1  # Length increases
				i += 1  # Move to next position

			else:
				# MISMATCH: Current character doesn't extend the match

				if l != 0:
					# FALLBACK: Try a shorter prefix using previously computed LPS
					# We "fall back" to the prefix indicated by lps[l-1]
					# This is the key optimization that makes KMP O(n)
					# Don't increment i - we'll retry matching at current position
					l = lps[l - 1]
				else:
					# No fallback possible (we're at the start)
					# No prefix-suffix match at this position
					lps[i] = 0
					i += 1  # Move to next position

		# Return the LPS value of the last position
		# This represents the longest prefix that is also suffix for the entire string
		return lps[n - 1]
