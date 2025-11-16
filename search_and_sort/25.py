"""
PROBLEM: Arithmetic Number (GeeksforGeeks)
Given first term 'A', common difference 'C', and target 'B' of an arithmetic sequence,
determine if 'B' exists in the sequence.
Link: https://practice.geeksforgeeks.org/problems/arithmetic-number2815/1

WHY THIS SOLUTION:
This is a MATHEMATICAL problem, not a search problem.
We use the arithmetic sequence formula to check in O(1) time.

Naive: Generate sequence until B or infinity - O(B/C) or infinite!
Mathematical: Use formula - O(1)

KEY INSIGHT:
In arithmetic sequence: a, a+c, a+2c, a+3c, ...
The nth term is: term_n = a + (n-1)*c

For B to be in sequence:
B = a + (n-1)*c
=> (B - a) = (n-1)*c
=> n-1 = (B - a) / c
=> n = (B - a) / c + 1

B exists if and only if:
1. n is a positive integer
2. (B - a) is divisible by c
3. (B - a) / c >= 0

APPROACH:
1. Handle edge case: if c == 0
   - Sequence is just [a, a, a, ...], so B must equal a
2. Check if (B - a) / c < 0
   - Negative means B is before the sequence starts
3. Check if (B - a) % c == 0
   - B is at an exact position in the sequence

TIME COMPLEXITY: O(1) - constant time arithmetic operations
SPACE COMPLEXITY: O(1) - only using variables

EXAMPLE 1: a=1, c=3, b=7
Sequence: 1, 4, 7, 10, 13, ...
(7-1)/3 = 6/3 = 2 (integer) → YES, b exists at position n=3

EXAMPLE 2: a=1, c=3, b=8
Sequence: 1, 4, 7, 10, 13, ...
(8-1)/3 = 7/3 = 2.33... (not integer) → NO, b doesn't exist

EXAMPLE 3: a=5, c=0, b=5
Sequence: 5, 5, 5, ... → YES

WHY INTERVIEWER WILL ACCEPT:
1. Recognizes mathematical solution over brute force
2. Handles edge cases (c=0, negative differences)
3. O(1) optimal solution
4. Shows formula manipulation skills
"""

# Arithmetic Number
# Link: https://practice.geeksforgeeks.org/problems/arithmetic-number2815/1

# a -> initial number, b -> target number, c -> common difference
a, b, c = [int(x) for x in input("Enter a, b, c: ").split()]

# General formula: b = a + (n-1) * c

def if_in_AP(initial, target, diff):
    """
    Check if target exists in arithmetic progression.

    Args:
        initial: First term of AP
        target: Number to check
        diff: Common difference

    Returns:
        1 if target exists in AP, 0 otherwise
    """
    # Edge case: zero common difference
    if diff == 0:
        # Sequence is [initial, initial, initial, ...]
        if initial == target:
            return 1
        else:
            return 0

    # Check if target is reachable from initial
    # (target - initial) must be non-negative for forward progression
    if (target - initial) / diff < 0:
        return 0  # Target is before the sequence starts

    # Check if target is at an exact position
    # (target - initial) must be divisible by diff
    if (target - initial) % diff == 0:
        return 1  # Target exists in the sequence
    else:
        return 0  # Target is between two terms

result = if_in_AP(a, b, c)
if result:
    print("YES, B exists in the arithmetic sequence")
else:
    print("NO, B does not exist in the arithmetic sequence")