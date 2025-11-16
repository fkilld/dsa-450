"""
PROBLEM: Check if Array is Subset of Another Array
===================================================
Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m.
Task: Check if a2[] is a subset of a1[] or not.

A subset means: Every element in a2 should be present in a1.
Note: Duplicates are allowed, and order doesn't matter.

Example 1:
    Input:  a1 = [11, 1, 13, 21, 3, 7]
            a2 = [11, 3, 7, 1]
    Output: "Yes"
    Explanation: All elements of a2 (11, 3, 7, 1) are present in a1

Example 2:
    Input:  a1 = [1, 2, 3, 4, 5, 6]
            a2 = [1, 2, 4]
    Output: "Yes"
    Explanation: All elements of a2 (1, 2, 4) are present in a1

Example 3:
    Input:  a1 = [10, 5, 2, 23, 19]
            a2 = [19, 5, 3]
    Output: "No"
    Explanation: Element 3 from a2 is not present in a1

APPROACH: Hash Map (Set) Lookup
================================
WHY THIS APPROACH?
- Checking if an element exists in a1 for each element in a2
- Using a hash map/set gives O(1) lookup time
- More efficient than nested loops which would be O(n*m)
- Trade-off: Use extra space O(n) for faster time complexity

ALTERNATIVE APPROACHES:
1. Nested Loops: O(n*m) time, O(1) space - Check each a2 element in a1
2. Sort Both Arrays: O(n log n + m log m) time, O(1) space - Use two pointers
3. Hash Map (current): O(n+m) time, O(n) space - Best for large arrays

HOW IT WORKS:
1. Create a hash map/dictionary from all elements in a1
2. For each element in a2:
   - Check if it exists in the hash map
   - If yes, increment counter
3. If counter equals m (size of a2), then a2 is a subset

FLOW EXAMPLE:
=============
a1 = [11, 1, 13, 21, 3, 7]  (n = 6)
a2 = [11, 3, 7, 1]          (m = 4)

Step 1: Build hash map from a1
    i=0: hash_map[11] = 1 → {11: 1}
    i=1: hash_map[1] = 1  → {11: 1, 1: 1}
    i=2: hash_map[13] = 1 → {11: 1, 1: 1, 13: 1}
    i=3: hash_map[21] = 1 → {11: 1, 1: 1, 13: 1, 21: 1}
    i=4: hash_map[3] = 1  → {11: 1, 1: 1, 13: 1, 21: 1, 3: 1}
    i=5: hash_map[7] = 1  → {11: 1, 1: 1, 13: 1, 21: 1, 3: 1, 7: 1}

    Final hash_map: {11: 1, 1: 1, 13: 1, 21: 1, 3: 1, 7: 1}

Step 2: Check each element of a2 in hash_map
    found_count = 0

    i=0: a2[0] = 11
        11 in hash_map? Yes
        found_count = 1

    i=1: a2[1] = 3
        3 in hash_map? Yes
        found_count = 2

    i=2: a2[2] = 7
        7 in hash_map? Yes
        found_count = 3

    i=3: a2[3] = 1
        1 in hash_map? Yes
        found_count = 4

Step 3: Check if all elements found
    found_count (4) == m (4)? Yes
    Return "Yes"

EXAMPLE WITH "No" RESULT:
==========================
a1 = [10, 5, 2, 23, 19]  (n = 5)
a2 = [19, 5, 3]          (m = 3)

hash_map from a1: {10: 1, 5: 1, 2: 1, 23: 1, 19: 1}

Check a2 elements:
    i=0: 19 in hash_map? Yes → found_count = 1
    i=1: 5 in hash_map? Yes → found_count = 2
    i=2: 3 in hash_map? No → found_count = 2 (no change)

found_count (2) == m (3)? No
Return "No"

WHY USE HASH MAP VALUE = 1?
The value 1 is just a marker that the element exists.
We could use any value, or even use a Python set instead of dictionary.

TIME COMPLEXITY:  O(n + m) - O(n) to build hash map, O(m) to check elements
SPACE COMPLEXITY: O(n) - Hash map stores n elements from a1
"""

def isSubset(a1, a2, n, m):
    """
    Check if array a2 is a subset of array a1 using hash map approach.

    Args:
        a1: First array (the larger set) of size n
        a2: Second array (potential subset) of size m
        n: Size of array a1
        m: Size of array a2

    Returns:
        "Yes" if a2 is a subset of a1, "No" otherwise

    Example:
        >>> isSubset([11, 1, 13, 21, 3, 7], [11, 3, 7, 1], 6, 4)
        "Yes"
        >>> isSubset([10, 5, 2, 23, 19], [19, 5, 3], 5, 3)
        "No"
    """
    # STEP 1: Build hash map from array a1
    # Create a dictionary to store all elements of a1
    # Key: element value, Value: 1 (marker that element exists)
    # This allows O(1) lookup time when checking a2 elements
    hash_map = {}

    # Populate the hash map with all elements from a1
    # Loop through each element in a1
    for i in range(n):
        # Add element to hash map
        # The value 1 is just a marker; we only care that the key exists
        # Could also use a set instead of dictionary for slightly better performance
        hash_map[a1[i]] = 1

    # STEP 2: Check how many elements of a2 exist in a1
    # Counter to track number of a2 elements found in a1
    # If this equals m at the end, then all elements of a2 are in a1
    found_count = 0

    # Check each element of a2 to see if it exists in hash_map
    for i in range(m):
        # Look up current element of a2 in our hash map
        # Dictionary lookup is O(1) average case
        if a2[i] in hash_map:
            # Element found in a1, increment our counter
            found_count += 1

    # STEP 3: Determine if a2 is a subset
    # If all elements of a2 were found in a1, then a2 is a subset
    # This happens when found_count equals m (total size of a2)
    # Otherwise, some elements of a2 are missing from a1
    return "Yes" if found_count == m else "No"


# Example test cases
if __name__ == "__main__":
    # Test case 1: a2 is a subset
    a1 = [11, 1, 13, 21, 3, 7]
    a2 = [11, 3, 7, 1]
    print(isSubset(a1, a2, len(a1), len(a2)))  # Expected: "Yes"

    # Test case 2: a2 is NOT a subset
    a1 = [10, 5, 2, 23, 19]
    a2 = [19, 5, 3]
    print(isSubset(a1, a2, len(a1), len(a2)))  # Expected: "No"