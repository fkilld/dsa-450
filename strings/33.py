"""
Rearrange Characters So No Two Adjacent Characters Are Same

PROBLEM DESCRIPTION:
Given a string with repeated characters, rearrange the string such that no two
adjacent characters are the same. If such arrangement is possible, return the
rearranged string, otherwise return "-1".

Example: "aaab" -> "abaa" or "aaba" (valid)
Example: "aaabb" -> "ababa" (valid)
Example: "aaaa" -> "-1" (impossible - too many 'a's)

WHY THIS APPROACH (Greedy Frequency-Based):
We use a GREEDY approach placing the most frequent character first because:
1. The most frequent character is the bottleneck - if we can't place it, solution is impossible
2. Mathematical constraint: max_frequency <= (n - max_frequency + 1)
   - We need enough "gaps" between max_char occurrences for other characters
   - If max_freq = 4, n = 6: we need at least 4-1 = 3 gaps, which requires 3 other chars
3. By placing max_char at all even positions first (0, 2, 4, ...), we guarantee separation
4. Then fill remaining characters in remaining positions (even, then odd)
5. This greedy strategy works because if max_char fits, all others will definitely fit

ALGORITHM:
Step 1: Count Character Frequencies
   - Build frequency map for all characters
   - Find the character with maximum frequency (max_char, max_freq)

Step 2: Check Feasibility
   - Constraint: max_freq <= n - max_freq + 1
   - Equivalently: max_freq <= ceil(n/2)
   - If violated, return "-1" (impossible to arrange)

Step 3: Place Maximum Frequency Character
   - Create result array of size n
   - Start at index 0 (even positions)
   - Place all occurrences of max_char at positions 0, 2, 4, 6, ...
   - Set freq[max_char] = 0 (fully placed)

Step 4: Place Remaining Characters
   - For each remaining character in frequency map:
     - While its frequency > 0:
       - If index >= n, reset to index = 1 (switch to odd positions)
       - Place character at current index
       - Move index by 2 (index += 2)
       - Decrement frequency

Step 5: Return Result
   - Convert result array to string and return

EDGE CASES:
1. Impossible arrangement: "aaaa" -> max_freq (4) > n - max_freq + 1 (1)
2. All characters distinct: "abc" -> already valid, any arrangement works
3. Two-character string with same chars: "aa" -> impossible
4. Two-character string with diff chars: "ab" -> valid
5. Empty string -> return ""

TIME COMPLEXITY: O(n)
- Step 1: Count frequencies -> O(n)
- Step 2: Find max frequency -> O(k) where k = distinct chars <= n
- Step 3: Place max_char -> O(max_freq) <= O(n)
- Step 4: Place other chars -> O(n - max_freq) <= O(n)
- Overall: O(n)

SPACE COMPLEXITY: O(n)
- Frequency map: O(k) where k = distinct chars <= n
- Result array: O(n)
- Overall: O(n)

EXAMPLE WALKTHROUGH:
Input: "aaabb"
Step 1: freq = {'a': 3, 'b': 2}, max_char = 'a', max_freq = 3
Step 2: Check: 3 <= 5 - 3 + 1 = 3 ✓ (feasible)
Step 3: Place 'a' at even positions
   idx=0: [a, _, _, _, _]
   idx=2: [a, _, a, _, _]
   idx=4: [a, _, a, _, a]
Step 4: Place 'b' (freq=2), continue from idx=6
   idx=6 >= 5, reset idx=1
   idx=1: [a, b, a, _, a]
   idx=3: [a, b, a, b, a]
Output: "ababa"

MATHEMATICAL PROOF OF FEASIBILITY:
For max_freq to be placeable:
- We need (max_freq - 1) gaps between max_freq occurrences
- These gaps must accommodate (n - max_freq) other characters
- Minimum requirement: max_freq - 1 <= n - max_freq
- Rearranging: max_freq <= n - max_freq + 1
- Equivalently: 2*max_freq <= n + 1, or max_freq <= ceil(n/2)
"""

# Rearrange characters
# question link => https://practice.geeksforgeeks.org/problems/rearrange-characters4649/1/

class Solution:
    def rearrangeString(self, string):
            n = len(string)

            # Step 1: Calculate frequency of each character
            freq = {}
            for char in string:
                if char not in freq:
                    freq[char] = 1
                else:
                    freq[char] += 1

            # Step 2: Find the character with maximum frequency
            max_freq = -1  # Frequency count of most common character
            max_char = ''  # The most common character itself
            for char in freq:
                if freq[char] > max_freq:
                    max_freq = freq[char]
                    max_char = char

            # Step 3: Check feasibility - can we place max_char without adjacency?
            # Mathematical constraint: max_freq must not exceed available "slots"
            # We need (max_freq - 1) gaps, which requires at least (max_freq - 1) other chars
            # Therefore: max_freq <= n - max_freq + 1
            if not max_freq <= n - max_freq + 1:
                return "-1"  # Impossible to rearrange

            # Step 4: Create result array and place max_char at even positions
            res = [''] * n
            idx = 0  # Current index for placement (starts at even positions)

            # Place all occurrences of max_char first to ensure they're separated
            while max_freq != 0:
                res[idx] = max_char
                idx += 2  # Move to next even position (0, 2, 4, 6, ...)
                max_freq -= 1

            freq[max_char] = 0  # Mark max_char as fully placed

            # Step 5: Place all remaining characters
            for char in freq:
                while freq[char] > 0:
                    # If we've filled all even positions, switch to odd positions
                    if idx >= n:
                        idx = 1  # Start filling odd positions (1, 3, 5, 7, ...)

                    res[idx] = char
                    idx += 2  # Move to next position (either even or odd series)
                    freq[char] -= 1

            return ''.join(res)

# print(rearrangeString("kkk"))