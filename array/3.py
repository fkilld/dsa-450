"""
PROBLEM: Sort an Array of 0s, 1s, and 2s (Dutch National Flag Problem)
=========================================================================
Given an array containing only 0s, 1s, and 2s, sort the array in-place.

Example:
    Input:  [0, 2, 1, 2, 0, 1, 0]
    Output: [0, 0, 0, 1, 1, 2, 2]

    Input:  [2, 2, 2, 0, 0, 1]
    Output: [0, 0, 1, 2, 2, 2]

APPROACH: Dutch National Flag Algorithm (Three-Way Partitioning)
==================================================================
WHY THIS APPROACH?
- Proposed by Edsger W. Dijkstra
- Single pass solution: O(n) time complexity
- In-place sorting: O(1) space complexity
- No need for counting sort or comparison-based sorting
- Uses three pointers to partition array into three regions

HOW IT WORKS:
We maintain three pointers to divide the array into four regions:
1. [0...low-1]: Contains all 0s (sorted)
2. [low...mid-1]: Contains all 1s (sorted)
3. [mid...high]: Contains unsorted elements (unknown region)
4. [high+1...n-1]: Contains all 2s (sorted)

Algorithm:
- Initialize: low = 0, mid = 0, high = n-1
- Process elements from mid pointer:
  * If arr[mid] == 0: Swap with arr[low], increment both low and mid
  * If arr[mid] == 1: Already in correct position, increment mid
  * If arr[mid] == 2: Swap with arr[high], decrement high (don't increment mid!)
- Continue until mid > high

FLOW EXAMPLE:
=============
Array: [0, 2, 1, 2, 0, 1, 0]
Goal: Sort to [0, 0, 0, 1, 1, 2, 2]

Initial State:
    low=0, mid=0, high=6
    [0, 2, 1, 2, 0, 1, 0]
     ↑
     L,M              H

Step 1: arr[mid]=0, swap with arr[low]
    [0, 2, 1, 2, 0, 1, 0]
     ↑
    Already same, increment low and mid
    low=1, mid=1, high=6

Step 2: arr[mid]=2, swap with arr[high]
    [0, 0, 1, 2, 0, 1, 2]
        ↑           ↑
        L,M         H
    Decrement high only
    low=1, mid=1, high=5

Step 3: arr[mid]=0, swap with arr[low]
    [0, 0, 1, 2, 0, 1, 2]
        ↑        ↑
        L,M      H
    Increment low and mid
    low=2, mid=2, high=5

Step 4: arr[mid]=1, already correct
    [0, 0, 1, 2, 0, 1, 2]
           ↑     ↑
           L,M   H
    Increment mid only
    low=2, mid=3, high=5

Step 5: arr[mid]=2, swap with arr[high]
    [0, 0, 1, 1, 0, 2, 2]
           ↑  ↑  ↑
           L  M  H
    Decrement high only
    low=2, mid=3, high=4

Step 6: arr[mid]=0, swap with arr[low]
    [0, 0, 0, 1, 1, 2, 2]
           ↑  ↑↑
           L  MH
    Increment low and mid
    low=3, mid=4, high=4

Step 7: arr[mid]=1, already correct
    [0, 0, 0, 1, 1, 2, 2]
              ↑ ↑
              L,M,H
    Increment mid
    low=3, mid=5, high=4

Step 8: mid > high, STOP
    Final: [0, 0, 0, 1, 1, 2, 2]

FLOWCHART:
==========
    ┌──────────────────────────┐
    │  Start: sort012(arr, n)  │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │ Initialize:              │
    │ low = 0, mid = 0         │
    │ high = n - 1             │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │   while mid <= high?     │
    └────┬────────────────┬────┘
         │ No             │ Yes
         │                ▼
         │     ┌────────────────────┐
         │     │  Check arr[mid]    │
         │     └──┬──────┬──────┬───┘
         │        │      │      │
         │      ==0    ==1    ==2
         │        │      │      │
         │        ▼      ▼      ▼
         │   ┌────────┐ ┌────────┐ ┌─────────────┐
         │   │ Swap   │ │ mid++  │ │ Swap        │
         │   │arr[low]│ │        │ │ arr[mid]    │
         │   │ with   │ │        │ │ with        │
         │   │arr[mid]│ │        │ │ arr[high]   │
         │   └───┬────┘ └───┬────┘ └──────┬──────┘
         │       │          │             │
         │       ▼          │             ▼
         │   ┌────────┐     │      ┌──────────┐
         │   │ low++  │     │      │ high--   │
         │   │ mid++  │     │      └─────┬────┘
         │   └───┬────┘     │            │
         │       │          │            │
         │       └──────────┴────────────┘
         │                  │
         │                  └──────┐
         │                         │
         ▼                         ▼
    ┌──────────────────────────────┐
    │   Return sorted array        │
    └──────────────────────────────┘

WHY DON'T WE INCREMENT mid WHEN SWAPPING WITH high?
=====================================================
When we swap arr[mid] with arr[high], the element that comes to arr[mid]
is from the unsorted region and hasn't been examined yet. We need to check
this element in the next iteration, so we don't increment mid.

When we swap arr[mid] with arr[low], we know the element coming from arr[low]
is either 0 or 1 (already processed), so it's safe to increment mid.

TIME COMPLEXITY:  O(n) - Single pass through array
SPACE COMPLEXITY: O(1) - In-place sorting, no extra space
"""

class Solution:
    """
    Sort an array containing only 0s, 1s, and 2s using the Dutch National Flag algorithm.

    This algorithm sorts the array in a single pass with O(n) time complexity
    without using any traditional sorting algorithm. It uses three pointers (low, mid, high)
    to partition the array into three sections: 0s, 1s, and 2s.

    This is a solution for the Dutch National Flag problem, originally proposed by
    Edsger W. Dijkstra.
    """

    def sort012(self, arr, n):
        """
        Sort an array of 0s, 1s, and 2s in-place.

        Parameters:
            arr (list): The array to be sorted containing only 0s, 1s, and 2s
            n (int): Length of the array

        Returns:
            list: The sorted array with 0s followed by 1s followed by 2s

        Time Complexity: O(n) - Single pass through array
        Space Complexity: O(1) - In-place sorting
        """
        # Pointer for the boundary of 0s region
        # All elements before 'low' are 0s
        low = 0

        # Pointer for the boundary of 2s region
        # All elements after 'high' are 2s
        high = n - 1

        # Pointer for current element being examined
        # Elements between low and mid-1 are 1s
        # Elements between mid and high are unsorted (unknown)
        mid = 0

        # Process all elements until mid crosses high
        while mid <= high:
            # Case 1: Current element is 0
            # Move it to the 0s region (left side)
            if arr[mid] == 0:
                # Swap current element with element at low pointer
                arr[low], arr[mid] = arr[mid], arr[low]

                # Increment low (expand 0s region boundary)
                low += 1

                # Increment mid (we know element from 'low' was 0 or 1, safe to move forward)
                mid += 1

            # Case 2: Current element is 1
            # It's already in the correct region (middle), just move forward
            elif arr[mid] == 1:
                mid += 1

            # Case 3: Current element is 2
            # Move it to the 2s region (right side)
            else:
                # Swap current element with element at high pointer
                arr[high], arr[mid] = arr[mid], arr[high]

                # Decrement high (expand 2s region boundary from right)
                high -= 1

                # DON'T increment mid here!
                # The element we just swapped from 'high' hasn't been examined yet
                # We need to check it in the next iteration

        return arr


# Test the solution
if __name__ == "__main__":
    s1 = Solution()

    # Test 1: Mixed array
    arr1 = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    n1 = len(arr1)
    print(f"Input:  {arr1}")
    print(f"Output: {s1.sort012(arr1, n1)}")  # Expected: [0, 0, 0, 1, 1, 1, 2, 2, 2]

    # Test 2: Reverse sorted
    arr2 = [2, 2, 2, 1, 1, 0, 0]
    n2 = len(arr2)
    print(f"\nInput:  {arr2}")
    print(f"Output: {s1.sort012(arr2, n2)}")  # Expected: [0, 0, 1, 1, 2, 2, 2]

    # Test 3: Already sorted
    arr3 = [0, 0, 1, 1, 2, 2]
    n3 = len(arr3)
    print(f"\nInput:  {arr3}")
    print(f"Output: {s1.sort012(arr3, n3)}")  # Expected: [0, 0, 1, 1, 2, 2]
