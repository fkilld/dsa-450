"""
Smallest Distinct Window

PROBLEM DESCRIPTION:
Given a string, find the length of the smallest substring that contains all
distinct characters present in the entire string.

Example: "aabcbcdbca"
- Distinct chars: {a, b, c, d} (4 chars)
- Smallest window containing all: "dbca" (length 4)

WHY THIS APPROACH (Sliding Window):
We use a SLIDING WINDOW with two pointers because:
1. We need to find a SUBSTRING (contiguous sequence), not subsequence
2. Sliding window efficiently explores all possible windows in O(n) time
3. We can dynamically expand (right pointer) to include characters and
   shrink (left pointer) to minimize window size
4. Using a hash map allows O(1) character frequency lookups
5. This avoids the O(n^2) brute force approach of checking all substrings

ALGORITHM:
Step 1: Count Distinct Characters
   - Create a hash map and count all unique characters in the string
   - This gives us 'n' = number of distinct characters we need in our window

Step 2: Initialize Window
   - Use two pointers: i (left/start), j (right/end)
   - Track 'count' = number of distinct characters currently in window
   - Initialize with first character in the window

Step 3: Expand Window (Right Pointer j)
   - While count < n (haven't found all distinct chars yet):
     - Add string[j] to window, increment its frequency
     - If this character's count becomes 1 (new distinct char), increment 'count'
     - Move j forward

Step 4: Shrink Window (Left Pointer i)
   - When count == n (all distinct chars found):
     - Update minimum window length: ans = min(ans, j - i)
     - Try to shrink from left:
       - Decrease frequency of string[i]
       - If frequency becomes 0 (lost a distinct char), decrement 'count'
       - Move i forward
     - Repeat shrinking while count == n

Step 5: Final Cleanup
   - After j reaches end, continue shrinking from left while count == n
   - This handles cases where optimal window ends at the string's end

EDGE CASES:
1. String with all same characters -> window size = 1
2. String where all characters are distinct -> window size = length of string
3. Single character string -> return 1
4. Empty string -> undefined (assume input is valid)

TIME COMPLEXITY: O(n)
- Each character is visited at most twice (once by j, once by i)
- Hash map operations (insert, lookup, update) are O(1)
- Overall: O(n) where n is the length of the string

SPACE COMPLEXITY: O(k)
- k = number of distinct characters in the string
- Hash map stores at most k unique characters
- In worst case (all unique chars), k = n, so O(n)

EXAMPLE WALKTHROUGH:
Input: "aabcbcdbca"
Distinct chars: {a, b, c, d}, n = 4

Window evolution:
i=0, j=0: "a" -> count=1, ans=inf
i=0, j=1: "aa" -> count=1, ans=inf
i=0, j=2: "aab" -> count=2, ans=inf
i=0, j=3: "aabc" -> count=3, ans=inf
i=0, j=4: "aabcb" -> count=3, ans=inf
i=0, j=5: "aabcbc" -> count=3, ans=inf
i=0, j=6: "aabcbcd" -> count=4, ans=7, shrink...
i=1, j=6: "abcbcd" -> count=4, ans=6, shrink...
i=2, j=6: "bcbcd" -> count=3, expand...
i=2, j=7: "bcbcdb" -> count=4, ans=6, shrink...
... continue until we find "dbca" with length 4

Output: 4
"""

# Smallest distinct window

class Solution:
    def findSubString(self, string):
        char_map = {}

        # Step 1: Create map of all unique characters in the string
        # Initialize all frequencies to 0 to identify distinct characters
        for char in string:
            if char not in char_map:
                char_map[char] = 0

        n = len(char_map)  # Total number of distinct characters we need to find

        # Step 2: Initialize sliding window
        i = 0  # Left pointer (window start)
        char_map[string[0]] = 1  # First character is already in the window
        j = 1  # Right pointer (window end)
        count = 1  # Number of distinct characters currently in window
        ans = float('inf')  # Minimum window length found so far

        # Step 3: Expand and shrink window using two pointers
        while j < len(string) and i <= j:
            # Expand window: add characters until we have all distinct chars
            if count < n:
                if char_map[string[j]] == 0:  # New distinct char entering window
                    count += 1
                char_map[string[j]] += 1  # Increment frequency
                j += 1  # Move right pointer forward

            # Shrink window: found all distinct chars, try to minimize length
            elif count == n:
                ans = min(ans, j - i)  # Update minimum window size
                if char_map[string[i]] == 1:  # Removing this char loses a distinct char
                    count -= 1
                char_map[string[i]] -= 1  # Decrement frequency
                i += 1  # Move left pointer forward to shrink window

        # Step 4: Final cleanup - j reached end, continue shrinking from left
        # This handles cases where the optimal window ends at the string's end
        while count == n:
            ans = min(ans, j - i)
            if char_map[string[i]] == 1:  # Losing a distinct character
                count -= 1
            char_map[string[i]] -= 1
            i += 1

        return ans
