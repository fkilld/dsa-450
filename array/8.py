"""
PROBLEM: Minimize the Heights II
==================================
Given an array arr[] denoting heights of N towers and a positive integer K,
you have to modify the height of each tower either by increasing or decreasing them by K only once.
After modifying, height should be a non-negative integer.
Find out what could be the possible minimum difference of the height of shortest
and longest towers after you have modified each tower.

Example:
    Input:  arr = [1, 5, 8, 10], k = 2
    Output: 5
    Explanation: Heights can become [3, 3, 6, 8] or [3, 7, 6, 8] etc.
                 Difference is 8-3 = 5 (minimum possible)

    Input:  arr = [3, 9, 12, 16, 20], k = 3
    Output: 11
    Explanation: Heights become [6, 6, 9, 13, 17]
                 Difference is 17-6 = 11

APPROACH: Sliding Window with All Possible Heights
====================================================
WHY THIS APPROACH?
- Each tower can be either increased by K or decreased by K (2 choices per tower)
- Brute force would be O(2^n) to try all combinations
- Key insight: We don't need to try all combinations, just find the smallest range
  that covers at least one variation of each tower
- We create a list of all possible heights (variations) and use sliding window
  to find the minimum range that includes all towers

HOW IT WORKS:
1. Generate all possible heights: For each tower, add both (height-k) and (height+k) if valid
2. Sort all variations by height value
3. Use sliding window to find smallest range containing at least one variation of each tower
4. Track which towers are included using a visited frequency array
5. The minimum range difference is our answer

FLOW EXAMPLE:
=============
Array: [1, 5, 8, 10], k = 2
Goal: Minimize (max_height - min_height) after modifications

Step 1: Generate all possible variations
    Tower 0 (height=1): Can't decrease (1-2=-1 invalid), can increase to 3
        Variations: [3, 0]
    Tower 1 (height=5): Can decrease to 3, can increase to 7
        Variations: [3, 1], [7, 1]
    Tower 2 (height=8): Can decrease to 6, can increase to 10
        Variations: [6, 2], [10, 2]
    Tower 3 (height=10): Can decrease to 8, can increase to 12
        Variations: [8, 3], [12, 3]

    All variations (unsorted): [[3,0], [3,1], [7,1], [6,2], [10,2], [8,3], [12,3]]

Step 2: Sort by height
    v = [[3,0], [3,1], [6,2], [7,1], [8,3], [10,2], [12,3]]

Step 3: Find minimum window containing all 4 towers (0,1,2,3)
    Initial window expansion:
    right=0: [3,0] → vis=[1,0,0,0], ele=1
    right=1: [3,1] → vis=[1,1,0,0], ele=2
    right=2: [6,2] → vis=[1,1,1,0], ele=3
    right=3: [7,1] → vis=[1,2,1,0], ele=3
    right=4: [8,3] → vis=[1,2,1,1], ele=4 (all towers covered!)

    Window [0,4]: Heights [3,3,6,7,8] → diff = 8-3 = 5

Step 4: Try to shrink window from left
    Remove left=0: [3,0] → vis=[0,2,1,1], ele=3 (still all 4)
    Remove left=1: [3,1] → vis=[0,1,1,1], ele=4 (still all 4)
    Window [2,4]: Heights [6,7,8] → diff = 8-6 = 2? NO! Missing tower 0!

    Actually after removing [3,0]: vis=[0,2,1,1], we need to expand right again
    right=5: [10,2] → vis=[0,2,2,1], ele=3 (missing tower 0)
    right=6: [12,3] → vis=[0,2,2,2], ele=3 (missing tower 0)

    Cannot find valid window anymore

Final: Minimum difference = 5

KEY INSIGHT:
We need to find the smallest range [min_height, max_height] such that for each tower,
at least one of its variations (original+k or original-k) falls within this range.

TIME COMPLEXITY:  O(n log n) - Sorting dominates (n variations to sort)
SPACE COMPLEXITY: O(n) - Storing all variations in list v
"""

class Solution:
    def get_min_diff(self, arr, n, k):
        """
        Minimize difference between max and min tower heights after modifications.

        Args:
            arr: Array of tower heights
            n: Number of towers
            k: Value to increase or decrease each tower

        Returns:
            Minimum possible difference between tallest and shortest tower
        """
        # v stores all possible height variations as [height, tower_index]
        v = []

        # vis[i] tracks how many times tower i appears in current window
        vis = [0] * n

        # Generate all possible height variations for each tower
        for i in range(n):
            # Add decreased height only if it stays non-negative
            if arr[i] - k >= 0:
                v.append([arr[i] - k, i])  # Negative variation
            # Always add increased height
            v.append([arr[i] + k, i])  # Positive variation

        # Sort variations by height (ascending order)
        # This allows us to use sliding window technique
        v.sort()

        # ele: Number of distinct towers covered in current window
        ele = 0
        # left, right: Window boundaries
        left = 0
        right = 0

        # Expand window from right until all n towers are covered
        # A tower is "covered" if at least one of its variations is in the window
        while ele < n and right < len(v):
            # If this tower appears for the first time in window
            if vis[v[right][1]] == 0:
                ele += 1  # Increment count of distinct towers

            # Increment frequency of this tower in current window
            vis[v[right][1]] += 1
            # Move right pointer to expand window
            right += 1

        # Calculate initial answer: difference between max and min heights in window
        # right-1 because we incremented right after including the element
        ans = v[right - 1][0] - v[left][0]

        # Try to find smaller windows by sliding
        while right < len(v):
            # Try to shrink window from left
            # If left tower appears only once, removing it will uncovered that tower
            if vis[v[left][1]] == 1:
                ele -= 1  # One tower will be uncovered

            # Decrease frequency of left tower
            vis[v[left][1]] -= 1
            # Move left pointer to shrink window
            left += 1

            # Expand window from right until all n towers are covered again
            while ele < n and right < len(v):
                if vis[v[right][1]] == 0:
                    ele += 1
                vis[v[right][1]] += 1
                right += 1

            # If we successfully covered all n towers
            if ele == n:
                # Update answer with minimum difference
                ans = min(ans, v[right - 1][0] - v[left][0])
            else:
                # Cannot cover all towers anymore, break
                break

        return ans

        


