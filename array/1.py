"""
PROBLEM: Maximum and Minimum of an Array using Minimum Number of Comparisons
==============================================================================
Find both the maximum and minimum elements in an array with the least number of comparisons.

Example:
    Input:  [3, 5, 1, 2, 4, 8]
    Output: min = 1, max = 8

APPROACH: Pair-wise Comparison
================================
WHY THIS APPROACH?
- Naive approach: Compare each element with min and max → 2(n-1) comparisons
- Optimized approach: Compare pairs first, then with min/max → ~1.5n comparisons
- This reduces comparisons by comparing elements in pairs before comparing with min/max

HOW IT WORKS:
1. If array has odd length: Initialize min and max to first element
2. If array has even length: Compare first two elements and set min and max accordingly
3. Process remaining elements in pairs:
   - Compare two elements with each other first (1 comparison)
   - Compare smaller one with current min (1 comparison)
   - Compare larger one with current max (1 comparison)
   - Total: 3 comparisons per 2 elements = 1.5 comparisons per element

FLOW EXAMPLE:
=============
Array: [3, 5, 1, 2, 4, 8]

Step 1: Initialize (even length)
    Compare arr[0]=3 and arr[1]=5
    min = 3, max = 5

Step 2: Compare pair (3, 1)
    3 < 1? No, so compare:
    - 1 < min(3)? Yes → min = 1
    - 3 > max(5)? No → max = 5

Step 3: Compare pair (2, 4)
    2 < 4? Yes, so compare:
    - 2 < min(1)? No → min = 1
    - 4 > max(5)? No → max = 5

Step 4: Compare pair (8, [next element if exists])
    8 < next? (no next element, but we compare 8)
    - 8 > max(5)? Yes → max = 8

Final: min = 1, max = 8

COMPARISON COUNT:
- Naive: 2(n-1) = 2(6-1) = 10 comparisons
- Optimized: 1 + 3(n/2) = 1 + 3(3) = 10 comparisons (approximately 1.5n)

TIME COMPLEXITY:  O(n) - Single pass through array
SPACE COMPLEXITY: O(1) - Only using two variables for min and max
"""

# Test array
# arr = [int(x) for x in input("Enter the array : ").split()]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def max_and_min(arr):
    """
    Find minimum and maximum elements using minimum comparisons.

    Args:
        arr: List of integers

    Returns:
        Tuple (min_element, max_element)
    """
    n = len(arr)

    # Initialize min and max based on whether array length is odd or even
    if n % 2 != 0:
        # Odd length: Use first element for both min and max initially
        arr_min = arr[0]
        arr_max = arr[0]
    else:
        # Even length: Compare first two elements to initialize
        if arr[0] < arr[1]:
            arr_min = arr[0]
            arr_max = arr[1]
        else:
            arr_min = arr[1]
            arr_max = arr[0]

    # Process remaining elements in pairs
    # This reduces total comparisons by comparing pairs first
    for i in range(n - 1):
        # Compare the pair arr[i] and arr[i+1]
        if arr[i] < arr[i + 1]:
            # arr[i] is smaller, arr[i+1] is larger in this pair
            # Check if smaller element is less than current min
            if arr[i] < arr_min:
                arr_min = arr[i]
            # Check if larger element is greater than current max
            if arr[i + 1] > arr_max:
                arr_max = arr[i + 1]
        else:
            # arr[i+1] is smaller, arr[i] is larger in this pair
            # Check if smaller element is less than current min
            if arr[i + 1] < arr_min:
                arr_min = arr[i + 1]
            # Check if larger element is greater than current max
            if arr[i] > arr_max:
                arr_max = arr[i]

    return arr_min, arr_max

# Test the function
# Expected output: (1, 9)
print(max_and_min(arr))