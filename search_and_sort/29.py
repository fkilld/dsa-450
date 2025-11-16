"""
PROBLEM: SUBSUMS - Subset Sums (SPOJ)
Given N numbers (1 ≤ N ≤ 34) where -20M ≤ Si ≤ 20M,
count how many subsets have sum in range [A, B] where -500M ≤ A ≤ B ≤ 500M.

WHY THIS SOLUTION:
This is a MEET IN THE MIDDLE problem!

Naive: Generate all 2^N subsets - O(2^34) ≈ 17 billion - too slow!
Meet in Middle: O(2^(N/2) * log(2^(N/2))) ≈ 130K * 17 - feasible!

KEY INSIGHT:
We can't generate all 2^34 subsets, but we CAN generate all 2^17 subsets!
Split array into two halves:
- Generate all subset sums for left half (2^17 sums)
- Generate all subset sums for right half (2^17 sums)
- For each sum in left half, binary search in right half for valid complements

If we want total sum in [A, B]:
- For each left_sum, we need right_sum where A ≤ left_sum + right_sum ≤ B
- This means: A - left_sum ≤ right_sum ≤ B - left_sum

APPROACH:
1. Split array into two halves
2. Generate all subset sums for left half (2^(n/2) subsets)
3. Generate all subset sums for right half (2^(n/2) subsets)
4. Sort right half sums
5. For each sum in left half:
   - Find count of right sums in range [A - left_sum, B - left_sum]
   - Use binary search (bisect_left and bisect_right)
6. Sum all counts

TIME COMPLEXITY: O(2^(N/2) * N/2)
- Generating each half: O(2^(N/2) * N/2)
- Sorting right half: O(2^(N/2) * log(2^(N/2)))
- Binary search for each left sum: O(2^(N/2) * log(2^(N/2)))
- Total: O(2^(N/2) * N/2)

SPACE COMPLEXITY: O(2^(N/2)) - for storing subset sums

EXAMPLE: arr = [1, -2, 3], A = -1, B = 2
Left half: [1] → sums: [0, 1]
Right half: [-2, 3] → sums: [0, -2, 3, 1]
Sorted right: [-2, 0, 1, 3]

For left_sum=0: need right_sum in [-1, 2] → count 3: [-2, 0, 1]
For left_sum=1: need right_sum in [-2, 1] → count 3: [-2, 0, 1]
Total: 6 subsets

WHY INTERVIEWER WILL ACCEPT:
1. Meet in the middle technique
2. Optimization from O(2^N) to O(2^(N/2))
3. Binary search application
4. Understanding of subset generation using bits
"""

# SUBSUMS - Subset Sums

# module to use bisect_left (lower_bound in C++)
# and bisect_right (upper_bound in C++)
import bisect

n, a, b = [int(x) for x in input("Enter n, a, b: ").split()]
arr = []

# Read n numbers
for i in range(n):
    arr.append(int(input("Enter number: ")))

def solve(arr, st, ed, v):
    """
    Generate all subset sums for arr[st:ed+1] using bit manipulation.

    Args:
        arr: Input array
        st: Start index
        ed: End index
        v: List to store subset sums
    """
    n = ed - st + 1  # Length of subarray

    # Generate all 2^n subsets using bit manipulation
    for i in range(2**n):
        s = 0
        j = st
        x = i

        # Use bits of i to select elements
        while x:
            if x & 1:  # If bit is set
                s += arr[j]
            j += 1
            x = x >> 1  # Right shift

        v.append(s)

def total_count(arr, a, b):
    """
    Count subsets with sum in range [a, b] using meet in the middle.

    Args:
        arr: Input array
        a: Lower bound of sum range
        b: Upper bound of sum range

    Returns:
        Count of valid subsets
    """
    n = len(arr)
    count = 0
    v1 = []  # Subset sums of first half
    v2 = []  # Subset sums of second half

    # Generate all subset sums for both halves
    solve(arr, 0, (n // 2) - 1, v1)
    solve(arr, n // 2, n - 1, v2)

    # Sort second half for binary search
    v2.sort()

    # For each sum in first half, find valid sums in second half
    for i in range(len(v1)):
        # We need: a ≤ v1[i] + v2[j] ≤ b
        # So: a - v1[i] ≤ v2[j] ≤ b - v1[i]
        low = bisect.bisect_left(v2, a - v1[i])   # First valid index
        high = bisect.bisect_right(v2, b - v1[i])  # Last valid index + 1
        count += high - low

    return count

result = total_count(arr, a, b)
print(f"Number of subsets with sum in [{a}, {b}]: {result}")

