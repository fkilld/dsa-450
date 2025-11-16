"""
COIN CHANGE PROBLEM
===================

Problem Statement:
-----------------
Given an array of coin denominations and a target sum, find the number of ways
to make that sum using the given coins. You have infinite supply of each coin.

Example:
    Input: coins = [1, 2, 3], sum = 4
    Output: 4
    Explanation: There are 4 ways to make sum 4:
        1. {1, 1, 1, 1}
        2. {1, 1, 2}
        3. {2, 2}
        4. {1, 3}

APPROACH & REASONING:
====================

This is an "Unbounded Knapsack" variation where we can use each coin unlimited times.

Key Insight:
-----------
For each coin, we have two choices:
1. Include the coin (if possible) and solve for remaining sum
2. Exclude the coin and solve without it

The total ways = ways including current coin + ways excluding current coin

Why DP?
-------
- Overlapping subproblems: Same sum with same coins calculated multiple times
- Optimal substructure: Solution builds from smaller subproblems

Two Approaches:
--------------
1. RECURSIVE (Top-Down with Memoization): Start from target, break down
2. ITERATIVE (Bottom-Up Tabulation): Start from 0, build up to target

FLOWCHART (Iterative Approach):
===============================

```mermaid
flowchart TD
    A[Start: coins array, sum n] --> B[Initialize table of size n+1 with 0s]
    B --> C[Set table0 = 1<br/>Base case: 1 way to make sum 0]
    C --> D[Loop: for each coin in coins]
    D --> E[Loop: for each sum j from coin value to n]
    E --> F[tablej += tablej - coin]
    F --> G{More sums to process?}
    G -->|Yes| E
    G -->|No| H{More coins?}
    H -->|Yes| D
    H -->|No| I[Return tablen]
    I --> J[End]
```

Complexity Analysis:
-------------------
Iterative Approach:
    Time: O(m * n) where m = number of coins, n = target sum
    Space: O(n) for the DP table

Recursive Approach:
    Time: O(m * n) with memoization
    Space: O(m * n) for DP table + O(m) recursion stack
"""

class Solution:

    def count_itr(self, arr, m, n):
        """
        ITERATIVE APPROACH (Bottom-Up Tabulation)
        ========================================

        This is the RECOMMENDED approach for interviews as it:
        - Has better space complexity
        - No recursion overhead
        - Easier to understand the DP table evolution

        Args:
            arr: List of coin denominations
            m: Number of different coins
            n: Target sum to achieve

        Returns:
            Number of ways to make sum n using given coins

        Algorithm Steps:
        ---------------
        1. Create a table where table[i] = number of ways to make sum i
        2. Initialize table[0] = 1 (one way to make 0: use no coins)
        3. For each coin:
               For each sum from coin_value to target:
                   Add the ways to make (sum - coin_value) to current sum
        4. Return table[n]

        Why this works:
        --------------
        table[j] accumulates ways to make sum j using coins processed so far.
        When processing coin c, table[j] already has ways without using c.
        We add table[j-c] which gives ways to make (j-c), then add coin c.
        """
        # table[i] stores the number of solutions for value i
        # Index represents the sum, value represents number of ways
        table = [0 for i in range(n + 1)]

        # Base case: There is exactly ONE way to make sum 0 - use no coins
        table[0] = 1

        # Process each coin one by one
        # This outer loop ensures we don't count permutations (e.g., {1,2} and {2,1})
        for i in range(m):
            # For current coin arr[i], update all sums from arr[i] to n
            # We start from arr[i] because we can't use this coin for smaller sums
            for j in range(arr[i], n + 1):
                # Current sum j can be achieved by:
                # - All previous ways to make j (without current coin)
                # - Plus all ways to make (j - arr[i]) and then add current coin
                table[j] += table[j - arr[i]]

                # Example: coins=[1,2], sum=3
                # After coin 1: table = [1, 1, 1, 1] (only using 1s)
                # Processing coin 2, sum 2: table[2] += table[0] = 1+1 = 2
                # Processing coin 2, sum 3: table[3] += table[1] = 1+1 = 2
                # Final: table = [1, 1, 2, 2]

        return table[n]


    def solve(self, arr, m, n):
        """
        RECURSIVE HELPER FUNCTION
        =========================

        This function implements the top-down memoization approach.
        It's more intuitive to derive but has recursion overhead.

        Args:
            arr: List of coin denominations
            m: Current coin index (process coins from m to 0)
            n: Remaining sum to achieve

        Returns:
            Number of ways to make sum n using coins from index 0 to m

        Recurrence Relation:
        -------------------
        count(m, n) = count(m, n - arr[m]) + count(m-1, n)
                      ^^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^^^^
                      Include current coin  Exclude current coin

        Base Cases:
        ----------
        - If n == 0: Found a valid combination, return 1
        - If n < 0: Invalid combination, return 0
        - If m < 0 and n > 0: No more coins but sum not reached, return 0
        """

        # Base case 1: All coins exhausted but sum not reached
        if m == -1 and n > 0:
            return 0

        # Base case 2: Sum achieved successfully
        if n == 0:
            return 1

        # Base case 3: Sum became negative (overshot)
        if n < 0:
            return 0

        # Check memoization table to avoid recomputation
        if self.dp[m][n] != -1:
            return self.dp[m][n]

        # Recursive case: Include current coin OR exclude it
        # Include: use arr[m] and solve for remaining sum (n - arr[m])
        #          Note: m stays same as we can reuse the coin (unbounded)
        # Exclude: don't use arr[m], move to next coin (m-1)
        self.dp[m][n] = self.solve(arr, m, n - arr[m]) + self.solve(arr, m - 1, n)

        return self.dp[m][n]


    def count(self, arr, m, n):
        """
        RECURSIVE APPROACH (Top-Down with Memoization)
        ============================================

        Main function that initializes the DP table and calls recursive solver.

        DP Table Structure:
        ------------------
        dp[i][j] = number of ways to make sum j using coins from index 0 to i

        Dimensions: m rows (coins) × (n+1) columns (sums from 0 to n)

        Example for coins=[1,2,3], sum=4:

             Sum:  0   1   2   3   4
        Coin 1:  [-1, -1, -1, -1, -1]
        Coin 2:  [-1, -1, -1, -1, -1]
        Coin 3:  [-1, -1, -1, -1, -1]

        -1 means not yet computed
        During recursion, we fill this table and reuse computed values
        """

        # Initialize DP table with -1 (indicating not yet computed)
        # dp[i][j] represents ways to make sum j using first i+1 coins
        self.dp = [[-1 for i in range(n + 1)] for i in range(m)]

        # Start recursion from last coin index (m-1) and full sum (n)
        return self.solve(arr, m - 1, n)


# ============================================================================
# TESTING & EXAMPLES
# ============================================================================

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Basic example
    coins1 = [1, 2, 3]
    sum1 = 4
    print(f"Test 1: coins={coins1}, sum={sum1}")
    print(f"Iterative: {sol.count_itr(coins1, len(coins1), sum1)}")  # Expected: 4
    print(f"Recursive: {sol.count(coins1, len(coins1), sum1)}")      # Expected: 4
    print()

    # Test Case 2: Single coin
    coins2 = [2]
    sum2 = 3
    print(f"Test 2: coins={coins2}, sum={sum2}")
    print(f"Iterative: {sol.count_itr(coins2, len(coins2), sum2)}")  # Expected: 0
    print()

    # Test Case 3: Sum is 0
    coins3 = [1, 2, 3]
    sum3 = 0
    print(f"Test 3: coins={coins3}, sum={sum3}")
    print(f"Iterative: {sol.count_itr(coins3, len(coins3), sum3)}")  # Expected: 1
    print()

    # Test Case 4: Larger example
    coins4 = [1, 2, 5]
    sum4 = 5
    print(f"Test 4: coins={coins4}, sum={sum4}")
    print(f"Iterative: {sol.count_itr(coins4, len(coins4), sum4)}")  # Expected: 4
    # Ways: {1,1,1,1,1}, {1,1,1,2}, {1,2,2}, {5}


"""
INTERVIEW TALKING POINTS:
========================

1. PROBLEM IDENTIFICATION:
   "This is a classic unbounded knapsack problem where we need to count
   combinations, not permutations. The key difference from 0-1 knapsack
   is that we can use each coin unlimited times."

2. APPROACH SELECTION:
   "I'll use the iterative bottom-up approach because:
   - Better space complexity O(n) vs O(m*n)
   - No recursion overhead
   - Easier to optimize further if needed"

3. WHY ORDER OF LOOPS MATTERS:
   "We loop over coins in the outer loop to avoid counting permutations.
   If we looped over sums first, we'd count {1,2} and {2,1} separately,
   which would give us permutations instead of combinations."

4. EDGE CASES TO DISCUSS:
   - Sum is 0 (return 1)
   - No coins available (return 0)
   - Target sum is negative (invalid input)
   - Coins larger than target (they won't be used)

5. OPTIMIZATION:
   "If asked about minimum coins instead of count, we'd modify the DP
   to track minimum instead of sum, with initial values as infinity."

6. VARIATIONS:
   - Minimum coins needed (change max to min, count to coins)
   - With limited coins (0-1 knapsack)
   - Print all combinations (need backtracking)
"""
