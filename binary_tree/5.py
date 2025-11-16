"""
PROBLEM: Inorder Traversal of Binary Tree
=========================================

Perform inorder traversal of a binary tree.
Inorder traversal visits nodes in the order: Left -> Root -> Right

This gives us the nodes in sorted order for a Binary Search Tree (BST).

Example:
    Input Tree:
           1
         /   \
        2     3
       / \
      4   5

    Output: [4, 2, 5, 1, 3]
    Explanation: Visit left subtree (4,2,5), then root (1), then right (3)

APPROACH & REASONING:
====================
Inorder traversal follows the pattern: LEFT -> ROOT -> RIGHT

TWO APPROACHES:
1. RECURSIVE: Natural and elegant, uses call stack
2. ITERATIVE: Uses explicit stack, no recursion

RECURSIVE APPROACH:
-------------------
Base case: If node is None, return
Recursive case:
  1. Visit left subtree
  2. Process current node
  3. Visit right subtree

ITERATIVE APPROACH:
------------------
The key insight: Simulate the recursion call stack manually
  1. Keep going left and push nodes to stack
  2. When we can't go left, pop from stack (this is the node to process)
  3. After processing, go right and repeat

WHY ITERATIVE IS TRICKY:
- We need to go as far left as possible before processing
- Stack stores the "path" from root to current leftmost node
- When we pop, we process that node, then explore its right subtree

ALGORITHM STEPS (Recursive):
1. If root is None, return
2. Recursively traverse left subtree
3. Process current node (print/store value)
4. Recursively traverse right subtree

ALGORITHM STEPS (Iterative):
1. Initialize empty stack and current = root
2. While stack is not empty OR current is not None:
   a. If current exists, push to stack and go left
   b. If current is None, pop from stack, process it, go right
3. Return result

FLOWCHART (Recursive):
         START
           |
           v
    <Is root NULL?>----YES----> [Return]
           |
          NO
           |
           v
    [Recursively traverse left]
           |
           v
    [Process current node]
           |
           v
    [Recursively traverse right]
           |
           v
          END

FLOWCHART (Iterative):
         START
           |
           v
    [Initialize stack, curr = root]
           |
           v
    <stack empty AND curr is NULL?>----YES----> [Return result]
           |
          NO
           |
           v
    <Is curr not NULL?>
         /        \
       YES         NO
        |           |
        v           v
   [Push curr   [Pop from stack
    to stack]    → curr]
        |           |
        v           v
   [curr =      [Add curr.data
    curr.left]   to result]
        |           |
        |           v
        |      [curr = curr.right]
        |           |
        └───────────┘
               |
        [Loop back to check]

EXAMPLE WALKTHROUGH (Iterative):
    Tree:    1
           /   \
          2     3
         /
        4

    Initial: stack=[], curr=1, result=[]

    Step 1: curr=1 exists, push 1, curr=1.left=2
            stack=[1], curr=2

    Step 2: curr=2 exists, push 2, curr=2.left=4
            stack=[1,2], curr=4

    Step 3: curr=4 exists, push 4, curr=4.left=None
            stack=[1,2,4], curr=None

    Step 4: curr=None, pop 4, process 4, curr=4.right=None
            stack=[1,2], curr=None, result=[4]

    Step 5: curr=None, pop 2, process 2, curr=2.right=None
            stack=[1], curr=None, result=[4,2]

    Step 6: curr=None, pop 1, process 1, curr=1.right=3
            stack=[], curr=3, result=[4,2,1]

    Step 7: curr=3 exists, push 3, curr=3.left=None
            stack=[3], curr=None

    Step 8: curr=None, pop 3, process 3, curr=3.right=None
            stack=[], curr=None, result=[4,2,1,3]

    Step 9: stack empty and curr=None, return [4,2,1,3]

TIME COMPLEXITY: O(N) where N is the number of nodes
    - Visit each node exactly once
    - Both recursive and iterative: O(N)

SPACE COMPLEXITY:
    - Recursive: O(H) for call stack, where H is height
    - Iterative: O(H) for explicit stack
    - Worst case (skewed tree): O(N)
    - Best case (balanced tree): O(log N)

INTERVIEW TIPS:
- Mention that inorder of BST gives sorted order
- Discuss difference between recursive and iterative
- Be ready to implement both approaches
- Related: Morris Traversal (O(1) space, no stack/recursion)
- Preorder: Root->Left->Right, Postorder: Left->Right->Root
"""

from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def inorder_recur(self, root):
        """
        Recursive inorder traversal: Left -> Root -> Right

        Args:
            root: Current node being processed
        """
        # BASE CASE: Reached beyond a leaf node
        if root is None:
            return

        # STEP 1: Visit entire left subtree first
        self.inorder_recur(root.left)

        # STEP 2: Process current node (print its data)
        # This happens after all left descendants are processed
        print(root.data, end=" ")

        # STEP 3: Visit entire right subtree
        self.inorder_recur(root.right)

    def inorder_itr(self, root):
        """
        Iterative inorder traversal using explicit stack.
        Simulates the recursion call stack manually.

        Args:
            root: Root node of the binary tree
        """
        # STEP 1: Initialize data structures
        stack = deque()  # Simulates recursion call stack
        curr = root      # Pointer to current node
        res = []         # Stores the inorder traversal result

        # STEP 2: Continue until we've processed all nodes
        # Loop runs while: we have nodes in stack OR we're exploring a path
        while stack or curr:
            # PHASE 1: Go as far left as possible
            if curr:
                # Push current node to stack (to process later)
                stack.append(curr)
                # Move to left child
                curr = curr.left

            # PHASE 2: Process node and explore right
            else:
                # Pop the topmost node (leftmost unprocessed node)
                curr = stack.pop()

                # Process the node (add to result)
                res.append(curr.data)

                # Now explore the right subtree
                # (if it exists, we'll go left again in next iteration)
                curr = curr.right

        # STEP 3: Print the final inorder traversal
        print(*res)

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
solution.inorder_recur(root)
print()
solution.inorder_itr(root)