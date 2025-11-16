"""
PROBLEM: Mirror (Invert) a Binary Tree
======================================

Convert a binary tree into its mirror image by swapping left and right
children of all nodes.

Example 1:
    Input Tree:          Output Tree:
         1                    1
       /   \                /   \
      2     3              3     2
     / \   / \            / \   / \
    4   5 6   7          7   6 5   4

Example 2:
    Input Tree:          Output Tree:
         1                    1
       /   \                /   \
      2     3              3     2
     /                          \
    4                            4

Example 3:
    Input Tree: NULL
    Output Tree: NULL

APPROACH & REASONING:
====================
This is a classic tree manipulation problem that demonstrates post-order
traversal logic.

KEY INSIGHT:
To mirror a tree, we need to swap left and right children of every node.
We must do this recursively for all nodes.

WHY POST-ORDER TRAVERSAL?
We first mirror the left and right subtrees, then swap them.
This ensures that when we swap, both subtrees are already mirrored.

However, PRE-ORDER also works! We can swap first, then recursively
mirror the children. Both approaches are valid.

ALGORITHM STEPS:
1. Base case: If root is None, return (nothing to mirror)
2. Recursively mirror the left subtree
3. Recursively mirror the right subtree
4. Swap left and right children of current node

FLOWCHART:
              START
                |
                v
         <Is root NULL?>----YES----> [Return]
                |
               NO
                |
                v
    [Recursively mirror left subtree]
                |
                v
    [Recursively mirror right subtree]
                |
                v
    [Swap root.left and root.right]
                |
                v
               END

VISUAL EXAMPLE:
    Original:        After mirroring left:    After mirroring right:    After swap:
        1                    1                      1                       1
      /   \                /   \                  /   \                   /   \
     2     3              2     3                2     3                 3     2
    / \   / \            / \   / \              / \   / \               / \   / \
   4   5 6   7          5   4 6   7            5   4 7   6             7   6 5   4

RECURSION TREE:
    mirror(1)
    ├─ mirror(2)
    │  ├─ mirror(4) → return
    │  ├─ mirror(5) → return
    │  └─ swap(2's children)
    ├─ mirror(3)
    │  ├─ mirror(6) → return
    │  ├─ mirror(7) → return
    │  └─ swap(3's children)
    └─ swap(1's children)

ALTERNATIVE APPROACH (Pre-order):
1. Swap left and right children first
2. Then recursively mirror left subtree
3. Then recursively mirror right subtree

Both approaches work! The current implementation uses post-order.

TIME COMPLEXITY: O(N) where N is the number of nodes
    - Visit each node exactly once
    - Perform O(1) swap operation at each node

SPACE COMPLEXITY: O(H) where H is the height
    - Recursion call stack uses O(H) space
    - Worst case (skewed tree): O(N)
    - Best case (balanced tree): O(log N)

INTERVIEW TIPS:
- Mention that this is also called "Inverting a Binary Tree"
- Discuss both recursive and iterative (using queue) approaches
- Explain that swapping can be done before or after recursive calls
- Famous problem: Max Howell (Homebrew creator) was asked this at Google
- Can be solved iteratively using level-order traversal
"""

class Solution:
    def mirror(self, root):
        """
        Convert a binary tree into its mirror image.

        This implementation uses post-order traversal: we first mirror
        the subtrees, then swap the children.

        Args:
            root: Root node of the binary tree

        Returns:
            None (modifies tree in-place)
        """
        # BASE CASE: Empty tree or leaf's child
        if root is None:
            return

        # RECURSIVE STEP 1: Mirror the entire left subtree
        # This ensures all nodes in left subtree are mirrored
        self.mirror(root.left)

        # RECURSIVE STEP 2: Mirror the entire right subtree
        # This ensures all nodes in right subtree are mirrored
        self.mirror(root.right)

        # POST-ORDER OPERATION: Swap left and right children
        # Python's tuple unpacking makes this elegant
        # This is equivalent to:
        #   temp = root.left
        #   root.left = root.right
        #   root.right = temp
        root.left, root.right = root.right, root.left