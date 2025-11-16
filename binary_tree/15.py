"""
PROBLEM: Boundary Traversal of Binary Tree
===========================================

Given a binary tree, return its boundary traversal in anti-clockwise direction.
The boundary includes:
1. Root node
2. Left boundary (excluding leaf nodes)
3. All leaf nodes (left to right)
4. Right boundary (excluding leaf nodes, in reverse order)

Example 1:
    Input Tree:
               20
             /    \
            8      22
           / \       \
          4   12      25
             /  \
            10  14

    Output: [20, 8, 4, 10, 14, 25, 22]
    Explanation:
        - Root: 20
        - Left boundary: 8 (4 is leaf, excluded here)
        - Leaf nodes: 4, 10, 14, 25
        - Right boundary (reverse): 22 (25 is leaf, excluded here)

Example 2:
    Input Tree:
           1
         /   \
        2     3

    Output: [1, 2, 3]

APPROACH & REASONING:
====================
Break the problem into three parts and combine results.

WHY THIS APPROACH?
- Modular: Handle left boundary, leaves, right boundary separately
- Clear logic for each component
- Easy to understand and debug

KEY INSIGHTS:
1. LEFT BOUNDARY:
   - Go left if possible, else go right
   - Don't include leaf nodes (handled separately)
   - Process top to bottom

2. LEAF NODES:
   - In-order traversal naturally gives left-to-right order
   - Check if both children are None

3. RIGHT BOUNDARY:
   - Go right if possible, else go left
   - Don't include leaf nodes
   - Process bottom to top (add after recursion)

ALGORITHM STEPS:
1. Add root to result
2. Get left boundary (excluding leaves):
   - Prefer left child, fall back to right child
   - Add node before recursion (top to bottom)
3. Get all leaf nodes (left to right):
   - Use in-order traversal
   - Check if node has no children
4. Get right boundary (excluding leaves):
   - Prefer right child, fall back to left child
   - Add node after recursion (bottom to top for reverse)
5. Combine all parts

FLOWCHART:
         START
           |
           v
    [Add root to result]
           |
           v
    [Get left boundary → result]
           |
           v
    [Get leaf nodes → result]
           |
           v
    [Get right boundary → result]
           |
           v
    [Return result]

    left_tree(root):
         START
           |
           v
    <Is root None?>----YES----> [Return]
           |
          NO
           |
           v
    <Has left child?>----YES----> [Add root, recurse left]
           |                            |
          NO                            v
           |                         [Return]
           v
    <Has right child?>----YES----> [Add root, recurse right]
           |                             |
          NO                             v
           |                          [Return]
           v
    [Return (leaf node, don't add)]

    leaf_nodes(root):
         START
           |
           v
    [Recurse left]
           |
           v
    <Is leaf?>----YES----> [Add to result]
           |                      |
          NO                      |
           |<--------------------
           v
    [Recurse right]

    right_tree(root):
         START
           |
           v
    <Has right child?>----YES----> [Recurse right, then add root]
           |                              |
          NO                              v
           |                           [Return]
           v
    <Has left child?>----YES----> [Recurse left, then add root]
           |                             |
          NO                             v
           |                          [Return]
           v
    [Return (leaf node, don't add)]

TIME COMPLEXITY: O(N) where N is the number of nodes
    - Each node visited at most once
    - Three separate traversals but total is O(N)

SPACE COMPLEXITY: O(H) where H is height
    - Recursion depth for each traversal
    - Result array is O(N) but that's output, not auxiliary space

INTERVIEW TIPS:
- Explain the three components clearly
- Emphasize why right boundary is added in reverse (post-order)
- Mention edge cases: root only, single branch trees
- Discuss why leaves are excluded from left/right boundaries
- Common follow-up: Handle when tree has only left or only right subtree
- Draw the boundary on a tree diagram to visualize
"""

class Solution:
    def left_tree(self, root, ans):
        """
        Adds left boundary nodes to result (excluding leaves).

        Traverses left boundary top-to-bottom. Prefers left child,
        falls back to right child if left doesn't exist.

        Args:
            root: Current node
            ans: Result list to append nodes to
        """
        # BASE CASE: Empty node
        if root is None:
            return

        # CASE 1: Left child exists
        if root.left != None:
            # Add current node (not a leaf since it has children)
            ans.append(root.data)
            # Continue down left boundary
            self.left_tree(root.left, ans)

        # CASE 2: No left child, but right child exists
        elif root.right != None:
            # Add current node (not a leaf since it has children)
            ans.append(root.data)
            # Go right to continue left boundary
            self.left_tree(root.right, ans)

        # CASE 3: Leaf node (both children None) - don't add
        # Leaves will be handled by leaf_nodes() function

    def leaf_nodes(self, root, ans):
        """
        Adds all leaf nodes to result in left-to-right order.

        Uses in-order traversal pattern (left, root, right) which
        naturally gives left-to-right order for leaves.

        Args:
            root: Current node
            ans: Result list to append nodes to
        """
        # BASE CASE: Empty node
        if root is None:
            return

        # STEP 1: Process left subtree first (in-order pattern)
        self.leaf_nodes(root.left, ans)

        # STEP 2: Check if current node is a leaf
        if root.left is None and root.right is None:
            # Both children are None - this is a leaf node
            ans.append(root.data)

        # STEP 3: Process right subtree
        self.leaf_nodes(root.right, ans)

    def right_tree(self, root, ans):
        """
        Adds right boundary nodes to result (excluding leaves) in reverse order.

        Traverses right boundary but adds nodes AFTER recursion, giving
        bottom-to-top order (reverse). Prefers right child, falls back to left.

        Args:
            root: Current node
            ans: Result list to append nodes to
        """
        # BASE CASE: Empty node
        if root is None:
            return

        # CASE 1: Right child exists
        if root.right != None:
            # Recurse first (post-order pattern)
            self.right_tree(root.right, ans)
            # Add current node AFTER recursion (bottom-to-top)
            # This gives us reverse order
            ans.append(root.data)

        # CASE 2: No right child, but left child exists
        elif root.left != None:
            # Recurse first
            self.right_tree(root.left, ans)
            # Add current node AFTER recursion
            ans.append(root.data)

        # CASE 3: Leaf node - don't add
        # Leaves already handled by leaf_nodes()

    def printBoundaryView(self, root):
        """
        Returns boundary traversal of binary tree in anti-clockwise direction.

        Boundary = root + left_boundary + leaves + right_boundary(reversed)

        Args:
            root: Root node of the binary tree

        Returns:
            List containing boundary traversal

        Time Complexity: O(N) - visit each node at most once
        Space Complexity: O(H) - recursion depth
        """
        # EDGE CASE: Empty tree
        if root is None:
            return []

        # STEP 1: Initialize result with root
        ans = [root.data]

        # STEP 2: Add left boundary (excluding root and leaves)
        # Start from root's left child
        self.left_tree(root.left, ans)

        # STEP 3: Add all leaf nodes (left to right)
        # This includes leaves from both left and right subtrees
        self.leaf_nodes(root, ans)

        # STEP 4: Add right boundary in reverse (excluding root and leaves)
        # Start from root's right child
        self.right_tree(root.right, ans)

        # STEP 5: Return complete boundary traversal
        return ans
