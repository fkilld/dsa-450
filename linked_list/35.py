"""
================================================================================
PROBLEM: First Non-Repeating Character in a Stream
================================================================================

DESCRIPTION:
Given a stream of characters (arriving one at a time), find the first
non-repeating character at each step. If no non-repeating character exists
at that step, return '#'.

Input:  Stream = "aabcc"
Step 1: 'a' arrives → first non-repeating = 'a'
Step 2: 'a' arrives → first non-repeating = 'a' (still appears once relatively)
Step 3: 'b' arrives → first non-repeating = 'b' (now 'a' appears twice)
Step 4: 'c' arrives → first non-repeating = 'b'
Step 5: 'c' arrives → first non-repeating = 'b'
Output: "aabbb"

Input:  Stream = "aabc"
Step 1: 'a' → 'a'
Step 2: 'a' → '#' (no non-repeating)
Step 3: 'b' → 'b'
Step 4: 'c' → 'b'
Output: "a#bb"

Note: Only lowercase alphabets (a-z) are present in the stream.

================================================================================
APPROACH & REASONING:
================================================================================

APPROACH: Frequency Array + Queue/List for Order

Key Insight:
- We need to track frequency of each character (to know if it's repeating)
- We also need to maintain order of first occurrence (to find FIRST non-repeating)
- Combine frequency counting with ordered tracking

Algorithm Steps:
1. Use frequency array (size 26) to count occurrences of each character
2. Use a list/queue to maintain order of characters as they arrive
3. For each new character:
   a. Add to list if it's first occurrence
   b. Increment frequency
   c. Scan the ordered list to find first character with frequency = 1
   d. If found, append it to result; otherwise append '#'

Time Complexity: O(n * 26) = O(n) where n is stream length
   - For each character, we scan at most 26 characters in the list
Space Complexity: O(26) = O(1) for frequency array + O(26) for queue = O(1)

Why this works:
- Frequency array tracks how many times each character appeared
- Ordered list tracks the sequence of unique characters
- First character in ordered list with frequency = 1 is our answer
- This simulates a stream processing scenario

Note on Linked List Connection:
- This problem is often solved using a doubly linked list + hash map
- The list maintains order, and we can remove repeated characters efficiently
- Current solution uses a simpler list but same concept

================================================================================
FLOWCHART:
================================================================================

    FirstNonRepeating(stream)
              |
              v
    Initialize:
    vis = [0]*26 (frequency)
    v = [] (ordered list)
    ans = ""
              |
              v
    For each character in stream
              |
              v
    +-------------------------+
    | i < len(stream)?        |-----> NO ----> return ans
    +-------------------------+
              |
             YES
              |
              v
    Get char = stream[i]
              |
              v
    +-----------------------+
    | First occurrence?     |
    | vis[char] == 0?       |
    +-----------------------+
              |        |
             YES      NO
              |        |
              v        |
         Add char      |
         to v list     |
              |        |
              +---+----+
                  |
                  v
         Increment frequency:
         vis[char] += 1
                  |
                  v
         Scan ordered list v
         to find first char
         with frequency == 1
                  |
         +--------+--------+
         |                 |
       Found            Not found
         |                 |
         v                 v
    ans += char       ans += '#'
         |                 |
         +--------+--------+
                  |
                  v
            Next iteration


    VISUAL EXAMPLE:

    Stream: "aabcc"

    Step 1: 'a' arrives
    vis: [1, 0, 0, ...]
    v: ['a']
    First non-repeat: 'a' → ans = "a"

    Step 2: 'a' arrives
    vis: [2, 0, 0, ...]
    v: ['a']  (already in list)
    First non-repeat: none (freq[a]=2) → ans = "a#"

    Step 3: 'b' arrives
    vis: [2, 1, 0, ...]
    v: ['a', 'b']
    First non-repeat: 'b' (freq[b]=1) → ans = "a#b"

    Step 4: 'c' arrives
    vis: [2, 1, 1, ...]
    v: ['a', 'b', 'c']
    First non-repeat: 'b' → ans = "a#bb"

    Step 5: 'c' arrives
    vis: [2, 1, 2, ...]
    v: ['a', 'b', 'c']
    First non-repeat: 'b' → ans = "a#bbb"

================================================================================
"""

class Solution:
    """
    Solution class to find first non-repeating character in a stream.
    """

    def FirstNonRepeating(self, a):
        """
        Find first non-repeating character at each step of the stream.

        Args:
            a: String representing the stream of characters

        Returns:
            String where each character represents the first non-repeating
            character at that step, or '#' if none exists

        Algorithm:
        1. Maintain frequency array for all 26 lowercase letters
        2. Maintain ordered list of unique characters seen so far
        3. For each new character:
           - Add to list if first occurrence
           - Update frequency
           - Find first character in list with frequency 1
           - Append result (character or '#') to answer

        Time Complexity: O(n * 26) = O(n) where n is length of stream
        Space Complexity: O(26) = O(1) for frequency + ordered list

        Example:
            Input:  "aabcc"
            Output: "a#bbb"
        """
        # Frequency counter for all 26 lowercase letters (a-z)
        vis = [0] * 26

        # List to maintain order of unique characters as they appear
        # This preserves the "first occurrence" order
        v = []

        # Result string to build answer character by character
        ans = ""

        # Process each character in the stream
        for i in range(len(a)):
            # Get current character
            char = a[i]

            # Check if this is the first occurrence of this character
            # Calculate index: 'a'->0, 'b'->1, ..., 'z'->25
            char_index = ord(char) - ord('a')

            if vis[char_index] == 0:
                # First occurrence: add to ordered list
                v.append(char)

            # Increment frequency count for this character
            vis[char_index] += 1

            # FIND FIRST NON-REPEATING CHARACTER
            # Scan through ordered list to find first char with frequency = 1
            f = 0  # Flag to track if we found a non-repeating character
            m = len(v)  # Current size of ordered list

            for j in range(m):
                # Get character at position j in ordered list
                current_char = v[j]
                current_index = ord(current_char) - ord('a')

                # Check if this character has appeared exactly once
                if vis[current_index] == 1:
                    # Found first non-repeating character
                    ans += current_char
                    f = 1
                    break

            # If no non-repeating character found, append '#'
            if f == 0:
                ans += "#"

        return ans


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - What characters are in the stream? (Usually lowercase a-z only)
   - What should we return if no non-repeating character exists? (Usually '#')
   - Should we return result for each step or just the final state? (Each step)
   - Can the stream be empty? (Yes, return empty string)
   - Is the stream given all at once or one character at a time? (All at once)

2. Edge Cases to Consider:
   - Empty stream (return "")
   - Single character (return that character)
   - All same characters "aaaa" (return "a###")
   - All unique characters "abcd" (return "aaaa" then "abbb" then "abcc" then "abcd")
   - Stream with all characters repeating exactly twice

3. Common Mistakes to Avoid:
   - Not maintaining order of first occurrence
   - Recalculating from scratch at each step (inefficient)
   - Confusing "first non-repeating" with "most recent non-repeating"
   - Not handling the '#' case properly
   - Off-by-one errors in frequency counting

4. Alternative Approaches:

   a) Using Queue + Hash Map (More Optimal):
      - Use queue to maintain non-repeating characters
      - Use hash map for frequency
      - Remove from queue when character becomes repeating
      - Time: O(n), Space: O(26) = O(1)

      from collections import deque, defaultdict

      def FirstNonRepeating_Optimal(self, stream):
          freq = defaultdict(int)
          queue = deque()
          result = ""

          for char in stream:
              freq[char] += 1
              if freq[char] == 1:
                  queue.append(char)

              # Remove repeating characters from front
              while queue and freq[queue[0]] > 1:
                  queue.popleft()

              result += queue[0] if queue else '#'

          return result

   b) Doubly Linked List + Hash Map:
      - Most optimal for very large streams
      - O(1) removal of repeating characters
      - More complex implementation

5. Follow-up Questions You Might Get:
   - Can you optimize to O(n) time per character?
     (Yes, use queue and remove repeating characters)
   - What if we need the kth non-repeating character?
     (Extend to track multiple positions)
   - How would you handle very large streams?
     (Use doubly linked list for O(1) operations)
   - What if characters can repeat more than twice?
     (Same approach works, frequency > 1 means repeating)

6. Why This Problem is in Linked List Section:
   - Optimal solution uses linked list (queue/deque)
   - Demonstrates maintaining order with efficient removal
   - Tests understanding of stream processing
   - Common interview problem combining multiple data structures

7. Time to Solve: Aim for 15-20 minutes including optimization discussion

8. Key Insights for Interview:
   - Stream processing requires incremental updates
   - Frequency tracking + order maintenance is the pattern
   - Trade-off: simple list vs queue with cleanup
   - This tests multiple concepts: arrays, queues, and hash maps

9. Optimization Comparison:
   Current Solution:
   - Time per step: O(26) = O(1)
   - Total time: O(n)
   - Simple to understand and implement

   Queue-based Solution:
   - Time per step: Amortized O(1)
   - Total time: O(n)
   - More optimal but slightly complex

10. Related Problems:
    - First unique character in a string (static version)
    - Sliding window with unique characters
    - LRU Cache (similar order maintenance concept)
    - Stream median (heap-based)

================================================================================
"""