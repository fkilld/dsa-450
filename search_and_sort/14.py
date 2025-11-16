"""
PROBLEM: Count Zero Sum Subarrays
Given an array arr[] of size n, find the total count of subarrays having sum equal to 0.

WHY THIS SOLUTION:
Naive approach: Check sum of every subarray - O(n^2) or O(n^3)
We use PREFIX SUM + HASHMAP to solve in O(n) time!

KEY INSIGHT:
If prefix_sum[i] == prefix_sum[j], then sum(arr[i+1...j]) = 0
Why? prefix_sum[j] - prefix_sum[i] = 0 means elements between i and j sum to zero.

Also: If prefix_sum = 0 at any point, subarray from start to that point has sum 0.

APPROACH:
1. Maintain running prefix sum
2. Use hashmap to store: {prefix_sum: count of occurrences}
3. For each element:
   - Add to prefix sum
   - If this prefix sum seen before k times, we found k new zero-sum subarrays
   - If prefix sum is 0, we found 1 zero-sum subarray from start
   - Update hashmap with current prefix sum

TIME COMPLEXITY: O(n) - single pass through array
SPACE COMPLEXITY: O(n) - hashmap stores at most n different prefix sums

EXAMPLE: arr = [4, -4, 1, -1]
Index 0: sum=4, map={4:1}, count=0
Index 1: sum=0, map={4:1, 0:1}, count=1 (subarray [4,-4])
Index 2: sum=1, map={4:1, 0:1, 1:1}, count=1
Index 3: sum=0, map={4:1, 0:2, 1:1}, count=2 (found 0 again, so +1)
Total: 2 zero-sum subarrays: [4,-4] and [1,-1]

WHY INTERVIEWER WILL ACCEPT:
1. Demonstrates prefix sum technique mastery
2. Shows HashMap usage for optimization
3. Optimization from O(n^2) to O(n)
4. Understanding of subarray sum properties
"""

# arr = [int(x) for x in input("Enter the array : ").split()]

n = 30
arr = [9, -10, -1, 5, 17, -18, 6, 19, -12, 5, 18, 14, 4, -19, 11, 8, -19, 18, -20, 14, 8, -14, 12, -12, 16, -11, 0, 3, -19, 16]

def give_counts(arr):
    """
    Count subarrays with sum equal to 0 using prefix sum and hashmap.

    Args:
        arr: Input array of integers

    Returns:
        Count of zero-sum subarrays
    """
    count = 0
    m = {}  # HashMap: {prefix_sum: frequency}
    s = 0   # Running prefix sum

    for el in arr:
        s += el  # Update prefix sum

        if s in m:
            # If we've seen this prefix sum before, we found zero-sum subarrays
            # The count equals how many times we've seen this sum before
            count += m[s]
            m[s] += 1
        else:
            # First time seeing this prefix sum
            if s == 0:
                # Subarray from start to current index has sum 0
                count += 1
            m[s] = 1

    return count

print(give_counts(arr))

