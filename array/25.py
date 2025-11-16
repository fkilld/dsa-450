"""
PROBLEM: Maximum Profit by Buying and Selling Stock At Most Twice
===================================================================
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously
(i.e., you must sell the stock before you buy again).

Example 1:
    Input:  prices = [3, 3, 5, 0, 0, 3, 1, 4]
    Output: 6
    Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3
                 Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 3
                 Total profit = 3 + 3 = 6

Example 2:
    Input:  prices = [1, 2, 3, 4, 5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 4
                 Only one transaction needed, total profit = 4

Example 3:
    Input:  prices = [7, 6, 4, 3, 1]
    Output: 0
    Explanation: No profitable transaction possible

APPROACH 1: Dynamic Programming (Bidirectional)
================================================
WHY THIS APPROACH?
- We need to track the best profit from at most 2 transactions
- We can split the problem: max profit from transaction 1 on left + max profit from transaction 2 on right
- dp[i] stores: maximum profit from ONE transaction in range [i, n-1] (right side)
- Then we update dp[i] to include: best profit from left transaction + best profit from right transaction

HOW IT WORKS:
1. Right Pass: Calculate maximum profit from selling on/after each day
   - Store in dp[i] the best profit achievable from day i to end
2. Left Pass: Calculate maximum profit from buying/selling up to each day
   - Combine with dp[i] (profit from remaining days) to get total profit from 2 transactions

FLOW EXAMPLE (Dynamic Programming):
====================================
Array: prices = [3, 3, 5, 0, 0, 3, 1, 4]
Indices:         0  1  2  3  4  5  6  7

RIGHT PASS: Calculate max profit selling on/after each day
-----------------------------------------------------------
Initialize: ma = prices[7] = 4 (max sell price)
            dp = [0, 0, 0, 0, 0, 0, 0, 0]

i=6: prices[6]=1, ma=4 (no change), dp[6] = max(0, 4-1) = 3
     dp = [0, 0, 0, 0, 0, 0, 3, 0]

i=5: prices[5]=3, ma=4 (no change), dp[5] = max(3, 4-3) = 3
     dp = [0, 0, 0, 0, 0, 3, 3, 0]

i=4: prices[4]=0, ma=4 (no change), dp[4] = max(3, 4-0) = 4
     dp = [0, 0, 0, 0, 4, 3, 3, 0]

i=3: prices[3]=0, ma=4 (no change), dp[3] = max(4, 4-0) = 4
     dp = [0, 0, 0, 4, 4, 3, 3, 0]

i=2: prices[2]=5, ma=5 (new max), dp[2] = max(4, 5-5) = 4
     dp = [0, 0, 4, 4, 4, 3, 3, 0]

i=1: prices[1]=3, ma=5 (no change), dp[1] = max(4, 5-3) = 4
     dp = [0, 4, 4, 4, 4, 3, 3, 0]

i=0: prices[0]=3, ma=5 (no change), dp[0] = max(4, 5-3) = 4
     dp = [4, 4, 4, 4, 4, 3, 3, 0]

After RIGHT pass, dp[i] = max profit from ONE transaction starting at day i or later

LEFT PASS: Add profit from buying/selling up to each day
---------------------------------------------------------
Initialize: mi = prices[0] = 3 (min buy price)

i=1: prices[1]=3, mi=3 (no change),
     dp[1] = max(dp[0], dp[1] + (3-3)) = max(4, 4+0) = 4
     dp = [4, 4, 4, 4, 4, 3, 3, 0]

i=2: prices[2]=5, mi=3 (no change),
     dp[2] = max(dp[1], dp[2] + (5-3)) = max(4, 4+2) = 6
     dp = [4, 4, 6, 4, 4, 3, 3, 0]

i=3: prices[3]=0, mi=0 (new min),
     dp[3] = max(dp[2], dp[3] + (0-0)) = max(6, 4+0) = 6
     dp = [4, 4, 6, 6, 4, 3, 3, 0]

i=4: prices[4]=0, mi=0 (no change),
     dp[4] = max(dp[3], dp[4] + (0-0)) = max(6, 4+0) = 6
     dp = [4, 4, 6, 6, 6, 3, 3, 0]

i=5: prices[5]=3, mi=0 (no change),
     dp[5] = max(dp[4], dp[5] + (3-0)) = max(6, 3+3) = 6
     dp = [4, 4, 6, 6, 6, 6, 3, 0]

i=6: prices[6]=1, mi=0 (no change),
     dp[6] = max(dp[5], dp[6] + (1-0)) = max(6, 3+1) = 6
     dp = [4, 4, 6, 6, 6, 6, 6, 0]

i=7: prices[7]=4, mi=0 (no change),
     dp[7] = max(dp[6], dp[7] + (4-0)) = max(6, 0+4) = 6
     dp = [4, 4, 6, 6, 6, 6, 6, 6]

Final: dp[7] = 6 (maximum profit from at most 2 transactions)

TIME COMPLEXITY:  O(n) - Two passes through the array
SPACE COMPLEXITY: O(n) - dp array of size n


APPROACH 2: State Machine (Without Extra Array)
================================================
WHY THIS APPROACH?
- Track 4 states: buy1, profit1, buy2, profit2
- Simpler to understand: simulates the actual buying/selling process
- Uses O(1) space instead of O(n)

HOW IT WORKS:
1. buy1: minimum cost to buy first stock (using our own money)
2. profit1: maximum profit from first transaction
3. buy2: minimum cost to buy second stock (using profit from first transaction)
4. profit2: maximum profit from both transactions

The key insight: buy2 = min(buy2, price - profit1)
This means we're using the profit from first transaction to reduce the effective cost of second purchase.

FLOW EXAMPLE (State Machine):
==============================
Array: prices = [3, 3, 5, 0, 0, 3, 1, 4]

Initialize: buy1 = inf, profit1 = 0, buy2 = inf, profit2 = 0

i=0: price=3
    buy1 = min(inf, 3) = 3         [Buy first stock at 3]
    profit1 = max(0, 3-3) = 0      [Sell at 3, profit = 0]
    buy2 = min(inf, 3-0) = 3       [Buy second at effective cost 3]
    profit2 = max(0, 3-3) = 0      [Sell second at 3, profit = 0]
    State: buy1=3, profit1=0, buy2=3, profit2=0

i=1: price=3
    buy1 = min(3, 3) = 3           [Keep first buy at 3]
    profit1 = max(0, 3-3) = 0      [No profit yet]
    buy2 = min(3, 3-0) = 3         [Keep second buy at 3]
    profit2 = max(0, 3-3) = 0      [No profit yet]
    State: buy1=3, profit1=0, buy2=3, profit2=0

i=2: price=5
    buy1 = min(3, 5) = 3           [Keep first buy at 3]
    profit1 = max(0, 5-3) = 2      [Sell at 5, profit = 2]
    buy2 = min(3, 5-2) = 3         [Keep second buy at effective cost 3]
    profit2 = max(0, 5-3) = 2      [Sell second at 5, profit = 2]
    State: buy1=3, profit1=2, buy2=3, profit2=2

i=3: price=0
    buy1 = min(3, 0) = 0           [Better to buy first at 0]
    profit1 = max(2, 0-0) = 2      [Keep max profit 2]
    buy2 = min(3, 0-2) = -2        [With profit 2, effective cost is -2]
    profit2 = max(2, 0-(-2)) = 2   [Keep max profit 2]
    State: buy1=0, profit1=2, buy2=-2, profit2=2

i=4: price=0
    buy1 = min(0, 0) = 0           [Keep first buy at 0]
    profit1 = max(2, 0-0) = 2      [Keep max profit 2]
    buy2 = min(-2, 0-2) = -2       [Keep second buy at effective cost -2]
    profit2 = max(2, 0-(-2)) = 2   [Keep max profit 2]
    State: buy1=0, profit1=2, buy2=-2, profit2=2

i=5: price=3
    buy1 = min(0, 3) = 0           [Keep first buy at 0]
    profit1 = max(2, 3-0) = 3      [Sell at 3, profit = 3]
    buy2 = min(-2, 3-3) = -2       [Keep second buy at effective cost -2]
    profit2 = max(2, 3-(-2)) = 5   [Sell second at 3, profit = 5]
    State: buy1=0, profit1=3, buy2=-2, profit2=5

i=6: price=1
    buy1 = min(0, 1) = 0           [Keep first buy at 0]
    profit1 = max(3, 1-0) = 3      [Keep max profit 3]
    buy2 = min(-2, 1-3) = -2       [Keep second buy at effective cost -2]
    profit2 = max(5, 1-(-2)) = 5   [Keep max profit 5]
    State: buy1=0, profit1=3, buy2=-2, profit2=5

i=7: price=4
    buy1 = min(0, 4) = 0           [Keep first buy at 0]
    profit1 = max(3, 4-0) = 4      [Sell at 4, profit = 4]
    buy2 = min(-2, 4-4) = -2       [Keep second buy at effective cost -2]
    profit2 = max(5, 4-(-2)) = 6   [Sell second at 4, profit = 6]
    State: buy1=0, profit1=4, buy2=-2, profit2=6

Final: profit2 = 6

Best Strategy Found:
- Buy first at day 3 (price=0), sell at day 5 (price=3), profit=3
- Buy second at day 6 (price=1), sell at day 7 (price=4), profit=3
- Total profit = 6

TIME COMPLEXITY:  O(n) - Single pass through the array
SPACE COMPLEXITY: O(1) - Only 4 variables used
"""

class Solution:
    def max_dp(self, prices):
        """
        Calculate maximum profit using dynamic programming with two passes.

        Args:
            prices: List of stock prices where prices[i] is price on day i

        Returns:
            Maximum profit achievable with at most 2 transactions
        """
        n = len(prices)

        # dp[i] will store the maximum profit achievable from day i onwards
        # Initially all zeros (no profit)
        dp = [0] * n

        # Track the maximum selling price seen so far (from right to left)
        # Start with the last day's price
        ma = prices[n - 1]

        # Track the minimum buying price seen so far (from left to right)
        # Start with the first day's price
        mi = prices[0]

        # RIGHT PASS: Calculate max profit from one transaction starting at each day
        # Traverse from second-last day to first day (right to left)
        for i in range(n - 2, -1, -1):
            # Update maximum selling price if current price is higher
            # This represents the best day to sell if we buy on day i
            if prices[i] > ma:
                ma = prices[i]

            # dp[i] = max profit from ONE transaction from day i to end
            # Either: take profit from next day, OR buy today and sell at ma
            dp[i] = max(dp[i + 1], ma - prices[i])

        # After right pass, dp[i] contains max profit from single transaction from day i onwards

        # LEFT PASS: Combine left transaction profit with right transaction profit
        # Traverse from second day to last day (left to right)
        for i in range(1, n):
            # Update minimum buying price if current price is lower
            # This represents the best day to buy before day i
            if prices[i] < mi:
                mi = prices[i]

            # dp[i] = max profit from TWO transactions up to day i
            # Either: keep previous day's max profit (dp[i-1])
            # OR: profit from selling first transaction today (prices[i] - mi)
            #     PLUS profit from second transaction after today (dp[i])
            dp[i] = max(dp[i - 1], dp[i] + (prices[i] - mi))

        # Return maximum profit from 2 transactions considering all days
        return dp[n - 1]

    def max_simple(self, prices, n):
        """
        Calculate maximum profit using state machine approach (O(1) space).
        Simulates the buying/selling process by tracking 4 states.

        Args:
            prices: List of stock prices where prices[i] is price on day i
            n: Length of prices array

        Returns:
            Maximum profit achievable with at most 2 transactions

        Reference: https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-stock-at-most-twice-set-2/
        """
        # Initialize costs to infinity (haven't bought yet)
        buy1 = buy2 = float('inf')

        # Initialize profits to 0 (no transactions yet)
        profit1 = profit2 = 0

        # Process each day's price
        for i in range(n):
            # STATE 1: Buy first stock
            # Track the minimum price to buy the first stock
            # We want to buy at the lowest price possible using our own money
            # If we already bought at a lower price, keep that purchase
            buy1 = min(buy1, prices[i])

            # STATE 2: Sell first stock
            # Track the maximum profit from the first transaction
            # Profit = selling price today - best buying price (buy1)
            # Keep the maximum profit seen so far
            profit1 = max(profit1, prices[i] - buy1)

            # STATE 3: Buy second stock
            # Track the effective cost of buying the second stock
            # We use profit from first transaction to reduce the cost
            # Effective cost = current price - profit from first transaction
            # This is like getting a discount on the second purchase
            # Example: If profit1 = 5 and prices[i] = 10, effective cost = 10 - 5 = 5
            buy2 = min(buy2, prices[i] - profit1)

            # STATE 4: Sell second stock
            # Track the maximum total profit from both transactions
            # Total profit = selling price today - effective cost of second stock (buy2)
            # Since buy2 already accounts for profit1, this gives us total profit
            profit2 = max(profit2, prices[i] - buy2)

        # Return the maximum profit from both transactions
        return profit2