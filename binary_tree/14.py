"""
PROBLEM: Diagonal Traversal of Binary Tree
===========================================

Given a binary tree, print all diagonal elements in the tree.
Diagonal traversal processes nodes along diagonals from top-left to bottom-right.

WHAT IS A DIAGONAL?
- All nodes that can be reached by going ONLY RIGHT form a diagonal
- To move to next diagonal, go LEFT once, then keep going RIGHT
- Think of drawing diagonal lines from top-left to bottom-right

Example 1:
    Input Tree:
               1
             /   \
            2     3
           / \     \
          4   5     6
                   /
                  7

    Diagonals:
        Diagonal 1 (from 1): 1 -> 3 -> 6
        Diagonal 2 (from 2): 2 -> 5 -> 7
        Diagonal 3 (from 4): 4

    Output: [1, 3, 6, 2, 5, 7, 4]

Example 2:
    Input Tree:
           1
         /   \
        2     3

    Output: [1, 3, 2]

APPROACH & REASONING:
====================
Think of diagonals as "right chains" starting from different nodes.

WHY THIS APPROACH?
- Use queue to track starting points of diagonals (left children)
- For each starting point, traverse entire right chain
- All nodes in a right chain belong to same diagonal
- Left children become starting points for next diagonals

KEY INSIGHT:
- Going RIGHT stays on same diagonal
- Going LEFT moves to next diagonal
- Queue holds entry points to different diagonals
- Process one diagonal completely before moving to next

ALGORITHM STEPS:
1. Initialize queue with root and empty result
2. While queue is not empty:
   a. Dequeue a node (diagonal starting point)
   b. Traverse entire right chain from this node:
      - Add node data to result
      - If left child exists, add to queue (new diagonal)
      - Move to right child (same diagonal)
   c. Repeat until right chain ends (temp becomes None)
3. Return result

FLOWCHART:
         START
           |
           v
    [Initialize queue with root]
           |
           v
    [Initialize empty result]
           |
           v
    <Is queue empty?>----YES----> [Return result]
           |
          NO
           |
           v
    [Dequeue starting node]
           |
           v
    [temp = starting node]
           |
           v
    <Is temp None?>----YES----> [Go back to queue check]
           |
          NO
           |
           v
    [Add temp.data to result]
           |
           v
    <Has left child?>----YES----> [Enqueue left (new diagonal)]
           |                             |
          NO                             |
           |<----------------------------
           v
    [temp = temp.right (same diagonal)]
           |
           v
    [Go back to temp None check]

TIME COMPLEXITY: O(N) where N is the number of nodes
    - Each node is visited exactly once
    - Each node is enqueued at most once

SPACE COMPLEXITY: O(N)
    - Queue can hold up to N nodes in worst case
    - For a left-skewed tree, all nodes go to queue
    - Result array holds N elements

INTERVIEW TIPS:
- Explain diagonal concept clearly (right chain = same diagonal)
- Emphasize: RIGHT keeps same diagonal, LEFT starts new diagonal
- Mention this is a modified BFS
- Draw a tree and show diagonals visually
- Compare with level-order (horizontal lines vs diagonal lines)
- Common follow-up: Print diagonals separately (group by diagonal)
"""

from collections import deque

def diagonal(root):
    """
    Performs diagonal traversal of a binary tree.

    Traverses nodes along diagonals from top-left to bottom-right.
    All nodes reachable by going only right are on same diagonal.

    Args:
        root: Root node of the binary tree

    Returns:
        List containing node values in diagonal order

    Time Complexity: O(N) - visit each node once
    Space Complexity: O(N) - queue can hold up to N nodes
    """
    # STEP 1: Initialize queue with root node
    # Queue will hold starting points of different diagonals
    # Initially, root is the starting point of first diagonal
    q = deque([root])

    # STEP 2: Initialize result list to store diagonal traversal
    ans = []

    # STEP 3: Process all diagonals
    while len(q) != 0:
        # STEP 4: Dequeue the starting node of current diagonal
        # This node is the leftmost node of current diagonal
        temp = q.popleft()

        # STEP 5: Traverse entire right chain (complete diagonal)
        # Keep going right until we reach the end
        while temp != None:
            # STEP 6: Add current node to result
            # This node is part of current diagonal
            ans.append(temp.data)

            # STEP 7: If left child exists, it's the start of a NEW diagonal
            # Add it to queue to process later
            # Left child is at next diagonal (down and to the left)
            if temp.left != None:
                q.append(temp.left)

            # STEP 8: Move to right child to continue on SAME diagonal
            # Right direction keeps us on same diagonal line
            # This is the key: right = same diagonal
            temp = temp.right

    # STEP 9: Return complete diagonal traversal
    return ans
