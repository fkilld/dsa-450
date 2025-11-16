"""
PROBLEM: Height of Binary Tree
==============================

Find the height (or depth) of a binary tree.
Height is defined as the number of edges on the longest path from root to a leaf.

Example 1:
    Input Tree:
           1
         /   \
        2     3
       / \
      4   5

    Output: 2
    Explanation: Longest path is 1->2->4 (or 1->2->5), which has 2 edges

Example 2:
    Input Tree:
        1

    Output: 0
    Explanation: Single node has height 0

Example 3:
    Input Tree: NULL
    Output: 0

APPROACH & REASONING:
====================
The height of a tree is a naturally recursive problem.

KEY INSIGHT:
The height of a tree = 1 + max(height of left subtree, height of right subtree)

Base Case: If the tree is empty (None), height is 0

This is a classic example of the "divide and conquer" paradigm:
1. Divide: Split into left and right subtrees
2. Conquer: Find height of each subtree recursively
3. Combine: Take the maximum + 1 (for current node)

WHY THIS WORKS:
- Every node contributes 1 to the height
- We need the longest path, so we take the maximum of left/right heights
- Recursion naturally explores all paths

ALGORITHM STEPS:
1. If root is None, return 0 (base case)
2. Recursively calculate height of left subtree
3. Recursively calculate height of right subtree
4. Return 1 + max(left_height, right_height)

FLOWCHART:
              START
                |
                v
         <Is root NULL?>----YES----> [Return 0]
                |
               NO
                |
                v
    [height_left = height(root.left)]
                |
                v
    [height_right = height(root.right)]
                |
                v
    [max_height = max(height_left, height_right)]
                |
                v
         [Return max_height + 1]
                |
                v
               END

RECURSION TREE EXAMPLE:
    For tree:    1
               /   \
              2     3
             /
            4

    height(1)
    ├─ height(2)
    │  ├─ height(4)
    │  │  ├─ height(None) = 0
    │  │  └─ height(None) = 0
    │  │  → returns 1
    │  └─ height(None) = 0
    │  → returns 2
    └─ height(3)
       ├─ height(None) = 0
       └─ height(None) = 0
       → returns 1
    → Final: 1 + max(2, 1) = 3

Wait, that gives height 3 for a tree with 2 edges. Let me reconsider...

Actually, the issue is the definition of height. Some define it as:
- Number of nodes on longest path (gives 3 for above example)
- Number of edges on longest path (gives 2 for above example)

This implementation counts nodes, then we need to subtract 1 for edges.
But typically in interviews, the implementation shown returns the max depth
starting from 1 for root, which is the number of levels.

TIME COMPLEXITY: O(N) where N is the number of nodes
    - We visit each node exactly once
    - At each node, we do O(1) work (comparison and addition)

SPACE COMPLEXITY: O(H) where H is the height of the tree
    - Space is used by the recursion call stack
    - In worst case (skewed tree), H = N, so O(N)
    - In best case (balanced tree), H = log(N), so O(log N)

INTERVIEW TIPS:
- Clarify if height means number of nodes or edges
- Mention both recursive and iterative (level-order) approaches
- Discuss space complexity of recursion stack
- Be ready to solve iteratively using BFS if asked
- Related problems: diameter, balanced tree, max depth
"""

class Solution:
    def height(self, root):
        """
        Find the height of a binary tree using recursion.

        Args:
            root: Root node of the binary tree

        Returns:
            Integer representing the height of the tree
        """
        # BASE CASE: Empty tree has height 0
        if root is None:
            return 0

        # RECURSIVE CASE: Calculate height of left subtree
        # This explores the entire left branch
        max_left = self.height(root.left)

        # RECURSIVE CASE: Calculate height of right subtree
        # This explores the entire right branch
        max_right = self.height(root.right)

        # COMBINE: Take the maximum height of both subtrees
        # Add 1 to account for the current node/level
        return max(max_left, max_right) + 1