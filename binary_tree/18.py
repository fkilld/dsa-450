"""
PROBLEM: Transform Binary Tree to Sum Tree
===========================================

Given a binary tree, transform it to a Sum Tree where:
- Each node's value = sum of all nodes in its left + right subtrees
- Leaf nodes become 0

Example:
    Input:           Output:
         10             20
        /  \           /  \
       -2   6        -2    6
      / \  / \      / \   / \
     8 -4  7  5    0   0 0   0

    Explanation:
    - Leaf nodes: 8,-4,7,5 → all become 0
    - Node -2: left(8) + right(-4) = 4, but becomes -2
    - Node 6: left(7) + right(5) = 12, but becomes 6
    - Root 10: left + right = 20

APPROACH & REASONING:
====================
Use postorder traversal (left-right-root) to:
1. Get sum from left subtree
2. Get sum from right subtree
3. Update current node
4. Return (old value + new value) to parent

WHY POSTORDER?
- Need subtree sums before processing parent
- Bottom-up approach
- Natural recursive structure

KEY INSIGHT:
- Store old value before updating
- New value = left sum + right sum
- Return old + new to parent (total contribution)

ALGORITHM STEPS:
1. If null → return 0
2. Recursively get left sum
3. Recursively get right sum
4. Store old value
5. Update node = left + right sum
6. Return old + new value

FLOWCHART:
    [Leaf?] → YES → [Return value]
         NO ↓
    [Get left sum] → [Get right sum] → [Update node] → [Return old+new]

TIME COMPLEXITY: O(N) - visit each node once
SPACE COMPLEXITY: O(H) - recursion stack height

INTERVIEW TIPS:
- Explain postorder necessity
- Discuss return value (old + new)
- Mention in-place transformation
"""

class Solution:
    def toSumTree(self, root):
        """
        Transforms tree to sum tree where each node = sum of its subtrees.

        Args:
            root: Root of binary tree

        Returns:
            Sum of all nodes in this subtree

        Time: O(N), Space: O(H)
        """
        # BASE CASE: Empty node contributes 0
        if root is None:
            return 0

        # STEP 1: Store original value (needed for return)
        old_val = root.data

        # STEP 2: Get sum of left subtree (postorder - left first)
        lst = self.toSumTree(root.left)

        # STEP 3: Get sum of right subtree (postorder - right second)
        rst = self.toSumTree(root.right)

        # STEP 4: Update current node to sum of subtrees
        root.data = lst + rst

        # STEP 5: Return total contribution to parent
        # Parent needs: original value + new value (sum of subtrees)
        return old_val + root.data
