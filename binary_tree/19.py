"""
PROBLEM: Construct Tree from Inorder and Preorder Traversal
=============================================================

Given inorder and preorder traversals, construct the unique binary tree.

Example:
    Inorder:  [9, 3, 15, 20, 7]
    Preorder: [3, 9, 20, 15, 7]

    Tree:
           3
         /   \
        9     20
             /  \
            15   7

APPROACH & REASONING:
====================
KEY INSIGHTS:
- Preorder: First element is always root
- Inorder: Elements left of root are in left subtree, right of root in right subtree

ALGORITHM:
1. First preorder element = root
2. Find root in inorder → splits into left/right subtrees
3. Recursively build left subtree
4. Recursively build right subtree

WHY THIS WORKS?
- Preorder gives us root ordering
- Inorder gives us left/right boundaries
- Combination uniquely determines tree

OPTIMIZATION:
- Use hashmap to find root in inorder in O(1)

FLOWCHART:
    [Take preorder[i]] → [Find in inorder] → [Split] → [Recurse left & right]

TIME COMPLEXITY: O(N) - process each node once
SPACE COMPLEXITY: O(N) - hashmap + recursion

INTERVIEW TIPS:
- Draw example showing how algorithm works
- Explain why we need both traversals
- Mention hashmap optimization
- Discuss other combinations (inorder+postorder works, but preorder+postorder doesn't)
"""

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def create_tree(self, inorder, preorder, in_start, in_end):
        """
        Recursively builds tree from inorder and preorder traversals.

        Args:
            inorder: Inorder traversal array
            preorder: Preorder traversal array
            in_start: Start index in inorder for current subtree
            in_end: End index in inorder for current subtree

        Returns:
            Root node of constructed subtree
        """
        # BASE CASE: No elements in current subtree
        if in_start > in_end:
            return None

        # STEP 1: Get current root from preorder
        # Preorder is processed left-to-right sequentially
        curr = preorder[self.preIdx]
        self.preIdx += 1  # Move to next element for next call

        # STEP 2: Create node for current root
        temp = Node(curr)

        # BASE CASE: Leaf node (no children to process)
        if in_start == in_end:
            return temp

        # STEP 3: Find root position in inorder using hashmap (O(1))
        # Elements before this index → left subtree
        # Elements after this index → right subtree
        inIdx = self.mp[curr]

        # STEP 4: Recursively build left subtree
        # Range: in_start to inIdx-1 in inorder
        temp.left = self.create_tree(inorder, preorder, in_start, inIdx - 1)

        # STEP 5: Recursively build right subtree
        # Range: inIdx+1 to in_end in inorder
        temp.right = self.create_tree(inorder, preorder, inIdx + 1, in_end)

        return temp

    def buildtree(self, inorder, preorder, n):
        """
        Main function to build tree from traversals.

        Args:
            inorder: Inorder traversal
            preorder: Preorder traversal
            n: Number of nodes

        Returns:
            Root of constructed tree
        """
        # STEP 1: Create hashmap for O(1) lookup of elements in inorder
        self.mp = {}
        for i in range(len(inorder)):
            self.mp[inorder[i]] = i

        # STEP 2: Initialize preorder index
        self.preIdx = 0

        # STEP 3: Build tree recursively
        return self.create_tree(inorder, preorder, 0, len(inorder) - 1)
