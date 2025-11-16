"""
Problem: Next Permutation
--------------------------
Given an array representing a permutation, rearrange it to the next lexicographically
greater permutation. If no such permutation exists (array is in descending order),
rearrange it to the smallest permutation (ascending order).

APPROACH: Multi-Step In-Place Rearrangement
--------------------------------------------
WHY THIS APPROACH?
- This is the optimal O(n) algorithm that modifies the array in-place
- Key insight: To get the next permutation, we need to make the smallest possible
  increase to the number, which means:
  1. Find the rightmost position where we can make an increase
  2. Make the smallest possible increase at that position
  3. Minimize everything after that position
- We can't use generation of all permutations (factorial time complexity)
- Sorting would destroy the permutation order
- This approach works by understanding the structure of lexicographic ordering

ALGORITHM:
1. Find the pivot (rightmost ascending pair):
   - Scan from right to left to find first index i where arr[i] > arr[i-1]
   - This i is our pivot point (idx in code)
   - If no such i exists, array is in descending order (largest permutation)

2. If no pivot found (idx == -1):
   - Array is already the largest permutation
   - Reverse entire array to get smallest permutation
   - Return

3. If pivot found:
   - Find the smallest element to the right of idx-1 that is larger than arr[idx-1]
   - This element should replace arr[idx-1] to create next larger permutation
   - Scan from idx to end, track the smallest element > arr[idx-1]

4. Swap arr[idx-1] with the found element

5. Reverse the suffix starting from idx:
   - Everything from idx onwards must be in ascending order for smallest increase
   - Since it was in descending order initially, reversing gives ascending order

TIME COMPLEXITY: O(n)
- Finding pivot: O(n)
- Finding swap position: O(n)
- Reversing suffix: O(n)
- Total: O(n)

SPACE COMPLEXITY: O(1)
- In-place modifications, only using constant extra space

EDGE CASES:
- Array is in descending order: reverse to get ascending (smallest permutation)
- Array is in ascending order: swap last two elements
- Array has duplicates: algorithm still works correctly
- Single element or empty array: no change needed

EXAMPLE 1:
Input: [1, 2, 3, 6, 5, 4]
- Pivot: idx = 3 (arr[3]=6 > arr[2]=3)
- Need to replace arr[2]=3 with next larger from [6,5,4]
- Next larger than 3 is 4
- Swap: [1, 2, 4, 6, 5, 3]
- Reverse from idx=3: [1, 2, 4, 3, 5, 6]
Output: [1, 2, 4, 3, 5, 6]

EXAMPLE 2:
Input: [3, 2, 1]
- No pivot found (descending order)
- Reverse entire array
Output: [1, 2, 3]
"""

class Solution:
    def nextPermutation(self, n, arr):
        # Step 1: Find the pivot point (rightmost ascending position)
        # idx will store the first position from right where arr[i] > arr[i-1]
        idx = -1

        # Scan from right to left to find the pivot
        # We need the rightmost position where increase is possible
        for i in range(n - 1, 0, -1):
            if arr[i] > arr[i - 1]:
                idx = i  # Found the pivot!
                break

        # Step 2: If no pivot found (array in descending order)
        # This means we have the largest permutation, so wrap to smallest
        if idx == -1:
            arr.reverse()  # Reverse entire array to get smallest permutation
        else:
            # Step 3: Find the smallest element > arr[idx-1] in the suffix
            # This element will replace arr[idx-1] to create next permutation
            prev = idx  # Start with the element at idx

            # Search from idx+1 to end for better candidate
            # We want smallest element that is still > arr[idx-1]
            for i in range(idx + 1, n):
                if arr[i] > arr[idx - 1] and arr[i] <= arr[prev]:
                    prev = i

            # Step 4: Swap arr[idx-1] with the found element
            # This makes the permutation larger at position idx-1
            arr[idx - 1], arr[prev] = arr[prev], arr[idx - 1]

            # Step 5: Reverse the suffix from idx to end
            # This ensures the suffix is in ascending order (smallest possible)
            # The suffix was in descending order, so reversing makes it ascending
            arr[idx:] = reversed(arr[idx:])

        return arr