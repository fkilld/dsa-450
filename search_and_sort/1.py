"""
PROBLEM: First and Last Occurrence in Sorted Array
Given a sorted array arr containing n elements with possibly duplicate elements,
the task is to find indexes of first and last occurrences of an element x in the given array.

WHY THIS SOLUTION:
We use Binary Search (O(log n)) instead of Linear Search (O(n)) because:
1. The array is SORTED - this is the key constraint that enables binary search
2. For an array of 1 million elements, binary search takes ~20 comparisons vs 1 million for linear search
3. Even though we search twice (first and last), 2*log(n) is still much better than O(n)

APPROACH:
We use a modified binary search that doesn't stop when element is found:
- For FIRST occurrence: When element is found, continue searching LEFT (right = mid - 1)
- For LAST occurrence: When element is found, continue searching RIGHT (left = mid + 1)

This ensures we find the boundary positions even with duplicates.

TIME COMPLEXITY: O(log n) for each search = O(2 log n) = O(log n)
SPACE COMPLEXITY: O(1) - only using variables, no extra data structures

EXAMPLE: arr = [1, 2, 2, 2, 3, 4], m = 2
- First occurrence: index 1
- Last occurrence: index 3
"""

arr = [int(x) for x in input("Enter the array : ").split()]
m = int(input("Enter the number to find : "))

def first_index(arr, m):
    """
    Find the first occurrence of element m using modified binary search.

    Key insight: When we find the element, we don't stop - we keep searching left
    to ensure we get the FIRST occurrence.
    """
    res = -1  # Initialize to -1 to handle case when element doesn't exist
    left = 0
    right = len(arr) - 1

    while right >= left:
        mid = (left + right) // 2

        if arr[mid] < m:
            # Element must be in right half
            left = mid + 1
        elif arr[mid] > m:
            # Element must be in left half
            right = mid - 1
        else:
            # Found the element! But keep searching left for first occurrence
            res = mid
            right = mid - 1  # This is the key: continue searching left

    return res

def last_index(arr, m):
    """
    Find the last occurrence of element m using modified binary search.

    Key insight: When we find the element, we keep searching right
    to ensure we get the LAST occurrence.
    """
    res = -1  # Initialize to -1 to handle case when element doesn't exist
    left = 0
    right = len(arr) - 1

    while right >= left:
        mid = (left + right) // 2

        if arr[mid] < m:
            # Element must be in right half
            left = mid + 1
        elif arr[mid] > m:
            # Element must be in left half
            right = mid - 1
        else:
            # Found the element! But keep searching right for last occurrence
            res = mid
            left = mid + 1  # This is the key: continue searching right

    return res

# Print results
first = first_index(arr, m)
last = last_index(arr, m)

if first != -1:
    print(f"First occurrence: {first}")
    print(f"Last occurrence: {last}")
else:
    print("Element not found in array")
