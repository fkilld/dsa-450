"""
PROBLEM: Find Three Numbers with Given Sum (3Sum Problem)
==========================================================
Given an array arr[] and a target sum X, find if there exists a triplet in the array
which sums up to X.

Example 1:
    Input:  arr = [1, 4, 45, 6, 10, 8], X = 13
    Output: True
    Explanation: 1 + 4 + 8 = 13 (triplet found)

Example 2:
    Input:  arr = [1, 2, 4, 3, 6], X = 10
    Output: True
    Explanation: 1 + 3 + 6 = 10 (triplet found)

Example 3:
    Input:  arr = [1, 2, 3], X = 10
    Output: False
    Explanation: No triplet sums to 10

APPROACH: Sort + Two Pointer Technique
=======================================
WHY THIS APPROACH?
- Brute force (3 nested loops) would be O(n³) - too slow for large arrays
- Sorting + two pointers reduces complexity to O(n²)
- After fixing one element, finding two elements that sum to target is a classic two-pointer problem
- Two pointers work on sorted arrays to efficiently find pairs

ALTERNATIVE APPROACHES:
1. Brute Force (3 loops): O(n³) time, O(1) space - Try all triplets
2. Hash Map: O(n²) time, O(n) space - Use hash map for third element
3. Sort + Two Pointers (current): O(n²) time, O(1) space - Best balance

HOW IT WORKS:
1. Sort the array first - O(n log n)
2. Fix the first element (i) and find two elements that sum to X - arr[i]
3. Use two pointers (j, k) on remaining elements:
   - j starts right after i
   - k starts at the end
   - If sum == X, found triplet
   - If sum < X, move j right (increase sum)
   - If sum > X, move k left (decrease sum)
4. Repeat for each element as the first element

FLOW EXAMPLE:
=============
Array: [1, 4, 45, 6, 10, 8], X = 13

Step 1: Sort the array
    arr = [1, 4, 6, 8, 10, 45]
    Indices: 0  1  2  3   4   5

Step 2: Fix first element, use two pointers for remaining

Iteration i=0: arr[i] = 1
    Target for j and k: X - arr[i] = 13 - 1 = 12
    j=1 (arr[1]=4), k=5 (arr[5]=45)

    Check: arr[0] + arr[1] + arr[5] = 1 + 4 + 45 = 50
        50 > 13, so move k left

    j=1 (arr[1]=4), k=4 (arr[4]=10)
    Check: arr[0] + arr[1] + arr[4] = 1 + 4 + 10 = 15
        15 > 13, so move k left

    j=1 (arr[1]=4), k=3 (arr[3]=8)
    Check: arr[0] + arr[1] + arr[3] = 1 + 4 + 8 = 13
        13 == 13, FOUND! Return True

Final Answer: True (triplet: 1, 4, 8)

DETAILED TWO-POINTER MECHANICS:
===============================
Why does moving pointers work?

After sorting: arr = [1, 4, 6, 8, 10, 45]
Fix i=0 (arr[i]=1), need two numbers that sum to 12

    j                                      k
    [4,  6,  8, 10, 45]

Current sum = 4 + 45 = 49 (too large)
- If we move j right, sum increases (array is sorted)
- So we must move k left to decrease sum

    j                  k
    [4,  6,  8, 10, 45]

Current sum = 4 + 10 = 14 (still too large)
- Move k left again

    j              k
    [4,  6,  8, 10, 45]

Current sum = 4 + 8 = 12 (perfect!)
With arr[i]=1, total = 1 + 4 + 8 = 13

EXAMPLE WITH NO SOLUTION:
==========================
Array: [1, 2, 3], X = 10

Step 1: Sort (already sorted)
    arr = [1, 2, 3]

Step 2: Try all combinations

i=0: arr[i]=1, need sum=9 from remaining [2, 3]
    j=1, k=2: 2 + 3 = 5 < 9
    Move j right: j=2, k=2 (j >= k, stop)
    No triplet found

i=1: arr[i]=2, need sum=8 from remaining [3]
    j=2, k=2 (j >= k, stop immediately)
    No triplet found

No more elements, return False

WHY SORT FIRST?
- Enables two-pointer technique
- Sorted array has property: moving right increases value, moving left decreases
- This allows us to adjust sum by moving pointers intelligently
- Without sorting, we can't determine which direction to move

TIME COMPLEXITY:  O(n²) - O(n log n) for sorting + O(n²) for nested loops
SPACE COMPLEXITY: O(1) - Only using pointers, in-place sorting (or O(n) if counting sort space)
"""

class Solution:
    def find3Numbers(self, arr, n, X):
        """
        Find if there exists a triplet in array that sums to X.

        Args:
            arr: Input array of integers
            n: Size of the array
            X: Target sum to find

        Returns:
            True if a triplet exists that sums to X, False otherwise

        Example:
            >>> sol = Solution()
            >>> sol.find3Numbers([1, 4, 45, 6, 10, 8], 6, 13)
            True
            >>> sol.find3Numbers([1, 2, 3], 3, 10)
            False
        """
        # STEP 1: Sort the array to enable two-pointer technique
        # Sorting is crucial because:
        # - It allows us to use two pointers efficiently
        # - Moving pointers left/right has predictable effect on sum
        # - Time: O(n log n)
        arr.sort()

        # STEP 2: Fix the first element of the triplet
        # Loop through array, treating each element as potential first element
        # We stop at n-2 because we need at least 2 more elements after i
        # for a valid triplet (i, j, k)
        for i in range(n - 2):
            # STEP 3: Use two pointers for remaining elements
            # After fixing arr[i], we need to find two numbers that sum to (X - arr[i])
            # This becomes a classic "two sum" problem on sorted array

            # Left pointer: starts immediately after i
            # This ensures we don't reuse arr[i] and only look at elements to the right
            j = i + 1

            # Right pointer: starts at the end of array
            k = n - 1

            # STEP 4: Find two elements (at j and k) that sum to X - arr[i]
            # Continue until pointers meet
            while j < k:
                # Calculate sum of current triplet
                current_sum = arr[i] + arr[j] + arr[k]

                # CASE 1: Found the target sum!
                if current_sum == X:
                    # Triplet found: (arr[i], arr[j], arr[k])
                    return True

                # CASE 2: Current sum is too small
                # Need to increase sum, so move left pointer right
                # This works because array is sorted: arr[j+1] > arr[j]
                elif current_sum < X:
                    j += 1

                # CASE 3: Current sum is too large
                # Need to decrease sum, so move right pointer left
                # This works because array is sorted: arr[k-1] < arr[k]
                else:  # current_sum > X
                    k -= 1

        # STEP 5: No triplet found after checking all possibilities
        # We've tried all valid combinations of (i, j, k)
        return False


# Example test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Triplet exists
    arr1 = [1, 4, 45, 6, 10, 8]
    print(sol.find3Numbers(arr1, len(arr1), 13))  # Expected: True (1 + 4 + 8 = 13)

    # Test case 2: No triplet exists
    arr2 = [1, 2, 3]
    print(sol.find3Numbers(arr2, len(arr2), 10))  # Expected: False

    # Test case 3: Triplet exists
    arr3 = [1, 2, 4, 3, 6]
    print(sol.find3Numbers(arr3, len(arr3), 10))  # Expected: True (1 + 3 + 6 = 10)