"""
PROBLEM: Find All Duplicate Subtrees
======================================

Given a binary tree, find all duplicate subtrees and return their roots.
Two subtrees are duplicates if they have identical structure and node values.

Example:
    Input:
            1
          /   \
         2     3
        /     / \
       4     2   4
            /
           4

    Output: [Node(2), Node(4)]
    Explanation:
        - Subtree at leftmost 2: (2 -> 4)
        - Subtree at middle 2: (2 -> 4) [DUPLICATE]
        - Subtree at leftmost 4: (4)
        - Subtree at middle 4: (4) [DUPLICATE]
        - Subtree at rightmost 4: (4) [DUPLICATE of duplicates]

    Only return first duplicate found for each unique subtree

APPROACH & REASONING:
====================
Serialize each subtree and use hashmap to track occurrences.

WHY SERIALIZATION?
- Convert tree structure to unique string
- Easy to compare using hashmap
- Can detect duplicates by counting occurrences

KEY INSIGHT:
- Serialize using postorder: (left)value(right)
- Use parentheses to capture structure
- When serialization seen exactly twice, add to result
- Only add once (when count becomes 2)

ALGORITHM STEPS:
1. Serialize each subtree recursively (postorder)
2. Store serializations in hashmap with counts
3. When count reaches 2 (first duplicate), add root to result
4. Don't add on subsequent occurrences (already in result)

FLOWCHART:
    [Serialize subtree] → [Check in map] → [Count==1?] → YES → [Add to result]
                                                NO ↓
                                          [Return serialization]

TIME COMPLEXITY: O(N) - visit each node once
SPACE COMPLEXITY: O(N) - hashmap + strings

INTERVIEW TIPS:
- Explain serialization format
- Discuss why we check count == 1 (add only first duplicate)
- Mention alternative: tree hashing
- Compare with checking if duplicate exists (simpler problem)
"""

from collections import defaultdict

class Solution:
    def inorder(self, root):
        """
        Serializes subtree and detects duplicates.

        Args:
            root: Root of current subtree

        Returns:
            str: Serialization of this subtree

        Side Effects:
            Updates self.map with serialization counts
            Adds duplicate roots to self.res

        Time: O(N), Space: O(N)
        """
        # BASE CASE: Null node
        if root is None:
            return ""

        # STEP 1: Create unique serialization for this subtree
        # Format: (left_serialization)value(right_serialization)
        # Parentheses ensure structure is captured
        s = "("
        s += self.inorder(root.left)  # Postorder: left first
        s += str(root.data)            # Then root
        s += self.inorder(root.right)  # Then right
        s += ")"

        # STEP 2: Check if this subtree appeared before
        # If count is exactly 1, this is the FIRST duplicate
        # Add to result (but not for subsequent duplicates)
        if s in self.map and self.map[s] == 1:
            self.res.append(root)

        # STEP 3: Increment occurrence count
        self.map[s] += 1

        # STEP 4: Return serialization to parent
        return s

    def printAllDups(self, root):
        """
        Finds all duplicate subtrees in binary tree.

        Args:
            root: Root of binary tree

        Returns:
            list: List of root nodes of duplicate subtrees

        Time: O(N), Space: O(N)
        """
        # Initialize hashmap to track serialization counts
        self.map = defaultdict(int)

        # Initialize result list
        self.res = []

        # Serialize all subtrees and collect duplicates
        self.inorder(root)

        return self.res
