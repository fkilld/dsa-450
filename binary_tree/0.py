"""
PROBLEM: Level Order Traversal of Binary Tree
============================================

Given a binary tree, find its level order traversal.
Level order traversal visits all nodes at each level from left to right,
starting from the root and moving down level by level.

Example:
    Input Tree:
           1
         /   \
        2     3
       / \
      4   5

    Output: [1, 2, 3, 4, 5]
    Explanation: Level 0: [1], Level 1: [2, 3], Level 2: [4, 5]

APPROACH & REASONING:
====================
This is a classic BFS (Breadth-First Search) problem. The key insight is to use
a queue (FIFO structure) to process nodes level by level.

WHY QUEUE?
- Queue ensures we process nodes in the order they were discovered
- When we visit a node, we add its children to the queue
- This naturally processes all nodes at level L before moving to level L+1

ALGORITHM STEPS:
1. Initialize a queue with the root node
2. While queue is not empty:
   a. Dequeue the front node
   b. Add its value to result
   c. Enqueue its left child (if exists)
   d. Enqueue its right child (if exists)
3. Return the result list

FLOWCHART:
         START
           |
           v
    [Initialize queue with root]
           |
           v
    [Initialize empty result list]
           |
           v
    <Is queue empty?>----YES----> [Return result]
           |
          NO
           |
           v
    [Dequeue front node]
           |
           v
    <Is node NULL?>----YES----> [Continue loop]
           |
          NO
           |
           v
    [Add node.data to result]
           |
           v
    [Enqueue left child if exists]
           |
           v
    [Enqueue right child if exists]
           |
           v
    [Go back to queue check]

TIME COMPLEXITY: O(N) where N is the number of nodes
    - We visit each node exactly once

SPACE COMPLEXITY: O(W) where W is the maximum width of the tree
    - In worst case (complete binary tree), the queue holds all nodes at the last level
    - For a complete binary tree, this is roughly N/2 nodes
    - So space is O(N) in worst case

INTERVIEW TIPS:
- Mention that this is BFS traversal
- Explain why queue is used (FIFO property)
- Discuss the difference from DFS (uses stack/recursion)
- Be ready to modify for level-by-level output (using level size)
"""

from collections import deque

class Solution:
    def levelOrder(self, root):
        """
        Performs level order traversal (BFS) on a binary tree.

        Args:
            root: Root node of the binary tree

        Returns:
            List of node values in level order
        """
        # STEP 1: Initialize queue with root
        # Using deque for O(1) append and popleft operations
        queue = deque()
        queue.append(root)

        # STEP 2: Initialize result list to store node values
        ans = []

        # STEP 3: Process all nodes level by level
        while len(queue) != 0:
            # STEP 4: Get the first node from queue (FIFO order)
            first = queue.popleft()

            # STEP 5: Process node only if it's not None
            if first != None:
                # STEP 6: Add children to queue for next level processing
                # Left child added first to maintain left-to-right order
                queue.append(first.left)
                queue.append(first.right)

                # STEP 7: Add current node's data to result
                ans.append(first.data)

        # STEP 8: Return the complete level order traversal
        return ans
            
        