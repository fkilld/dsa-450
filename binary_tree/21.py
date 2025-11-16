"""
PROBLEM: Check if Binary Tree is a Sum Tree
=============================================

A Sum Tree is a binary tree where value of each node equals sum of all nodes
in its left and right subtrees. Leaf nodes are considered sum trees with sum 0.

Example 1 (Sum Tree):
    Input:
           26
         /    \
        10     3
       /  \     \
      4    6     3

    Output: True
    Explanation:
        - Leaf nodes: 4, 6, 3 are sum trees (sum = 0)
        - Node 10: 4 + 6 = 10 ✓
        - Node 3: 3 = 3 ✓ (right child only)
        - Node 26: 10 + 6 + 4 + 3 + 3 = 26 ✓

Example 2 (Not Sum Tree):
    Input:
          10
         /  \
        5    15

    Output: False (10 ≠ 5 + 15)

APPROACH & REASONING:
====================
Use postorder traversal to compute sums bottom-up and verify at each node.

WHY POSTORDER?
- Need to know subtree sums before checking current node
- Leaf nodes serve as base case
- Propagate sums upward

KEY INSIGHT:
- Return sum of entire subtree to parent
- Check condition at each internal node
- Use global flag to track validity

ALGORITHM STEPS:
1. If null → return 0
2. If leaf → return node value
3. Get left subtree sum recursively
4. Get right subtree sum recursively
5. Check: left_sum + right_sum == node.data
6. Return total (left + right + node)

FLOWCHART:
    [Null?] → YES → [Return 0]
         NO ↓
    [Leaf?] → YES → [Return value]
         NO ↓
    [Get left sum] → [Get right sum] → [Check sum] → [Return total]

TIME COMPLEXITY: O(N) - visit each node once
SPACE COMPLEXITY: O(H) - recursion depth

INTERVIEW TIPS:
- Emphasize leaf node base case
- Explain why we return full sum to parent
- Discuss global flag approach
- Mention early termination optimization
"""

class Solution:
    def sum_tree(self, root):
        """
        Checks if tree is sum tree and returns subtree sum.

        Args:
            root: Root of current subtree

        Returns:
            Sum of all nodes in this subtree

        Side Effects:
            Sets self.sum to False if not a sum tree
        """
        # BASE CASE: Null node contributes 0
        if root is None:
            return 0

        # BASE CASE: Leaf node - always valid sum tree
        # Leaf's "sum" is its own value (for parent's calculation)
        if root.left is None and root.right is None:
            return root.data

        # OPTIMIZATION: Early termination if already invalid
        if self.sum == False:
            return False

        # STEP 1: Get left subtree sum (postorder - left first)
        a = self.sum_tree(root.left)

        # STEP 2: Get right subtree sum (postorder - right second)
        b = self.sum_tree(root.right)

        # STEP 3: Check sum tree property for current node
        # node.data must equal sum of its children
        if a + b != root.data:
            self.sum = False  # Mark as invalid

        # STEP 4: Return total sum of this subtree to parent
        # Parent needs: left sum + right sum + current node
        return a + b + root.data

    def isSumTree(self, root):
        """
        Checks if entire tree is a sum tree.

        Args:
            root: Root of binary tree

        Returns:
            bool: True if sum tree, False otherwise

        Time: O(N), Space: O(H)
        """
        # Initialize global flag (assume valid)
        self.sum = True

        # Compute sums and check validity
        res = self.sum_tree(root)

        return self.sum
