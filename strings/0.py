"""
Problem: Reverse a String
--------------------------
Given a string (or list of characters), reverse it in-place.

APPROACH: Two Pointer Technique
-------------------------------
WHY THIS APPROACH?
- We use the two-pointer technique because it's the most efficient way to reverse in-place
- It requires NO extra space (O(1) space complexity)
- It only requires n/2 swaps, making it optimal
- In-place modification saves memory compared to creating a new reversed string

ALGORITHM:
1. Initialize two pointers: left (i) at start, right (j) at end
2. While left < right:
   - Swap characters at positions i and j
   - Move left pointer forward (i++)
   - Move right pointer backward (j--)
3. Stop when pointers meet in the middle

TIME COMPLEXITY: O(n) - we visit each element once (actually n/2 swaps)
SPACE COMPLEXITY: O(1) - only using two pointer variables, no extra space

EDGE CASES:
- Empty string: while loop won't execute
- Single character: while loop won't execute (i >= j)
- Two characters: one swap occurs
"""

class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        # Initialize left pointer at beginning
        i = 0
        # Initialize right pointer at end
        j = len(s) - 1

        # Continue swapping until pointers meet in middle
        while i < j:
            # Swap characters at both ends using Python's tuple unpacking
            s[i], s[j] = s[j], s[i]
            # Move left pointer forward
            i += 1
            # Move right pointer backward
            j -= 1
        return s
        