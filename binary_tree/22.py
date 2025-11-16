"""
PROBLEM: Check if All Leaf Nodes are at Same Level
====================================================

Given a binary tree, check if all leaf nodes are at the same depth.

Example 1 (True):
    Input:
           1
         /   \
        2     3
       / \
      4   5

    Output: True
    All leaves (4, 5, 3) are at level 2

Example 2 (False):
    Input:
           1
         /   \
        2     3
       /
      4

    Output: False
    Leaves at different levels: 4 at level 2, 3 at level 1

APPROACH & REASONING:
====================
Track the depth of the first leaf found, then verify all other leaves
are at the same depth.

WHY THIS WORKS?
- First leaf we find sets the "expected" level
- All subsequent leaves must match this level
- If any leaf differs, return False

KEY INSIGHT:
- Use level parameter in recursion
- Store first leaf's level globally
- Compare all subsequent leaves to it

ALGORITHM STEPS:
1. Traverse tree with level tracking
2. When first leaf found, store its level
3. For each subsequent leaf:
   - Check if level matches stored level
   - If not, return False
4. Return True if all leaves match

FLOWCHART:
    [Traverse with level] → [Leaf?] → YES → [First?] → YES → [Store level]
                                                 NO ↓
                                           [Compare with stored level]

TIME COMPLEXITY: O(N) - visit all nodes in worst case
SPACE COMPLEXITY: O(H) - recursion depth

INTERVIEW TIPS:
- Explain why we need the first leaf's level
- Discuss early termination on mismatch
- Mention both DFS and BFS approaches
"""

class Solution:
    def leaf_nodes(self, root, level):
        """
        Recursively checks if all leaves are at same level.

        Args:
            root: Current node
            level: Depth of current node

        Returns:
            bool: True if all leaves at same level from this subtree

        Time: O(N), Space: O(H)
        """
        # BASE CASE: Null node is trivially valid
        if root is None:
            return True

        # BASE CASE: Found a leaf node
        if root.left is None and root.right is None:
            # If this is the first leaf we've encountered
            if self.level == 0:
                self.level = level  # Store this level as reference
                return True  # First leaf is always valid

            # Subsequent leaves: check if at same level as first leaf
            return level == self.level

        # RECURSIVE CASE: Internal node
        # Both subtrees must have leaves at same level
        # AND operator ensures both sides are valid
        return self.leaf_nodes(root.left, level + 1) and \
               self.leaf_nodes(root.right, level + 1)

    def check(self, root):
        """
        Main function to check if all leaves are at same level.

        Args:
            root: Root of binary tree

        Returns:
            bool: True if all leaves at same level

        Time: O(N), Space: O(H)
        """
        # Initialize level tracker (0 means not set yet)
        self.level = 0

        # Check all leaves starting from level 0
        ans = self.leaf_nodes(root, 0)

        return ans
