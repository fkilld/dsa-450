"""
PROBLEM: Product Array Puzzle
Given an array nums[] of size n, construct a Product Array P (of same size n)
such that P[i] is equal to the product of all elements except nums[i].
Constraint: Cannot use division operator.

WHY THIS SOLUTION:
If division allowed: Calculate total product, then P[i] = total_product / nums[i]
But without division, we need a clever approach using LEFT and RIGHT products.

KEY INSIGHT:
For each index i, the product of all elements except nums[i] equals:
Product of all elements to the LEFT of i × Product of all elements to the RIGHT of i

We can precompute these in two passes!

APPROACH:
1. Create left[] array where left[i] = product of all elements left of i
2. Create right[] array where right[i] = product of all elements right of i
3. Result: res[i] = left[i] × right[i]

Building left array:
- left[0] = 1 (no elements to the left)
- left[i] = left[i-1] × arr[i-1]

Building right array:
- right[n-1] = 1 (no elements to the right)
- right[i] = right[i+1] × arr[i+1]

TIME COMPLEXITY: O(n)
- First pass to build left array: O(n)
- Second pass to build right array: O(n)
- Third pass to compute result: O(n)
- Total: O(n)

SPACE COMPLEXITY: O(n) - for left and right arrays

EXAMPLE: arr = [10, 3, 5, 6, 2]
Left array:  [1, 10, 30, 150, 900]
Right array: [180, 60, 12, 2, 1]
Result:      [1×180, 10×60, 30×12, 150×2, 900×1] = [180, 600, 360, 300, 900]

Verification: P[1] = 10×5×6×2 = 600 ✓

WHY INTERVIEWER WILL ACCEPT:
1. Shows understanding of prefix/suffix computation pattern
2. Avoids division operator cleverly
3. Optimal O(n) solution
4. Clear thought process about decomposing the problem
"""

# arr = [int(x) for x in input("Enter the array : ").split()]
arr = [10, 3, 5, 6, 2]

def puzzle_product(arr):
    """
    Calculate product array without using division operator.
    Uses left and right product arrays.

    Args:
        arr: Input array of integers

    Returns:
        Array where P[i] = product of all elements except arr[i]
    """
    n = len(arr)
    res = []
    l = [0] * n  # Left products: l[i] = product of all elements left of i
    r = [0] * n  # Right products: r[i] = product of all elements right of i

    # Initialize boundaries
    l[0] = 1      # No elements to the left of index 0
    r[n-1] = 1    # No elements to the right of index n-1

    # Build left product array
    # l[i] contains product of all elements from index 0 to i-1
    for i in range(1, n):
        l[i] = l[i - 1] * arr[i - 1]

    # Build right product array
    # r[i] contains product of all elements from index i+1 to n-1
    for i in range(n-2, -1, -1):
        r[i] = r[i + 1] * arr[i + 1]

    # Compute result: product of left and right for each index
    for i in range(n):
        res.append(l[i] * r[i])

    return res

print(*puzzle_product(arr))