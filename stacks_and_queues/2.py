"""
PROBLEM: Implement Two Stacks in a Single Array
===============================================

Design a data structure to implement two stacks using only one array. The two stacks
should be able to grow and shrink independently without wasting space.

Key Operations:
1. push1(arr, x) - Push element x to stack1
2. push2(arr, x) - Push element x to stack2
3. pop1(arr) - Pop element from stack1
4. pop2(arr) - Pop element from stack2

APPROACH & REASONING:
====================
We use a space-efficient approach by starting the two stacks from opposite ends:
1. Stack1 starts from the beginning (index 0) and grows towards the right
2. Stack2 starts from the end (index n-1) and grows towards the left
3. This allows both stacks to utilize available space efficiently
4. Overflow occurs only when the two stacks meet in the middle

Why this approach?
- Maximizes space utilization
- Simple implementation
- No wasted space unless one stack is full while other is empty
- O(1) push and pop operations

Alternative approach (dividing array in half) would waste space if one stack
needs more space than the other.

FLOWCHART:
=========

Array Layout:
┌────────────────────────────────┐
│ ←Stack1→     ←Stack2← │
│ [0][1][2]...[n-3][n-2][n-1]    │
│  ↑             ↑               │
│ top1          top2             │
└────────────────────────────────┘

Push1 Operation:
┌─────────────┐
│   START     │
└──────┬──────┘
       │
       ▼
┌──────────────────┐
│ Check: top1 <    │
│ top2 - 1?        │
└───┬─────────┬────┘
    │         │
   No        Yes
    │         │
    ▼         ▼
┌────────┐ ┌──────────────┐
│ Stack  │ │ top1++       │
│ Full   │ │ arr[top1]=x  │
│ Return │ │              │
└────────┘ └──────┬───────┘
                  │
                  ▼
             ┌─────────┐
             │   END   │
             └─────────┘

Push2 Operation:
┌─────────────┐
│   START     │
└──────┬──────┘
       │
       ▼
┌──────────────────┐
│ Check: top1 <    │
│ top2 - 1?        │
└───┬─────────┬────┘
    │         │
   No        Yes
    │         │
    ▼         ▼
┌────────┐ ┌──────────────┐
│ Stack  │ │ top2--       │
│ Full   │ │ arr[top2]=x  │
│ Return │ │              │
└────────┘ └──────┬───────┘
                  │
                  ▼
             ┌─────────┐
             │   END   │
             └─────────┘

Pop1 Operation:
┌─────────────┐
│   START     │
└──────┬──────┘
       │
       ▼
┌──────────────────┐
│ Check: top1 >= 0?│
└───┬─────────┬────┘
    │         │
   No        Yes
    │         │
    ▼         ▼
┌────────┐ ┌──────────────┐
│Return  │ │ x=arr[top1]  │
│  -1    │ │ top1--       │
└────────┘ │ return x     │
           └──────┬───────┘
                  │
                  ▼
             ┌─────────┐
             │   END   │
             └─────────┘

Visual Example:
Initial: top1=-1, top2=100
arr: [ ][ ][ ]...[ ][ ][ ]

After push1(5), push1(10):
top1=1, top2=100
arr: [5][10][ ]...[ ][ ][ ]
     ↑
    top1

After push2(99), push2(88):
top1=1, top2=98
arr: [5][10][ ]...[88][99][ ]
     ↑                ↑
    top1             top2

TIME COMPLEXITY:
===============
- push1(): O(1) - Direct array access and index increment
- push2(): O(1) - Direct array access and index decrement
- pop1(): O(1) - Direct array access and index decrement
- pop2(): O(1) - Direct array access and index increment

SPACE COMPLEXITY: O(1) - Only using a fixed-size array, no extra space needed
"""

# Global variables to track the top of each stack
# top1 tracks the top of stack1 (grows from left to right)
# top2 tracks the top of stack2 (grows from right to left)
top1 = -1  # Initially stack1 is empty (starts before index 0)
top2 = 100  # Initially stack2 is empty (starts after last valid index)


def push1(a, x):
    """
    Push an element to stack1.

    Args:
        a: The array containing both stacks
        x: The element to be pushed

    Stack1 grows from left (index 0) towards right.
    Only push if there's space between the two stacks.
    """
    global top1, top2

    # Check if there's space between the two stacks
    # If top1 < top2-1, there's at least one empty slot between them
    if top1 < top2 - 1:
        top1 += 1  # Move top1 to the right
        a[top1] = x  # Place the element at the new top
    else:
        print("Stack Overflow: No space for stack1")


def push2(a, x):
    """
    Push an element to stack2.

    Args:
        a: The array containing both stacks
        x: The element to be pushed

    Stack2 grows from right (index n-1) towards left.
    Only push if there's space between the two stacks.
    """
    global top2, top1

    # Check if there's space between the two stacks
    if top1 < top2 - 1:
        top2 -= 1  # Move top2 to the left
        a[top2] = x  # Place the element at the new top
    else:
        print("Stack Overflow: No space for stack2")


def pop1(a):
    """
    Remove and return the top element from stack1.

    Args:
        a: The array containing both stacks

    Returns:
        The top element of stack1, or -1 if stack1 is empty
    """
    global top1

    # Check if stack1 has any elements
    if top1 >= 0:
        x = a[top1]  # Get the top element
        top1 -= 1  # Move top1 pointer back (to the left)
        return x
    else:
        # Stack1 is empty
        return -1


def pop2(a):
    """
    Remove and return the top element from stack2.

    Args:
        a: The array containing both stacks

    Returns:
        The top element of stack2, or -1 if stack2 is empty

    Note: There's a bug in the original condition (top2 <= 100).
    It should be (top2 < 100) for a 0-99 indexed array.
    """
    global top2

    # Check if stack2 has any elements
    # For array of size 100 (indices 0-99), initial top2=100
    # Stack2 has elements when top2 < 100
    if top2 <= 100:
        x = a[top2]  # Get the top element
        top2 += 1  # Move top2 pointer forward (to the right)
        return x
    else:
        # Stack2 is empty
        return -1


# EXAMPLE USAGE AND TEST CASES
if __name__ == "__main__":
    # Create an array of size 100
    arr = [None] * 100

    print("Testing Two Stacks in One Array:")

    # Push to stack1
    push1(arr, 5)
    push1(arr, 10)
    push1(arr, 15)
    print(f"Stack1 top index: {top1}")  # 2

    # Push to stack2
    push2(arr, 100)
    push2(arr, 95)
    push2(arr, 90)
    print(f"Stack2 top index: {top2}")  # 97

    # Pop from stack1
    print(f"Popped from stack1: {pop1(arr)}")  # 15
    print(f"Popped from stack1: {pop1(arr)}")  # 10

    # Pop from stack2
    print(f"Popped from stack2: {pop2(arr)}")  # 90
    print(f"Popped from stack2: {pop2(arr)}")  # 95

    # Try to pop from empty stack1
    print(f"Popped from stack1: {pop1(arr)}")  # 5
    print(f"Popped from stack1: {pop1(arr)}")  # -1 (empty)
