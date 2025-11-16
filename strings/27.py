"""
Minimum Number of Flips to Make Binary String Alternating

PROBLEM:
Given a binary string (containing only '0' and '1'), find the minimum number of flips
required to make the string alternating. An alternating string has no two adjacent
characters that are the same (e.g., "010101" or "101010").

WHY THIS APPROACH:
We use Two-Pattern Comparison because:
1. There are only 2 possible alternating patterns for any length:
   - Pattern 1: Start with '0' -> "0101010..."
   - Pattern 2: Start with '1' -> "1010101..."
2. We can count mismatches with each pattern independently
3. The minimum of the two counts is our answer
4. This is simpler than trying to build the alternating string dynamically
5. Single pass through the string is sufficient (O(n) time)

ALGORITHM:
1. Initialize two counters (c1 and c2) to count flips for each pattern
2. Pattern 1 (even positions have '0', odd positions have '1'):
   - For each position i:
     * If i is even and s[i] == '1': increment c1 (should be '0')
     * If i is odd and s[i] == '0': increment c1 (should be '1')
3. Pattern 2 (even positions have '1', odd positions have '0'):
   - For each position i:
     * If i is even and s[i] == '0': increment c2 (should be '1')
     * If i is odd and s[i] == '1': increment c2 (should be '0')
4. Return minimum of c1 and c2

TIME COMPLEXITY: O(n) where n is length of string
- Two separate passes through the string (could be optimized to one pass)
- Each position checked once per pass

SPACE COMPLEXITY: O(1)
- Only two counter variables used
- No additional data structures

EDGE CASES:
1. Already alternating: Returns 0
2. All same characters: Returns n/2 (flip half the characters)
3. Single character: Returns 0 (already alternating)
4. Length 2: Returns 0 if different, 1 if same

EXAMPLES:
Input: "001"
Output: 1 (flip middle: "001" -> "011" or "001" -> "001")
Wait, let's check: "001" -> flip to "010" (1 flip) or "101" (2 flips)
Minimum is 1

Input: "0001010111"
Pattern 1 (0101010101): positions 3,7,8 need flips = 3 flips
Pattern 2 (1010101010): positions 0,1,2,4,6,9 need flips = 6 flips
Output: 3

Input: "111000"
Pattern 1 (010101): positions 0,1,3,4 need flips = 4 flips
Pattern 2 (101010): positions 2,5 need flips = 2 flips
Output: 2
"""

class Solution:
    def minFlips(self, s):
        """
        Calculate minimum flips needed to make string alternating

        Args:
            s: Binary string containing only '0' and '1'

        Returns:
            Minimum number of flips required
        """
        c1 = 0  # Counter for Pattern 1: "010101..."
        c2 = 0  # Counter for Pattern 2: "101010..."

        # Count flips needed for Pattern 1 (even positions = '0', odd positions = '1')
        for i in range(len(s)):
            if i % 2 == 0 and s[i] == '1':
                # Even position should be '0' but found '1'
                c1 += 1
            elif i % 2 != 0 and s[i] == '0':
                # Odd position should be '1' but found '0'
                c1 += 1

        # Count flips needed for Pattern 2 (even positions = '1', odd positions = '0')
        for i in range(len(s)):
            if i % 2 == 0 and s[i] == '0':
                # Even position should be '1' but found '0'
                c2 += 1
            elif i % 2 != 0 and s[i] == '1':
                # Odd position should be '0' but found '1'
                c2 += 1

        # Return the minimum flips between the two patterns
        return min(c1, c2)