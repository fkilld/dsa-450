"""
PROBLEM: Left View of Binary Tree
===================================

Given a binary tree, return the left view of the tree.
The left view contains all nodes that are visible when the tree is viewed from the left side.
In other words, the leftmost node at each level.

Example 1:
    Input Tree:
               1
             /   \
            2     3
           / \     \
          4   5     6
                   /
                  7

    Output: [1, 2, 4, 7]
    Explanation:
        Level 0: Node 1 (leftmost)
        Level 1: Node 2 (leftmost)
        Level 2: Node 4 (leftmost)
        Level 3: Node 7 (leftmost)

Example 2:
    Input Tree:
           1
         /   \
        2     3

    Output: [1, 2]

APPROACH & REASONING:
====================
This is a level-order traversal problem with a twist - we only need the first node at each level.

WHY LEVEL ORDER TRAVERSAL?
- We need to identify nodes level by level
- At each level, we want only the leftmost node
- Queue-based BFS naturally processes levels from left to right

KEY INSIGHT:
- Use BFS with level tracking
- For each level, record the size of queue (nodes at current level)
- Only add the FIRST node (i=0) from each level to result
- This ensures we get leftmost node at each level

ALTERNATIVE APPROACH (Not implemented here):
- DFS with level tracking: Visit left before right, track first node at each depth
- But BFS is more intuitive for this problem

ALGORITHM STEPS:
1. Handle edge case: if root is None, return empty list
2. Initialize queue with root node
3. Initialize result list
4. While queue is not empty:
   a. Get current level size n (number of nodes at this level)
   b. For each node in current level (iterate n times):
      - Dequeue node
      - If it's the first node (i==0), add to result
      - Enqueue left child if exists
      - Enqueue right child if exists
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
    [For i = 0 to n-1]
           |
           v
    [Dequeue node]
           |
           v
    <Is i == 0?>----YES----> [Add node to result]
           |                        |
          NO                        |
           |<----------------------
           v
    [Enqueue left child if exists]
           |
           v
    [Enqueue right child if exists]
           |
           v
    [Continue to next node in level]
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
- Explain this is a BFS problem with level tracking
- Emphasize the key: Track level size to identify first node
- Mention alternative: DFS with depth tracking (visit left first)
- Be ready to solve Right View (take last node instead of first)
- Common follow-up: Top View (requires horizontal distance tracking)
- Discuss why we need level size (to know when level ends)
"""

from collections import deque

def leftView(root):
    """
    Returns the left view of a binary tree (leftmost node at each level).

    Args:
        root: Root node of the binary tree

    Returns:
        List containing values of leftmost nodes at each level

    Time Complexity: O(N) - visit each node once
    Space Complexity: O(W) - queue holds at most W nodes (width)
    """
    # EDGE CASE: If tree is empty, return empty list
    if root is None:
        return []

    # STEP 1: Initialize queue for BFS traversal
    # Queue will process nodes level by level
    q = deque()
    q.append(root)

    # STEP 2: Initialize result list to store left view nodes
    ans = []

    # STEP 3: Process all levels of the tree
    while len(q) != 0:
        # STEP 4: Get the number of nodes at current level
        # This is crucial - it tells us when current level ends
        n = len(q)

        # STEP 5: Process all nodes at current level
        for i in range(n):
            # STEP 6: Dequeue the leftmost node at current level
            temp = q.popleft()

            # STEP 7: If this is the FIRST node of the level, add to result
            # i == 0 means this is the leftmost node at this level
            if i == 0:
                ans.append(temp.data)

            # STEP 8: Enqueue left child for next level processing
            # Left child is added first to maintain left-to-right order
            if temp.left != None:
                q.append(temp.left)

            # STEP 9: Enqueue right child for next level processing
            if temp.right != None:
                q.append(temp.right)

    # STEP 10: Return the complete left view
    return ans
