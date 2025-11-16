"""
PROBLEM: Weighted Job Scheduling (LeetCode)
Given N jobs with start time, end time, and profit, find the maximum profit
subset of non-overlapping jobs.
Link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/

WHY THIS SOLUTION:
Naive: Try all subsets - O(2^N) - exponential!
We use DYNAMIC PROGRAMMING + BINARY SEARCH for O(N log N):
1. Sort jobs by end time
2. For each job, decide: include it or exclude it
3. Use binary search to find latest non-conflicting job

KEY INSIGHT:
dp[i] = maximum profit considering jobs 0 to i

For job i, we have two choices:
1. EXCLUDE job i: profit = dp[i-1]
2. INCLUDE job i: profit = jobs[i].profit + dp[last_non_conflicting_job]

We take the maximum of these two.

Binary search helps find the last job that ends before job i starts.

APPROACH:
1. Create job list: [start, end, profit]
2. Sort by end time
3. Initialize dp[0] = first job's profit
4. For each job i (from 1 to n-1):
   - Find last non-conflicting job using binary search
   - inc = job[i].profit + dp[last] (if exists)
   - exc = dp[i-1]
   - dp[i] = max(inc, exc)
5. Return dp[n-1]

TIME COMPLEXITY: O(N log N)
- Sorting: O(N log N)
- For each job: binary search O(log N)
- Total: O(N log N)

SPACE COMPLEXITY: O(N) - for dp array

EXAMPLE: jobs = [(1,3,50), (2,5,20), (4,6,70), (6,7,30)]
After sorting by end time: same
dp[0] = 50
dp[1]: inc=20, exc=50 → dp[1]=50
dp[2]: last non-conflicting is job 0, inc=70+50=120, exc=50 → dp[2]=120
dp[3]: last non-conflicting is job 2, inc=30+120=150, exc=120 → dp[3]=150
Answer: 150 (jobs 0,2,3)

WHY INTERVIEWER WILL ACCEPT:
1. Shows DP optimization thinking
2. Binary search for optimization
3. Classic interval scheduling problem
4. Optimal O(N log N) solution
"""

# Weighted Job Scheduling in O(n Log n) time
# Question link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/

def max_profit(start, finish, profit):
    """
    Find maximum profit from non-overlapping jobs.

    Args:
        start: List of start times
        finish: List of end times
        profit: List of profits

    Returns:
        Maximum profit achievable
    """
    n = len(start)

    # Create job list: [start, finish, profit]
    jobs = []
    for i in range(n):
        jobs.append([start[i], finish[i], profit[i]])

    # Sort jobs by finish time
    jobs.sort(key=lambda x: x[1])

    # dp[i] = max profit considering jobs 0 to i
    dp = [0] * n
    dp[0] = jobs[0][2]  # First job's profit

    # Process each job
    for i in range(1, n):
        # Option 1: Include current job
        inc = jobs[i][2]  # Current job's profit

        # Find last non-conflicting job using binary search
        last = -1
        low = 0
        high = i - 1

        while low <= high:
            mid = (low + high) // 2
            # Check if job[mid] ends before job[i] starts
            if jobs[mid][1] <= jobs[i][0]:
                last = mid
                low = mid + 1  # Try to find later non-conflicting job
            else:
                high = mid - 1

        # Add profit from last non-conflicting job
        if last != -1:
            inc += dp[last]

        # Option 2: Exclude current job
        exc = dp[i - 1]

        # Take maximum
        dp[i] = max(inc, exc)

    return dp[n - 1]

# Test
# start = [1, 2, 4, 6]
# finish = [3, 5, 6, 7]
# profit = [50, 20, 70, 30]
# print(f"Maximum profit: {max_profit(start, finish, profit)}")

