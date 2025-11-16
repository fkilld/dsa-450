"""
PROBLEM: Minimum Swaps to Bring Elements <= K Together
========================================================
Given an array of n positive integers and a number k, find the minimum number of swaps
required to bring all the numbers less than or equal to k together.

Example:
    Input:  arr = [2, 1, 5, 6, 3], k = 3
    Output: 1
    Explanation:
        Elements <= 3: [2, 1, 3] (total count = 3)
        To bring them together, we need a window of size 3
        Best window: [2, 1, 5] → swap 5 with 3 → [2, 1, 3] (1 swap)

    Input:  arr = [2, 7, 9, 5, 8, 7, 4], k = 5
    Output: 2
    Explanation:
        Elements <= 5: [2, 5, 4] (total count = 3)
        Best window of size 3: [9, 5, 8] has 2 "bad" elements (9, 8)
        Need 2 swaps to replace them with 2 and 4

APPROACH: Sliding Window Technique
====================================
WHY THIS APPROACH?
- We need to find a contiguous subarray where all elements <= k can fit
- The size of this window = count of elements <= k in entire array
- We slide this window across the array to find the position with minimum "bad" elements
- "Bad" elements are those > k inside our window (need to be swapped out)
- Minimum bad elements = minimum swaps needed

KEY INSIGHT:
If there are 'count' elements <= k in the array, we need a contiguous window of
size 'count' to bring them all together. We find which window position requires
the fewest swaps.

HOW IT WORKS:
1. Count total elements <= k (this is our window size)
2. In the first window of this size, count "bad" elements (elements > k)
3. Slide the window across array:
   - Remove contribution of leftmost element leaving the window
   - Add contribution of rightmost element entering the window
   - Track minimum bad elements across all windows
4. Return minimum bad elements (each needs one swap)

FLOW EXAMPLE:
=============
Array: [2, 1, 5, 6, 3]
k = 3
Goal: Bring all elements <= 3 together with minimum swaps

Step 1: Count elements <= k
    2 <= 3? Yes (count = 1)
    1 <= 3? Yes (count = 2)
    5 <= 3? No
    6 <= 3? No
    3 <= 3? Yes (count = 3)

    Total count = 3 (elements: 2, 1, 3)
    Window size = 3

Step 2: Count "bad" elements in first window [2, 1, 5]
    2 <= 3? Yes (good)
    1 <= 3? Yes (good)
    5 <= 3? No (bad!)

    bad = 1
    min_swaps = 1

Step 3: Slide window to [1, 5, 6] (indices 1-3)
    Remove: arr[0]=2 (was good, no change to bad count)
    Add: arr[3]=6 > 3 (bad!)

    bad = 1 - 0 + 1 = 2
    min_swaps = min(1, 2) = 1

Step 4: Slide window to [5, 6, 3] (indices 2-4)
    Remove: arr[1]=1 (was good, no change to bad count)
    Add: arr[4]=3 <= 3 (good)

    bad = 2 - 0 + 0 = 2
    min_swaps = min(1, 2) = 1

Final: min_swaps = 1

VISUALIZATION OF ALL WINDOWS:
    Window [2, 1, 5]: bad elements = 1 (just 5) → Best!
    Window [1, 5, 6]: bad elements = 2 (5 and 6)
    Window [5, 6, 3]: bad elements = 2 (5 and 6)

DETAILED EXAMPLE WITH STEP-BY-STEP WINDOW SLIDING:
===================================================
Array: [2, 7, 9, 5, 8, 7, 4]
k = 5
Goal: Minimum swaps to bring all elements <= 5 together

Step 1: Count elements <= k
    Elements <= 5: [2, 5, 4]
    count = 3 (window size)

Step 2: First window [2, 7, 9] (indices 0-2)
    2 <= 5? Yes (good)
    7 <= 5? No (bad!)
    9 <= 5? No (bad!)
    bad = 2, min_swaps = 2

Step 3: Slide to [7, 9, 5] (indices 1-3)
    Remove arr[0]=2: 2 <= 5, so bad -= 0
    Add arr[3]=5: 5 <= 5, so bad += 0
    bad = 2, min_swaps = 2

Step 4: Slide to [9, 5, 8] (indices 2-4)
    Remove arr[1]=7: 7 > 5, so bad -= 1
    Add arr[4]=8: 8 > 5, so bad += 1
    bad = 2, min_swaps = 2

Step 5: Slide to [5, 8, 7] (indices 3-5)
    Remove arr[2]=9: 9 > 5, so bad -= 1
    Add arr[5]=7: 7 > 5, so bad += 1
    bad = 2, min_swaps = 2

Step 6: Slide to [8, 7, 4] (indices 4-6)
    Remove arr[3]=5: 5 <= 5, so bad -= 0
    Add arr[6]=4: 4 <= 5, so bad += 0
    bad = 2, min_swaps = 2

Final: min_swaps = 2

All windows have 2 bad elements, so we need 2 swaps.
For example, take window [2, 7, 9]:
    - Swap 7 with 5 → [2, 5, 9]
    - Swap 9 with 4 → [2, 5, 4]
    Total: 2 swaps

WHY THIS WORKS:
- We don't actually perform swaps, we just count how many would be needed
- In any window of size 'count', the bad elements are those > k
- Each bad element needs to be swapped with a good element from outside the window
- The window with minimum bad elements gives us the minimum swaps

TIME COMPLEXITY:  O(n) - Two passes: one to count, one to slide window
SPACE COMPLEXITY: O(1) - Only using a few variables (count, bad, min_swaps)
"""

def minSwap(arr, n, k):
    """
    Find minimum swaps to bring all elements <= k together using sliding window.

    Args:
        arr: List of positive integers
        n: Length of the array
        k: The given number

    Returns:
        Minimum number of swaps required
    """
    # Step 1: Count the number of elements less than or equal to k
    # This tells us the size of the contiguous subarray we're trying to form
    count = 0 
    for i in range(n):
        if arr[i] <= k:
            count += 1
    
    # Step 2: Count the number of elements greater than k in the first window of size 'count'
    # These are the elements that would need to be swapped out of this window
    bad = 0 
    for i in range(count):
        if arr[i] > k:
            bad += 1
    
    # Step 3: Initialize the minimum number of swaps required
    min_swaps = bad
    
    # Step 4: Slide the window of size 'count' through the array
    # We check each possible position to find where minimum swaps would be needed
    for i in range(1, n - count + 1):
        # Remove contribution of the element leaving the window
        if arr[i - 1] > k:
            bad -= 1
            
        # Add contribution of the element entering the window
        if arr[i + count - 1] > k:
            bad += 1
            
        # Update the minimum swaps count if current window has fewer "bad" elements
        min_swaps = min(min_swaps, bad)
    
    return min_swaps
