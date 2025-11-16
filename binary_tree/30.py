"""
PROBLEM: Lowest Common Ancestor (LCA) in Binary Tree
======================================================

Given a binary tree and two nodes n1 and n2, find their Lowest Common Ancestor.
LCA is the lowest (deepest) node that has both n1 and n2 as descendants.

Example:
    Input:
            1
          /   \
         2     3
        / \   / \
       4   5 6   7

    Query: LCA(4, 5)
    Output: Node 2 (lowest node having both 4 and 5 as descendants)

    Query: LCA(4, 6)
    Output: Node 1 (root is the LCA)

APPROACH & REASONING:
====================
Use recursive search to find nodes and identify LCA during traversal.

WHY THIS APPROACH?
- If current node is n1 or n2, it could be LCA (if other is in its subtree)
- If n1 in left subtree and n2 in right subtree (or vice versa), current node is LCA
- Bottom-up propagation naturally finds LCA

KEY INSIGHT:
- Return non-null when we find n1 or n2
- If both left and right return non-null → current node is LCA
- If only one side returns non-null → propagate it up

ALGORITHM STEPS:
1. If root is null → return null
2. If root is n1 or n2 → return root (potential LCA)
3. Recursively search in left subtree
4. Recursively search in right subtree
5. If both left and right are non-null → root is LCA
6. Otherwise, return whichever is non-null

FLOWCHART:
    [Root == n1/n2?] → YES → [Return root]
          NO ↓
    [Search left] → [Search right] → [Both found?] → YES → [Return root]
                                           NO ↓
                                      [Return non-null side]

TIME COMPLEXITY: O(N) - may visit all nodes
SPACE COMPLEXITY: O(H) - recursion depth

INTERVIEW TIPS:
- Explain the three cases clearly
- Discuss why we return early when root matches
- Mention BST optimization (use values to guide search)
- Common follow-up: LCA with parent pointers
"""

class Solution:
    def lca(self, root, n1, n2):
        """
        Finds the Lowest Common Ancestor of n1 and n2.

        Args:
            root: Root of binary tree
            n1: First node value
            n2: Second node value

        Returns:
            Node: LCA of n1 and n2, or None if not found

        Time: O(N), Space: O(H)
        """
        # BASE CASE 1: Empty tree
        if root is None:
            return None

        # BASE CASE 2: Found one of the target nodes
        # This node is a potential LCA (if the other node is in its subtree)
        if root.data == n1 or root.data == n2:
            return root

        # STEP 1: Search for n1 and n2 in left subtree (postorder)
        left_node = self.lca(root.left, n1, n2)

        # STEP 2: Search for n1 and n2 in right subtree (postorder)
        right_node = self.lca(root.right, n1, n2)

        # STEP 3: Determine LCA based on search results
        # CASE 1: Both searches returned non-null
        # This means n1 is in one subtree and n2 is in the other
        # Therefore, current root is the LCA
        if left_node != None and right_node != None:
            return root

        # CASE 2: Only left subtree returned a node
        # Either both n1,n2 are in left subtree, or only one exists
        # Propagate the result upward
        if left_node:
            return left_node

        # CASE 3: Only right subtree returned a node
        # Either both n1,n2 are in right subtree, or only one exists
        # Propagate the result upward
        else:
            return right_node
