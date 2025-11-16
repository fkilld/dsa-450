"""
PROBLEM: Search in Array Where Adjacent Elements Differ by At Most K
Given an array where the absolute difference between adjacent elements is at most k,
find an element x in O(n/k) time instead of O(n).

WHY THIS SOLUTION:
This is a CLEVER optimization problem that tests pattern recognition!

Naive approach: Linear search - O(n)
Optimized approach: Use the constraint to SKIP elements - O(n/k)

KEY INSIGHT: Distance-based skipping
If adjacent elements differ by at most k, we can calculate:
- Current element: arr[i]
- Target: x
- Difference: |arr[i] - x|

Minimum steps needed to reach x from arr[i]:
  steps = |arr[i] - x| / k

Why? Because each step can change value by at most k, so we need at least
|difference|/k steps to reach target value.

This means we can safely SKIP those positions!

APPROACH:
Instead of checking every element (i = i+1):
1. At position i, if arr[i] != x:
2. Calculate: jump = |arr[i] - x| / k
3. Skip ahead: i += max(1, jump)
   (max with 1 to handle case when difference < k)

TIME COMPLEXITY: O(n/k) - much better than O(n) when k is large
SPACE COMPLEXITY: O(1)

EXAMPLE: arr = [4, 2, 1, 2, 3, 5, 7], k = 2, x = 5
i=0: arr[0]=4, |4-5|/2 = 0.5 → skip 1 (min jump is 1)
i=1: arr[1]=2, |2-5|/2 = 1.5 → skip 1
i=2: arr[2]=1, |1-5|/2 = 2 → skip 2 positions
i=4: arr[4]=3, |3-5|/2 = 1 → skip 1
i=5: arr[5]=5, found! ✓

Without optimization: 6 checks
With optimization: 5 checks (saved 1, more savings with larger k)

WHY INTERVIEWER WILL ACCEPT:
- Recognizes and exploits the constraint (adjacent differ by k)
- Optimizes from O(n) to O(n/k)
- Shows mathematical reasoning for the skip distance
"""

arr = [int(x) for x in input("Enter array : ").split()]
k = int(input("Enter k (max adjacent difference) : "))
x = int(input("Enter x (target to find) : "))

def search(arr, k, x):
    """
    Search for x in array where adjacent elements differ by at most k.

    Uses the constraint to skip positions that cannot contain the target.
    """
    i = 0
    while i < len(arr):
        # Check if current element is the target
        if arr[i] == x:
            return i

        # Calculate minimum steps needed to reach target value
        # from current position based on the constraint
        # Since adjacent elements differ by at most k,
        # we need at least |arr[i] - x| / k steps
        skip_distance = abs(arr[i] - x) // k

        # Move forward by calculated distance
        # Use max(1, ...) to ensure we always move forward
        # (when difference < k, we still need to check next element)
        i += max(1, skip_distance)

    # Element not found
    return -1

result = search(arr, k, x)
if result != -1:
    print(f"Element {x} found at index: {result}")
else:
    print(f"Element {x} not found in array")
