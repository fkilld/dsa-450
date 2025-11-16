"""
PROBLEM: PRATA - Roti Prata (SPOJ)
P pratas need to be made by L cooks with different ranks.
A cook with rank R takes:
- R minutes for 1st prata
- R + 2R = 3R minutes for 2nd prata (cumulative)
- 3R + 3R = 6R minutes for 3rd prata (cumulative)
- Generally: R + 2R + 3R + ... + nR = R*(n*(n+1)/2) for n pratas

Find the MINIMUM time needed to cook all P pratas.
Link: https://www.spoj.com/problems/PRATA/

WHY THIS SOLUTION:
Another BINARY SEARCH ON ANSWER problem!
We binary search on the time, not the allocation.

Naive: Try all time values - O(max_time * L)
Binary Search: O(L * log(max_time) * sqrt(P))

KEY INSIGHT:
If we can cook P pratas in T time, we can also cook them in > T time.
This monotonic property enables binary search!

For a given time T and cook with rank R:
- Solve: R*(n*(n+1)/2) <= T
- This gives us max pratas this cook can make

APPROACH:
1. Binary search on time [0, worst_case]
   - Worst case: 1 cook with highest rank makes all pratas
   - Time = R*(P*(P+1)/2)
2. For each mid time:
   - Calculate how many pratas each cook can make
   - Sum up all pratas
   - If total >= P: This time works, try smaller
   - Else: Need more time
3. Return minimum time that works

TIME COMPLEXITY: O(L * log(time) * sqrt(P))
- Binary search: O(log(10^8))
- Each check: O(L * sqrt(P)) - for each cook, solve quadratic
- Total: O(L * log(time) * sqrt(P))

SPACE COMPLEXITY: O(1)

EXAMPLE: P=10, cooks=[1,2,3,4]
Cook 1 (rank=1): 1,3,6,10,15,21,28,36,45,55 minutes for 1-10 pratas
Cook 2 (rank=2): 2,6,12,20,30,42,56,72,90,110 minutes
...
Binary search finds minimum time where total pratas >= 10

WHY INTERVIEWER WILL ACCEPT:
1. Binary search on answer pattern
2. Mathematical formula for series sum
3. Understanding of parallel task completion
4. SPOJ problem solving skills
"""

# PRATA - Roti Prata
# Link: https://www.spoj.com/problems/PRATA/

p = int(input("Enter no. of parathas: "))
n = int(input("Enter no. of chefs: "))
arr = [int(x) for x in input("Enter ranks: ").split()]

def check(arr, n, p, mid):
    """
    Check if we can make p pratas in mid time with given cooks.

    Args:
        arr: Array of cook ranks
        n: Number of cooks
        p: Number of pratas needed
        mid: Time limit to check

    Returns:
        True if we can make >= p pratas in mid time
    """
    paratha = 0

    # Calculate pratas each cook can make in mid time
    for i in range(n):
        time = 0
        j = 1  # Multiplier for current prata

        # For cook with rank arr[i]:
        # 1st prata: arr[i] minutes
        # 2nd prata: arr[i]*2 more minutes
        # 3rd prata: arr[i]*3 more minutes, etc.
        while time + arr[i] * j <= mid:
            time += arr[i] * j
            paratha += 1
            j += 1

        # Early exit if we already have enough pratas
        if paratha >= p:
            return True

    return paratha >= p

def min_time(p, arr):
    """
    Find minimum time to make p pratas.

    Args:
        p: Number of pratas needed
        arr: Array of cook ranks

    Returns:
        Minimum time needed
    """
    # Binary search on time
    lb = 0
    ub = 10**8  # Worst case: 1 cook with rank 8 makes 1000 pratas
    ans = ub

    while lb <= ub:
        mid = (lb + ub) // 2

        # Check if mid time is sufficient
        if check(arr, len(arr), p, mid):
            ans = mid  # This works, try smaller time
            ub = mid - 1
        else:
            lb = mid + 1  # Need more time

    return ans

result = min_time(p, arr)
print(f"Minimum time needed: {result} minutes")
