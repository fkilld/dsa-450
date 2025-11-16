"""
PROBLEM: Bishu and Soldiers (HackerEarth)
Bishu fights N soldiers with various powers across Q rounds.
In each round with power M, Bishu can defeat all soldiers with power <= M.
For each round, find: (1) count of defeated soldiers, (2) sum of their powers.
Note: Soldiers respawn after each round.

WHY THIS SOLUTION:
Naive approach: For each query, scan array - O(Q*N)
We use BINARY SEARCH + PREFIX SUM for O((N+Q)*log N):
1. Sort once - enables binary search
2. Precompute prefix sums - enables O(1) sum queries
3. Binary search for each query - O(log N) per query

KEY INSIGHT:
After sorting, if Bishu has power M:
- Binary search finds position where all elements <= M
- This position gives us COUNT of defeated soldiers
- Prefix sum at this position gives TOTAL POWER sum

APPROACH:
1. Sort soldiers array by power
2. Build prefix sum array: prev_sum[i] = sum of first i soldiers
3. For each query with power M:
   - Binary search to find upper bound (first position > M)
   - This index gives count of soldiers with power <= M
   - prev_sum[index] gives their total power

TIME COMPLEXITY:
- Sorting: O(N log N)
- Building prefix sum: O(N)
- Each query: O(log N) for binary search
- Total: O(N log N + Q log N) = O((N+Q) log N)

SPACE COMPLEXITY: O(N) - for sorted array and prefix sum array

EXAMPLE: soldiers = [1, 2, 3, 4, 5, 6, 7]
Sorted: [1, 2, 3, 4, 5, 6, 7]
Prefix sum: [0, 1, 3, 6, 10, 15, 21, 28]

Query 1: Bishu's power = 3
- Binary search finds index 3 (first element > 3 is at index 3)
- Count = 3 soldiers defeated
- Sum = prev_sum[3] = 6

Query 2: Bishu's power = 10
- Binary search finds index 7
- Count = 7 soldiers defeated
- Sum = prev_sum[7] = 28

WHY INTERVIEWER WILL ACCEPT:
1. Shows binary search application for range queries
2. Demonstrates prefix sum optimization
3. Efficient O((N+Q)log N) vs naive O(Q*N)
4. Understanding of upper bound search
"""

# input
# arr = [int(x) for x in input("Enter the power of soldiers : ").split()]
# q = int(input("Enter number of rounds : "))

def bishu(arr):
    """
    Process multiple rounds of Bishu fighting soldiers.
    Uses binary search and prefix sums for efficiency.

    Args:
        arr: Array of soldier powers
    """
    def binary_search(arr, x):
        """
        Find upper bound: first index where arr[i] > x.
        Returns count of elements <= x.

        Args:
            arr: Sorted array
            x: Target value

        Returns:
            Index of first element > x (or len(arr) if all <= x)
        """
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            if arr[mid] <= x:
                l = mid + 1  # Search right half
            else:
                r = mid      # Search left half
        return l

    n = len(arr)
    # Sort to enable binary search
    arr.sort()

    # Build prefix sum array
    # prev_sum[i] = sum of first i soldiers
    prev_sum = [0]
    sum = 0
    for i in range(n):
        sum += arr[i]
        prev_sum.append(sum)

    print("Prefix sums:", prev_sum)

    q = int(input("Enter the number of rounds : "))
    for i in range(q):
        power = int(input("Enter bishu's power : "))

        # Find how many soldiers can be defeated
        index = binary_search(arr, power)

        # Print count and sum
        print(f"Count: {index}, Total power sum: {prev_sum[index]}")

# Test with example
bishu([1, 2, 3, 4, 5, 6, 7])

# Solution reference: https://paste.ubuntu.com/p/Q6TqPnCQfN/