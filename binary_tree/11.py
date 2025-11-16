"""
PROBLEM: Bottom View of Binary Tree
=====================================

Given a binary tree, return the bottom view of the tree.
The bottom view contains all nodes visible when the tree is viewed from the bottom.
For each horizontal distance, we want the LAST (bottommost) node.

Example 1:
    Input Tree:
               1  (hd=0, level=0)
             /   \
            2     3 (hd=-1,+1, level=1)
           / \     \
          4   5     6 (hd=-2,-1,+2, level=2)
                   /
                  7 (hd=+1, level=3)

    Output: [4, 2, 5, 7, 6]
    Explanation:
        HD=-2: Node 4 (only node at this distance)
        HD=-1: Node 5 (replaces Node 2, as it's below)
        HD=0:  Node 1 (no nodes below it)
        HD=1:  Node 7 (replaces Node 3, as it's below)
        HD=2:  Node 6 (only node at this distance)

Example 2:
    Input Tree:
           1
         /   \
        2     3

    Output: [2, 1, 3]

APPROACH & REASONING:
====================
This is very similar to Top View, but we want the LAST node at each horizontal distance.

WHY THIS APPROACH?
- Use BFS to process level by level (top to bottom)
- Track horizontal distance for each node
- For each HD, KEEP UPDATING the node value (last update = bottommost)
- Unlike Top View where we check "if not in map", here we always update

KEY INSIGHT:
- Top View: Only record FIRST occurrence (don't update if HD exists)
- Bottom View: Always UPDATE (last update = bottommost node)
- BFS ensures we process top to bottom, so last update is bottom

DIFFERENCE FROM TOP VIEW:
Top View:
    if hd not in distance:
        distance[hd] = node.data

Bottom View:
    distance[hd] = node.data  # Always update!

ALGORITHM STEPS:
1. Handle edge case: if root is None, return empty list
2. Initialize:
   - Queue with [root, 0] (node with its HD)
   - Empty dictionary to map HD -> node value
   - min_hd to track leftmost HD
3. While queue is not empty:
   a. Dequeue [node, hd]
   b. ALWAYS update dictionary[hd] = node.data (overwrite previous)
   c. Update min_hd if current hd is smaller
   d. Enqueue left child with hd-1
   e. Enqueue right child with hd+1
4. Build result by traversing dictionary from min_hd onwards
5. Return result

FLOWCHART:
         START
           |
           v
    <Is root None?>----YES----> [Return []]
           |
          NO
           |
           v
    [Initialize queue with [root, 0]]
           |
           v
    [Initialize distance map & min_hd]
           |
           v
    <Is queue empty?>----YES----> [Build result from map]
           |                             |
          NO                             v
           |                          [END]
           v
    [Dequeue [node, hd]]
           |
           v
    [ALWAYS update map[hd] = node.data]
           |
           v
    [Update min_hd = min(min_hd, hd)]
           |
           v
    <Has left child?>----YES----> [Enqueue [left, hd-1]]
           |                             |
          NO                             |
           |<----------------------------
           v
    <Has right child?>----YES----> [Enqueue [right, hd+1]]
           |                              |
          NO                              |
           |<-----------------------------
           v
    [Go back to queue check]

TIME COMPLEXITY: O(N) where N is the number of nodes
    - Visit each node once during BFS
    - Dictionary operations are O(1) average

SPACE COMPLEXITY: O(N)
    - Queue: O(W) where W is maximum width
    - Dictionary: O(W) for unique horizontal distances
    - Overall: O(N) in worst case

INTERVIEW TIPS:
- Explain the key difference from Top View (always update vs. check first)
- Emphasize BFS ensures top-to-bottom processing
- Mention that last update at any HD is the bottommost node
- Compare: Top View (first) vs Bottom View (last)
- Discuss horizontal distance concept
- Common follow-up: Combine Top and Bottom view in one traversal
"""

from collections import deque, defaultdict

def bottomView(root):
    """
    Returns the bottom view of a binary tree (last node at each horizontal distance).

    Args:
        root: Root node of the binary tree

    Returns:
        List containing values of bottommost nodes at each horizontal distance

    Time Complexity: O(N) - visit each node once
    Space Complexity: O(N) - queue + dictionary
    """
    # EDGE CASE: If tree is empty, return empty list
    if root is None:
        return []

    # STEP 1: Initialize queue with [node, horizontal_distance]
    # Root starts at horizontal distance 0
    q = deque([[root, 0]])

    # STEP 2: Initialize dictionary to track LAST node at each horizontal distance
    # Using defaultdict(int) for convenience
    # Key: horizontal distance, Value: node data
    # Unlike Top View, we ALWAYS update - no "if not in" check
    mapping = defaultdict(int)

    # STEP 3: Track minimum horizontal distance for result construction
    mi = float('inf')

    # STEP 4: Process all nodes using BFS (top to bottom)
    while len(q) != 0:
        # STEP 5: Dequeue node with its horizontal distance
        node, hd = q.popleft()

        # STEP 6: ALWAYS update the mapping
        # This is the KEY difference from Top View
        # Since we process top to bottom, the last update will be the bottommost node
        # We OVERWRITE previous values at this HD
        mapping[hd] = node.data

        # STEP 7: Update minimum horizontal distance
        # We need this to know where to start building result
        if mi > hd:
            mi = hd

        # STEP 8: Enqueue left child with decreased horizontal distance
        # Left child is at hd - 1 (one position to the left)
        if node.left != None:
            q.append([node.left, hd - 1])

        # STEP 9: Enqueue right child with increased horizontal distance
        # Right child is at hd + 1 (one position to the right)
        if node.right != None:
            q.append([node.right, hd + 1])

    # STEP 10: Build result list by traversing from minimum HD onwards
    ans = []

    # STEP 11: Traverse dictionary from leftmost (min) to rightmost
    # Keep incrementing HD until we've covered all recorded distances
    while mi in mapping:
        ans.append(mapping[mi])
        mi += 1

    # STEP 12: Return the complete bottom view
    return ans
