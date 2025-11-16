"""
PROBLEM: EKO - Eko (SPOJ)
Lumberjack needs M meters of wood. He has a machine that cuts all trees at height H,
taking everything above H. Find the MAXIMUM height H such that he gets at least M meters.

WHY THIS SOLUTION:
Another BINARY SEARCH ON ANSWER problem!
We binary search on the sawblade height.

Naive: Try every possible height - O(max_height * N)
Binary Search: O(N log(max_height))

KEY INSIGHT:
If we can get M meters with height H, we can also get >= M meters with height < H.
This monotonic property enables binary search!

Higher sawblade → Less wood collected
Lower sawblade → More wood collected

We want MAXIMUM height that gives >= M meters.

APPROACH:
1. Sort tree heights (optional, helps with bounds)
2. Binary search on sawblade height [0, max_tree_height]
3. For each mid height:
   - Calculate total wood: sum of (tree[i] - mid) for all tree[i] > mid
   - If total >= M: This height works, try higher (lb = mid + 1)
   - If total < M: Need to cut more, lower blade (ub = mid - 1)
4. Return maximum feasible height

TIME COMPLEXITY: O(N log(max_height))
- Sorting: O(N log N) - optional
- Binary search: log(max_height) iterations
- Each check: O(N) to calculate total wood
- Total: O(N log(max_height))

SPACE COMPLEXITY: O(1) - only using variables

EXAMPLE: trees = [20, 15, 10, 17], M = 7
Binary search on height [0, 20]:
- mid=10: (20-10)+(15-10)+(17-10) = 10+5+7 = 22 >= 7 - works, try higher
- mid=15: (20-15)+(17-15) = 5+2 = 7 >= 7 - works, try higher
- mid=17: (20-17) = 3 < 7 - doesn't work, lower blade
- mid=16: (20-16)+(17-16) = 4+1 = 5 < 7 - doesn't work
Answer: 15

WHY INTERVIEWER WILL ACCEPT:
1. Recognizes binary search on answer
2. Understanding of maximization with constraint
3. Greedy calculation of wood collected
4. SPOJ classic problem
"""

# EKO - Eko

n, m = [int(x) for x in input("Enter n, m : ").split()]
arr = [int(x) for x in input("Enter tree heights : ").split()]

def get_height(arr, n, m):
    """
    Find maximum sawblade height that gives at least m meters of wood.

    Args:
        arr: Array of tree heights
        n: Number of trees
        m: Required meters of wood

    Returns:
        Maximum sawblade height
    """
    arr.sort()

    # Binary search bounds
    lb = 0  # Minimum possible height
    ub = arr[-1]  # Maximum tree height
    ans = 0

    while lb <= ub:
        mid = (lb + ub) // 2

        # Calculate wood collected if sawblade at height mid
        total_cut = 0
        for h in range(n):
            if arr[h] > mid:
                total_cut += arr[h] - mid

        # Check if we get enough wood
        if total_cut >= m:
            ans = mid  # This height works
            lb = mid + 1  # Try higher sawblade (less wood, but maybe still enough)
        else:
            ub = mid - 1  # Need more wood, lower the blade

    return ans

result = get_height(arr, n, m)
print(f"Maximum sawblade height: {result}")