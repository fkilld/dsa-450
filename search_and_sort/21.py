"""
PROBLEM: Aggressive Cows (SPOJ)
Place C cows in N stalls such that the minimum distance between any two cows
is MAXIMIZED. Find this maximum minimum distance.

WHY THIS SOLUTION:
This is a classic BINARY SEARCH ON ANSWER problem.
We don't search for positions - we search for the ANSWER (minimum distance)!

Naive approach: Try all combinations - O(N^C) - exponential!
Binary search on answer: O(N log N + N log(max_position))

KEY INSIGHT:
If we can place C cows with minimum distance D, we can also place them with
any distance < D. This MONOTONIC property enables binary search!

Search space: minimum distance from 0 to (max_position - min_position)

APPROACH:
1. Sort stall positions
2. Binary search on minimum distance (not positions!)
3. For each mid value, check: "Can we place C cows with min distance = mid?"
   - Greedy: Place first cow at arr[0]
   - Place next cow at first position >= prev + mid
   - If we can place all C cows, answer is feasible
4. If feasible, try larger distance (lb = mid + 1)
   If not feasible, try smaller distance (ub = mid - 1)

TIME COMPLEXITY: O(N log N + N * log(max_position))
- Sorting: O(N log N)
- Binary search: log(10^9) ≈ 30 iterations
- Each check: O(N)
- Total: O(N log N)

SPACE COMPLEXITY: O(1) - only using variables

EXAMPLE: stalls = [1, 2, 8, 4, 9], C = 3
Sorted: [1, 2, 4, 8, 9]
Binary search on distance [0, 8]:
- Try mid=4: Place at 1, 8 (only 2 cows) - not feasible
- Try mid=2: Place at 1, 4, 8 (3 cows) - feasible!
- Try mid=3: Place at 1, 4, 8 (3 cows) - feasible!
- Try mid=4: Not feasible
Answer: 3

WHY INTERVIEWER WILL ACCEPT:
1. Recognizes "binary search on answer" pattern
2. Understanding of monotonic property
3. Greedy placement strategy
4. Classic competitive programming problem
"""

# Aggressive Cows

t = int(input("No. of test cases : "))
for _ in range(t):
    n, c = [int(x) for x in input("Enter n, c : ").split()]
    arr = []  # Stall positions

    for i in range(n):
        arr.append(int(input("Enter the stall position : ")))

    # Sort stalls to enable greedy placement
    arr.sort()

    # Binary search on the answer (minimum distance)
    lb = 0
    ub = 10 ** 9  # Maximum possible distance
    ans = 0

    while lb <= ub:
        mid = (lb + ub) // 2  # Try this as minimum distance

        # Check if we can place C cows with minimum distance = mid
        cow = 1  # Place first cow at arr[0]
        prev = arr[0]

        for i in range(1, len(arr)):
            # If current stall is at least 'mid' distance from previous cow
            if arr[i] - prev >= mid:
                prev = arr[i]  # Place cow here
                cow += 1
                if cow == c:
                    break

        # If we successfully placed all C cows
        if cow == c:
            ans = mid  # This distance works
            lb = mid + 1  # Try for larger distance
        else:
            ub = mid - 1  # Try smaller distance

    print(f"Maximum minimum distance: {ans}")
        