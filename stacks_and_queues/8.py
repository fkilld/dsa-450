"""
PROBLEM: Next Greater Element
==============================

Given an array, find the Next Greater Element (NGE) for every element.
The Next Greater Element for an element x is the first greater element
on the right side of x in the array.

Elements for which no greater element exists, return -1.

Examples:
- arr = [4, 5, 2, 25]
  NGE = [5, 25, 25, -1]

- arr = [13, 7, 6, 12]
  NGE = [-1, 12, 12, -1]

- arr = [1, 2, 3, 4]
  NGE = [2, 3, 4, -1]

APPROACH & REASONING:
====================
We use a Stack-based approach with indices for O(n) time complexity.

Naive Approach (O(n²)):
For each element, scan all elements to the right to find the next greater.
This is inefficient for large arrays.

Optimized Stack Approach (O(n)):
1. Use stack to store indices of elements
2. For each element, pop all smaller elements from stack
3. The current element is the NGE for all popped elements
4. Process array left to right

Why Stack?
- Stack maintains elements in decreasing order
- When we find a larger element, it's the NGE for all smaller elements in stack
- Each element is pushed and popped at most once → O(n) time

Key Insight:
If we haven't found NGE for an element yet, it's because we haven't seen
a larger element. Stack keeps track of elements waiting for their NGE.

FLOWCHART:
=========

┌────────────────┐
│    START       │
└───────┬────────┘
        │
        ▼
┌────────────────┐
│ Initialize:    │
│ stack = [0]    │
│ ans = [-1]*n   │
└───────┬────────┘
        │
        ▼
┌────────────────┐
│ For i=1 to n-1 │◄──────┐
└───┬────────────┘       │
    │                    │
    ▼                    │
┌────────────────┐       │
│ curr = arr[i]  │       │
└───────┬────────┘       │
        │                │
        ▼                │
┌────────────────┐       │
│ While stack    │       │
│ not empty AND  │◄──┐   │
│ arr[top]<curr  │   │   │
└───┬───────┬────┘   │   │
    │       │        │   │
   No      Yes       │   │
    │       │        │   │
    │       ▼        │   │
    │  ┌─────────┐   │   │
    │  │ top =   │   │   │
    │  │ stack.  │   │   │
    │  │ pop()   │   │   │
    │  └────┬────┘   │   │
    │       │        │   │
    │       ▼        │   │
    │  ┌─────────┐   │   │
    │  │ans[top] │   │   │
    │  │ = curr  │   │   │
    │  └────┬────┘   │   │
    │       │        │   │
    │       └────────┘   │
    │                    │
    ▼                    │
┌────────────────┐       │
│ If arr[top] >  │       │
│ curr:          │       │
│ stack.push(top)│       │
└───────┬────────┘       │
        │                │
        ▼                │
┌────────────────┐       │
│ stack.push(i)  │       │
└───────┬────────┘       │
        │                │
        └────────────────┘
        │
        ▼
┌────────────────┐
│  Return ans    │
└───────┬────────┘
        │
        ▼
┌────────────────┐
│      END       │
└────────────────┘

Example Trace for [4, 5, 2, 25]:

Step 1: i=0, arr[0]=4
  stack = [0]
  ans = [-1, -1, -1, -1]

Step 2: i=1, arr[1]=5
  curr=5, top=0, arr[0]=4 < 5
  Pop 0, set ans[0]=5
  stack = [1]
  ans = [5, -1, -1, -1]

Step 3: i=2, arr[2]=2
  curr=2, top=1, arr[1]=5 > 2
  Push top back, push 2
  stack = [1, 2]
  ans = [5, -1, -1, -1]

Step 4: i=3, arr[3]=25
  curr=25, top=2, arr[2]=2 < 25
  Pop 2, set ans[2]=25
  curr=25, top=1, arr[1]=5 < 25
  Pop 1, set ans[1]=25
  stack = [3]
  ans = [5, 25, 25, -1]

TIME COMPLEXITY:
===============
- O(n) where n is the length of the array
- Each element is pushed once and popped once
- Total operations = 2n = O(n)

SPACE COMPLEXITY:
================
- O(n) for the stack
- In worst case (descending array), all elements in stack
- O(n) for the answer array
"""

class Solution:
    def nextLargerElement(self, arr, n):
        """
        Find the next greater element for each element in the array.

        Args:
            arr: Input array of integers
            n: Length of the array

        Returns:
            List where ans[i] is the next greater element for arr[i],
            or -1 if no greater element exists
        """
        # Stack stores indices of array elements (not the elements themselves)
        stack = []

        # Initialize answer array with -1 (default for no NGE found)
        ans = [-1] * n

        # Push the index of first element onto the stack
        stack.append(0)

        # Iterate through the array starting from second element
        for i in range(1, n):
            # Get the current element
            curr = arr[i]

            # Pop elements from stack while:
            # 1. Stack is not empty
            # 2. Current element is greater than element at stack top
            top = stack.pop()

            while arr[top] < curr:
                # Current element is the NGE for the element at index 'top'
                ans[top] = curr

                # If stack becomes empty, break out of the loop
                if len(stack) == 0:
                    break

                # Continue checking with next element in stack
                top = stack.pop()

            # If the element at top is greater than current element,
            # push it back to stack (it might be NGE for future elements)
            if arr[top] > curr:
                stack.append(top)

            # Push current element's index onto stack
            # It's waiting for its NGE
            stack.append(i)

        # Elements remaining in stack have no NGE (already initialized to -1)
        return ans


# EXAMPLE USAGE AND TEST CASES
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([4, 5, 2, 25], [5, 25, 25, -1]),
        ([13, 7, 6, 12], [-1, 12, 12, -1]),
        ([1, 2, 3, 4], [2, 3, 4, -1]),
        ([4, 3, 2, 1], [-1, -1, -1, -1]),  # Descending
        ([1, 2, 3, 4, 5], [2, 3, 4, 5, -1]),  # Ascending
        ([5], [-1]),  # Single element
    ]

    print("Testing Next Greater Element:")
    for arr, expected in test_cases:
        result = solution.nextLargerElement(arr, len(arr))
        status = "✓" if result == expected else "✗"
        print(f"{status} {arr}")
        print(f"   NGE: {result}")
        print(f"   Expected: {expected}\n")
