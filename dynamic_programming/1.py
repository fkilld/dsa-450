"""
0-1 KNAPSACK PROBLEM
====================

Problem Statement:
-----------------
Given weights and values of n items, put these items in a knapsack of capacity W
to get the maximum total value in the knapsack. You can either take an item or
leave it (0-1 property - can't take fraction or multiple copies).

Example:
    Input:
        values = [60, 100, 120]
        weights = [10, 20, 30]
        W = 50
    Output: 220
    Explanation: Take items with values 100 and 120 (weights 20 + 30 = 50)

APPROACH & REASONING:
====================

This is the CLASSIC Dynamic Programming problem that forms the basis for many
other DP problems like subset sum, partition, and others.

Key Insight:
-----------
For each item, we have exactly TWO choices:
1. Include the item (if weight permits) and add its value
2. Exclude the item and continue with remaining items

We take the MAXIMUM of these two choices.

Why DP?
-------
- Overlapping subproblems: Same weight with same items considered multiple times
- Optimal substructure: Optimal solution contains optimal solutions to subproblems
- Without DP: Time complexity would be O(2^n) - exponential!
- With DP: Time complexity becomes O(n * W) - pseudo-polynomial

Decision at each step:
---------------------
For item i with weight w[i] and value v[i]:
    If w[i] <= current_capacity:
        dp[i][capacity] = max(
            v[i] + dp[i-1][capacity - w[i]],  // Include item i
            dp[i-1][capacity]                  // Exclude item i
        )
    Else:
        dp[i][capacity] = dp[i-1][capacity]    // Can't include (too heavy)

FLOWCHART:
==========

```mermaid
flowchart TD
    A[Start: n items, weights, values, capacity W] --> B[Create DP table n+1 x W+1]
    B --> C[Initialize first row and column to 0<br/>0 items or 0 capacity = 0 value]
    C --> D[Loop: for each item i from 1 to n]
    D --> E[Loop: for each weight w from 1 to W]
    E --> F{Is i==0 OR w==0?}
    F -->|Yes| G[dpi,w = 0]
    F -->|No| H{Can item i fit?<br/>wti-1 <= w}
    H -->|Yes| I[dpi,w = max of:<br/>1 Include: vali-1 + dpi-1,w-wti-1<br/>2 Exclude: dpi-1,w]
    H -->|No| J[dpi,w = dpi-1,w<br/>Exclude item]
    G --> K{More weights?}
    I --> K
    J --> K
    K -->|Yes| E
    K -->|No| L{More items?}
    L -->|Yes| D
    L -->|No| M[Return dpn,W]
    M --> N[End]
```

DP Table Visualization:
=======================

For values=[60,100,120], weights=[10,20,30], W=50:

         Capacity: 0    10   20   30   40   50
    Item 0 (none): 0     0    0    0    0    0
    Item 1 (v=60): 0    60   60   60   60   60
    Item 2 (v=100):0    60  100  160  160  160
    Item 3 (v=120):0    60  100  160  180  220
                                            ^^^
                                     Maximum value

How to fill each cell:
    dp[2][30] = max(100 + dp[1][10], dp[1][30])
              = max(100 + 60, 60) = 160
    (Include item 2: value 100 + best from 10 capacity with item 1)

Complexity Analysis:
-------------------
Time Complexity: O(n * W)
    - n items × W capacity
    - Each cell computed in O(1) time

Space Complexity: O(n * W)
    - DP table of size (n+1) × (W+1)
    - Can be optimized to O(W) using 1D array

Space Optimization Possible:
    Since we only need previous row, we can use O(W) space.
    Traverse from right to left to avoid overwriting needed values.
"""

class Solution:

    def knapSack(self, W, wt, val, n):
        """
        0-1 KNAPSACK - BOTTOM-UP TABULATION
        ===================================

        This is the STANDARD approach taught in interviews and courses.

        Args:
            W: Maximum weight capacity of knapsack
            wt: List of weights of items (0-indexed)
            val: List of values of items (0-indexed)
            n: Number of items

        Returns:
            Maximum value achievable with given capacity

        DP State Definition:
        -------------------
        dp[i][w] = Maximum value achievable using:
                   - First i items (items 0 to i-1)
                   - Knapsack capacity w

        Base Cases:
        ----------
        dp[0][w] = 0  (no items, any capacity → value = 0)
        dp[i][0] = 0  (any items, no capacity → value = 0)

        Recurrence Relation:
        -------------------
        For item i-1 (array is 0-indexed):
            If wt[i-1] <= w:
                dp[i][w] = max(
                    val[i-1] + dp[i-1][w - wt[i-1]],  # Include item i-1
                    dp[i-1][w]                        # Exclude item i-1
                )
            Else:
                dp[i][w] = dp[i-1][w]  # Can't include, too heavy

        Algorithm Steps:
        ---------------
        1. Create (n+1) × (W+1) DP table initialized to 0
        2. For each item i from 1 to n:
             For each capacity w from 1 to W:
                 If item can fit (wt[i-1] <= w):
                     Choose max of including or excluding
                 Else:
                     Exclude item (copy value from previous row)
        3. Return dp[n][W]
        """

        # Create DP table with (n+1) rows and (W+1) columns
        # Extra row/column for base case (0 items or 0 capacity)
        # Rows represent items considered (0 to n)
        # Columns represent capacity (0 to W)
        dp = [[0 for i in range(W + 1)] for i in range(n + 1)]

        # Build the DP table bottom-up
        for i in range(n + 1):
            for w in range(W + 1):

                # Base case: No items or no capacity
                # If either no item is present (i=0) or capacity is zero (w=0)
                # then maximum value achievable is 0
                if i == 0 or w == 0:
                    dp[i][w] = 0

                # Case 1: Current item can fit in knapsack
                # Check if weight of (i-1)th item <= current capacity w
                # Note: We use (i-1) because dp table has extra row, but
                #       wt and val arrays are 0-indexed
                elif wt[i - 1] <= w:
                    # We have two choices:

                    # Choice 1: INCLUDE current item (i-1)
                    #   - Add its value: val[i-1]
                    #   - Add best value from remaining capacity: dp[i-1][w - wt[i-1]]
                    #   - Use i-1 (previous row) because we can't reuse same item
                    include_value = val[i - 1] + dp[i - 1][w - wt[i - 1]]

                    # Choice 2: EXCLUDE current item
                    #   - Take the best value without this item: dp[i-1][w]
                    exclude_value = dp[i - 1][w]

                    # Take maximum of both choices
                    dp[i][w] = max(include_value, exclude_value)

                # Case 2: Current item is too heavy, can't fit
                else:
                    # No choice but to exclude this item
                    # Copy the best value from previous items with same capacity
                    dp[i][w] = dp[i - 1][w]

        # Return the maximum value achievable with all items and full capacity
        return dp[n][W]


    def knapSack_optimized(self, W, wt, val, n):
        """
        SPACE-OPTIMIZED VERSION - O(W) SPACE
        ====================================

        Since we only need the previous row to compute current row,
        we can optimize space from O(n*W) to O(W).

        KEY TRICK: Traverse capacity from RIGHT to LEFT
        This prevents overwriting values we still need.

        Why right to left?
        -----------------
        If we go left to right:
            dp[10] might update using dp[5]
            But dp[5] was already updated in this iteration!
            This causes us to use the same item multiple times.

        Going right to left ensures we use OLD values from previous iteration.
        """

        # 1D array representing current row of DP table
        dp = [0 for _ in range(W + 1)]

        # Process each item
        for i in range(n):
            # Traverse from right to left (W to wt[i])
            # This ensures we don't overwrite values we need
            for w in range(W, wt[i] - 1, -1):
                # Update dp[w] with max of including or excluding current item
                # dp[w] currently holds value without item i (from previous iteration)
                # dp[w - wt[i]] holds best value for reduced capacity
                dp[w] = max(dp[w], val[i] + dp[w - wt[i]])

        return dp[W]


# ============================================================================
# TESTING & EXAMPLES
# ============================================================================

if __name__ == "__main__":
    sol = Solution()

    print("=" * 60)
    print("0-1 KNAPSACK PROBLEM - TEST CASES")
    print("=" * 60)

    # Test Case 1: Basic example
    print("\nTest 1: Classic Example")
    val1 = [60, 100, 120]
    wt1 = [10, 20, 30]
    W1 = 50
    n1 = len(val1)
    print(f"Values:  {val1}")
    print(f"Weights: {wt1}")
    print(f"Capacity: {W1}")
    result1 = sol.knapSack(W1, wt1, val1, n1)
    result1_opt = sol.knapSack_optimized(W1, wt1, val1, n1)
    print(f"Maximum value (2D DP): {result1}")
    print(f"Maximum value (1D optimized): {result1_opt}")
    print(f"Expected: 220 (items 2 and 3)")

    # Test Case 2: Can't fit all items
    print("\n" + "-" * 60)
    print("\nTest 2: Limited Capacity")
    val2 = [10, 20, 30]
    wt2 = [1, 1, 1]
    W2 = 2
    n2 = len(val2)
    print(f"Values:  {val2}")
    print(f"Weights: {wt2}")
    print(f"Capacity: {W2}")
    result2 = sol.knapSack(W2, wt2, val2, n2)
    print(f"Maximum value: {result2}")
    print(f"Expected: 50 (items with values 20 and 30)")

    # Test Case 3: Single item
    print("\n" + "-" * 60)
    print("\nTest 3: Single Item")
    val3 = [100]
    wt3 = [50]
    W3 = 50
    n3 = len(val3)
    print(f"Values:  {val3}")
    print(f"Weights: {wt3}")
    print(f"Capacity: {W3}")
    result3 = sol.knapSack(W3, wt3, val3, n3)
    print(f"Maximum value: {result3}")
    print(f"Expected: 100")

    # Test Case 4: Zero capacity
    print("\n" + "-" * 60)
    print("\nTest 4: Zero Capacity")
    val4 = [10, 20, 30]
    wt4 = [5, 10, 15]
    W4 = 0
    n4 = len(val4)
    print(f"Values:  {val4}")
    print(f"Weights: {wt4}")
    print(f"Capacity: {W4}")
    result4 = sol.knapSack(W4, wt4, val4, n4)
    print(f"Maximum value: {result4}")
    print(f"Expected: 0")

    print("\n" + "=" * 60)


"""
INTERVIEW TALKING POINTS:
========================

1. PROBLEM RECOGNITION:
   "This is the classic 0-1 Knapsack problem - foundational DP problem.
   The '0-1' means we can either take an item completely or leave it.
   This is different from fractional knapsack (which uses greedy approach)
   or unbounded knapsack (where we can take unlimited copies)."

2. WHY GREEDY DOESN'T WORK:
   "We might think to use greedy by value/weight ratio, but that doesn't
   guarantee optimal solution. Example:
   Items: [(v=100,w=20), (v=60,w=10)]
   Capacity: 50
   Greedy by ratio would prefer item 2 (ratio=6) over item 1 (ratio=5),
   but we can take both! Only DP finds optimal solution."

3. STATE REPRESENTATION:
   "I'll use dp[i][w] to represent max value using first i items with
   capacity w. This naturally leads to our recurrence relation where
   we decide to include or exclude each item."

4. OPTIMIZATION DISCUSSION:
   "The standard solution uses O(n*W) space. If interviewer asks about
   optimization, I can reduce to O(W) by using 1D array and traversing
   right to left. This works because we only need the previous row."

5. VARIATIONS TO MENTION:
   - Subset Sum: Special case where values = weights
   - Equal Sum Partition: Can we split array into two equal halves?
   - Minimum Subset Sum Difference: Minimize |sum1 - sum2|
   - Count of Subsets with Given Sum
   - Target Sum (with +/- signs)

6. EDGE CASES:
   - Empty knapsack (W=0) → return 0
   - No items (n=0) → return 0
   - All items too heavy → return 0
   - Single item → return value if fits, else 0

7. TIME COMPLEXITY NOTE:
   "O(n*W) is pseudo-polynomial because it depends on W (a number),
   not the input size. If W is very large (e.g., 10^9), this becomes
   impractical. The problem is NP-complete, so no known polynomial solution."

8. HOW TO RECONSTRUCT SOLUTION:
   "If asked which items to include, we can backtrack through DP table:
   Starting from dp[n][W], if dp[i][w] != dp[i-1][w], item i-1 was included.
   Move to dp[i-1][w - wt[i-1]] and repeat."

COMMON MISTAKES TO AVOID:
========================
1. Forgetting the (i-1) index when accessing wt[] and val[] arrays
2. Not handling base cases (i=0 or w=0)
3. Using i instead of i-1 in the recurrence (allows reusing same item)
4. In space-optimized version, going left to right instead of right to left
5. Confusing with unbounded knapsack (where we use dp[i][w-wt[i]] instead)
"""
