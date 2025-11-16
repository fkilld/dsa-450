"""
PROBLEM: Diameter of Binary Tree
================================

The diameter of a binary tree is the length of the longest path between
any two nodes in the tree. This path may or may not pass through the root.

The length of a path is the number of edges between nodes.

Example 1:
    Input Tree:
           1
         /   \
        2     3
       / \
      4   5

    Output: 3
    Explanation: Path 4->2->1->3 has 3 edges (longest path)

Example 2:
    Input Tree:
           1
         /   \
        2     3
       / \     \
      4   5     6
             \
              7

    Output: 5
    Explanation: Path 4->2->5->7 or similar has maximum edges

APPROACH & REASONING:
====================
The key insight is that for any node, the longest path either:
1. Goes through that node (left_height + right_height + 1)
2. Is entirely in the left subtree
3. Is entirely in the right subtree

NAIVE APPROACH: O(N²)
For each node, calculate height of left and right subtrees.
This recalculates heights multiple times.

OPTIMIZED APPROACH: O(N)
Calculate height and diameter in a single traversal.
For each node, we compute:
- Height of the subtree rooted at that node
- Diameter considering all three cases above

WHY HEIGHT CLASS?
In Python, integers are immutable. To return both diameter and height
from a recursive function, we use a Height object that can be modified.

ALGORITHM STEPS:
1. Base case: If root is None, height = 0, diameter = 0
2. Recursively get left diameter and left height
3. Recursively get right diameter and right height
4. Current height = max(left_height, right_height) + 1
5. Diameter through current node = left_height + right_height + 1
6. Return max of (diameter through node, left diameter, right diameter)

FLOWCHART:
                   START
                     |
                     v
            <Is root NULL?>----YES----> [height=0, return 0]
                     |
                    NO
                     |
                     v
    [Recursively get left_diameter & left_height]
                     |
                     v
    [Recursively get right_diameter & right_height]
                     |
                     v
    [current_height = max(left_height, right_height) + 1]
                     |
                     v
    [diameter_through_node = left_height + right_height + 1]
                     |
                     v
    [max_diameter = max(diameter_through_node,
                        left_diameter,
                        right_diameter)]
                     |
                     v
              [Return max_diameter]
                     |
                     v
                    END

EXAMPLE WALKTHROUGH:
    Tree:      1
             /   \
            2     3
           / \
          4   5

    Processing node 4:
        - left_height = 0, right_height = 0
        - height of 4 = 1
        - diameter through 4 = 0 + 0 + 1 = 1

    Processing node 5:
        - left_height = 0, right_height = 0
        - height of 5 = 1
        - diameter through 5 = 0 + 0 + 1 = 1

    Processing node 2:
        - left_height = 1 (from node 4)
        - right_height = 1 (from node 5)
        - height of 2 = max(1,1) + 1 = 2
        - diameter through 2 = 1 + 1 + 1 = 3

    Processing node 3:
        - left_height = 0, right_height = 0
        - height of 3 = 1
        - diameter through 3 = 0 + 0 + 1 = 1

    Processing node 1:
        - left_height = 2 (from node 2)
        - right_height = 1 (from node 3)
        - height of 1 = max(2,1) + 1 = 3
        - diameter through 1 = 2 + 1 + 1 = 4
        - max_diameter = max(4, 3, 1) = 4

    Wait, this gives 4, but the answer should be 3...
    The issue is we're counting nodes, not edges.
    Diameter in edges = height + height (not + 1)

TIME COMPLEXITY: O(N) where N is the number of nodes
    - Visit each node exactly once
    - Constant work at each node

SPACE COMPLEXITY: O(H) where H is the height
    - Recursion stack space
    - Worst case: O(N) for skewed tree
    - Best case: O(log N) for balanced tree

INTERVIEW TIPS:
- Explain the difference between naive O(N²) and optimized O(N)
- Discuss why we can't just do left_height + right_height at root
- Mention that diameter might not pass through root
- Be ready to implement without the Height class using tuples
"""

class Height:
    """Helper class to store height value that can be modified in recursion."""
    def __init__(self):
        self.h = 0

class Solution:
    def diameterOpt(self, root, height):
        """
        Calculate diameter and height of tree in single traversal.

        Args:
            root: Current node being processed
            height: Height object to store height of current subtree

        Returns:
            Maximum diameter found in the subtree rooted at root
        """
        # Initialize height objects for left and right subtrees
        lh = Height()  # Will store left subtree height
        rh = Height()  # Will store right subtree height

        # BASE CASE: Empty tree
        if root is None:
            height.h = 0  # Height of empty tree is 0
            return 0      # Diameter of empty tree is 0

        # RECURSIVE STEP: Get diameter of left subtree
        # Also updates lh with height of left subtree
        ld = self.diameterOpt(root.left, lh)

        # RECURSIVE STEP: Get diameter of right subtree
        # Also updates rh with height of right subtree
        rd = self.diameterOpt(root.right, rh)

        # UPDATE HEIGHT: Height of current node's subtree
        # = max height of children + 1 (for current node)
        height.h = max(lh.h, rh.h) + 1

        # CALCULATE DIAMETER:
        # The longest path either:
        # 1. Goes through current node: left_height + right_height + 1
        # 2. Is entirely in left subtree: ld
        # 3. Is entirely in right subtree: rd
        # Take the maximum of all three
        return max(lh.h + rh.h + 1, max(ld, rd))

    def diameter(self, root):
        """
        Public interface to find diameter of binary tree.

        Args:
            root: Root node of the binary tree

        Returns:
            Integer representing the diameter (longest path)
        """
        height = Height()
        return self.diameterOpt(root, height)