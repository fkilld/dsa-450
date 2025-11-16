"""
PROBLEM: Count Perfect Squares Less Than N
Given a number N, count how many perfect squares (1, 4, 9, 16, 25...) are less than N.

WHY THIS SOLUTION:
This is a MATHEMATICAL problem, not a searching problem!

Bad approach: O(n) - iterate and check each number if it's a perfect square
Good approach: O(1) - use math!

KEY INSIGHT:
If we want perfect squares < N, we need to find the largest k where k² < N
This means k < √N
So the count is simply floor(√N) or floor(√N) - 1 depending on whether N itself is a perfect square

APPROACH:
1. Calculate √N
2. If N is a perfect square (k² == N), exclude it: return k - 1
3. If N is not a perfect square, include floor(√N): return k

This reduces O(n) to O(1)!

TIME COMPLEXITY: O(1) - just one square root operation
SPACE COMPLEXITY: O(1)

EXAMPLE 1: N = 10
√10 ≈ 3.16, floor = 3
3² = 9 ≠ 10, so N is not a perfect square
Perfect squares < 10: 1, 4, 9 → count = 3 ✓

EXAMPLE 2: N = 16
√16 = 4
4² = 16 == N, so N IS a perfect square
Perfect squares < 16: 1, 4, 9 → count = 3 (exclude 16 itself)
Return 4 - 1 = 3 ✓

WHY INTERVIEWER WILL ACCEPT:
- Recognizes that this is a math problem, not a brute force problem
- Optimizes from O(n) to O(1) using mathematical insight
- Shows understanding of perfect squares and square roots
"""

from math import sqrt

n = int(input("Enter the number : "))

# Calculate the floor of square root of n
num = int(sqrt(n))

# Check if n itself is a perfect square
if num * num == n:
    # n is a perfect square, exclude it from count
    # Example: n=16, num=4, perfect squares < 16 are 1,4,9 (count=3)
    print(num - 1)
else:
    # n is not a perfect square, include num
    # Example: n=10, num=3, perfect squares < 10 are 1,4,9 (count=3)
    print(num)
