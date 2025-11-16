"""
PROBLEM: Implement Stack from Scratch
=====================================

A Stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
The last element inserted is the first one to be removed.

Key Operations:
1. push(val) - Add element to top of stack
2. pop() - Remove and return top element
3. peek() - View top element without removing
4. isEmpty() - Check if stack is empty
5. size() - Get number of elements in stack

APPROACH & REASONING:
====================
We use a Python list (dynamic array) as the underlying data structure because:
1. Lists support O(1) amortized append and pop from the end
2. The end of the list represents the top of the stack
3. Simple and efficient implementation

FLOWCHART:
=========

Push Operation:
┌─────────────┐
│   START     │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│ Receive value   │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│ Append to end   │
│   of list       │
└──────┬──────────┘
       │
       ▼
┌─────────────┐
│     END     │
└─────────────┘

Pop Operation:
┌─────────────┐
│   START     │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│ Check if empty  │
└────┬───────┬────┘
     │       │
   Empty   Not Empty
     │       │
     ▼       ▼
┌────────┐ ┌────────────┐
│ Return │ │ Remove &   │
│  None  │ │ return last│
└────────┘ └──────┬─────┘
                  │
                  ▼
             ┌─────────┐
             │   END   │
             └─────────┘

TIME COMPLEXITY:
===============
- push(): O(1) - Append to end of list
- pop(): O(1) - Remove from end of list
- peek(): O(1) - Access last element
- isEmpty(): O(1) - Check length
- size(): O(1) - Get length

SPACE COMPLEXITY: O(n) where n is the number of elements in stack
"""

class Stack:
    def __init__(self) -> None:
        """
        Initialize an empty stack using a list.
        The list will grow dynamically as elements are added.
        """
        self.stack = []

    def push(self, val):
        """
        Push an element onto the stack.

        Args:
            val: The value to be pushed onto the stack

        The element is always inserted at the end of the list,
        which represents the top of the stack.
        """
        self.stack.append(val)

    def pop(self):
        """
        Remove and return the top element from the stack.

        Returns:
            The element at the top of the stack, or None if empty

        Note: This implementation doesn't return the popped value.
        Consider modifying to return self.stack.pop() for better usability.
        """
        if not self.isEmpty():
            # Remove the element from the end (top of stack)
            return self.stack.pop()
        return None

    def printStack(self):
        """
        Display the current state of the stack.
        Useful for debugging and visualization.
        """
        print(f"Stack right now : {self.stack}")

    def peek(self):
        """
        Return the top element without removing it.

        Returns:
            The element at the top of the stack, or None if empty

        This allows inspection of the top element without modifying the stack.
        """
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def size(self):
        """
        Get the current number of elements in the stack.

        Returns:
            Integer representing the size of the stack
        """
        return len(self.stack) if self.stack else 0

    def isEmpty(self):
        """
        Check if the stack is empty.

        Returns:
            True if stack is empty, False otherwise

        This is useful before performing pop or peek operations
        to avoid errors.
        """
        return len(self.stack) == 0


# EXAMPLE USAGE AND TEST CASES
if __name__ == "__main__":
    # Create a new stack
    stack = Stack()

    print("Testing Stack Operations:")
    print(f"Is empty: {stack.isEmpty()}")  # True

    # Push elements
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.printStack()  # [10, 20, 30]

    # Peek at top
    print(f"Top element: {stack.peek()}")  # 30

    # Get size
    print(f"Stack size: {stack.size()}")  # 3

    # Pop elements
    print(f"Popped: {stack.pop()}")  # 30
    stack.printStack()  # [10, 20]

    print(f"Is empty: {stack.isEmpty()}")  # False
