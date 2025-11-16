"""
PROBLEM: Postorder Traversal of Binary Tree
============================================

Given a binary tree, perform postorder traversal using both recursive and iterative approaches.
Postorder traversal visits nodes in the order: Left -> Right -> Root

Example 1:
    Input Tree:
               1
             /   \
            2     3
           /      / \
          4      5   6
                / \
               7   8

    Output: 4 2 7 8 5 6 3 1
    Explanation: Visit left subtree (4, 2), right subtree (7, 8, 5, 6, 3), then root (1)

Example 2:
    Input Tree:
           1
         /   \
        2     3

    Output: 2 3 1

APPROACH & REASONING:
====================
Postorder is one of the three fundamental DFS (Depth-First Search) traversals.
It's particularly useful for deletion operations (delete children before parent).

WHY TWO APPROACHES?
1. RECURSIVE: Simple and mirrors the definition
   - Uses implicit call stack
   - Natural way to express postorder logic

2. ITERATIVE: Uses a clever trick with reverse logic
   - Uses explicit stack and result deque
   - Process in reverse postorder, then reverse result
   - Avoids complex state management

KEY INSIGHT FOR ITERATIVE:
- Postorder: Left -> Right -> Root
- If we process Root -> Right -> Left and reverse, we get Left -> Right -> Root
- This is similar to preorder but with reversed child order
- Use deque to append results and pop in reverse order

ALGORITHM STEPS (RECURSIVE):
1. If root is None, return
2. Recursively traverse left subtree
3. Recursively traverse right subtree
4. Print/process root data

ALGORITHM STEPS (ITERATIVE):
1. Initialize stack and result deque
2. Push root to stack
3. While stack is not empty:
   a. Pop node from stack
   b. Append node data to result deque
   c. Push left child (if exists)
   d. Push right child (if exists)
4. Pop from result deque in reverse order to get postorder

FLOWCHART (ITERATIVE):
         START
           |
           v
    [Initialize stack with root]
           |
           v
    [Initialize result deque]
           |
           v
    <Is stack empty?>----YES----> [Print result in reverse]
           |                             |
          NO                             v
           |                          [END]
           v
    [Pop node from stack]
           |
           v
    [Append node.data to result]
           |
           v
    <Has left child?>----YES----> [Push left to stack]
           |                             |
          NO                             |
           |<----------------------------
           v
    <Has right child?>----YES----> [Push right to stack]
           |                              |
          NO                              |
           |<-----------------------------
           v
    [Go back to stack check]

TIME COMPLEXITY: O(N) where N is the number of nodes
    - Both approaches visit each node exactly once

SPACE COMPLEXITY:
    - Recursive: O(H) where H is height (call stack)
    - Iterative: O(N) for result deque + O(H) for stack
    - In worst case: O(N)
    - In best case: O(log N)

INTERVIEW TIPS:
- Explain the order: Left -> Right -> Root (LRN pattern)
- Mention use case: Useful for tree deletion (delete children first)
- Discuss the clever trick: Reverse of (Root->Right->Left) gives postorder
- Compare with Preorder (RLR) and Inorder (LRN)
- Highlight that recursive is simpler but iterative gives more control
- Common follow-up: Implement using single stack without deque
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
    def postorder_recur(self, root):
        """
        Recursive postorder traversal (Left -> Right -> Root).

        Args:
            root: Root node of the binary tree

        Time Complexity: O(N) - visit each node once
        Space Complexity: O(H) - recursion call stack, H is height
        """
        # BASE CASE: If node is None, return immediately
        if root is None:
            return

        # STEP 1: Recursively traverse left subtree first
        self.postorder_recur(root.left)

        # STEP 2: Recursively traverse right subtree
        self.postorder_recur(root.right)

        # STEP 3: Process root node last (Root in Left-Right-Root)
        print(root.data, end=" ")

    def postorder_itr(self, root):
        """
        Iterative postorder traversal using stack and deque.

        Uses clever trick: Process Root->Right->Left and reverse to get Left->Right->Root

        Args:
            root: Root node of the binary tree

        Time Complexity: O(N) - visit each node once
        Space Complexity: O(N) - result deque + O(H) stack space
        """
        # STEP 1: Initialize stack for traversal
        stack = deque()
        stack.append(root)

        # STEP 2: Initialize result deque to store nodes
        # We'll append to this and then pop in reverse order
        ans = deque()

        # STEP 3: Process nodes in Root->Right->Left order
        while stack:
            # STEP 4: Pop node from stack
            curr = stack.pop()

            # STEP 5: Append to result deque
            # This builds the reverse of postorder
            ans.append(curr.data)

            # STEP 6: Push LEFT child first (so RIGHT is processed first)
            # This is opposite of preorder to achieve reverse effect
            if curr.left != None:
                stack.append(curr.left)
            if curr.right != None:
                stack.append(curr.right)

        # STEP 7: Pop from deque in reverse order to get postorder
        # Deque gives us LIFO when we pop from right end
        while ans:
            print(ans.pop(), end=" ")

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
# Output: 4 2 7 8 5 6 3 1
solution.postorder_recur(root)
print()
solution.postorder_itr(root)
