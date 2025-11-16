"""
PROBLEM: Smallest Factorial Number
Given a number n, find the smallest number whose factorial contains at least n trailing zeros.

WHY THIS SOLUTION:
We use BINARY SEARCH ON ANSWER combined with mathematical formula for trailing zeros.

Naive: Calculate factorials one by one - O(answer * log(answer))
Binary Search: O(log(answer) * log(answer))

KEY INSIGHT:
Trailing zeros in n! come from factors of 10 = 2 × 5.
Since there are always more 2s than 5s in n!, count of trailing zeros = count of 5s.

Count of 5s in n! = floor(n/5) + floor(n/25) + floor(n/125) + ...

Example: 25! has floor(25/5) + floor(25/25) = 5 + 1 = 6 trailing zeros

If we want n trailing zeros, we binary search for the smallest number whose
factorial has >= n trailing zeros.

APPROACH:
1. Binary search on answer [0, 5*n]
   - Upper bound: 5*n is safe (each multiple of 5 adds at least 1 zero)
2. For each mid value, count trailing zeros using formula
3. If count >= n: This works, try smaller (high = mid)
   If count < n: Need larger number (low = mid + 1)
4. Return the smallest number that works

TIME COMPLEXITY: O(log(n) * log(n))
- Binary search: O(log(5n)) = O(log n)
- Counting zeros: O(log n) - dividing by 5, 25, 125, ...
- Total: O(log^2 n)

SPACE COMPLEXITY: O(1) - only using variables

EXAMPLE: Find smallest number with 6 trailing zeros
Binary search [0, 30]:
- mid=15: zeros = 15/5 + 15/25 = 3 + 0 = 3 < 6 → search right
- mid=22: zeros = 22/5 + 22/25 = 4 + 0 = 4 < 6 → search right
- mid=26: zeros = 26/5 + 26/25 = 5 + 1 = 6 >= 6 → search left
- mid=25: zeros = 25/5 + 25/25 = 5 + 1 = 6 >= 6 → search left
- mid=24: zeros = 24/5 + 24/25 = 4 + 0 = 4 < 6 → search right
Answer: 25 (25! has exactly 6 trailing zeros)

WHY INTERVIEWER WILL ACCEPT:
1. Mathematical insight about factorial zeros
2. Binary search on answer pattern
3. Efficient O(log^2 n) solution
4. Understanding of number theory
"""

# Smallest factorial number

n = int(input("Enter n: "))

def check(p, n):
    """
    Check if p! has at least n trailing zeros.

    Args:
        p: Number to check factorial of
        n: Required trailing zeros

    Returns:
        True if p! has >= n trailing zeros
    """
    count = 0
    f = 5

    # Count factors of 5 in p!
    # This gives us the number of trailing zeros
    while f <= p:
        count += p // f  # Add multiples of current power of 5
        f *= 5           # Move to next power of 5

    return count >= n

def find_min(n):
    """
    Find smallest number whose factorial has at least n trailing zeros.

    Args:
        n: Required trailing zeros

    Returns:
        Smallest number
    """
    # Edge case: need at least 1 zero
    if n == 1:
        return 5  # 5! = 120 has 1 trailing zero

    # Binary search on the answer
    low = 0
    high = 5 * n  # Safe upper bound

    while low < high:
        mid = (low + high) // 2

        # Check if mid! has enough trailing zeros
        if check(mid, n):
            high = mid  # This works, try smaller
        else:
            low = mid + 1  # Need larger number

    return low

result = find_min(n)
print(f"Smallest number whose factorial has {n} trailing zeros: {result}")