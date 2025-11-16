"""
PROBLEM: Find Pair with Given Difference
Given a sorted array and a number N, find if there exists a pair with difference N.

WHY THIS SOLUTION:
This is the "Two Pointer" technique on a SORTED array - super efficient!

Naive approach: O(n²) - check all pairs
Better approach: Binary search for each element - O(n log n)
Best approach (this): Two pointers - O(n)!

KEY INSIGHT: Sorted Array + Two Pointers
Since array is sorted, we can maintain two pointers and make smart decisions:
- If difference is too small → move right pointer forward (increase difference)
- If difference is too large → move left pointer forward (decrease difference)

This works because array is SORTED!

APPROACH:
1. Sort the array first (if not sorted)
2. Use two pointers: i = 0, j = 1
3. While both in bounds:
   - If arr[j] - arr[i] == target: found!
   - If arr[j] - arr[i] < target: increment j (need larger difference)
   - If arr[j] - arr[i] > target: increment i (need smaller difference)

TIME COMPLEXITY: O(n log n) for sorting + O(n) for two pointers = O(n log n)
SPACE COMPLEXITY: O(1) - if we ignore sorting space

EXAMPLE: arr = [5, 20, 3, 2, 5, 80], target_diff = 78
After sorting: [2, 3, 5, 5, 20, 80]

i=0, j=1: arr[1]-arr[0] = 3-2 = 1 < 78 → j++
i=0, j=2: arr[2]-arr[0] = 5-2 = 3 < 78 → j++
i=0, j=3: arr[3]-arr[0] = 5-2 = 3 < 78 → j++
i=0, j=4: arr[4]-arr[0] = 20-2 = 18 < 78 → j++
i=0, j=5: arr[5]-arr[0] = 80-2 = 78 = 78 → Found! ✓

WHY INTERVIEWER WILL ACCEPT:
- Recognizes sorted array enables two-pointer technique
- Optimizes from O(n²) or O(n log n) to O(n) for the search part
- Shows understanding of when to move which pointer
"""

# Input values (commented out for testing)
# l, n = [int(x) for x in input("Enter target_difference, n : ").split()]
# arr = [int(x) for x in input("Enter array : ").split()]

# Test case
target_difference = 78
arr = [5, 20, 3, 2, 5, 80]

def find_pair(arr, target_diff):
    """
    Find if there exists a pair with given difference using two pointers.

    Args:
        arr: Array of numbers (will be sorted)
        target_diff: Target difference to find

    Returns:
        True if pair exists, False otherwise
    """
    n = len(arr)

    # Two pointers: i follows j
    i, j = 0, 1

    while i < n and j < n:
        # Skip if both pointers point to same index
        # Calculate current difference
        if i != j:
            current_diff = arr[j] - arr[i]

            if current_diff == target_diff:
                # Found the pair!
                print(f"Pair found: ({arr[i]}, {arr[j]})")
                return True
            elif current_diff < target_diff:
                # Difference too small, need to increase it
                # Move right pointer forward to get larger value
                j += 1
            else:
                # Difference too large, need to decrease it
                # Move left pointer forward to get larger minimum value
                i += 1
        else:
            # Move j if i and j are same
            j += 1

    return False

# Sort the array first (TWO POINTER requires sorted array!)
arr.sort()
print(f"Sorted array: {arr}")

# Find the pair
if find_pair(arr, target_difference):
    print(f"Pair with difference {target_difference} exists")
else:
    print(f"Pair with difference {target_difference} does not exist")
