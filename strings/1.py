"""
Problem: Check if String is Palindrome
---------------------------------------
Given a string S, check if it reads the same forwards and backwards.

APPROACH: Two Pointer Technique
-------------------------------
WHY THIS APPROACH?
- Two pointers is optimal for palindrome checking because:
  * We need to compare characters from both ends moving inward
  * O(1) space complexity - no extra storage needed
  * O(n/2) comparisons - we only need to check half the string
  * Early termination possible when mismatch found
- Alternative approaches like reversing and comparing use O(n) extra space

ALGORITHM:
1. Place one pointer at start (i=0), another at end (j=len-1)
2. Compare characters at both positions
3. If they don't match → NOT a palindrome (return 0)
4. If they match → move both pointers inward
5. Continue until pointers cross (i >= j)
6. If all comparisons pass → IS a palindrome (return 1)

TIME COMPLEXITY: O(n/2) ≈ O(n) - worst case checks all n/2 pairs
SPACE COMPLEXITY: O(1) - only two pointer variables used

EDGE CASES:
- Empty string: returns 1 (considered palindrome)
- Single character: returns 1 (palindrome by definition)
- Even length palindrome: "abba"
- Odd length palindrome: "racecar"

EXAMPLES:
- "racecar" → 1 (palindrome)
- "hello" → 0 (not palindrome)
- "a" → 1 (single char is palindrome)
"""

class Solution:
    def isPalindrome(self, string):
        # Left pointer starts at beginning
        i = 0
        # Right pointer starts at end
        j = len(string) - 1

        # Traverse from both ends toward center
        # Continue while pointers haven't crossed
        while i <= j:
            # If characters don't match, it's not a palindrome
            if string[i] != string[j]:
                return 0  # Return 0 for false

            # Move left pointer forward
            i += 1
            # Move right pointer backward
            j -= 1

        # All characters matched - it's a palindrome
        return 1  # Return 1 for true