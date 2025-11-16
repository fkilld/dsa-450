"""
PROBLEM: Right View of Binary Tree
====================================

Given a binary tree, return the right view of the tree.
The right view contains all nodes that are visible when the tree is viewed from the right side.
In other words, the rightmost node at each level.

Example 1:
    Input Tree:
               1
             /   \
            2     3
           / \     \
          4   5     6
                   /
                  7

    Output: [1, 3, 6, 7]
    Explanation:
        Level 0: Node 1 (rightmost)
        Level 1: Node 3 (rightmost)
        Level 2: Node 6 (rightmost)
        Level 3: Node 7 (rightmost)

Example 2:
    Input Tree:
           1
         /   \
        2     3

    Output: [1, 3]

APPROACH & REASONING:
====================
This is a level-order traversal problem where we need the last (rightmost) node at each level.

WHY THIS APPROACH?
- We process nodes level by level using BFS
- At each level, we keep updating temp with each node
- After processing all nodes in a level, temp holds the last (rightmost) node
- We add this rightmost node to our result

KEY INSIGHT:
- Similar to Left View, but we want the LAST node instead of FIRST
- Don't need to check index - just keep updating temp
- After inner loop completes, temp will hold the rightmost node
- This is simpler than tracking indices

ALTERNATIVE APPROACH (Not implemented here):
- Track index and add node when i == n-1
- DFS with level tracking (visit right before left)

ALGORITHM STEPS:
1. Handle edge case: if root is None, return empty list
2. Initialize queue with root node
3. Initialize result list
4. While queue is not empty:
   a. Get current level size n
   b. Initialize temp as None
   c. For each node in current level:
      - Dequeue node and store in temp
      - Enqueue left child if exists
      - Enqueue right child if exists
   d. After loop, temp holds rightmost node - add to result
5. Return result list

FLOWCHART:
         START
           |
           v
    <Is root None?>----YES----> [Return []]
           |
          NO
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
    [n = size of queue (level size)]
           |
           v
    [temp = None]
           |
           v
    [For each node in level]
           |
           v
    [Dequeue node into temp]
           |
           v
    [Enqueue left child if exists]
           |
           v
    [Enqueue right child if exists]
           |
           v
    <All nodes processed?>----NO----> [Continue loop]
           |
          YES
           |
           v
    [Add temp.data to result]
           |
           v
    [Go back to queue check]

TIME COMPLEXITY: O(N) where N is the number of nodes
    - We visit each node exactly once during BFS
    - Each node is enqueued and dequeued once

SPACE COMPLEXITY: O(W) where W is the maximum width of tree
    - Queue holds at most all nodes at the widest level
    - For complete binary tree, width at last level is N/2
    - Result array holds at most H nodes (height)
    - Overall: O(W) ≈ O(N) in worst case

INTERVIEW TIPS:
- Explain this is mirror of Left View problem
- Emphasize the technique: Keep updating temp, last value is rightmost
- Compare with Left View: First node vs Last node
- Mention this is simpler than tracking indices
- Common follow-up: Solve both Left and Right view in one traversal
- Discuss optimization: No need to check index, just keep last node
"""

from collections import deque

def rightView(root):
    """
    Returns the right view of a binary tree (rightmost node at each level).

    Args:
        root: Root node of the binary tree

    Returns:
        List containing values of rightmost nodes at each level

    Time Complexity: O(N) - visit each node once
    Space Complexity: O(W) - queue holds at most W nodes (width)
    """
    # EDGE CASE: If tree is empty, return empty list
    if root is None:
        return []

    # STEP 1: Initialize queue for BFS traversal with root
    # Using list notation for initialization
    q = deque([root])

    # STEP 2: Initialize result list to store right view nodes
    ans = []

    # STEP 3: Process all levels of the tree
    while len(q) != 0:
        # STEP 4: Get the number of nodes at current level
        # This tells us how many nodes to process before moving to next level
        n = len(q)

        # STEP 5: Initialize temp to hold nodes from current level
        # After processing all nodes in level, this will hold the rightmost node
        temp = None

        # STEP 6: Process all nodes at current level
        for _ in range(n):
            # STEP 7: Dequeue node and store in temp
            # Each iteration overwrites temp, so at end it holds the LAST (rightmost) node
            temp = q.popleft()

            # STEP 8: Enqueue left child for next level processing
            # Using Pythonic check (truthy/falsy)
            if temp.left:
                q.append(temp.left)

            # STEP 9: Enqueue right child for next level processing
            if temp.right:
                q.append(temp.right)

        # STEP 10: After processing all nodes in level, temp holds rightmost node
        # Add it to result
        ans.append(temp.data)

    # STEP 11: Return the complete right view
    return ans
