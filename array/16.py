"""
PROBLEM: Best Time to Buy and Sell Stock
==========================================
Given an array 'prices' where prices[i] is the price of a given stock on the ith day,
find the maximum profit you can achieve from one transaction (buy once and sell once).

You must buy before you sell. If you cannot achieve any profit, return 0.

Example:
    Input:  prices = [7, 1, 5, 3, 6, 4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6)
                 Profit = 6 - 1 = 5

    Input:  prices = [7, 6, 4, 3, 1]
    Output: 0
    Explanation: Prices keep decreasing, no profit possible

    Input:  prices = [1, 2, 3, 4, 5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5)
                 Profit = 5 - 1 = 4

    Input:  prices = [2, 4, 1, 3, 5]
    Output: 4
    Explanation: Buy on day 3 (price = 1) and sell on day 5 (price = 5)
                 Profit = 5 - 1 = 4

APPROACH: Single Pass with Minimum Tracking
=============================================
WHY THIS APPROACH?
- Optimal time complexity: O(n) - Single pass through array
- Minimal space complexity: O(1) - Only two variables needed
- Simple and intuitive: Track minimum buy price and maximum profit
- No need to check all pairs of buy/sell days
- Works for all edge cases (decreasing prices, single day, etc.)

ALTERNATIVE APPROACHES:
1. Brute Force: Check all pairs (i, j) where i < j - O(n²) time
2. Divide and Conquer: Split array recursively - O(n log n) time
3. Single Pass (This approach): Optimal - O(n) time, O(1) space

KEY INSIGHT:
For each day, we want to know:
"If I sell today, what's the maximum profit I could make?"

To answer this, we need to know the minimum price we've seen so far
(best day to buy before today). Then profit = today's price - min price.

We track:
1. min_buy: The lowest price seen so far (best buying opportunity)
2. max_profit: The maximum profit we can achieve

HOW IT WORKS:
1. Initialize min_buy to first day's price
2. Initialize max_profit to 0 (no profit yet)
3. For each day's price:
   a. If price <= min_buy, update min_buy (found better buying day)
   b. Else, calculate profit if we sell today: price - min_buy
   c. Update max_profit if this profit is better than current max_profit
4. Return max_profit

FLOW EXAMPLE:
=============
Array: [7, 1, 5, 3, 6, 4]
Goal: Find maximum profit from one buy-sell transaction

Initial State:
    min_buy = 7 (first day price)
    max_profit = 0

Step 1: Process prices[0] = 7
    price = 7
    price == min_buy, no action
    Current state: min_buy = 7, max_profit = 0

Step 2: Process prices[1] = 1
    price = 1
    price < min_buy (1 < 7)
    Update min_buy = 1 (better buying opportunity!)
    Current state: min_buy = 1, max_profit = 0
    [Best to buy on day 2 at price 1]

Step 3: Process prices[2] = 5
    price = 5
    price > min_buy (5 > 1)
    profit = 5 - 1 = 4
    profit (4) > max_profit (0)
    Update max_profit = 4
    Current state: min_buy = 1, max_profit = 4
    [If we sell on day 3, profit = 4]

Step 4: Process prices[3] = 3
    price = 3
    price > min_buy (3 > 1)
    profit = 3 - 1 = 2
    profit (2) < max_profit (4)
    No update to max_profit
    Current state: min_buy = 1, max_profit = 4
    [Selling on day 4 gives less profit than day 3]

Step 5: Process prices[4] = 6
    price = 6
    price > min_buy (6 > 1)
    profit = 6 - 1 = 5
    profit (5) > max_profit (4)
    Update max_profit = 5
    Current state: min_buy = 1, max_profit = 5
    [If we sell on day 5, profit = 5 - BEST!]

Step 6: Process prices[5] = 4
    price = 4
    price > min_buy (4 > 1)
    profit = 4 - 1 = 3
    profit (3) < max_profit (5)
    No update to max_profit
    Current state: min_buy = 1, max_profit = 5
    [Selling on day 6 gives less profit than day 5]

Final Result: max_profit = 5
Best strategy: Buy at 1 (day 2), sell at 6 (day 5)

FLOWCHART:
==========
    ┌──────────────────────────────┐
    │  Start: maxProfit(prices)    │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │ Initialize:                  │
    │ min_buy = prices[0]          │
    │ max_profit = 0               │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │ For each price in prices     │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │   Is price <= min_buy?       │
    └────┬────────────────────┬────┘
         │ Yes                │ No
         │                    │
         ▼                    ▼
    ┌────────────┐   ┌──────────────────────┐
    │ min_buy =  │   │ Calculate profit:    │
    │ price      │   │ profit = price - buy │
    │            │   └──────────┬───────────┘
    │ (Better    │              │
    │  buying    │              ▼
    │  day!)     │   ┌──────────────────────┐
    └─────┬──────┘   │ Is profit > max?     │
          │          └────┬────────────┬────┘
          │               │ Yes        │ No
          │               │            │
          │               ▼            │
          │    ┌──────────────────┐   │
          │    │ max_profit =     │   │
          │    │ profit           │   │
          │    │                  │   │
          │    │ (New best        │   │
          │    │  profit!)        │   │
          │    └────┬─────────────┘   │
          │         │                 │
          └─────────┴─────────────────┘
                    │
                    ▼
    ┌──────────────────────────────┐
    │ More prices in array?        │
    └────┬────────────────────┬────┘
         │ Yes                │ No
         │                    │
         │ (loop back)        ▼
         │          ┌──────────────────┐
         └─────────►│ Return max_profit│
                    └──────────────────┘

WHY UPDATE min_buy WHEN PRICE IS LOWER?
=========================================
When we find a lower price, it becomes a better buying opportunity
for ALL future selling days. Even if we've already found some profit,
we should update min_buy because:

1. Future prices might be even higher
2. Buying at a lower price gives more profit for the same selling price
3. We're looking for the global maximum profit

Example: [5, 2, 8, 1, 10]
- Day 1-3: Buy at 5, sell at 8 → profit = 3
- Day 4: Found price 1 < 5, update min_buy = 1
- Day 5: Sell at 10 → profit = 10 - 1 = 9 (better than 3!)

WHY NOT UPDATE max_profit WHEN price <= min_buy?
==================================================
When price <= min_buy, we update our buying price. We can't sell
on the same day we buy, so we don't calculate profit for this day.
We'll calculate profit when we process future days.

SPECIAL CASES:
==============
1. Decreasing Prices [7, 6, 4, 3, 1]:
   - min_buy keeps updating
   - max_profit stays 0 (never enters else branch)
   - Return 0 (no profit possible)

2. Increasing Prices [1, 2, 3, 4, 5]:
   - min_buy = 1 (first day)
   - max_profit keeps updating: 1, 2, 3, 4
   - Return 4 (buy day 1, sell day 5)

3. Single Day [5]:
   - Only one element, loop runs once
   - Returns 0 (can't buy and sell same day)

TIME COMPLEXITY:  O(n) - Single pass through array
SPACE COMPLEXITY: O(1) - Only two variables (min_buy, max_profit)
"""


def maxProfit(prices):
    """
    Find the maximum profit from one stock buy-sell transaction.

    This function uses a greedy approach to track the minimum buying price
    seen so far and calculates the maximum possible profit at each step.

    Args:
        prices (list): List of stock prices where prices[i] is the price on day i

    Returns:
        int: Maximum profit achievable, or 0 if no profit is possible

    Time Complexity: O(n) - Single pass through the prices array
    Space Complexity: O(1) - Only two variables used

    Example:
        >>> maxProfit([7, 1, 5, 3, 6, 4])
        5
        >>> maxProfit([7, 6, 4, 3, 1])
        0
    """
    # Edge case: Empty array or single element
    # Cannot make a transaction, return 0
    if not prices or len(prices) < 2:
        return 0

    # Initialize max_profit to 0 (default if no profit can be made)
    # We track the maximum profit we can achieve
    max_profit = 0

    # Initialize min_buy to the first day's price
    # This represents the minimum price we've seen so far (best buying opportunity)
    min_buy = prices[0]

    # Iterate through each price in the array
    for price in prices:
        # Case 1: Current price is lower than or equal to our minimum buying price
        # This means we found a better (or equal) day to buy
        if price <= min_buy:
            # Update the minimum buying price
            # This is our new best buying opportunity
            min_buy = price

        # Case 2: Current price is higher than our minimum buying price
        # We can potentially make profit by selling today
        else:
            # Calculate profit if we sell today
            # profit = selling price - buying price
            profit = price - min_buy

            # If this profit is better than our current maximum, update it
            # We're looking for the maximum profit across all possible transactions
            if profit > max_profit:
                max_profit = profit

    # Return the maximum profit we can achieve
    # If no profit is possible (prices only decrease), this will be 0
    return max_profit


# Test cases
if __name__ == "__main__":
    # Test 1: Standard case with optimal buy-sell opportunity
    prices1 = [7, 1, 5, 3, 6, 4]
    result1 = maxProfit(prices1)
    print(f"Prices: {prices1}")
    print(f"Maximum profit: {result1}")  # Expected: 5
    print("Explanation: Buy at 1, sell at 6 → profit = 5\n")

    # Test 2: Decreasing prices - no profit possible
    prices2 = [7, 6, 4, 3, 1]
    result2 = maxProfit(prices2)
    print(f"Prices: {prices2}")
    print(f"Maximum profit: {result2}")  # Expected: 0
    print("Explanation: Prices keep decreasing, no profit possible\n")

    # Test 3: Increasing prices - best to buy first day, sell last day
    prices3 = [1, 2, 3, 4, 5]
    result3 = maxProfit(prices3)
    print(f"Prices: {prices3}")
    print(f"Maximum profit: {result3}")  # Expected: 4
    print("Explanation: Buy at 1, sell at 5 → profit = 4\n")

    # Test 4: Buy opportunity in middle
    prices4 = [2, 4, 1, 3, 5]
    result4 = maxProfit(prices4)
    print(f"Prices: {prices4}")
    print(f"Maximum profit: {result4}")  # Expected: 4
    print("Explanation: Buy at 1, sell at 5 → profit = 4\n")

    # Test 5: Single peak
    prices5 = [3, 2, 1, 4]
    result5 = maxProfit(prices5)
    print(f"Prices: {prices5}")
    print(f"Maximum profit: {result5}")  # Expected: 3
    print("Explanation: Buy at 1, sell at 4 → profit = 3\n")

    # Test 6: Two transactions possible but only one allowed
    prices6 = [1, 5, 2, 6]
    result6 = maxProfit(prices6)
    print(f"Prices: {prices6}")
    print(f"Maximum profit: {result6}")  # Expected: 5
    print("Explanation: Buy at 1, sell at 6 → profit = 5")
    print("(Not 1→5 and 2→6, only one transaction allowed)\n")
