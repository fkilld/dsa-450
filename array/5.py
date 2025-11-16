"""
PROBLEM: Union of Two Arrays
==============================
Find the count of distinct elements that appear in either array or both (union of two arrays).

Example:
    Input:  a = [1, 2, 3, 4, 5], b = [1, 2, 3]
    Output: 5
    Explanation: Union has elements {1, 2, 3, 4, 5}

    Input:  a = [85, 25, 1, 32, 54, 6], b = [85, 2]
    Output: 7
    Explanation: Union has elements {1, 2, 6, 25, 32, 54, 85}

    Input:  a = [1, 2, 1, 1, 2], b = [2, 2, 1, 2, 1]
    Output: 2
    Explanation: Union has elements {1, 2} (duplicates are counted once)

APPROACH: Hash Map / Dictionary
=================================
WHY THIS APPROACH?
- Need to count unique/distinct elements only
- Hash map provides O(1) average time for lookup and insertion
- Can handle duplicates within arrays efficiently
- Single pass through both arrays

ALTERNATIVE APPROACHES:
1. Sorting + Two Pointers: O((n+m) log(n+m)) time, O(1) space
2. Hash Set: Similar to hash map but using set instead of dictionary
3. Brute Force: O(n*m) time checking each element

HOW IT WORKS:
1. Create a hash map (dictionary) to track seen elements
2. Iterate through first array 'a':
   - If element not in map, add it and increment count
   - If already in map, skip it (duplicate)
3. Iterate through second array 'b':
   - If element not in map, add it and increment count
   - If already in map, skip it (duplicate from array 'a' or within 'b')
4. Return the count of unique elements

FLOW EXAMPLE:
=============
Array a: [1, 2, 3, 4, 5, 6]
Array b: [6, 7, 8, 9, 10, 11]
Goal: Count distinct elements in union

Step 1: Process array 'a'
    i=0: a[0]=1, not in map → occur={1:1}, count=1
    i=1: a[1]=2, not in map → occur={1:1, 2:1}, count=2
    i=2: a[2]=3, not in map → occur={1:1, 2:1, 3:1}, count=3
    i=3: a[3]=4, not in map → occur={1:1, 2:1, 3:1, 4:1}, count=4
    i=4: a[4]=5, not in map → occur={1:1, 2:1, 3:1, 4:1, 5:1}, count=5
    i=5: a[5]=6, not in map → occur={1:1, 2:1, 3:1, 4:1, 5:1, 6:1}, count=6

Step 2: Process array 'b'
    i=0: b[0]=6, in map (skip) → count=6
    i=1: b[1]=7, not in map → occur={..., 6:1, 7:1}, count=7
    i=2: b[2]=8, not in map → occur={..., 7:1, 8:1}, count=8
    i=3: b[3]=9, not in map → occur={..., 8:1, 9:1}, count=9
    i=4: b[4]=10, not in map → occur={..., 9:1, 10:1}, count=10
    i=5: b[5]=11, not in map → occur={..., 10:1, 11:1}, count=11

Final: count = 11 (elements: 1,2,3,4,5,6,7,8,9,10,11)

FLOWCHART:
==========
    ┌─────────────────────────────┐
    │  Start: union(a, n, b, m)   │
    └──────────────┬──────────────┘
                   │
                   ▼
    ┌─────────────────────────────┐
    │ Initialize:                 │
    │ occur = {} (empty dict)     │
    │ count = 0                   │
    └──────────────┬──────────────┘
                   │
                   ▼
    ┌─────────────────────────────┐
    │ For each element in array a │
    └──────────────┬──────────────┘
                   │
                   ▼
    ┌─────────────────────────────┐
    │   Is a[i] in occur?         │
    └────┬───────────────────┬────┘
         │ Yes (duplicate)   │ No (new)
         │                   │
         │                   ▼
         │      ┌────────────────────────┐
         │      │ occur[a[i]] = 1        │
         │      │ count += 1             │
         │      └────────────┬───────────┘
         │                   │
         └───────────────────┘
                   │
                   ▼
    ┌─────────────────────────────┐
    │ For each element in array b │
    └──────────────┬──────────────┘
                   │
                   ▼
    ┌─────────────────────────────┐
    │   Is b[i] in occur?         │
    └────┬───────────────────┬────┘
         │ Yes (duplicate)   │ No (new)
         │                   │
         │                   ▼
         │      ┌────────────────────────┐
         │      │ occur[b[i]] = 1        │
         │      │ count += 1             │
         │      └────────────┬───────────┘
         │                   │
         └───────────────────┘
                   │
                   ▼
    ┌─────────────────────────────┐
    │      Return count           │
    └─────────────────────────────┘

TIME COMPLEXITY:  O(n + m) - Single pass through both arrays
SPACE COMPLEXITY: O(n + m) - Hash map can store at most n+m unique elements

WHY USE HASH MAP INSTEAD OF SORTING?
======================================
Sorting approach would be:
1. Merge both arrays
2. Sort the merged array: O((n+m) log(n+m))
3. Count unique elements in one pass: O(n+m)
Total: O((n+m) log(n+m)) time, O(n+m) space

Hash map approach:
Total: O(n+m) time, O(n+m) space

Hash map is faster when arrays are large!
"""

class Solution:
    """
    Solution class for finding the union of two arrays.

    Union of two arrays is the set of distinct elements that appear
    in either array or both arrays.
    """

    def union(self, a, n, b, m):
        """
        Find the count of distinct elements in the union of two arrays.

        Args:
            a (list): First input array
            n (int): Length of first array
            b (list): Second input array
            m (int): Length of second array

        Returns:
            int: Count of distinct elements in union

        Time Complexity: O(n + m) - Traverse both arrays once
        Space Complexity: O(n + m) - Hash map in worst case
        """
        # Dictionary to track elements we've already counted
        # Key: the element, Value: 1 (marking that we've seen it)
        occur = {}

        # Counter for the total number of unique elements found
        count = 0

        # Phase 1: Process all elements from array 'a'
        for i in range(n):
            # Check if this element has been seen before
            if a[i] not in occur:
                # If not seen before, mark it as seen in our dictionary
                occur[a[i]] = 1
                # Increment our unique elements counter
                count += 1
            # If element already exists in occur, skip it (duplicate)

        # Phase 2: Process all elements from array 'b'
        for i in range(m):
            # Check if this element has been seen before
            # (either in array 'a' or earlier in 'b')
            if b[i] not in occur:
                # If not seen before, mark it as seen in our dictionary
                occur[b[i]] = 1
                # Increment our unique elements counter
                count += 1
            # If element already exists in occur, skip it (duplicate)

        # Return the total count of unique elements (the union size)
        return count


# Test cases
if __name__ == "__main__":
    # Create an instance of the Solution class
    s = Solution()

    # Test 1: Arrays with one common element
    a1 = [1, 2, 3, 4, 5, 6]
    b1 = [6, 7, 8, 9, 10, 11]
    n1 = len(a1)
    m1 = len(b1)
    print(f"Array a: {a1}")
    print(f"Array b: {b1}")
    print(f"Union count: {s.union(a1, n1, b1, m1)}")  # Expected: 11

    # Test 2: Arrays with multiple duplicates
    a2 = [1, 2, 1, 1, 2]
    b2 = [2, 2, 1, 2, 1]
    n2 = len(a2)
    m2 = len(b2)
    print(f"\nArray a: {a2}")
    print(f"Array b: {b2}")
    print(f"Union count: {s.union(a2, n2, b2, m2)}")  # Expected: 2

    # Test 3: No common elements
    a3 = [1, 3, 5]
    b3 = [2, 4, 6]
    n3 = len(a3)
    m3 = len(b3)
    print(f"\nArray a: {a3}")
    print(f"Array b: {b3}")
    print(f"Union count: {s.union(a3, n3, b3, m3)}")  # Expected: 6
