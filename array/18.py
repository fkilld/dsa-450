"""
PROBLEM: Find Common Elements in Three Sorted Arrays
======================================================
Given three arrays sorted in increasing order, find all distinct elements that
are common to all three arrays.

Example:
    Input:  a = [1, 5, 10, 20, 40, 80]
            b = [6, 7, 20, 80, 100]
            c = [3, 4, 15, 20, 30, 70, 80, 120]
    Output: [20, 80]
    Explanation: 20 and 80 are the only elements present in all three arrays

    Input:  a = [1, 5, 5]
            b = [3, 4, 5, 5, 10]
            c = [5, 5, 10, 20]
    Output: [5]
    Explanation: 5 is common (duplicates are counted only once)

    Input:  a = [1, 2, 3]
            b = [4, 5, 6]
            c = [7, 8, 9]
    Output: []
    Explanation: No common elements

APPROACH: Hash Map (Dictionary) Frequency Counting
===================================================
WHY THIS APPROACH?
- Hash maps provide O(1) average time for lookup and insertion
- Efficient for handling duplicates within each array
- Works well even if arrays are not sorted (though this problem has sorted arrays)
- Simple to implement and understand
- Can easily be extended to more than three arrays

ALTERNATIVE APPROACHES:
1. Three Pointers (Better for sorted arrays): O(n1 + n2 + n3) time, O(1) space
   - Since arrays are sorted, we can use three pointers
   - Move the pointer with smallest current element forward
   - More space efficient but requires arrays to be sorted

2. Brute Force: O(n1 * n2 * n3) time, O(1) space
   - For each element in array a, check if it exists in b and c
   - Very inefficient for large arrays

HOW IT WORKS (Hash Map Approach):
1. Create frequency maps (dictionaries) for all three arrays
   - Each map stores: {element: frequency_count}
2. Iterate through first array 'a':
   - Check if element exists in all three maps (m1, m2, m3)
   - If yes, add to result list
   - Remove from m1 to avoid duplicates in result
3. Return the list of common elements

FLOW EXAMPLE:
=============
Array a: [1, 5, 10, 20, 40, 80]
Array b: [6, 7, 20, 80, 100]
Array c: [3, 4, 15, 20, 30, 70, 80, 120]
Goal: Find elements common to all three arrays

Step 1: Create frequency maps
    m1 = {1:1, 5:1, 10:1, 20:1, 40:1, 80:1}
    m2 = {6:1, 7:1, 20:1, 80:1, 100:1}
    m3 = {3:1, 4:1, 15:1, 20:1, 30:1, 70:1, 80:1, 120:1}

Step 2: Check each element of array 'a'
    i=0: a[0]=1
         1 in m1? YES
         1 in m2? NO  → Skip

    i=1: a[1]=5
         5 in m1? YES
         5 in m2? NO  → Skip

    i=2: a[2]=10
         10 in m1? YES
         10 in m2? NO  → Skip

    i=3: a[3]=20
         20 in m1? YES
         20 in m2? YES
         20 in m3? YES  → Add to result
         res = [20]
         Remove 20 from m1: m1 = {1:1, 5:1, 10:1, 40:1, 80:1}

    i=4: a[4]=40
         40 in m1? YES
         40 in m2? NO  → Skip

    i=5: a[5]=80
         80 in m1? YES
         80 in m2? YES
         80 in m3? YES  → Add to result
         res = [20, 80]
         Remove 80 from m1: m1 = {1:1, 5:1, 10:1, 40:1}

Final Result: [20, 80]

FLOWCHART:
==========
    ┌─────────────────────────────────────────┐
    │ Start: commonElements(a, b, c, n1, n2, n3)│
    └──────────────────┬──────────────────────┘
                       │
                       ▼
    ┌─────────────────────────────────────────┐
    │ Initialize:                             │
    │ m1 = {}, m2 = {}, m3 = {}              │
    │ res = []                                │
    └──────────────────┬──────────────────────┘
                       │
                       ▼
    ┌─────────────────────────────────────────┐
    │ Build frequency map m1 from array a     │
    │ For each element: m1[element] = count   │
    └──────────────────┬──────────────────────┘
                       │
                       ▼
    ┌─────────────────────────────────────────┐
    │ Build frequency map m2 from array b     │
    │ For each element: m2[element] = count   │
    └──────────────────┬──────────────────────┘
                       │
                       ▼
    ┌─────────────────────────────────────────┐
    │ Build frequency map m3 from array c     │
    │ For each element: m3[element] = count   │
    └──────────────────┬──────────────────────┘
                       │
                       ▼
    ┌─────────────────────────────────────────┐
    │ For each element a[i] in array a        │
    └──────────────────┬──────────────────────┘
                       │
                       ▼
    ┌─────────────────────────────────────────┐
    │ Is a[i] in m1 AND m2 AND m3?            │
    └────────┬───────────────────────┬────────┘
             │ No                    │ Yes
             │                       │
             │                       ▼
             │         ┌──────────────────────────┐
             │         │ Add a[i] to result list  │
             │         │ res.append(a[i])         │
             │         └──────────┬───────────────┘
             │                    │
             │                    ▼
             │         ┌──────────────────────────┐
             │         │ Remove a[i] from m1      │
             │         │ (to avoid duplicates)    │
             │         └──────────┬───────────────┘
             │                    │
             └────────────────────┘
                       │
                       ▼
    ┌─────────────────────────────────────────┐
    │ Return res (list of common elements)    │
    └─────────────────────────────────────────┘

TIME COMPLEXITY:  O(n1 + n2 + n3)
- Building m1: O(n1)
- Building m2: O(n2)
- Building m3: O(n3)
- Checking elements: O(n1) with O(1) lookups
- Total: O(n1 + n2 + n3)

SPACE COMPLEXITY: O(n1 + n2 + n3)
- Three hash maps can store up to n1 + n2 + n3 elements
- Result list can have at most min(n1, n2, n3) elements

WHY REMOVE FROM m1 AFTER ADDING TO RESULT?
===========================================
If array 'a' has duplicate elements like [5, 5, 10], we don't want to add
5 twice to the result. By removing from m1 after first occurrence, we ensure
each distinct element appears only once in the result.

OPTIMIZATION FOR SORTED ARRAYS:
================================
Since the problem states arrays are sorted, a more space-efficient approach
would be using three pointers:
- Time: O(n1 + n2 + n3)
- Space: O(1) (excluding result)

However, the hash map approach is more general and works for unsorted arrays too.
"""

class Solution:
    """
    Solution class for finding common elements in three arrays.
    This class implements methods to identify elements that appear in all three given arrays.
    The implementation uses dictionary-based frequency mapping to efficiently track occurrences.
    """

    def mapping(self, arr, m):
        """
        Creates or updates a frequency map for elements in an array.

        This helper function builds a dictionary where each unique element
        in the array is a key, and its value is the count of occurrences.

        Args:
            arr (list): Input array whose elements need to be counted
            m (dict): Dictionary to store the frequency mapping

        Returns:
            dict: Updated frequency map with counts of each element

        Time Complexity: O(n) where n is length of arr
        Space Complexity: O(n) for storing unique elements
        """
        # Iterate through each element in the array
        for i in range(len(arr)):
            # Check if element is not yet in the dictionary
            if arr[i] not in m:
                # First occurrence: initialize count to 1
                m[arr[i]] = 1
            else:
                # Subsequent occurrence: increment the count
                m[arr[i]] += 1

        # Return the updated frequency map
        return m

    def commonElements(self, a, b, c, n1, n2, n3):
        """
        Finds all common elements present in three arrays using hash maps.

        The algorithm works by:
        1. Creating frequency maps for all three arrays
        2. Checking elements from first array for presence in all maps
        3. Adding common elements to result while avoiding duplicates

        Args:
            a (list): First input array (sorted in increasing order)
            b (list): Second input array (sorted in increasing order)
            c (list): Third input array (sorted in increasing order)
            n1 (int): Length of first array
            n2 (int): Length of second array
            n3 (int): Length of third array

        Returns:
            list: Sorted list of distinct elements common to all three arrays

        Time Complexity: O(n1 + n2 + n3) - Linear time as we iterate through each array once
        Space Complexity: O(n1 + n2 + n3) - Additional space for the three frequency maps

        Example:
            >>> sol = Solution()
            >>> sol.commonElements([1, 5, 10, 20, 40, 80],
            ...                    [6, 7, 20, 80, 100],
            ...                    [3, 4, 15, 20, 30, 70, 80, 120], 6, 5, 8)
            [20, 80]
        """
        # Initialize three empty dictionaries to store frequency maps
        # m1: frequency map for array 'a'
        # m2: frequency map for array 'b'
        # m3: frequency map for array 'c'
        m1, m2, m3 = {}, {}, {}

        # Build frequency map for array 'a'
        # Each element in 'a' is mapped to its occurrence count
        m1 = self.mapping(a, m1)

        # Build frequency map for array 'b'
        m2 = self.mapping(b, m2)

        # Build frequency map for array 'c'
        m3 = self.mapping(c, m3)

        # List to store the common elements found in all three arrays
        res = []

        # Iterate through all elements in array 'a'
        for i in range(n1):
            # Check if current element exists in ALL three frequency maps
            # This ensures the element is present in all three arrays
            if a[i] in m1 and a[i] in m2 and a[i] in m3:
                # Element is common to all three arrays
                # Add it to the result list
                res.append(a[i])

                # Remove this element from m1 to avoid adding duplicates
                # If array 'a' has duplicates like [5, 5], we only want 5 once in result
                m1.pop(a[i])

        # Return the list of common elements
        # Since we iterate through 'a' which is sorted, result is also sorted
        return res


# Test cases
if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()

    # Test 1: Arrays with two common elements
    a1 = [1, 5, 10, 20, 40, 80]
    b1 = [6, 7, 20, 80, 100]
    c1 = [3, 4, 15, 20, 30, 70, 80, 120]
    n1, m1, p1 = len(a1), len(b1), len(c1)
    print(f"Array a: {a1}")
    print(f"Array b: {b1}")
    print(f"Array c: {c1}")
    print(f"Common elements: {sol.commonElements(a1, b1, c1, n1, m1, p1)}")
    # Expected: [20, 80]

    # Test 2: Arrays with duplicates
    a2 = [1, 5, 5]
    b2 = [3, 4, 5, 5, 10]
    c2 = [5, 5, 10, 20]
    n2, m2, p2 = len(a2), len(b2), len(c2)
    print(f"\nArray a: {a2}")
    print(f"Array b: {b2}")
    print(f"Array c: {c2}")
    print(f"Common elements: {sol.commonElements(a2, b2, c2, n2, m2, p2)}")
    # Expected: [5]

    # Test 3: No common elements
    a3 = [1, 2, 3]
    b3 = [4, 5, 6]
    c3 = [7, 8, 9]
    n3, m3, p3 = len(a3), len(b3), len(c3)
    print(f"\nArray a: {a3}")
    print(f"Array b: {b3}")
    print(f"Array c: {c3}")
    print(f"Common elements: {sol.commonElements(a3, b3, c3, n3, m3, p3)}")
    # Expected: []

    # Test 4: All elements common
    a4 = [1, 2, 3]
    b4 = [1, 2, 3]
    c4 = [1, 2, 3]
    n4, m4, p4 = len(a4), len(b4), len(c4)
    print(f"\nArray a: {a4}")
    print(f"Array b: {b4}")
    print(f"Array c: {c4}")
    print(f"Common elements: {sol.commonElements(a4, b4, c4, n4, m4, p4)}")
    # Expected: [1, 2, 3]
