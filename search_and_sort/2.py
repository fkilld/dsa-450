"""
PROBLEM: Value Equal to Index
Given an array of N positive integers, find all elements whose value equals their index (1-based).

WHY THIS SOLUTION:
This is a straightforward linear search problem where we CANNOT use binary search because:
1. The array is NOT necessarily sorted
2. We need to check the relationship between VALUE and INDEX (not search for a value)
3. There's no pattern to exploit - we must check each element

A single pass O(n) solution is optimal here because:
- We need to examine every element at least once
- We cannot skip any elements since any position might have value == index
- No preprocessing (like sorting) would help us

APPROACH:
Simply iterate through the array and check if arr[i] == i+1 (since array uses 0-based indexing
but problem uses 1-based indexing).

TIME COMPLEXITY: O(n) - must check every element
SPACE COMPLEXITY: O(k) where k is the number of matching elements (for result array)

EXAMPLE: arr = [15, 2, 45, 4, 7]
- Index 1 (0 in array): arr[0]=15, not equal to 1
- Index 2 (1 in array): arr[1]=2, equals 2 ✓
- Index 3 (2 in array): arr[2]=45, not equal to 3
- Index 4 (3 in array): arr[3]=4, equals 4 ✓
- Index 5 (4 in array): arr[4]=7, not equal to 5
Result: [2, 4]

INTERVIEW TIP:
This problem tests whether you understand when NOT to use binary search.
Not every array problem needs binary search - only when there's a sorted property to exploit.
"""

arr = [int(x) for x in input("Enter the array : ").split()]

# Result list to store all matching indices
res = []

# Iterate through array checking each element
for i in range(len(arr)):
    # Check if value equals 1-based index
    # arr[i] is the value, (i + 1) is the 1-based index
    if i + 1 == arr[i]:
        res.append(i + 1)

# Print result
if res:
    print("Elements equal to their index:", res)
else:
    print("No elements found where value equals index")
