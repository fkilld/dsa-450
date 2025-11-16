"""
PROBLEM: House Robber (Stickler Thief) - Dynamic Programming
A thief wants to rob houses in a line but cannot rob two consecutive houses.
Maximize the money he can steal.

WHY THIS SOLUTION:
This is a CLASSIC Dynamic Programming problem, not really a search/sort problem!

Naive approach: Try all combinations - O(2^n) exponential!
Optimized approach: Dynamic Programming - O(n) time, O(n) or O(1) space

KEY INSIGHT: Optimal Substructure
At each house i, the thief has TWO choices:
1. Rob house i: get arr[i] + max money from houses up to i-2
2. Skip house i: get max money from houses up to i-1

Recurrence relation:
  dp[i] = max(arr[i] + dp[i-2], dp[i-1])

This is optimal because we're always taking the maximum at each step!

APPROACH:
1. Create dp array where dp[i] = max money robbed up to house i
2. Base cases:
   - dp[0] = arr[0] (only one house, rob it)
   - dp[1] = max(arr[0], arr[1]) (two houses, rob the richer one)
3. For each subsequent house i:
   - Option 1: Rob it → arr[i] + dp[i-2]
   - Option 2: Skip it → dp[i-1]
   - Take maximum

TIME COMPLEXITY: O(n) - single pass
SPACE COMPLEXITY: O(n) - for dp array (can be optimized to O(1))

EXAMPLE: arr = [5, 3, 4, 11, 2]
dp[0] = 5 (rob house 0)
dp[1] = max(5, 3) = 5 (skip house 1)
dp[2] = max(4+5, 5) = 9 (rob houses 0 and 2)
dp[3] = max(11+5, 9) = 16 (rob houses 1 and 3)
dp[4] = max(2+9, 16) = 16 (skip house 4)
Answer: 16

WHY INTERVIEWER WILL ACCEPT:
- Classic DP problem, tests understanding of optimal substructure
- Clear recurrence relation
- Shows ability to identify and solve DP problems
- Can discuss space optimization (O(1) using only two variables)
"""

n = int(input("Enter length : "))
arr = [int(x) for x in input("Enter the array : ").split()]

def give_max(arr, n):
    """
    Calculate maximum money that can be robbed without robbing consecutive houses.

    Uses dynamic programming with O(n) time and O(n) space.

    Args:
        arr: Array of money in each house
        n: Number of houses

    Returns:
        Maximum money that can be robbed
    """
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])

    # Create DP array where dp[i] = max money stolen up to house i
    dp = [0] * n

    # Initialize base cases
    dp[0] = arr[0]  # Only one house, rob it
    dp[1] = max(arr[0], arr[1])  # Two houses, pick richer one

    # Fill DP array using recurrence relation
    for i in range(2, n):
        # dp[i] represents the max money that can be stolen up to house i
        # Choice 1: Rob current house + max from non-adjacent houses (i-2)
        # Choice 2: Skip current house, keep max from previous house (i-1)
        dp[i] = max(arr[i] + dp[i-2], dp[i-1])

    # The last element contains the maximum money for all houses
    return dp[-1]

max_money = give_max(arr, n)
print(f"Maximum money that can be robbed: {max_money}")

# SPACE OPTIMIZATION NOTE:
# This can be done in O(1) space using only two variables:
# prev2 = dp[i-2]
# prev1 = dp[i-1]
# curr = max(arr[i] + prev2, prev1)
# Then shift: prev2 = prev1, prev1 = curr
