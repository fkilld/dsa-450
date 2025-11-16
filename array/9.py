"""
PROBLEM: Minimum Number of Jumps
==================================
Given an array where each element represents the maximum number of steps that can be made
forward from that element. Find the minimum number of jumps to reach the end of the array.

Example:
    Input:  arr = [2, 3, 1, 1, 4]
    Output: 2
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

    Input:  arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    Output: 3
    Explanation: First jump from 0 to 1, second jump from 1 to 4, third jump from 4 to end.

APPROACH: Greedy Algorithm with Range Tracking
===============================================
WHY THIS APPROACH?
- We use a greedy approach to always extend our reachable range as far as possible
- We track the current "ladder" (steps remaining) and the maximum reach from current range
- When we exhaust current ladder, we take a jump to extend to new maximum reach
- This ensures we use minimum jumps by always choosing the farthest reachable position

KEY VARIABLES:
- mr (max_reach): The farthest index we can reach from current range
- step: Remaining steps in current ladder before we need to take next jump
- jumps: Total number of jumps taken so far

HOW IT WORKS:
1. Initialize: mr = arr[0], step = arr[0], jumps = 1
2. For each position, update max_reach = max(mr, arr[i] + i)
3. Decrease step by 1 for each move
4. When step becomes 0, we need a new jump:
   - If we can't reach beyond current position (i >= mr), return -1
   - Otherwise, jump and set step = mr - i

FLOW EXAMPLE:
=============
Array: [2, 3, 1, 1, 4]
Goal: Reach index 4 (last index)

Initial state:
    mr = arr[0] = 2 (can reach up to index 2)
    step = 2 (can take 2 steps before needing jump)
    jumps = 1 (started with one jump from index 0)

i=1: arr[1]=3
    mr = max(2, 3+1) = 4 (can now reach index 4!)
    step = 2-1 = 1 (one step remaining)

i=2: arr[2]=1
    mr = max(4, 1+2) = 4 (still can reach index 4)
    step = 1-1 = 0 (no steps remaining)

    step == 0, so we need a jump:
    jumps = 2 (took second jump)
    step = mr - i = 4 - 2 = 2 (new ladder has 2 steps)

i=3: arr[3]=1
    mr = max(4, 1+3) = 4
    step = 2-1 = 1

i=4: Reached end!
    Return jumps = 2

EDGE CASES:
- Array length 1: Already at end, return 0
- First element is 0: Cannot move, return -1
- At any point if i >= mr: Cannot proceed, return -1

TIME COMPLEXITY:  O(n) - Single pass through array
SPACE COMPLEXITY: O(1) - Only using a few variables
"""

class Solution:
    def minJumps(self, arr, n):
        """
        Find minimum number of jumps to reach the end of array.

        Args:
            arr: Array where arr[i] represents max steps from index i
            n: Length of the array

        Returns:
            Minimum number of jumps, or -1 if end cannot be reached
        """
        # Edge case: Already at the end
        if n == 1:
            return 0

        # Edge case: Cannot move from start
        elif arr[0] == 0:
            return -1

        else:
            # mr: Maximum reach - farthest index we can reach from current range
            mr = arr[0]

            # step: Steps remaining in current "ladder" before we need to jump
            step = arr[0]

            # jumps: Number of jumps taken (starting with 1 from index 0)
            jumps = 1

            # Traverse the array starting from index 1
            for i in range(1, n):
                # If we've reached the last index, return the jump count
                if i == n - 1:
                    return jumps

                # Update the maximum reach from current position
                # arr[i] + i = farthest index we can reach if we jump from position i
                mr = max(mr, arr[i] + i)

                # We use one step to move to the next position
                step -= 1

                # If no more steps remaining in current ladder
                if step == 0:
                    # We need to take a jump
                    jumps += 1

                    # Check if we can't move forward (stuck)
                    if i >= mr:
                        return -1

                    # Calculate new ladder size: distance from current to max reach
                    step = mr - i

