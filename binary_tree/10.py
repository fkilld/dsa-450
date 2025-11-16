"""
PROBLEM: Top View of Binary Tree
==================================

Given a binary tree, return the top view of the tree.
The top view contains all nodes visible when the tree is viewed from the top.
Nodes are identified by their horizontal distance from the root.

Example 1:
    Input Tree:
               1  (hd=0)
             /   \
        (hd=-1) 2     3 (hd=1)
           /  \     \
      (hd=-2)4   5   6 (hd=2)
                     /
                (hd=1) 7

    Output: [4, 2, 1, 3, 6]
    Explanation:
        HD=-2: Node 4 (first at this distance)
        HD=-1: Node 2 (first at this distance)
        HD=0:  Node 1 (first at this distance)
        HD=1:  Node 3 (first at this distance, blocks 7)
        HD=2:  Node 6 (first at this distance)

Example 2:
    Input Tree:
           1
         /   \
        2     3

    Output: [2, 1, 3]

APPROACH & REASONING:
====================
This problem requires tracking horizontal distance (HD) from root.

WHAT IS HORIZONTAL DISTANCE?
- Root has HD = 0
- Going left decreases HD by 1 (HD - 1)
- Going right increases HD by 1 (HD + 1)
- Nodes with same HD are in same vertical line

WHY THIS APPROACH?
- Use BFS to process level by level (top to bottom)
- Track horizontal distance for each node
- For each HD, only record the FIRST node encountered (topmost)
- Map ensures we don't overwrite once a HD is recorded

KEY INSIGHT:
- BFS ensures we see nodes level by level (top to bottom)
- First node we see at any HD is the topmost node at that vertical line
- Use dictionary to check if HD is already mapped
- Track minimum HD to traverse result in order

ALTERNATIVE APPROACH (Not implemented here):
- Use recursion with level tracking
- But BFS is simpler for top-down view

ALGORITHM STEPS:
1. Handle edge case: if root is None, return empty list
2. Initialize:
   - Queue with [root, 0] (node with its HD)
   - Empty dictionary to map HD -> node value
   - min_hd to track leftmost HD
3. While queue is not empty:
   a. Dequeue [node, hd]
   b. If hd not in dictionary, add it (first occurrence = topmost)
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
    <Is hd in map?>----NO----> [Add hd->node.data to map]
           |                          |
          YES                         |
           |<------------------------
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
    - Building result is O(W) where W is width

SPACE COMPLEXITY: O(N)
    - Queue: O(W) where W is maximum width
    - Dictionary: O(W) for unique horizontal distances
    - Result: O(W)
    - Overall: O(N) in worst case

INTERVIEW TIPS:
- Explain horizontal distance concept clearly
- Mention why BFS (level-by-level ensures topmost)
- Highlight the key: Only record FIRST occurrence of each HD
- Compare with Bottom View (record LAST occurrence)
- Discuss tracking min_hd for ordered result construction
- Common follow-up: Vertical Order Traversal (all nodes at each HD)
"""

from collections import deque

class Solution:
    def topView(self, root):
        """
        Returns the top view of a binary tree (first node at each horizontal distance).

        Args:
            root: Root node of the binary tree

        Returns:
            List containing values of topmost nodes at each horizontal distance

        Time Complexity: O(N) - visit each node once
        Space Complexity: O(N) - queue + dictionary
        """
        # EDGE CASE: If tree is empty, return empty list
        if root is None:
            return []

        # STEP 1: Initialize dictionary to track first node at each horizontal distance
        # Key: horizontal distance, Value: node data
        # We only store the FIRST node we encounter at each HD (topmost)
        distance = {}

        # STEP 2: Initialize queue with [node, horizontal_distance]
        # Root starts at horizontal distance 0
        q = deque([[root, 0]])

        # STEP 3: Track minimum horizontal distance to build result in order
        # Initialize with infinity to find actual minimum
        mi = float('inf')

        # STEP 4: Process all nodes using BFS
        while len(q) != 0:
            # STEP 5: Dequeue node with its horizontal distance
            curr = q.popleft()
            node, hd = curr[0], curr[1]

            # STEP 6: If this horizontal distance not seen before, record it
            # This is crucial - we only record FIRST (topmost) node at each HD
            if hd not in distance:
                distance[hd] = node.data

                # STEP 7: Update minimum horizontal distance
                # We need this to know where to start building result
                mi = min(mi, hd)

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
        while mi in distance:
            ans.append(distance[mi])
            mi += 1

        # STEP 12: Return the complete top view
        return ans
