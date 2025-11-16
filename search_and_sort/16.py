"""
PROBLEM: Sort by Set Bit Count
Given an array of integers, sort the array in descending order according to
count of set bits in binary representation of array elements.
Note: For integers having same number of set bits, maintain their original order (stable sort).

WHY THIS SOLUTION:
We use Python's built-in stable sort with a custom key function.
This leverages:
1. Timsort (Python's sort) - already stable, O(n log n)
2. bin().count('1') - efficient bit counting

KEY INSIGHT:
Python's sort is STABLE - elements with equal keys maintain their relative order.
This automatically handles the requirement for same bit count elements.

Alternative approaches:
- Manual bit counting with Brian Kernighan's algorithm
- Bucket sort by bit count (0-32 buckets for 32-bit integers)
- Priority queue with custom comparator

APPROACH:
1. Use sort() with reverse=True for descending order
2. Key function: count number of '1's in binary representation
3. Python's stable sort ensures equal elements maintain original order

TIME COMPLEXITY: O(n log n)
- Sorting: O(n log n)
- Bit counting for each element: O(log(max_value)) ≈ O(32) = O(1) for integers
- Total: O(n log n)

SPACE COMPLEXITY: O(1) if in-place, O(n) for Timsort's merge operations

EXAMPLE: arr = [5, 2, 3, 9, 4, 6, 7, 15, 32]
Binary representations and bit counts:
5 = 101 (2 bits), 2 = 10 (1 bit), 3 = 11 (2 bits), 9 = 1001 (2 bits)
4 = 100 (1 bit), 6 = 110 (2 bits), 7 = 111 (3 bits), 15 = 1111 (4 bits), 32 = 100000 (1 bit)

Sorted by bit count (descending):
15(4 bits), 7(3 bits), 5(2 bits), 3(2 bits), 9(2 bits), 6(2 bits), 2(1 bit), 4(1 bit), 32(1 bit)

WHY INTERVIEWER WILL ACCEPT:
1. Clean, Pythonic solution using built-in functions
2. Understanding of stable sort property
3. Knowledge of binary representations
4. Efficient O(n log n) solution
"""

# Input array
# arr = [int(x) for x in input("Enter the array : ").split()]
arr = [5, 2, 3, 9, 4, 6, 7, 15, 32]

def sort_by_bits(arr):
    """
    Sort array in descending order by count of set bits.
    Maintains stability for elements with same bit count.

    Args:
        arr: Array of integers

    Returns:
        Sorted array
    """
    # Alternative approach using separate function:
    # def count_bits(a):
    #     """Count number of 1s in binary representation."""
    #     return bin(a).count('1')
    #
    # arr.sort(reverse=True, key=count_bits)

    # Inline lambda approach - more concise
    # bin(x) converts to binary string like '0b101'
    # .count('1') counts occurrences of '1' character
    arr.sort(reverse=True, key=lambda x: bin(x).count('1'))
    return arr

print(sort_by_bits(arr))