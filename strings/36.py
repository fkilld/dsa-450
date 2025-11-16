"""
Smallest Window in String Containing All Characters of Another String

PROBLEM DESCRIPTION:
Given two strings s and p, find the smallest substring in s that contains all
characters of p (including duplicates). If no such window exists, return -1.

Example: s = "timetopractice", p = "toc"
Output: "toprac" (contains t, o, c)

Example: s = "zoomlazapzo", p = "oza"
Output: "apzo" (contains o, z, a)

WHY THIS APPROACH (Sliding Window with Hash Array):
We use a SLIDING WINDOW with two hash arrays because:
1. We need to find a SUBSTRING (contiguous), not subsequence
2. Sliding window explores all possible windows in O(n) time
3. Two hash arrays allow O(1) character frequency comparison:
   - hash_pat[]: stores frequency of characters in pattern p
   - hash_str[]: stores frequency of characters in current window of s
4. We expand window until all pattern chars are found, then shrink to minimize
5. Using fixed-size array (256) for all ASCII chars is faster than dynamic hash map
6. This avoids O(n²) brute force of checking all substrings

ALTERNATIVE APPROACHES (Not Used):
1. Brute Force: Check all substrings O(n²) - too slow
2. Hash Map: Works but array is faster for fixed ASCII range
3. Two Pointers without frequency: Can't handle duplicate characters correctly

ALGORITHM:
Step 1: Initial Validation
   - If len(s) < len(p), no window possible, return -1

Step 2: Build Pattern Hash
   - Create hash_pat[256] to count frequency of each character in p
   - This tells us what we need to find in s

Step 3: Initialize Window Variables
   - start: left pointer of current window
   - start_index: left pointer of best window found (initially -1)
   - min_len: minimum window length found (initially infinity)
   - count: how many characters from p we've found in current window

Step 4: Expand Window (iterate i from 0 to len(s))
   - Add s[i] to hash_str (increment frequency)
   - If hash_str[s[i]] <= hash_pat[s[i]], increment count
     (we only count if we actually needed this character)

Step 5: Shrink Window (when count == len(p))
   - We have all required characters, try to minimize window
   - While character at 'start' is not needed or excess:
     - If hash_str[start] > hash_pat[start], we have extra, remove it
     - If hash_pat[start] == 0, this char not in pattern, remove it
     - Increment start pointer
   - Update min_len and start_index if this window is smaller

Step 6: Return Result
   - If start_index == -1, no valid window found, return -1
   - Otherwise return substring s[start_index : start_index + min_len]

EDGE CASES:
1. s shorter than p -> return -1
2. p not in s -> return -1
3. p is empty -> return "" or first char
4. s == p -> return s
5. Multiple valid windows -> return smallest
6. Characters with duplicates: "aa" in "baa" -> handle with frequency count

TIME COMPLEXITY: O(n + m)
- n = length of s, m = length of p
- Building hash_pat: O(m)
- Main loop iterates through s: O(n)
- Inner while loop: each character removed at most once, so O(n) total
- Overall: O(n + m)

SPACE COMPLEXITY: O(1)
- Two hash arrays of fixed size 256: O(1)
- A few variables: O(1)
- Overall: O(1) - not dependent on input size

EXAMPLE WALKTHROUGH:
Input: s = "timetopractice", p = "toc"

Step 1: Build hash_pat: t=1, o=1, c=1
Step 2: Expand window:
  i=0: 't' -> count=1
  i=1: 'i' -> count=1
  i=2: 'm' -> count=1
  i=3: 'e' -> count=1
  i=4: 't' -> count=1 (already have enough 't')
  i=5: 'o' -> count=2
  i=6: 'p' -> count=2
  i=7: 'r' -> count=2
  i=8: 'a' -> count=2
  i=9: 'c' -> count=3 (found all!)

Step 3: Shrink window:
  start=0, remove unnecessary chars
  After shrinking: window = "toprac", len=6

Continue expanding and shrinking...
Final answer: "toprac"
"""

# Smallest window in a string containing all the characters of another string

class Solution:

    def smallestWindow(self, s, p):
        """
        Find smallest window in s containing all characters of p.

        Args:
            s: source string to search in
            p: pattern string whose characters we need to find

        Returns:
            Smallest substring of s containing all chars of p, or -1 if not found
        """
        len1 = len(s)
        len2 = len(p)

        # Step 1: Validation - pattern can't be longer than string
        if len1 < len2:
            return -1

        # Step 2: Create hash arrays for ASCII characters (0-255)
        hash_pat = [0] * 256  # Frequency of chars in pattern p
        hash_str = [0] * 256  # Frequency of chars in current window of s

        # Step 3: Build pattern frequency hash
        # Count occurrences of each character in pattern
        for i in range(len2):
            hash_pat[ord(p[i])] += 1

        # Step 4: Initialize sliding window variables
        start = 0  # Left pointer of current window
        start_index = -1  # Left pointer of best (smallest) window found
        min_len = float('inf')  # Length of smallest window found

        count = 0  # Number of required characters found in current window

        # Step 5: Expand window by moving right pointer (i)
        for i in range(len1):
            # Add current character to window
            hash_str[ord(s[i])] += 1

            # Increment count only if this character is needed and not excess
            # If hash_str[char] <= hash_pat[char], we still need this character
            if hash_str[ord(s[i])] <= hash_pat[ord(s[i])]:
                count += 1

            # Step 6: When all required characters found, try to shrink window
            if count == len2:
                # Remove unnecessary characters from left side of window
                # A character is unnecessary if:
                # 1. It's not in pattern (hash_pat[char] == 0), OR
                # 2. We have excess of it (hash_str[char] > hash_pat[char])
                while hash_str[ord(s[start])] > hash_pat[ord(s[start])] or hash_pat[ord(s[start])] == 0:
                    if hash_str[ord(s[start])] > hash_pat[ord(s[start])]:
                        hash_str[ord(s[start])] -= 1
                    start += 1

                # Calculate current window size
                len_window = i - start + 1

                # Update minimum window if current is smaller
                if min_len > len_window:
                    min_len = len_window
                    start_index = start

        # Step 7: Return result
        if start_index == -1:
            return -1  # No valid window found
        else:
            return s[start_index: start_index + min_len]