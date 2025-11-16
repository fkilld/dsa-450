"""
PROBLEM: Merge Two Sorted Arrays Without Extra Space
Given two sorted arrays arr1[] of size N and arr2[] of size M,
merge them into one sorted order without using any extra space.
Final result: arr1 contains first N smallest elements, arr2 contains rest.

WHY THIS SOLUTION:
Using extra space O(n+m) is trivial - just merge into new array.
The challenge: merge IN-PLACE with O(1) space.

We implement TWO methods:
1. INSERTION METHOD - O(n*m) time, simple to understand
2. GAP METHOD (Shell Sort inspired) - O((n+m)*log(n+m)) time, optimal

KEY INSIGHT (Gap Method):
Treat both arrays as ONE virtual array and apply Shell Sort's gap technique:
- Start with gap = ceil((n+m)/2)
- Compare and swap elements that are 'gap' distance apart
- Reduce gap by half each iteration
- When gap becomes 0, arrays are merged

APPROACH (Gap Method):
1. Calculate initial gap = ceil((n+m)/2)
2. While gap > 0:
   a. Compare elements within arr1 that are 'gap' apart
   b. Compare elements across arr1 and arr2 that are 'gap' apart
   c. Compare elements within arr2 that are 'gap' apart
   d. Reduce gap: gap = ceil(gap/2)
3. Arrays are now merged in-place

TIME COMPLEXITY:
- Insertion Method: O(n*m) - for each element in arr2, scan arr1
- Gap Method: O((n+m) * log(n+m)) - log(n+m) passes, each pass O(n+m)

SPACE COMPLEXITY: O(1) - only using pointers, no extra arrays

EXAMPLE: arr1 = [1, 5, 9, 10, 15, 20], arr2 = [2, 3, 8, 13]
Gap method with gap=5:
- Compare arr1[0] with arr2[0]: 1 vs 2 (no swap)
- Compare arr1[1] with arr2[1]: 5 vs 3 (swap)
- Continue reducing gap until fully merged
Final: arr1 = [1, 2, 3, 5, 8, 9], arr2 = [10, 13, 15, 20]

WHY INTERVIEWER WILL ACCEPT:
1. Understanding of in-place constraints
2. Knowledge of Shell Sort and its applications
3. Ability to think of arrays as unified structure
4. Shows optimization from O(n*m) to O((n+m)*log(n+m))
"""

arr1 = [int(x) for x in input("Enter array 1: ").split()]
arr2 = [int(x) for x in input("Enter array 2: ").split()]

# METHOD 1: Insertion-based merge
def merge(arr1, arr2):
    """
    Merge two sorted arrays using insertion technique.
    For each element in arr2, find its correct position in arr1.

    Time: O(n*m), Space: O(1)
    """
    n = len(arr1)
    m = len(arr2)

    # Process arr2 elements from end to beginning
    for i in range(m-1, -1, -1):
        last = arr1[n-1]  # Store last element of arr1
        j = n - 2

        # Shift arr1 elements that are greater than arr2[i]
        while j >= 0 and arr1[j] > arr2[i]:
            arr1[j + 1] = arr1[j]
            j -= 1

        # If shifting occurred, place arr2[i] in arr1 and last in arr2
        if j != n - 2 or last > arr2[i]:
            arr1[j + 1] = arr2[i]
            arr2[i] = last

    return arr1, arr2

# METHOD 2: Gap method (Shell Sort inspired) - OPTIMAL
def next_gap(gap):
    """Calculate next gap for Shell Sort style merging."""
    if gap > 1:
        return (gap // 2) + (gap % 2)  # Ceiling division
    else:
        return 0

def gap_merge(arr1, arr2):
    """
    Merge two sorted arrays using gap method (Shell Sort technique).
    Treat both arrays as one virtual array and compare elements 'gap' apart.

    Time: O((n+m)*log(n+m)), Space: O(1)
    """
    n = len(arr1)
    m = len(arr2)
    gap = next_gap(n + m)

    while gap > 0:
        # Phase 1: Compare elements within arr1
        i = 0
        while i + gap < n:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1

        # Phase 2: Compare elements across arr1 and arr2
        j = gap - n if gap > n else 0
        while i < n and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

        # Phase 3: Compare elements within arr2
        if j < m:
            j = 0
            while j + gap < m:
                if arr2[j] > arr2[j + gap]:
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                j += 1

        # Reduce gap for next iteration
        gap = next_gap(gap)

    return arr1, arr2

# Test with gap method (optimal solution)
result1, result2 = gap_merge(arr1, arr2)
print("Array 1:", result1)
print("Array 2:", result2)

