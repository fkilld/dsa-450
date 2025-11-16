"""
PROBLEM: Count Triplets with Sum Smaller than X
Given an array arr[] of distinct integers of size N and a sum value X,
find the count of triplets with sum smaller than the given sum value X.

WHY THIS SOLUTION:
Naive approach would be O(n^3) - checking every possible triplet.
We use SORT + TWO POINTER technique to reduce it to O(n^2):
1. Sorting enables two-pointer technique
2. For each element as first element, we use two pointers for remaining elements
3. When we find a valid triplet, we can count MULTIPLE triplets at once

KEY INSIGHT:
When arr[i] + arr[left] + arr[right] < x, then arr[i] + arr[left] + arr[k] < x
for ALL k where left < k <= right. This is because array is sorted!
So we can add (right - left) triplets in one go instead of counting one by one.

APPROACH:
1. Sort the array - O(n log n)
2. Fix first element at index i (iterate from 0 to n-2)
3. Use two pointers (left = i+1, right = n-1) for remaining subarray
4. If sum < x: count += (right - left), move left pointer right
5. If sum >= x: move right pointer left
6. Continue until all triplets are counted

TIME COMPLEXITY: O(n^2)
- Sorting: O(n log n)
- Outer loop: O(n)
- Inner two-pointer traversal: O(n)
- Total: O(n log n) + O(n^2) = O(n^2)

SPACE COMPLEXITY: O(1) - only using pointers, modifying array in-place

EXAMPLE: arr = [5, 1, 3, 4, 7], x = 12
After sorting: [1, 3, 4, 5, 7]
i=0 (arr[i]=1): left=1, right=4
  - 1+3+7=11<12, count += 4-1 = 3 (triplets: [1,3,7], [1,3,5], [1,3,4])
  - Continue this process...
Final count: 4 triplets

WHY INTERVIEWER WILL ACCEPT:
1. Shows optimization from O(n^3) to O(n^2)
2. Demonstrates two-pointer technique mastery
3. Understanding of sorted array properties
4. Efficient counting without explicit enumeration
"""

l, x = input("Enter l, x: ").split()
arr = [int(x) for x in input("Enter array: ").split()]

def give_triplets(arr, x):
    """
    Count triplets with sum smaller than x using sorting and two-pointer technique.

    Args:
        arr: Array of distinct integers
        x: Target sum value

    Returns:
        Count of triplets with sum < x
    """
    n = len(arr)
    # Sort array to enable two-pointer technique
    arr.sort()
    count = 0

    # Fix first element of triplet
    for i in range(n - 2):
        # Use two pointers for remaining elements
        left = i + 1
        right = n - 1

        while left < right:
            # Calculate current triplet sum
            if arr[left] + arr[right] + arr[i] < x:
                # KEY: If sum is valid, ALL triplets with indices
                # between left and right are also valid
                count += right - left
                left += 1
            else:
                # Sum too large, reduce it by moving right pointer
                right -= 1
    return count

print(give_triplets(arr, x))