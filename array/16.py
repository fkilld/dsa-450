# Best Time to Buy and Sell Stock
"""
Problem Statement:
Given an array 'prices' where prices[i] is the price of a given stock on the i-th day,
find the maximum profit you can achieve by buying one stock and selling it later.
You want to maximize profit by choosing a single day to buy and a different day in the future to sell.
If you cannot achieve any profit, return 0.

Example:
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Approach:
- Keep track of the minimum buying price seen so far
- For each price, calculate the potential profit and update the maximum profit if needed
- Only one transaction (buy once, sell once) is allowed

Time Complexity: O(n) - We iterate through the array once
Space Complexity: O(1) - We use constant extra space
"""

def maxProfit(prices):
    # Initialize the maximum profit to 0 (default if no profit can be made)
    sell = 0
    # Initialize the minimum buying price to the first day's price
    buy = prices[0]
    # Iterate through each price in the array
    for pr in prices:
        # If current price is lower than our buying price, update the buying price
        # This is a better day to buy the stock
        if pr <= buy:
            buy = pr
        # If current price is higher than our buying price, we can make profit
        else:
            # Calculate potential profit and update if it's better than our current maximum
            if pr - buy > sell:
                sell = pr - buy
    # Return the maximum profit possible
    return sell

maxProfit([7, 1, 5, 3, 6, 4]) # Expected output: 5 (buy at 1 and sell at 6)
# maxProfit([7, 6, 4, 3, 1]) # Expected output: 0 (no profit possible)
# maxProfit([1, 2, 3, 4, 5]) # Expected output: 4 (buy at 1 and sell at 5)
# maxProfit([2, 4, 1, 3, 5]) # Expected output: 4 (buy at 1 and sell at 5)