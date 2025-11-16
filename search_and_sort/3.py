"""
PROBLEM: Search in Rotated Sorted Array
An ascending sorted array is rotated at an unknown pivot index.
Find a target value in O(log n) time.

Example: [0,1,2,4,5,6,7] rotated at index 3 becomes [4,5,6,7,0,1,2]

WHY THIS SOLUTION:
We use Modified Binary Search because:
1. Standard binary search won't work - array is not fully sorted
2. But linear search O(n) is too slow when better solution exists
3. Key insight: After rotation, ONE half is always sorted

The rotated array has this property:
- At any mid point, either left half [left...mid] OR right half [mid...right] is sorted
- We can identify which half is sorted by comparing arr[left] with arr[mid]
- Once we know which half is sorted, we can check if target is in that sorted half

This maintains O(log n) complexity!

APPROACH:
1. Find mid point
2. Determine which half is sorted:
   - If arr[left] <= arr[mid]: left half is sorted
   - Otherwise: right half is sorted
3. Check if target is in the sorted half using simple comparison
4. Search in the appropriate half

TIME COMPLEXITY: O(log n) - binary search
SPACE COMPLEXITY: O(1) - iterative approach

EXAMPLE: arr = [4,5,6,7,0,1,2], target = 0
Step 1: mid=3 (value 7), left half [4,5,6,7] is sorted, target not in it, search right
Step 2: mid=5 (value 1), right half [1,2] is sorted, target in left
Step 3: mid=4 (value 0), found!

WHY INTERVIEWER WILL ACCEPT:
- Recognizes the "sorted but rotated" pattern
- Optimizes from O(n) to O(log n) using binary search variant
- Handles all edge cases (no rotation, rotation at different points)
"""

arr = [int(x) for x in input("Enter the rotated sorted array : ").split()]
target = int(input("Enter the number to find in array : "))

def find(arr, x):
    """
    Search for target x in rotated sorted array using modified binary search.

    The key insight: In a rotated sorted array, at least one half is always sorted.
    We identify the sorted half and decide which half to search.
    """
    left = 0
    right = len(arr) - 1

    while right >= left:
        mid = (left + right) // 2

        # Found the target
        if arr[mid] == x:
            return mid

        # Check if LEFT half is sorted
        # If arr[left] <= arr[mid], elements from left to mid are in order
        if arr[mid] >= arr[left]:
            # Left half is sorted, check if target is in this sorted range
            if x >= arr[left] and x <= arr[mid]:
                # Target is in sorted left half
                right = mid - 1
            else:
                # Target must be in right half
                left = mid + 1
        else:
            # RIGHT half is sorted (arr[mid] < arr[left] means rotation point is in left half)
            # Check if target is in the sorted right range
            if x >= arr[mid] and x <= arr[right]:
                # Target is in sorted right half
                left = mid + 1
            else:
                # Target must be in left half
                right = mid - 1

    # Target not found in array
    return -1

result = find(arr, target)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in array")
