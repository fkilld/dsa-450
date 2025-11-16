"""
PROBLEM: Check for Duplicate Subtree in Binary Tree
=====================================================

Given a binary tree, check if it contains duplicate subtrees of size 2 or more.
Two subtrees are duplicates if they have the same structure and node values.

Example 1 (Has Duplicates):
    Input:
           1
         /   \
        2     3
       /     / \
      4     2   4
           /
          4

    Output: 1 (True)
    Subtree rooted at 2 appears twice

Example 2 (No Duplicates):
    Input:
           1
         /   \
        2     3

    Output: 0 (False)

APPROACH & REASONING:
====================
Serialize each subtree into a unique string, use hashmap to detect duplicates.

WHY STRING SERIALIZATION?
- Each unique subtree structure has unique string representation
- HashMap can track occurrences efficiently
- Easy to compare subtrees

KEY INSIGHT:
- Serialize subtree: "root_value + left_string + right_string"
- Use marker "$" for null nodes
- If serialization appears twice, found duplicate

ALGORITHM STEPS:
1. Serialize each subtree recursively
2. Store serialization in hashmap with count
3. If any serialization count > 1, duplicate exists
4. Leaf nodes get their value as serialization

FLOWCHART:
    [Serialize subtree] → [Add to map] → [Count > 1?] → YES → [Duplicate found]

TIME COMPLEXITY: O(N) - visit each node once
SPACE COMPLEXITY: O(N) - hashmap + strings

INTERVIEW TIPS:
- Explain serialization format
- Discuss why we need markers for null
- Mention size constraint (≥ 2 nodes)
- Compare with other approaches (tree hashing)
"""

from collections import defaultdict

class Solution:
    def solve(self, root):
        """
        Serializes subtree and tracks occurrences.

        Args:
            root: Root of current subtree

        Returns:
            String serialization of this subtree

        Side Effects:
            Updates self.map with serialization frequencies
        """
        # BASE CASE: Null node represented by marker
        if root is None:
            return "$"

        # Initialize string for this subtree
        s = ""

        # BASE CASE: Leaf node - just its value
        if root.left is None and root.right is None:
            s += str(root.data)
            return s

        # STEP 1: Add current node's value
        s += str(root.data)

        # STEP 2: Recursively serialize left subtree (postorder)
        s += self.solve(root.left)

        # STEP 3: Recursively serialize right subtree (postorder)
        s += self.solve(root.right)

        # STEP 4: Track frequency of this serialization
        self.map[s] += 1

        # STEP 5: Return serialization to parent
        return s

    def dupSub(self, root):
        """
        Checks if tree contains duplicate subtrees.

        Args:
            root: Root of binary tree

        Returns:
            int: 1 if duplicates exist, 0 otherwise

        Time: O(N), Space: O(N)
        """
        # Initialize frequency map
        self.map = defaultdict(int)

        # Serialize all subtrees
        self.solve(root)

        # Check if any subtree appears more than once
        for string in self.map:
            if self.map[string] > 1:
                return 1

        return 0
