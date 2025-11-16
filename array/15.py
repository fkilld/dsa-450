"""
PROBLEM: Count Inversions
===========================
Given an array of integers, find the Inversion Count in the array.

An inversion is a pair of indices (i, j) such that:
- i < j (i comes before j)
- arr[i] > arr[j] (element at i is greater than element at j)

In other words, an inversion occurs when a larger element appears before
a smaller element in the array.

Example:
    Input:  [2, 4, 1, 3, 5]
    Output: 3
    Explanation: Inversions are (2,1), (4,1), (4,3)
                 - arr[0]=2 > arr[2]=1
                 - arr[1]=4 > arr[2]=1
                 - arr[1]=4 > arr[3]=3

    Input:  [5, 4, 3, 2, 1]
    Output: 10
    Explanation: Every pair is an inversion (descending order)
                 Pairs: (5,4), (5,3), (5,2), (5,1), (4,3), (4,2), (4,1), (3,2), (3,1), (2,1)

    Input:  [1, 2, 3, 4, 5]
    Output: 0
    Explanation: No inversions (already sorted)

APPROACH: Modified Merge Sort
===============================
WHY THIS APPROACH?
- Brute force: Check all pairs → O(n²) time
- Optimized: Use divide-and-conquer with merge sort → O(n log n)
- Key insight: While merging two sorted halves, we can count inversions efficiently
- When element from right half is smaller than element from left half,
  it forms inversions with ALL remaining elements in left half

HOW IT WORKS:
1. Divide array into two halves recursively (like merge sort)
2. Count inversions in left half
3. Count inversions in right half
4. Count inversions while merging (cross-inversions)
5. During merge: If arr[i] > arr[j] (i from left, j from right),
   then arr[i], arr[i+1], ..., arr[mid] all form inversions with arr[j]
   Count = (mid - i + 1)

WHY MERGE SORT?
- Merge sort naturally divides the problem
- While merging, we compare elements from both halves
- If left element > right element, we know ALL remaining left elements are also greater
  (because left half is sorted)
- This allows us to count multiple inversions in O(1) time during merge

FLOW EXAMPLE:
=============
Input: [2, 4, 1, 3, 5]
Goal: Count total inversions

Initial call: merge_sort(arr, temp, 0, 4)

                        [2, 4, 1, 3, 5]
                       /               \
                 [2, 4, 1]            [3, 5]
                /         \           /      \
            [2, 4]        [1]       [3]      [5]
            /    \
          [2]    [4]

Step 1: Divide (recursion)
    Left half: [2, 4, 1]
        Left: [2, 4] → Left: [2], Right: [4]
        Right: [1]
    Right half: [3, 5]
        Left: [3], Right: [5]

Step 2: Merge [2] and [4]
    Both sorted, no inversions
    Result: [2, 4], inv = 0

Step 3: Merge [2, 4] and [1]
    Compare arr[0]=2 with arr[2]=1
        2 > 1? Yes → Inversions!
        Count = mid - i + 1 = 1 - 0 + 1 = 2
        (Both 2 and 4 are > 1)
        Place 1 first: temp = [1, ...]
        inv = 2

    Now merge remaining:
        Place 2: temp = [1, 2, ...]
        Place 4: temp = [1, 2, 4]

    Result: [1, 2, 4], inv = 2

Step 4: Merge [3] and [5]
    3 < 5, no inversions
    Result: [3, 5], inv = 0

Step 5: Merge [1, 2, 4] and [3, 5]
    Compare 1 with 3: 1 < 3, no inversion
    Compare 2 with 3: 2 < 3, no inversion
    Compare 4 with 3: 4 > 3? Yes!
        Inversions = mid - i + 1 = 2 - 2 + 1 = 1
        (Only 4 is > 3, as 1 and 2 already placed)
        inv = 1

    Result: [1, 2, 3, 4, 5], inv = 1

Total inversions: 0 (from [2,4]) + 2 (from [2,4,1]) + 0 (from [3,5]) + 1 (final merge)
                = 3

DETAILED MERGE EXAMPLE:
=======================
Merging [2, 4] (sorted) and [1] (sorted)

    left = 0, mid = 1, right = 2
    i = 0 (first half: indices 0-1)
    j = 2 (second half: index 2)
    k = 0 (temp array index)
    inv = 0

    Step 1: Compare arr[0]=2 with arr[2]=1
        2 < 1? No → 2 > 1 (INVERSION!)
        How many inversions?
            All elements from i to mid are > arr[j]
            Inversions = mid - i + 1 = 1 - 0 + 1 = 2
            (Elements 2 and 4 both > 1)

        Place arr[j]=1 in temp[k]
        temp = [1, _, _]
        inv = 2, j = 3, k = 1

    Step 2: j > right, so copy remaining from left half
        temp[1] = arr[0] = 2
        temp[2] = arr[1] = 4
        temp = [1, 2, 4]

    Step 3: Copy temp back to arr
        arr = [1, 2, 4]

    Return inv = 2

KEY INSIGHT:
When we find arr[i] > arr[j] during merge (where i is from left sorted half
and j is from right sorted half), we know that:
- arr[i], arr[i+1], ..., arr[mid] are all > arr[j]
- Because left half is sorted, all these elements form inversions with arr[j]
- We can count all these inversions in O(1): count = mid - i + 1

TIME COMPLEXITY:  O(n log n) - Same as merge sort
SPACE COMPLEXITY: O(n) - Temporary array for merging
"""

class Solution:

    def merge(self, arr, temp, left, mid, right):
        """
        Merge two sorted halves and count inversions.

        Args:
            arr: Original array
            temp: Temporary array for merging
            left: Start index of first half
            mid: End index of first half
            right: End index of second half

        Returns:
            Number of inversions found during merge
        """
        i = left        # Pointer for first half [left...mid]
        j = mid + 1     # Pointer for second half [mid+1...right]
        k = left        # Pointer for temp array
        inv = 0         # Inversion count

        # Merge the two halves while counting inversions
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                # No inversion: left element <= right element (correct order)
                # Copy left element to temp
                temp[k] = arr[i]
                i += 1
                k += 1
            else:
                # INVERSION FOUND: arr[i] > arr[j]
                # Since left half is sorted, ALL elements from i to mid are > arr[j]
                # Each of them forms an inversion with arr[j]
                inv += mid - i + 1

                # Copy right element to temp (it's smaller)
                temp[k] = arr[j]
                j += 1
                k += 1

        # Copy remaining elements from left half (if any)
        # These don't form new inversions
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1

        # Copy remaining elements from right half (if any)
        # These don't form new inversions
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1

        # Copy merged result back to original array
        for i in range(left, right + 1):
            arr[i] = temp[i]

        return inv

    def merge_sort(self, arr, temp, left, right):
        """
        Recursively divide array and count inversions.

        Args:
            arr: Array to sort and count inversions
            temp: Temporary array for merging
            left: Left boundary of current segment
            right: Right boundary of current segment

        Returns:
            Total number of inversions in segment [left...right]
        """
        inv = 0

        # Base case: single element has no inversions
        if left < right:
            # Find middle point
            mid = (left + right) // 2

            # Count inversions in left half
            inv += self.merge_sort(arr, temp, left, mid)

            # Count inversions in right half
            inv += self.merge_sort(arr, temp, mid + 1, right)

            # Count inversions while merging (cross-inversions)
            # These are inversions where one element is in left half
            # and the other is in right half
            inv += self.merge(arr, temp, left, mid, right)

        return inv

    def inversionCount(self, arr, n):
        """
        Count total number of inversions in array.

        Args:
            arr: Input array
            n: Size of array

        Returns:
            Total inversion count
        """
        # Create temporary array for merge sort
        # Same size as input array
        temp = [0] * n

        # Perform modified merge sort to count inversions
        return self.merge_sort(arr, temp, 0, n - 1)