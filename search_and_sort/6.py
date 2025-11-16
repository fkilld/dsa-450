"""
PROBLEM: Find Missing and Repeating Numbers
Given an unsorted array of size n with elements in range [1, n],
one number appears twice and one number is missing. Find both.

WHY THIS SOLUTION:
We could use extra space (HashSet or count array) but that takes O(n) space.
This solution uses a BRILLIANT in-place technique with O(1) space!

KEY INSIGHT: Array Indices as Hash
- Elements are in range [1, n], perfect for using indices [0, n-1]
- We can mark visited elements by making them NEGATIVE
- If we see a negative number at position, we know that index was visited before = DUPLICATE
- After marking, positive numbers indicate their index was never visited = MISSING

This is also called "Index-based marking" or "Sign-flip technique"

APPROACH:
1. First pass: Mark visited elements by making arr[element-1] negative
   - For each element, go to its corresponding index (element - 1)
   - If that position is already negative → element is DUPLICATE
   - Otherwise, make it negative to mark as visited
2. Second pass: Find positive numbers
   - Positive number at index i means (i+1) was never visited = MISSING

TIME COMPLEXITY: O(n) - two passes
SPACE COMPLEXITY: O(1) - in-place modification

EXAMPLE: arr = [3, 1, 2, 5, 3]
First pass (marking):
  i=0: arr[2] = -2  (mark 3)
  i=1: arr[0] = -3  (mark 1)
  i=2: arr[1] = -1  (mark 2)
  i=3: arr[4] = -3  (mark 5)
  i=4: arr[2] is already negative! → 3 is REPEAT
Array becomes: [-3, -1, -2, 5, -3]

Second pass:
  arr[3] = 5 is positive → index 3 → 4 is MISSING

WHY INTERVIEWER WILL ACCEPT:
- Uses O(1) space instead of O(n) (space-optimal solution)
- Clever use of sign as a marker
- Demonstrates understanding of constraint exploitation (range [1,n])
"""

arr = [int(x) for x in input("Enter the array : ").split()]

repeat, miss = 0, 0

# FIRST PASS: Mark visited elements by making them negative
# If already negative, it's the duplicate
for i in range(len(arr)):
    # Get the index corresponding to current element
    # Use abs() because we might have already made some numbers negative
    index = abs(arr[i]) - 1

    # Check if this index was already visited (marked negative)
    if arr[index] < 0:
        # Already negative means we've seen this number before
        repeat = abs(arr[i])
    else:
        # First time seeing this number, mark it as visited
        # by making the value at this index negative
        arr[index] *= -1

# SECOND PASS: Find the missing number
# The index with positive value is the missing number
for i in range(len(arr)):
    if arr[i] > 0:
        # Index i has positive value, so (i+1) is missing
        miss = i + 1
        break

print(f"Repeating: {repeat}")
print(f"Missing: {miss}")
