"""
PROBLEM: Preorder Traversal of Binary Tree
===========================================

Given a binary tree, perform preorder traversal using both recursive and iterative approaches.
Preorder traversal visits nodes in the order: Root -> Left -> Right

Example 1:
    Input Tree:
               1
             /   \
            2     3
           /      / \
          4      5   6
                / \
               7   8

    Output: 1 2 4 3 5 7 8 6
    Explanation: Visit root (1), then left subtree (2, 4), then right subtree (3, 5, 7, 8, 6)

Example 2:
    Input Tree:
           1
         /   \
        2     3

    Output: 1 2 3

APPROACH & REASONING:
====================
Preorder is one of the three fundamental DFS (Depth-First Search) traversals.

WHY TWO APPROACHES?
1. RECURSIVE: Simple and intuitive, mirrors the definition directly
   - Uses implicit call stack
   - Cleaner code but may cause stack overflow for very deep trees

2. ITERATIVE: More control, better for large trees
   - Uses explicit stack data structure
   - No stack overflow risk, better space control
   - Mimics the recursive call stack behavior

KEY INSIGHT FOR ITERATIVE:
- Stack is LIFO (Last In First Out)
- To visit left before right, we push RIGHT child first, then LEFT child
- This ensures LEFT child is on top and gets processed next

ALGORITHM STEPS (RECURSIVE):
1. If root is None, return
2. Print/process root data
3. Recursively traverse left subtree
4. Recursively traverse right subtree

ALGORITHM STEPS (ITERATIVE):
1. Initialize empty stack and result list
2. Push root to stack
3. While stack is not empty:
   a. Pop node from stack
   b. Add node data to result
   c. Push right child (if exists) - goes to stack first
   d. Push left child (if exists) - goes to stack second, so processed first
4. Return result

FLOWCHART (ITERATIVE):
         START
           |
           v
    [Initialize stack with root]
           |
           v
    [Initialize empty result]
           |
           v
    <Is stack empty?>----YES----> [Return result]
           |
          NO
           |
           v
    [Pop node from stack]
           |
           v
    [Add node.data to result]
           |
           v
    <Has right child?>----YES----> [Push right to stack]
           |                              |
          NO                              |
           |<-----------------------------
           v
    <Has left child?>----YES----> [Push left to stack]
           |                             |
          NO                             |
           |<----------------------------
           v
    [Go back to stack check]

TIME COMPLEXITY: O(N) where N is the number of nodes
    - Both approaches visit each node exactly once

SPACE COMPLEXITY:
    - Recursive: O(H) where H is height (call stack space)
    - Iterative: O(H) where H is height (explicit stack space)
    - In worst case (skewed tree): O(N)
    - In best case (balanced tree): O(log N)

INTERVIEW TIPS:
- Explain the order: Root -> Left -> Right (RLR pattern)
- Mention this is a DFS traversal
- Discuss trade-offs: Recursive (simple) vs Iterative (control)
- Highlight why we push right before left in iterative approach
- Be ready to compare with Inorder (LRt) and Postorder (LRt)
- Common follow-up: Implement without recursion or without stack
"""

from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        """
        Node structure for binary tree.

        Args:
            data: Value stored in the node
            left: Pointer to left child
            right: Pointer to right child
        """
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def preorder_recur(self, root):
        """
        Recursive preorder traversal (Root -> Left -> Right).

        Args:
            root: Root node of the binary tree

        Time Complexity: O(N) - visit each node once
        Space Complexity: O(H) - recursion call stack, H is height
        """
        # BASE CASE: If node is None, return immediately
        if root is None:
            return

        # STEP 1: Process root node first (Root in Root-Left-Right)
        print(root.data, end=" ")

        # STEP 2: Recursively traverse left subtree
        self.preorder_recur(root.left)

        # STEP 3: Recursively traverse right subtree
        self.preorder_recur(root.right)

    def preorder_itr(self, root):
        """
        Iterative preorder traversal using explicit stack.

        Args:
            root: Root node of the binary tree

        Time Complexity: O(N) - visit each node once
        Space Complexity: O(H) - stack space, H is height
        """
        # STEP 1: Initialize stack for iterative traversal
        # Using deque for O(1) append and pop operations
        stack = deque()
        ans = []

        # STEP 2: Start with root node on stack
        stack.append(root)

        # STEP 3: Process nodes while stack is not empty
        while stack:
            # STEP 4: Pop the top node from stack (LIFO order)
            curr = stack.pop()

            # STEP 5: Add current node's data to result
            ans.append(curr.data)

            # STEP 6: Push children to stack
            # CRITICAL: Push RIGHT child first, then LEFT child
            # This ensures LEFT child is on top and processed next
            # Remember: Stack is LIFO, so last in (left) comes out first
            if curr.right != None:
                stack.append(curr.right)  # Right pushed first
            if curr.left != None:
                stack.append(curr.left)   # Left pushed second (top of stack)

        # STEP 7: Print the complete traversal
        print(*ans)

# Driver code
""" Construct the following tree
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
"""

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

solution = Solution()
# Output: 1 2 4 3 5 7 8 6
solution.preorder_recur(root)
print()
solution.preorder_itr(root)
