"""
PROBLEM: Count Pairs with Given Sum
=====================================
Given an array of N integers and an integer K, find the number of pairs of elements
in the array whose sum is equal to K.

Note: A pair (i, j) is the same as (j, i), and we should count each pair only once.

Example:
    Input:  arr = [1, 5, 7, 1], K = 6
    Output: 2
    Explanation: Pairs are (1, 5) and (1, 5) → indices (0,1) and (3,1)

    Input:  arr = [1, 1, 1, 1], K = 2
    Output: 6
    Explanation: All pairs sum to 2: (0,1), (0,2), (0,3), (1,2), (1,3), (2,3)

    Input:  arr = [10, 12, 10, 15, -1], K = 125
    Output: 0
    Explanation: No pairs sum to 125

    Input:  arr = [1, 5, 7, -1, 5], K = 6
    Output: 3
    Explanation: Pairs are (1, 5), (7, -1), (1, 5) → indices (0,1), (2,3), (0,4)

APPROACH: Hash Map (Frequency Counting)
=========================================
WHY THIS APPROACH?
- Efficient time complexity: O(n) - Two passes through array
- Uses hash map for O(1) lookup time
- Handles duplicates correctly by tracking frequencies
- Better than brute force O(n²) approach
- Works with negative numbers and duplicates

ALTERNATIVE APPROACHES:
1. Brute Force: Check all pairs (i, j) - O(n²) time, O(1) space
2. Sort + Two Pointers: Sort array and use two pointers - O(n log n) time, O(1) space
3. Hash Map (This approach): Optimal for unsorted - O(n) time, O(n) space

KEY INSIGHT:
For each element arr[i], we need to find if (K - arr[i]) exists in the array.
Instead of searching the entire array each time (O(n)), we use a hash map
to store element frequencies, allowing O(1) lookup.

Important: Each pair is counted twice (once for each element), so we divide by 2.

HOW IT WORKS:
1. Build frequency map: Count occurrences of each element
2. For each element arr[i]:
   a. Calculate complement: x = K - arr[i]
   b. If x exists in map, add its frequency to count
      (This counts all pairs where arr[i] is paired with x)
   c. Special case: If x == arr[i], subtract 1
      (Avoid counting element with itself)
3. Return count // 2 (divide by 2 as each pair counted twice)

WHY DIVIDE BY 2?
=================
Each pair (a, b) is counted twice in our algorithm:
- Once when we process element 'a' (finding 'b' as complement)
- Once when we process element 'b' (finding 'a' as complement)

Example: arr = [1, 5], K = 6
- Process 1: complement = 5, found in map → count += 1
- Process 5: complement = 1, found in map → count += 1
- Total count = 2, but actual pairs = 1
- Return count // 2 = 1 ✓

WHY SUBTRACT 1 WHEN x == arr[i]?
==================================
When K = 2 * arr[i], the element pairs with itself.
We need to avoid counting the same element at the same index as a pair.

Example: arr = [3, 3, 6], K = 6
When processing arr[0] = 3:
- complement x = 6 - 3 = 3
- frequency of 3 in map = 2
- But we can't pair arr[0] with itself!
- count += 2 - 1 = 1 (pair arr[0] with arr[1] only)

FLOW EXAMPLE:
=============
Array: [1, 5, 7, 1], K = 6
Goal: Count pairs that sum to 6

Phase 1: Build Frequency Map
-----------------------------
Initial: freq_map = {}, count = 0

Process arr[0] = 1:
    1 not in freq_map → freq_map[1] = 1
    freq_map = {1: 1}

Process arr[1] = 5:
    5 not in freq_map → freq_map[5] = 1
    freq_map = {1: 1, 5: 1}

Process arr[2] = 7:
    7 not in freq_map → freq_map[7] = 1
    freq_map = {1: 1, 5: 1, 7: 1}

Process arr[3] = 1:
    1 in freq_map → freq_map[1] += 1
    freq_map = {1: 2, 5: 1, 7: 1}

Phase 2: Count Pairs
--------------------
Initial: count = 0

Process arr[0] = 1:
    x = 6 - 1 = 5
    Is 5 in freq_map? Yes
    count += freq_map[5] = 0 + 1 = 1
    Is x == arr[0]? No (5 ≠ 1)
    Current count = 1

Process arr[1] = 5:
    x = 6 - 5 = 1
    Is 1 in freq_map? Yes
    count += freq_map[1] = 1 + 2 = 3
    Is x == arr[1]? No (1 ≠ 5)
    Current count = 3

Process arr[2] = 7:
    x = 6 - 7 = -1
    Is -1 in freq_map? No
    count remains 3
    Current count = 3

Process arr[3] = 1:
    x = 6 - 1 = 5
    Is 5 in freq_map? Yes
    count += freq_map[5] = 3 + 1 = 4
    Is x == arr[3]? No (5 ≠ 1)
    Current count = 4

Final count = 4
Return count // 2 = 4 // 2 = 2 ✓

Pairs found: (1,5) at indices (0,1) and (1,5) at indices (3,1)

DETAILED EXAMPLE WITH DUPLICATES:
==================================
Array: [1, 1, 1, 1], K = 2
Goal: Count pairs that sum to 2

Phase 1: Build Frequency Map
    freq_map = {1: 4}  (four 1's)

Phase 2: Count Pairs
Process arr[0] = 1:
    x = 2 - 1 = 1
    count += freq_map[1] = 0 + 4 = 4
    x == arr[0] (1 == 1) → count -= 1 = 3

Process arr[1] = 1:
    x = 2 - 1 = 1
    count += freq_map[1] = 3 + 4 = 7
    x == arr[1] (1 == 1) → count -= 1 = 6

Process arr[2] = 1:
    x = 2 - 1 = 1
    count += freq_map[1] = 6 + 4 = 10
    x == arr[2] (1 == 1) → count -= 1 = 9

Process arr[3] = 1:
    x = 2 - 1 = 1
    count += freq_map[1] = 9 + 4 = 13
    x == arr[3] (1 == 1) → count -= 1 = 12

Final count = 12
Return count // 2 = 12 // 2 = 6 ✓

Verification: Pairs are (0,1), (0,2), (0,3), (1,2), (1,3), (2,3) = 6 pairs

FLOWCHART:
==========
    ┌──────────────────────────────────┐
    │ Start: getPairsCount(arr, n, k)  │
    └────────────┬─────────────────────┘
                 │
                 ▼
    ┌──────────────────────────────────┐
    │ Initialize:                      │
    │ freq_map = {} (empty dict)       │
    │ count = 0                        │
    └────────────┬─────────────────────┘
                 │
                 ▼
    ┌──────────────────────────────────┐
    │ PHASE 1: Build Frequency Map     │
    │ For i = 0 to n-1                 │
    └────────────┬─────────────────────┘
                 │
                 ▼
    ┌──────────────────────────────────┐
    │   Is arr[i] in freq_map?         │
    └────┬────────────────────────┬────┘
         │ No                     │ Yes
         │                        │
         ▼                        ▼
    ┌────────────────┐   ┌───────────────────┐
    │ freq_map[arr[i]│   │ freq_map[arr[i]]  │
    │ = 1            │   │ += 1              │
    │ (first time)   │   │ (increment count) │
    └────┬───────────┘   └────┬──────────────┘
         │                    │
         └────────┬───────────┘
                  │
                  ▼
    ┌──────────────────────────────────┐
    │ More elements in array?          │
    └────┬────────────────────────┬────┘
         │ Yes (loop)             │ No
         │                        │
         └────────────────────────┘
                                  │
                                  ▼
    ┌──────────────────────────────────┐
    │ PHASE 2: Count Pairs             │
    │ For i = 0 to n-1                 │
    └────────────┬─────────────────────┘
                 │
                 ▼
    ┌──────────────────────────────────┐
    │ Calculate complement:            │
    │ x = k - arr[i]                   │
    └────────────┬─────────────────────┘
                 │
                 ▼
    ┌──────────────────────────────────┐
    │   Is x in freq_map?              │
    └────┬────────────────────────┬────┘
         │ No                     │ Yes
         │                        │
         │                        ▼
         │         ┌─────────────────────────┐
         │         │ count += freq_map[x]    │
         │         │ (add all pairs with x)  │
         │         └──────────┬──────────────┘
         │                    │
         │                    ▼
         │         ┌─────────────────────────┐
         │         │   Is x == arr[i]?       │
         │         └────┬────────────────┬───┘
         │              │ Yes            │ No
         │              │                │
         │              ▼                │
         │    ┌──────────────────┐      │
         │    │ count -= 1       │      │
         │    │ (avoid self-pair)│      │
         │    └────┬─────────────┘      │
         │         │                    │
         └─────────┴────────────────────┘
                   │
                   ▼
    ┌──────────────────────────────────┐
    │ More elements in array?          │
    └────┬────────────────────────┬────┘
         │ Yes (loop)             │ No
         │                        │
         └────────────────────────┘
                                  │
                                  ▼
    ┌──────────────────────────────────┐
    │ Return count // 2                │
    │ (each pair counted twice)        │
    └──────────────────────────────────┘

MATHEMATICAL FORMULA FOR IDENTICAL ELEMENTS:
============================================
When all n elements are identical and K = 2 * element:
Number of pairs = n * (n - 1) / 2

Example: arr = [1, 1, 1, 1], K = 2, n = 4
Pairs = 4 * 3 / 2 = 6 ✓

This is the combination formula C(n, 2) = "n choose 2"

Our algorithm computes this correctly:
- Each element adds (freq - 1) after pairing with all others
- Sum = 4 + 4 + 4 + 4 - 4 (subtract 1 each time) = 12
- Divide by 2: 12 / 2 = 6 ✓

EDGE CASES:
===========
1. Empty array: Return 0
2. Single element: Return 0 (can't form pair)
3. No pairs sum to K: Return 0
4. All elements same: Use combination formula
5. Negative numbers: Works correctly
6. Zero in array: Works correctly

TIME COMPLEXITY:  O(n) - Two passes through array (build map + count pairs)
SPACE COMPLEXITY: O(n) - Hash map stores at most n unique elements
"""


class Solution:
    """
    Solution class for counting pairs with a given sum.

    This class provides an efficient method to count the number of pairs
    in an array that sum to a specified value. It uses a hash map to
    track element frequencies for O(n) time complexity.

    The algorithm handles duplicates correctly and avoids counting
    the same pair twice or pairing an element with itself.
    """

    def getPairsCount(self, arr, n, k):
        """
        Count the number of pairs in the array that sum to k.

        This method uses a two-phase approach:
        1. Build a frequency map of all elements
        2. For each element, check if its complement exists and count pairs

        Args:
            arr (list): The input array of integers
            n (int): Size of the array
            k (int): Target sum value

        Returns:
            int: Number of pairs in the array that sum to k

        Time Complexity: O(n) - Two passes through the array
        Space Complexity: O(n) - Hash map in worst case stores all unique elements

        Example:
            >>> solution = Solution()
            >>> solution.getPairsCount([1, 5, 7, 1], 4, 6)
            2
        """
        # Dictionary to track frequency of each element
        # Key: the element value, Value: count of occurrences
        freq_map = {}

        # Counter for the total number of pairs found
        count = 0

        # PHASE 1: Build frequency map
        # Count the occurrence of each element in the array
        for i in range(n):
            # If this element appears for the first time
            if arr[i] not in freq_map:
                # Initialize its frequency to 1
                freq_map[arr[i]] = 1
            else:
                # If element already seen, increment its frequency
                freq_map[arr[i]] += 1

        # PHASE 2: Count pairs
        # For each element, find how many elements it can pair with
        for i in range(n):
            # Calculate the complement: what value do we need to reach sum k?
            # If arr[i] + x = k, then x = k - arr[i]
            x = k - arr[i]

            # Check if the complement exists in our frequency map
            if x in freq_map:
                # Add the frequency of complement to count
                # This counts all possible pairs of arr[i] with x
                # (arr[i] can pair with every occurrence of x)
                count += freq_map[x]

                # Special case: If complement equals current element
                # We need to avoid pairing element with itself at same index
                if x == arr[i]:
                    # Subtract 1 to exclude self-pairing
                    # (arr[i] cannot pair with itself)
                    count -= 1

        # Each pair (a, b) has been counted twice:
        # - Once when processing 'a' (finding 'b')
        # - Once when processing 'b' (finding 'a')
        # So we divide by 2 to get the actual number of unique pairs
        return count // 2


# Test cases
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Test 1: Standard case with duplicates
    arr1 = [1, 5, 7, 1]
    n1 = len(arr1)
    k1 = 6
    result1 = solution.getPairsCount(arr1, n1, k1)
    print(f"Array: {arr1}, K: {k1}")
    print(f"Number of pairs: {result1}")  # Expected: 2
    print("Pairs: (1,5) at indices (0,1) and (1,5) at indices (3,1)\n")

    # Test 2: All elements same
    arr2 = [1, 1, 1, 1]
    n2 = len(arr2)
    k2 = 2
    result2 = solution.getPairsCount(arr2, n2, k2)
    print(f"Array: {arr2}, K: {k2}")
    print(f"Number of pairs: {result2}")  # Expected: 6
    print("Pairs: (0,1), (0,2), (0,3), (1,2), (1,3), (2,3)\n")

    # Test 3: No pairs sum to K
    arr3 = [10, 12, 10, 15, -1]
    n3 = len(arr3)
    k3 = 125
    result3 = solution.getPairsCount(arr3, n3, k3)
    print(f"Array: {arr3}, K: {k3}")
    print(f"Number of pairs: {result3}")  # Expected: 0
    print("No pairs sum to 125\n")

    # Test 4: Array with negative numbers
    arr4 = [1, 5, 7, -1, 5]
    n4 = len(arr4)
    k4 = 6
    result4 = solution.getPairsCount(arr4, n4, k4)
    print(f"Array: {arr4}, K: {k4}")
    print(f"Number of pairs: {result4}")  # Expected: 3
    print("Pairs: (1,5), (7,-1), (1,5) at indices (0,1), (2,3), (0,4)\n")

    # Test 5: Single pair
    arr5 = [1, 2, 3, 4]
    n5 = len(arr5)
    k5 = 5
    result5 = solution.getPairsCount(arr5, n5, k5)
    print(f"Array: {arr5}, K: {k5}")
    print(f"Number of pairs: {result5}")  # Expected: 2
    print("Pairs: (1,4), (2,3)\n")

    # Test 6: Array with zeros
    arr6 = [0, 0, 5, 5]
    n6 = len(arr6)
    k6 = 0
    result6 = solution.getPairsCount(arr6, n6, k6)
    print(f"Array: {arr6}, K: {k6}")
    print(f"Number of pairs: {result6}")  # Expected: 1
    print("Pairs: (0,0) at indices (0,1)\n")

    # Test 7: Large numbers
    arr7 = [100, 200, 300, 400, 500]
    n7 = len(arr7)
    k7 = 500
    result7 = solution.getPairsCount(arr7, n7, k7)
    print(f"Array: {arr7}, K: {k7}")
    print(f"Number of pairs: {result7}")  # Expected: 2
    print("Pairs: (100,400), (200,300)\n")
