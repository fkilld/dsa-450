"""
PROBLEM: Merge Two Sorted Arrays Without Extra Space
======================================================
Given two sorted arrays arr1[] of size N and arr2[] of size M.
Each array is sorted in non-decreasing order. Merge the two arrays into
one sorted array in non-decreasing order without using any extra space.

After merging:
- arr1[] should contain the first N smallest elements
- arr2[] should contain the remaining M elements
- Both arrays should be sorted

Example:
    Input:  arr1 = [1, 3, 5, 7], arr2 = [0, 2, 6, 8, 9]
    Output: arr1 = [0, 1, 2, 3], arr2 = [5, 6, 7, 8, 9]

    Input:  arr1 = [10, 12], arr2 = [5, 18, 20]
    Output: arr1 = [5, 10], arr2 = [12, 18, 20]

APPROACH: Gap Method (Shell Sort Variation)
=============================================
WHY THIS APPROACH?
- Cannot use extra space O(1) constraint
- Simple approach: Compare last of arr1 with first of arr2 (O(n*m) time)
- Gap method: Uses gap sequence to compare and swap elements efficiently
- Similar to shell sort but applied across two arrays
- Time: O((n+m) log(n+m)), Space: O(1)

HOW IT WORKS:
1. Start with gap = ceil((n+m)/2)
2. Compare elements that are 'gap' distance apart and swap if needed
3. Handle three cases:
   a) Both elements in arr1
   b) One in arr1, one in arr2
   c) Both elements in arr2
4. Reduce gap: gap = ceil(gap/2)
5. Repeat until gap becomes 0

The gap sequence ensures elements gradually move to their correct positions.

FLOW EXAMPLE:
=============
arr1 = [1, 3, 5, 7], n = 4
arr2 = [0, 2, 6, 8, 9], m = 5
Total elements = 9

Step 1: Initial gap = ceil(9/2) = 5
    Compare elements 5 positions apart:

    i=0, i+gap=5 (arr1[0]=1 vs arr2[0]=0):
        1 > 0? Yes → Swap
        arr1 = [0, 3, 5, 7], arr2 = [1, 2, 6, 8, 9]

    i=1, i+gap=6 (arr1[1]=3 vs arr2[1]=2):
        3 > 2? Yes → Swap
        arr1 = [0, 2, 5, 7], arr2 = [1, 3, 6, 8, 9]

    i=2, i+gap=7 (arr1[2]=5 vs arr2[2]=6):
        5 > 6? No → No swap

    i=3, i+gap=8 (arr1[3]=7 vs arr2[3]=8):
        7 > 8? No → No swap

    After gap=5: arr1=[0, 2, 5, 7], arr2=[1, 3, 6, 8, 9]

Step 2: gap = ceil(5/2) = 3
    Compare elements 3 positions apart:

    Within arr1:
    i=0, i+3=3: (0 vs 7) → No swap

    Across arr1 and arr2:
    i=1, j=0: (arr1[1]=2 vs arr2[0]=1) → Swap
        arr1 = [0, 1, 5, 7], arr2 = [2, 3, 6, 8, 9]
    i=2, j=1: (arr1[2]=5 vs arr2[1]=3) → Swap
        arr1 = [0, 1, 3, 7], arr2 = [2, 5, 6, 8, 9]
    i=3, j=2: (arr1[3]=7 vs arr2[2]=6) → Swap
        arr1 = [0, 1, 3, 6], arr2 = [2, 5, 7, 8, 9]

    Within arr2:
    j=0, j+3=3: (arr2[0]=2 vs arr2[3]=8) → No swap
    j=1, j+3=4: (arr2[1]=5 vs arr2[4]=9) → No swap

    After gap=3: arr1=[0, 1, 3, 6], arr2=[2, 5, 7, 8, 9]

Step 3: gap = ceil(3/2) = 2
    Similar comparisons with gap=2
    After gap=2: arr1=[0, 1, 3, 5], arr2=[2, 6, 7, 8, 9]

Step 4: gap = ceil(2/2) = 1
    This is essentially bubble sort pass
    After gap=1: arr1=[0, 1, 2, 3], arr2=[5, 6, 7, 8, 9]

Step 5: gap = ceil(1/2) = 0
    Stop (gap becomes 0)

Final: arr1 = [0, 1, 2, 3], arr2 = [5, 6, 7, 8, 9]

KEY INSIGHT:
The gap method progressively sorts by comparing elements at decreasing gaps,
similar to Shell Sort. Starting with large gaps moves elements closer to
their final positions, then smaller gaps fine-tune the ordering.

TIME COMPLEXITY:  O((n+m) * log(n+m)) - log(n+m) gap iterations, each O(n+m)
SPACE COMPLEXITY: O(1) - No extra space used, in-place swapping
"""

class Solution:
    def merge(self, arr1, arr2, n, m):
        """
        Merge two sorted arrays without using extra space.

        Args:
            arr1: First sorted array (will contain n smallest elements after merge)
            arr2: Second sorted array (will contain remaining m elements after merge)
            n: Size of first array
            m: Size of second array

        Returns:
            None (modifies arrays in-place)
        """
        def next_gap(gap):
            """
            Calculate next gap in the sequence.
            Returns ceiling of gap/2 (upper bound).

            Args:
                gap: Current gap value

            Returns:
                Next gap value (ceil(gap/2)), or 0 if gap <= 1
            """
            if gap > 1:
                # (gap // 2) gives floor division
                # (gap % 2) adds 1 if gap is odd, giving us ceiling
                return (gap // 2) + (gap % 2)
            else:
                return 0

        # Start with initial gap = ceil((n+m)/2)
        gap = next_gap(n + m)

        # Continue until gap becomes 0
        while gap > 0:
            # PHASE 1: Compare elements within first array
            i = 0
            while i + gap < n:
                # Both elements are in arr1
                # If left element > right element, swap them
                if arr1[i] > arr1[i + gap]:
                    arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
                i += 1

            # PHASE 2: Compare elements across both arrays
            # j starts from the appropriate position in arr2
            # If gap > n, comparison spans into arr2
            j = gap - n if gap > n else 0

            while i < n and j < m:
                # Compare element from arr1 with element from arr2
                if arr1[i] > arr2[j]:
                    arr1[i], arr2[j] = arr2[j], arr1[i]
                i += 1
                j += 1

            # PHASE 3: Compare elements within second array
            # Only if we haven't covered entire arr2 in phase 2
            if j < m:
                j = 0
                while j + gap < m:
                    # Both elements are in arr2
                    if arr2[j] > arr2[j + gap]:
                        arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                    j += 1

            # Reduce gap for next iteration
            gap = next_gap(gap)