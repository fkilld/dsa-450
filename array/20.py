"""
PROBLEM: Find if There Exists a Subarray with Sum Equal to Zero
==================================================================
Given an array of positive and negative numbers, determine if there exists a
subarray (of size at least one) with sum equal to 0.

A subarray is a contiguous portion of an array.

Example:
    Input:  arr = [4, 2, -3, 1, 6]
    Output: True
    Explanation: Subarray [2, -3, 1] has sum = 0

    Input:  arr = [4, 2, 0, 1, 6]
    Output: True
    Explanation: Subarray [0] has sum = 0

    Input:  arr = [-3, 2, 3, 1, 6]
    Output: False
    Explanation: No subarray with sum 0 exists

    Input:  arr = [1, 2, -2, 1]
    Output: True
    Explanation: Subarray [2, -2] has sum = 0

APPROACH: Prefix Sum with Hash Map
====================================
WHY THIS APPROACH?
- Efficient O(n) time complexity using prefix sums
- Hash map enables O(1) lookup for previously seen sums
- Avoids brute force O(n²) approach of checking all subarrays
- Single pass through the array
- Space-time tradeoff: uses O(n) space for O(n) time

KEY INSIGHT:
If the prefix sum at index j equals the prefix sum at index i (where i < j),
then the subarray from index i+1 to j has sum = 0.

This is because: sum[i+1...j] = prefix_sum[j] - prefix_sum[i] = 0

ALTERNATIVE APPROACHES:
1. Brute Force: O(n²) time, O(1) space
   - Check sum of all possible subarrays
   - For each starting index i, compute sum for all ending indices j
   - Very inefficient for large arrays

2. Sorting (doesn't work here):
   - Sorting would destroy subarray information
   - Cannot be used for this problem

HOW IT WORKS (Prefix Sum Approach):
1. Initialize:
   - Empty hash map to store seen prefix sums
   - Variable 's' to track running/prefix sum
   - Flag 'f' to indicate if zero-sum subarray found

2. Iterate through array:
   - Add current element to running sum 's'
   - Check three conditions:
     a) If s == 0: subarray from start to current index has sum 0
     b) If s in hash map: we've seen this sum before, so subarray between
        previous occurrence and now has sum 0
     c) If arr[i] == 0: single element subarray with sum 0

3. If any condition is true, return True
   Otherwise, store current prefix sum in hash map

4. Return False if no zero-sum subarray found

FLOW EXAMPLE:
=============
Array: [4, 2, -3, 1, 6]
Goal: Find if there's a subarray with sum = 0

Initial State:
    s = 0 (prefix sum)
    m = {} (hash map of seen prefix sums)
    f = 0 (flag: 0 = not found, 1 = found)

Step 1: i=0, arr[0]=4
    s = 0 + 4 = 4
    Check: s == 0? NO
    Check: s in m? NO (m is empty)
    Check: arr[0] == 0? NO
    Action: Add to map
    m = {4: 1}
    f = 0

Step 2: i=1, arr[1]=2
    s = 4 + 2 = 6
    Check: s == 0? NO
    Check: s in m? NO (6 not in {4:1})
    Check: arr[1] == 0? NO
    Action: Add to map
    m = {4: 1, 6: 1}
    f = 0

Step 3: i=2, arr[2]=-3
    s = 6 + (-3) = 3
    Check: s == 0? NO
    Check: s in m? NO (3 not in {4:1, 6:1})
    Check: arr[2] == 0? NO
    Action: Add to map
    m = {4: 1, 6: 1, 3: 1}
    f = 0

Step 4: i=3, arr[3]=1
    s = 3 + 1 = 4
    Check: s == 0? NO
    Check: s in m? YES! (4 is in {4:1, 6:1, 3:1})

    FOUND! Prefix sum 4 appeared before at index 0
    This means subarray from index 1 to 3 has sum 0
    Subarray: [2, -3, 1]
    Verification: 2 + (-3) + 1 = 0 ✓

    Action: Set flag
    f = 1
    Break loop

Result: Return True (f == 1)

ANOTHER EXAMPLE WITH ZERO ELEMENT:
===================================
Array: [4, 2, 0, 1, 6]

Step 1: i=0, arr[0]=4 → s=4, m={4:1}, f=0
Step 2: i=1, arr[1]=2 → s=6, m={4:1, 6:1}, f=0
Step 3: i=2, arr[2]=0
    s = 6 + 0 = 6
    Check: s == 0? NO
    Check: s in m? YES (6 is in {4:1, 6:1})
    OR
    Check: arr[2] == 0? YES

    Either condition is true!
    f = 1
    Break loop

Result: Return True

FLOWCHART:
==========
    ┌─────────────────────────────────┐
    │ Start: subArrayExists(arr, n)   │
    └───────────────┬─────────────────┘
                    │
                    ▼
    ┌─────────────────────────────────┐
    │ Initialize:                     │
    │ f = 0 (flag)                    │
    │ m = {} (hash map)               │
    │ s = 0 (prefix sum)              │
    └───────────────┬─────────────────┘
                    │
                    ▼
    ┌─────────────────────────────────┐
    │ For i in range(len(arr))        │
    └───────────────┬─────────────────┘
                    │
                    ▼
    ┌─────────────────────────────────┐
    │ s = s + arr[i]                  │
    │ (Update prefix sum)             │
    └───────────────┬─────────────────┘
                    │
                    ▼
    ┌─────────────────────────────────┐
    │ Check Condition 1:              │
    │ Is s == 0?                      │
    └──────┬────────────────────┬─────┘
           │ Yes                │ No
           │                    │
           ▼                    ▼
    ┌──────────────┐  ┌─────────────────────┐
    │ f = 1        │  │ Check Condition 2:  │
    │ Break        │  │ Is s in m?          │
    └──────┬───────┘  └────┬──────────────┬─┘
           │               │ Yes          │ No
           │               │              │
           │               ▼              ▼
           │      ┌──────────────┐  ┌─────────────────┐
           │      │ f = 1        │  │ Check Cond. 3:  │
           │      │ Break        │  │ Is arr[i] == 0? │
           │      └──────┬───────┘  └────┬──────────┬─┘
           │             │               │ Yes      │ No
           │             │               │          │
           │             │               ▼          ▼
           │             │      ┌──────────────┐  ┌────────┐
           │             │      │ f = 1        │  │ m[s]=1 │
           │             │      │ Break        │  │ (Store)│
           │             │      └──────┬───────┘  └───┬────┘
           │             │             │              │
           │             │             │              │
           └─────────────┴─────────────┴──────────────┘
                                       │
                                       ▼
                          ┌─────────────────────────┐
                          │ Return True if f == 1   │
                          │ Return False if f == 0  │
                          └─────────────────────────┘

WHY DOES THIS WORK?
====================
Prefix Sum Property:
- prefix_sum[j] = arr[0] + arr[1] + ... + arr[j]
- sum(arr[i+1...j]) = prefix_sum[j] - prefix_sum[i]

If prefix_sum[j] == prefix_sum[i], then:
- sum(arr[i+1...j]) = prefix_sum[j] - prefix_sum[i] = 0

Example:
    Array: [1, 2, -2, 1]

    Prefix sums:
    i=0: prefix[0] = 1
    i=1: prefix[1] = 1 + 2 = 3
    i=2: prefix[2] = 3 + (-2) = 1
    i=3: prefix[3] = 1 + 1 = 2

    Notice: prefix[0] = prefix[2] = 1
    Therefore: sum(arr[1...2]) = prefix[2] - prefix[0] = 1 - 1 = 0
    Subarray [2, -2] has sum 0 ✓

TIME COMPLEXITY:  O(n)
- Single pass through array: O(n)
- Each hash map operation (lookup/insert): O(1) average
- Total: O(n)

SPACE COMPLEXITY: O(n)
- Hash map can store up to n unique prefix sums
- In worst case (no duplicates), we store all n prefix sums

EDGE CASES:
===========
1. Array contains zero:
   - Single element [0] forms a zero-sum subarray
   - Condition arr[i] == 0 handles this

2. Entire array sums to zero:
   - Prefix sum becomes 0 at last element
   - Condition s == 0 handles this

3. Empty array:
   - Not considered in this implementation
   - Would need separate check

4. Single element (non-zero):
   - Will correctly return False
   - No subarray with sum 0 exists

5. All positive or all negative:
   - Will correctly return False (unless contains 0)
   - Prefix sum keeps increasing/decreasing
"""

class Solution:
    """
    A class to solve the subarray with zero sum problem.

    This class provides a method to efficiently check if an array contains
    any contiguous subarray that sums to zero using the prefix sum technique.
    """

    def subArrayExists(self, arr, n):
        """
        Check if there is a subarray with sum equal to 0.

        This function uses the prefix sum approach to find a subarray with sum 0.
        We keep track of prefix sums and check if we've seen the same sum before,
        which would indicate that the elements in between sum to zero.

        The algorithm checks three conditions:
        1. If prefix sum becomes 0: subarray from start has sum 0
        2. If prefix sum was seen before: subarray between occurrences has sum 0
        3. If current element is 0: single-element subarray with sum 0

        Args:
            arr (list): An array of integers (positive and negative)
            n (int): Size of the array (not used in implementation,
                     but kept for interface compatibility)

        Returns:
            bool: True if there exists a subarray with sum = 0, False otherwise

        Time Complexity: O(n) - Single pass through array with O(1) hash operations
        Space Complexity: O(n) - Hash map can store up to n prefix sums

        Example:
            >>> sol = Solution()
            >>> sol.subArrayExists([4, 2, -3, 1, 6], 5)
            True  # Subarray [2, -3, 1] has sum 0
            >>> sol.subArrayExists([1, 2, 3, 4], 4)
            False  # No subarray with sum 0
        """
        # Flag to indicate if subarray with sum 0 exists
        # 0 = not found, 1 = found
        f = 0

        # Dictionary to store prefix sums we've encountered
        # Key: prefix sum value
        # Value: 1 (just marking that we've seen this sum)
        m = {}

        # Variable to keep track of the running/prefix sum
        # prefix_sum[i] = arr[0] + arr[1] + ... + arr[i]
        s = 0

        # Iterate through each element in the array
        for i in range(len(arr)):
            # Add current element to the running prefix sum
            s += arr[i]

            # CONDITION 1: Check if prefix sum is 0
            # If yes, subarray from index 0 to current index has sum 0
            # Example: [3, -1, -2] → at index 2, prefix sum = 0
            if s == 0:
                f = 1  # Mark that we found a zero-sum subarray
                break  # No need to continue searching

            # CONDITION 2: Check if this prefix sum was seen before
            # If yes, it means the subarray between the previous occurrence
            # and current index has sum 0
            # Example: [1, 2, -2, 1]
            #   At i=0: s=1, store in map
            #   At i=2: s=1 again! So arr[1..2] = [2, -2] has sum 0
            elif s in m:
                f = 1  # Mark that we found a zero-sum subarray
                break  # No need to continue searching

            # CONDITION 3: Check if current element itself is 0
            # A single element [0] forms a zero-sum subarray
            elif arr[i] == 0:
                f = 1  # Mark that we found a zero-sum subarray
                break  # No need to continue searching

            else:
                # None of the conditions met
                # Store the current prefix sum in the hash map
                # We mark it as 1 to indicate we've seen this sum
                m[s] = 1

        # Return True if flag is 1 (found), False if flag is 0 (not found)
        return True if f == 1 else False


# Test cases
if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()

    # Test 1: Subarray in middle with sum 0
    print("Test 1: Subarray [2, -3, 1] has sum 0")
    print("=" * 50)
    arr1 = [4, 2, -3, 1, 6]
    n1 = len(arr1)
    print(f"Array: {arr1}")
    print(f"Has zero-sum subarray: {sol.subArrayExists(arr1, n1)}")
    # Expected: True (subarray [2, -3, 1] sums to 0)
    print()

    # Test 2: Array contains zero element
    print("Test 2: Array contains 0")
    print("=" * 50)
    arr2 = [4, 2, 0, 1, 6]
    n2 = len(arr2)
    print(f"Array: {arr2}")
    print(f"Has zero-sum subarray: {sol.subArrayExists(arr2, n2)}")
    # Expected: True (subarray [0] sums to 0)
    print()

    # Test 3: No zero-sum subarray
    print("Test 3: No zero-sum subarray")
    print("=" * 50)
    arr3 = [1, 2, 3, 4, 5]
    n3 = len(arr3)
    print(f"Array: {arr3}")
    print(f"Has zero-sum subarray: {sol.subArrayExists(arr3, n3)}")
    # Expected: False
    print()

    # Test 4: Entire array sums to zero
    print("Test 4: Entire array sums to 0")
    print("=" * 50)
    arr4 = [3, 4, -7]
    n4 = len(arr4)
    print(f"Array: {arr4}")
    print(f"Has zero-sum subarray: {sol.subArrayExists(arr4, n4)}")
    # Expected: True (entire array sums to 0)
    print()

    # Test 5: Adjacent elements sum to zero
    print("Test 5: Adjacent elements [2, -2] sum to 0")
    print("=" * 50)
    arr5 = [1, 2, -2, 1]
    n5 = len(arr5)
    print(f"Array: {arr5}")
    print(f"Has zero-sum subarray: {sol.subArrayExists(arr5, n5)}")
    # Expected: True (subarray [2, -2] sums to 0)
    print()

    # Test 6: All negative numbers
    print("Test 6: All negative numbers")
    print("=" * 50)
    arr6 = [-1, -2, -3, -4]
    n6 = len(arr6)
    print(f"Array: {arr6}")
    print(f"Has zero-sum subarray: {sol.subArrayExists(arr6, n6)}")
    # Expected: False
    print()

    # Test 7: Complex case with multiple possibilities
    print("Test 7: Multiple zero-sum subarrays exist")
    print("=" * 50)
    arr7 = [1, -1, 2, -2, 3, -3]
    n7 = len(arr7)
    print(f"Array: {arr7}")
    print(f"Has zero-sum subarray: {sol.subArrayExists(arr7, n7)}")
    # Expected: True (many subarrays: [1,-1], [2,-2], [3,-3], [1,-1,2,-2], etc.)
