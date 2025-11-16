"""
Minimum Swaps for Bracket Balancing

PROBLEM:
Given a string with equal number of '[' and ']' brackets (but not necessarily balanced),
find the minimum number of swaps needed to make the bracket sequence balanced.
A balanced sequence has every opening bracket '[' matched with a closing bracket ']'
that comes after it.

For example: "[][[]]" is balanced, but "][" is not.

WHY THIS APPROACH:
Two methods are provided:

Method 1 (minimumNumberOfSwaps): Uses Position Tracking with O(n) extra space
- We track positions of all '[' brackets to know where to swap from
- When we encounter unbalanced ']', we know exactly which '[' to swap with
- This makes the logic clear and easy to understand

Method 2 (min_swaps): Space-Optimized Counter Approach with O(1) extra space
- Instead of storing positions, we just count open/close brackets
- Track "fault" (excess closing brackets that need fixing)
- When we find an opening bracket, we can fix pending faults
- More space-efficient but same time complexity

Both methods achieve O(n) time complexity.

ALGORITHM:

Method 1 - Position Tracking (minimumNumberOfSwaps):
1. Preprocess: Store positions of all '[' brackets in a list
2. Iterate through string with index idx pointing to next available '['
3. Maintain count: increment for '[', decrement for ']'
4. When count goes negative (too many ']'):
   - Swap current ']' with the '[' at pos[idx]
   - Add distance to answer (pos[idx] - current_position)
   - Reset count to 1 (we now have one open bracket)
   - Increment idx
5. Return total swaps

Method 2 - Counter Approach (min_swaps):
1. Track open_br (count of '['), close_br (count of ']'), fault (excess ']')
2. For each character:
   - If ']': increment close_br, update fault = close_br - open_br
   - If '[': increment open_br, reduce fault if any exists
3. Each time we see '[' with fault > 0, we fix one unbalanced ']'
4. Add fault to answer (number of fixes), then decrement fault
5. Return total swaps

TIME COMPLEXITY: O(n) for both methods
- Single pass through the string
- Constant time operations per character

SPACE COMPLEXITY:
- Method 1: O(n) for storing positions of '[' brackets
- Method 2: O(1) only using counters

EDGE CASES:
1. Already balanced: Returns 0
2. Completely reversed "]][[": Returns n/2 swaps
3. Single pair "][": Returns 1
4. Empty string: Returns 0

EXAMPLES:
Input: "[][["
Output: 2
Explanation: Swap positions to get "[[]][]"

Input: "]]][[["
Output: 3 (need to swap all closing brackets with opening ones)

Input: "[]][]["
Unbalanced ']' at index 2, 4
Output: 2

WHY TWO METHODS:
- Method 1 is more intuitive and easier to understand
- Method 2 is more space-efficient (better for large inputs)
- Both demonstrate different problem-solving approaches
"""

class Solution:
    def minimumNumberOfSwaps(self, s):
        """
        Method 1: Find minimum swaps using position tracking
        Tracks exact positions of '[' brackets for precise swapping

        Args:
            s: String with equal number of '[' and ']' brackets

        Returns:
            Minimum number of swaps needed to balance the brackets
        """
        # Step 1: Preprocess - store positions of all '[' brackets
        pos = []
        for i in range(len(s)):
            if s[i] == '[':
                pos.append(i)

        # Step 2: Process string and perform swaps
        idx = 0      # Points to next available '[' position in pos list
        ans = 0      # Total number of swaps needed
        count = 0    # Balance counter: +1 for '[', -1 for ']'
        s = list(s)  # Convert to list for in-place character swapping

        for i in range(len(s)):
            if s[i] == '[':
                count += 1  # Found opening bracket, increase balance
                idx += 1    # Move to next '[' position
            else:
                count -= 1  # Found closing bracket, decrease balance

                # Imbalance detected: more ']' than '[' so far
                if count < 0:
                    # Calculate swap distance: how far is the next '['
                    ans += pos[idx] - i

                    # Swap current ']' with next available '['
                    s[i], s[pos[idx]] = s[pos[idx]], s[i]

                    # After swap, we have '[' at current position
                    count = 1
                    idx += 1

        return ans

    def min_swaps(self, s):
        """
        Method 2: Find minimum swaps using space-optimized counter approach
        Uses O(1) space by tracking counts instead of positions

        Args:
            s: String with equal number of '[' and ']' brackets

        Returns:
            Minimum number of swaps needed to balance the brackets
        """
        open_br = 0   # Count of '[' brackets seen so far
        close_br = 0  # Count of ']' brackets seen so far
        fault = 0     # Number of excess ']' brackets (need fixing)
        ans = 0       # Total swaps needed

        for i in range(len(s)):
            if s[i] == ']':
                close_br += 1
                # Calculate imbalance: if close_br > open_br, we have excess ']'
                fault = close_br - open_br
            else:
                # Found an opening bracket '['
                open_br += 1

                # If there are unbalanced ']' brackets, this '[' can fix them
                if fault > 0:
                    # Add the number of positions we need to swap backwards
                    ans += fault
                    # One fault is now fixed by this '['
                    fault -= 1

        return ans
