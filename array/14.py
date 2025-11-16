"""
PROBLEM: Next Permutation
===========================
Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.

If such arrangement is not possible, rearrange it as the lowest possible order
(i.e., sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Example:
    Input:  [1, 2, 3]
    Output: [1, 3, 2]

    Input:  [3, 2, 1]
    Output: [1, 2, 3] (wrap around to smallest)

    Input:  [1, 1, 5]
    Output: [1, 5, 1]

    Input:  [1, 3, 5, 4, 2]
    Output: [1, 4, 2, 3, 5]

APPROACH: Find Pivot, Swap, and Reverse
=========================================
WHY THIS APPROACH?
- Lexicographic ordering means dictionary order (like words in a dictionary)
- To get next permutation, we need smallest increase from right
- Three key observations:
  1. From right, find first decreasing element (pivot) - this marks where increase can happen
  2. Swap pivot with smallest element greater than it (from right)
  3. Reverse everything after pivot to get smallest arrangement

HOW IT WORKS:
1. From right to left, find first index i where arr[i] < arr[i+1] (pivot point)
2. If no such index exists, array is in descending order → reverse entire array
3. From right, find smallest element greater than arr[i] (call it arr[j])
4. Swap arr[i] and arr[j]
5. Reverse the subarray from i+1 to end

Why reverse after swap?
- After swap, elements from i+1 to end are in descending order
- We want the smallest permutation, so we reverse to make it ascending

FLOW EXAMPLE 1:
===============
Input: [1, 3, 5, 4, 2]
Goal: Find next permutation

Step 1: Find pivot (first decreasing element from right)
    [1, 3, 5, 4, 2]
           ^     (compare from right)
    i=4: arr[4]=2 vs arr[3]=4 → 2 < 4? No
    i=3: arr[3]=4 vs arr[2]=5 → 4 < 5? No
    i=2: arr[2]=5 vs arr[1]=3 → 5 < 3? No
    i=1: arr[1]=3 vs arr[0]=1 → 3 < 1? No

    Wait, we want arr[i] > arr[i-1] from the loop perspective:
    i=4: arr[4]=2 > arr[3]=4? No
    i=3: arr[3]=4 > arr[2]=5? No
    i=2: arr[2]=5 > arr[1]=3? Yes! → idx = 2

    Pivot element: arr[idx-1] = arr[1] = 3
    [1, 3, 5, 4, 2]
        ^ pivot at index 1

Step 2: Find smallest element > pivot (which is 3) from right side
    Elements after pivot: [5, 4, 2]
    Which elements > 3? → 5, 4
    Smallest among them: 4

    prev = idx = 2 (initially pointing to 5)
    i=3: arr[3]=4 > arr[1]=3? Yes. arr[4]=4 <= arr[2]=5? Yes → prev = 3
    i=4: arr[4]=2 > arr[1]=3? No

    Element to swap with: arr[prev] = arr[3] = 4

Step 3: Swap pivot with arr[prev]
    Swap arr[1]=3 with arr[3]=4
    [1, 4, 5, 3, 2]
        ^     ^

Step 4: Reverse from idx to end
    Reverse arr[2:] = [5, 3, 2]
    [1, 4, 2, 3, 5]
           -------
           (reversed)

Final: [1, 4, 2, 3, 5]

VERIFICATION:
[1, 3, 5, 4, 2] → [1, 4, 2, 3, 5]
All permutations between: [1, 3, 5, 4, 2] and [1, 4, 2, 3, 5]?
[1, 3, 5, 4, 2] < [1, 4, ...] ✓ (3 < 4 at position 1)
Is [1, 4, 2, 3, 5] the immediate next? Yes!

FLOW EXAMPLE 2 (Edge Case - Descending Order):
===============================================
Input: [3, 2, 1]
Goal: Find next permutation

Step 1: Find pivot
    i=2: arr[2]=1 > arr[1]=2? No
    i=1: arr[1]=2 > arr[0]=3? No
    idx = -1 (no pivot found)

Step 2: Array is in descending order (largest permutation)
    Reverse entire array to get smallest permutation
    [3, 2, 1] → [1, 2, 3]

Final: [1, 2, 3]

FLOW EXAMPLE 3:
===============
Input: [1, 2, 3]

Step 1: Find pivot
    i=2: arr[2]=3 > arr[1]=2? Yes → idx = 2

Step 2: Find element > arr[1]=2 from right
    Only arr[2]=3 > 2
    prev = 2

Step 3: Swap arr[1] with arr[2]
    [1, 3, 2]

Step 4: Reverse arr[2:]
    [2] → [2] (single element, no change)

Final: [1, 3, 2]

TIME COMPLEXITY:  O(n) - Linear scan to find pivot, swap, and reverse
SPACE COMPLEXITY: O(1) - In-place modifications only
"""

class Solution:
    def next_perm(self, arr):
        """
        Rearrange array to next lexicographic permutation.

        Args:
            arr: List of integers

        Returns:
            None (modifies array in-place)
        """
        idx = -1  # Will store the position after pivot point
        n = len(arr)

        # Step 1: Find the pivot point (rightmost position where arr[i] > arr[i-1])
        # This is the first pair from right where sequence increases
        # Everything after this is in descending order
        for i in range(n - 1, 0, -1):
            if arr[i] > arr[i - 1]:
                idx = i  # Mark position after the pivot
                break

        # Step 2: Check if array is in descending order (largest permutation)
        if idx == -1:
            # No pivot found means array is completely descending
            # Next permutation wraps around to smallest (ascending order)
            arr.reverse()
        else:
            # Step 3: Find the smallest element greater than pivot (arr[idx-1])
            # We search from idx onwards (right part which is in descending order)
            prev = idx  # Initially points to first element after pivot

            # Find smallest element > pivot element
            for i in range(idx + 1, n):
                # Check if current element is greater than pivot
                # AND smaller than or equal to current candidate
                if arr[i] > arr[idx - 1] and arr[i] <= arr[prev]:
                    prev = i

            # Step 4: Swap the pivot element with the element just greater than it
            # This ensures we get the next larger permutation
            arr[idx - 1], arr[prev] = arr[prev], arr[idx - 1]

            # Step 5: Reverse the subarray from idx to end
            # After swap, elements from idx onwards are still in descending order
            # Reverse them to get ascending order (smallest arrangement)
            # This gives us the immediate next permutation
            arr[idx:] = reversed(arr[idx:])

            


