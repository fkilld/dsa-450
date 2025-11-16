"""
PROBLEM: Find the Duplicate Number
====================================
Given an array of n+1 integers where each integer is in the range [1, n] inclusive,
there is exactly one repeated number. Find and return this duplicate number.

Example:
    Input:  nums = [1, 3, 4, 2, 2]
    Output: 2
    Explanation: The number 2 appears twice.

    Input:  nums = [3, 1, 3, 4, 2]
    Output: 3

APPROACH: Hash Map (Dictionary) Tracking
==========================================
WHY THIS APPROACH?
- Simple and intuitive: Use a hash map to track which numbers we've seen
- As we traverse, if we encounter a number already in our hash map, it's the duplicate
- Time-efficient O(n), but uses O(n) extra space

ALTERNATIVE APPROACHES:
1. Sort and compare adjacent elements: O(n log n) time, O(1) space
2. Floyd's Cycle Detection: O(n) time, O(1) space (treats array as linked list)
3. Hash Map (current): O(n) time, O(n) space

HOW IT WORKS:
1. Create an empty dictionary to track seen numbers
2. For each element in array:
   - If element already exists in dictionary → it's the duplicate, return it
   - Otherwise, add element to dictionary

FLOW EXAMPLE:
=============
Array: [1, 3, 4, 2, 2]

Step 1: el=1
    1 in num? No
    num = {1: 1}

Step 2: el=3
    3 in num? No
    num = {1: 1, 3: 1}

Step 3: el=4
    4 in num? No
    num = {1: 1, 3: 1, 4: 1}

Step 4: el=2
    2 in num? No
    num = {1: 1, 3: 1, 4: 1, 2: 1}

Step 5: el=2
    2 in num? Yes! Found duplicate
    Return 2

TIME COMPLEXITY:  O(n) - Single pass through array
SPACE COMPLEXITY: O(n) - Dictionary stores up to n elements
"""

class Solution:
    def findDuplicate(self, nums):
        """
        Find the duplicate number in an array.

        Args:
            nums: Array of n+1 integers in range [1, n]

        Returns:
            The duplicate number
        """
        # Dictionary to keep track of elements we've seen
        # Key: element value, Value: 1 (marking that we've seen it)
        num = {}

        # Traverse through each element in the array
        for el in nums:
            # Check if this element has been seen before
            if el in num:
                # If element is occurring again, it's the duplicate
                return el
            else:
                # Element is occurring for the first time, mark it as seen
                num[el] = 1