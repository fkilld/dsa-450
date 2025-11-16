"""
Longest Common Prefix

PROBLEM:
Given an array of strings, find the longest common prefix string amongst all strings.
If there is no common prefix, return an empty string "".

WHY THIS APPROACH:
We use Iterative Reduction with Shortest String Optimization because:
1. The longest possible prefix cannot be longer than the shortest string
2. By starting with the shortest string as candidate, we minimize iterations
3. We iteratively reduce the prefix when it doesn't match, rather than building it up
4. This approach is intuitive and handles edge cases naturally
5. We restart comparison from beginning when prefix is reduced (ensures correctness)

ALTERNATIVE APPROACHES NOT USED:
- Vertical scanning: Would compare character by character across all strings
- Divide and conquer: More complex, no significant benefit for this problem
- Trie-based: Overkill for simple prefix finding

ALGORITHM:
1. Find the shortest string in the array (potential longest prefix)
2. Use this shortest string as initial prefix candidate
3. Iterate through all strings in the array:
   a. Check if current prefix matches the beginning of current string
   b. If yes, move to next string
   c. If no:
      - Remove last character from prefix
      - Restart from first string (reset i to 0)
   d. If prefix becomes empty, no common prefix exists
4. Return the final prefix

TIME COMPLEXITY: O(n * m²) where:
- n is the number of strings
- m is the length of shortest string
- In worst case, we might reduce prefix by 1 char and restart n times
- Each restart scans through strings: O(n * m) for each of m reductions

SPACE COMPLEXITY: O(m)
- Storing the prefix string of length up to m
- No additional data structures used

EDGE CASES:
1. Empty array: Returns ""
2. Array with one string: Returns that string
3. No common prefix: Returns ""
4. All strings identical: Returns the entire string
5. One empty string in array: Returns "" (empty string has no prefix)

EXAMPLES:
Input: ["flower", "flow", "flight"]
Output: "fl"

Input: ["dog", "racecar", "car"]
Output: "" (no common prefix)

Input: ["interspecies", "interstellar", "interstate"]
Output: "inters"
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        Find longest common prefix using iterative reduction approach

        Args:
            strs: List of strings

        Returns:
            Longest common prefix string, or "" if none exists
        """
        # Step 1: Find the shortest string (maximum possible prefix length)
        sl = float('inf')  # Initialize with infinity
        prefix = ""

        for string in strs:
            if len(string) < sl:
                sl = len(string)
                prefix = string[:len(string)]  # Use shortest string as initial candidate

        # Step 2: Iteratively check and reduce prefix until it matches all strings
        i = 0
        while i < len(strs):
            # Early exit: if prefix is reduced to empty, no common prefix exists
            if prefix == "":
                break

            # Check if current prefix matches the beginning of strs[i]
            if prefix != strs[i][:len(prefix)]:
                # Mismatch found: reduce prefix by removing last character
                prefix = prefix[:len(prefix) - 1]
                # Restart comparison from first string with new reduced prefix
                i = 0
            else:
                # Match found: move to next string
                i += 1

        return prefix