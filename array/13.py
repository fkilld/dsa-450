"""
PROBLEM: Merge Overlapping Intervals
======================================
Given an array of intervals where intervals[i] = [start_i, end_i],
merge all overlapping intervals, and return an array of the non-overlapping
intervals that cover all the intervals in the input.

Two intervals [a, b] and [c, d] overlap if b >= c (assuming a <= c after sorting).

Example:
    Input:  [[1,3], [2,6], [8,10], [15,18]]
    Output: [[1,6], [8,10], [15,18]]
    Explanation: [1,3] and [2,6] overlap → merge to [1,6]

    Input:  [[1,4], [4,5]]
    Output: [[1,5]]
    Explanation: [1,4] and [4,5] overlap at point 4

    Input:  [[1,4], [0,4]]
    Output: [[0,4]]
    Explanation: After sorting: [0,4] and [1,4] overlap

APPROACH: Sort and Merge
==========================
WHY THIS APPROACH?
- Overlapping intervals are easier to detect when sorted by start time
- After sorting, we only need to compare each interval with the last merged interval
- We can merge in-place by keeping track of the last merged position
- Single pass after sorting: O(n log n) time, O(1) extra space

HOW IT WORKS:
1. Sort intervals by start time
2. Keep track of the last merged interval's position (idx)
3. For each subsequent interval:
   - If it overlaps with last merged interval → extend the end time
   - If it doesn't overlap → move to next position and store new interval
4. Return the merged intervals (from index 0 to idx)

OVERLAP CONDITION:
Two intervals [a, b] and [c, d] overlap if:
- After sorting by start: a <= c (guaranteed)
- And b >= c (end of first interval >= start of second interval)

FLOW EXAMPLE:
=============
Input: [[1,3], [2,6], [8,10], [15,18]]

Step 1: Sort by start time
    Already sorted: [[1,3], [2,6], [8,10], [15,18]]
    idx = 0 (points to first interval)

Step 2: Process interval [2,6] at i=1
    Check overlap: arr[idx][1]=3 >= arr[i][0]=2?
        Yes, 3 >= 2 → Intervals overlap!

    Merge: arr[idx][1] = max(3, 6) = 6
    Now: [[1,6], [2,6], [8,10], [15,18]]
          ^idx=0

    Visualization:
        [1,3]  : |------|
        [2,6]  :     |---------|
        Merged : |------------|
                 [1,6]

Step 3: Process interval [8,10] at i=2
    Check overlap: arr[idx][1]=6 >= arr[i][0]=8?
        No, 6 < 8 → No overlap

    Move to next position: idx = 1
    Copy interval: arr[1] = [8,10]
    Now: [[1,6], [8,10], [8,10], [15,18]]
                  ^idx=1

    Visualization:
        [1,6]  : |------|
        [8,10] :           |---|
        (No overlap, separate intervals)

Step 4: Process interval [15,18] at i=3
    Check overlap: arr[idx][1]=10 >= arr[i][0]=15?
        No, 10 < 15 → No overlap

    Move to next position: idx = 2
    Copy interval: arr[2] = [15,18]
    Now: [[1,6], [8,10], [15,18], [15,18]]
                          ^idx=2

Step 5: Return merged intervals
    Return arr[:idx+1] = arr[:3] = [[1,6], [8,10], [15,18]]

EXAMPLE 2 - Complete Overlap:
Input: [[1,4], [2,3]]

Step 1: Sort → [[1,4], [2,3]]
Step 2: Compare [2,3] with [1,4]:
    4 >= 2? Yes → Overlap
    Merge: max(4, 3) = 4
    Result: [[1,4]]

    Visualization:
        [1,4]: |--------|
        [2,3]:   |---|
        [2,3] is completely inside [1,4]

EDGE CASES:
- Empty array: Return []
- Single interval: Return as is
- No overlaps: Return all intervals
- All overlap: Return single merged interval

TIME COMPLEXITY:  O(n log n) - Sorting dominates
SPACE COMPLEXITY: O(1) - In-place merging (excluding output space)
"""

class Solution:
    def merge(self, arr):
        """
        Merge all overlapping intervals.

        Args:
            arr: List of intervals, where each interval is [start, end]

        Returns:
            List of merged non-overlapping intervals
        """
        # Edge case: empty or single interval
        if not arr or len(arr) <= 1:
            return arr

        # Sort intervals by start time
        # This ensures we can merge in a single pass from left to right
        # After sorting, if interval i overlaps with i+1, they will be adjacent
        arr.sort()

        # idx tracks the position of the last merged interval
        # We build the result in-place in the same array
        idx = 0

        # Iterate through remaining intervals starting from index 1
        for i in range(1, len(arr)):
            # Check if current interval overlaps with last merged interval
            # Overlap condition: end of last merged >= start of current
            if arr[idx][1] >= arr[i][0]:
                # Intervals overlap - merge them
                # Update the end time to be the maximum of both intervals
                # We take max because current interval might be completely contained
                # Example: [1,6] and [2,4] → merged end = max(6,4) = 6
                arr[idx][1] = max(arr[idx][1], arr[i][1])
            else:
                # No overlap - this is a separate interval
                # Move idx to next position to store this new interval
                idx += 1
                # Copy current interval to the new position
                arr[idx] = arr[i]

        # Return only the merged intervals (from 0 to idx inclusive)
        # We slice the array because we merged in-place and idx points to last valid interval
        return arr[:idx + 1]