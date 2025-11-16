"""
BINARY SEARCH TREE - CHECK IF A TREE IS BST
============================================

Problem Statement:
    Given a binary tree, determine if it is a valid Binary Search Tree (BST).

    A valid BST must satisfy:
    - Left subtree of a node contains only nodes with keys < node's key
    - Right subtree of a node contains only nodes with keys > node's key
    - Both left and right subtrees must also be BSTs

Approaches:

1. RANGE-BASED VALIDATION (Optimal):
   - For each node, maintain a valid range [min, max]
   - Root can be any value: (-∞, +∞)
   - Left child must be in range: (min, parent.data - 1)
   - Right child must be in range: (parent.data + 1, max)
   - If any node falls outside its range, tree is not BST

2. INORDER TRAVERSAL APPROACH:
   - Inorder traversal of BST produces sorted sequence
   - During inorder traversal, check if current > previous
   - If we find current <= previous, tree is not BST
   - More space efficient in practice

Why Simple Parent-Child Comparison Fails:
    Consider:    10
                /  \
               5    15
                   /  \
                  6   20

    Left child 5 < 10 ✓, Right child 15 > 10 ✓
    But 6 is in right subtree of 10, yet 6 < 10 ✗
    This is NOT a valid BST!

Time Complexity: O(n) - must visit all nodes
Space Complexity:
    - Range method: O(h) recursive stack
    - Inorder method: O(h) recursive stack

Flowchart - Range Based:
    ┌─────────────────┐
    │  Start          │
    │ (min=-∞,max=+∞) │
    └────────┬────────┘
             │
             ▼
    ┌────────────────┐
    │  root == None? │──Yes──►Return True
    └────────┬───────┘
             │No
             ▼
    ┌────────────────────┐
    │root.data < min OR  │──Yes──►Return False
    │root.data > max?    │
    └────────┬───────────┘
             │No
             ▼
    ┌─────────────────────┐
    │Validate left subtree│
    │(min, root.data-1)   │
    └────────┬────────────┘
             │
             ▼
    ┌─────────────────────┐
    │Validate right       │
    │subtree              │
    │(root.data+1, max)   │
    └────────┬────────────┘
             │
             ▼
    ┌────────────────────┐
    │Return left AND     │
    │      right         │
    └────────────────────┘

Flowchart - Inorder:
    ┌─────────────┐
    │   Start     │
    │prev = None  │
    └──────┬──────┘
           │
           ▼
    ┌──────────────┐
    │Inorder Left  │
    └──────┬───────┘
           │
           ▼
    ┌────────────────────┐
    │prev != None AND    │──Yes──►Set flag=False
    │prev.data >= curr?  │        Return
    └────────┬───────────┘
             │No
             ▼
    ┌────────────────┐
    │ prev = curr    │
    └────────┬───────┘
             │
             ▼
    ┌──────────────┐
    │Inorder Right │
    └──────────────┘
"""


class Node:
    """
    Node class for binary tree

    Attributes:
        data: The value stored in the node
        left: Reference to left child
        right: Reference to right child
    """
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    def isBSTUtil(self, root, mi, ma):
        """
        Helper function to check if tree is BST using range validation

        This is the RECOMMENDED approach for interviews as it's:
        - Easy to understand and explain
        - Handles all edge cases correctly
        - Clear logic with explicit bounds

        Args:
            root: Current node being validated
            mi: Minimum allowed value for this node (inclusive)
            ma: Maximum allowed value for this node (inclusive)

        Returns:
            Boolean indicating if subtree rooted at 'root' is a valid BST

        Example:
            >>> root = Node(50)
            >>> root.left = Node(30)
            >>> root.right = Node(70)
            >>> sol = Solution()
            >>> sol.isBSTUtil(root, float('-inf'), float('inf'))
            True
        """
        # Base case: empty tree is a BST
        if root is None:
            return True

        # Current node's data must be within the allowed range
        # If it falls outside, this is not a valid BST
        if root.data < mi or root.data > ma:
            return False

        # Recursively validate left and right subtrees
        # Left subtree: all values must be < root.data
        # Right subtree: all values must be > root.data
        return (self.isBSTUtil(root.left, mi, root.data - 1) and
                self.isBSTUtil(root.right, root.data + 1, ma))

    def isBST(self, root):
        """
        Check if binary tree is a valid BST using range-based approach

        Args:
            root: Root of the binary tree

        Returns:
            Boolean indicating if tree is a valid BST

        Example:
            >>> root = Node(10)
            >>> root.left = Node(5)
            >>> root.right = Node(15)
            >>> sol = Solution()
            >>> sol.isBST(root)
            True

        Time: O(n), Space: O(h)
        """
        max_int = float('inf')
        min_int = float('-inf')
        return self.isBSTUtil(root, min_int, max_int)

    # ===== ALTERNATIVE APPROACH: Inorder Traversal =====

    def inorderBST(self, root):
        """
        Helper function for inorder traversal based validation

        Performs inorder traversal and checks if values are in ascending order.
        Uses instance variables: self.prev and self.flag

        Args:
            root: Current node in traversal
        """
        if root is None:
            return

        # Traverse left subtree first
        self.inorderBST(root.left)

        # Check current node
        # In a valid BST, inorder traversal is strictly increasing
        if self.prev is not None and self.prev.data >= root.data:
            self.flag = False
            return

        # Update previous node for next comparison
        self.prev = root

        # Traverse right subtree
        self.inorderBST(root.right)

    def isBSTInorder(self, root):
        """
        Check if binary tree is a valid BST using inorder traversal

        This approach leverages the property that inorder traversal
        of a BST produces a sorted sequence.

        Args:
            root: Root of the binary tree

        Returns:
            Boolean indicating if tree is a valid BST

        Example:
            >>> root = Node(10)
            >>> root.left = Node(5)
            >>> root.right = Node(15)
            >>> sol = Solution()
            >>> sol.isBSTInorder(root)
            True

        Time: O(n), Space: O(h)
        """
        self.flag = True  # Assume tree is BST initially
        self.prev = None  # Track previous node in inorder traversal
        self.inorderBST(root)
        return self.flag


# Example Usage and Testing
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Valid BST
    print("Test 1: Valid BST")
    #         50
    #        /  \
    #      30    70
    #     /  \   / \
    #   20  40 60  80
    root1 = Node(50)
    root1.left = Node(30)
    root1.right = Node(70)
    root1.left.left = Node(20)
    root1.left.right = Node(40)
    root1.right.left = Node(60)
    root1.right.right = Node(80)

    print(f"Range-based: {sol.isBST(root1)}")        # True
    print(f"Inorder-based: {sol.isBSTInorder(root1)}")  # True

    # Test 2: Invalid BST (violates range constraint)
    print("\nTest 2: Invalid BST")
    #         10
    #        /  \
    #       5    15
    #           /  \
    #          6   20    (6 < 10, violates BST property)
    root2 = Node(10)
    root2.left = Node(5)
    root2.right = Node(15)
    root2.right.left = Node(6)   # This makes it invalid!
    root2.right.right = Node(20)

    print(f"Range-based: {sol.isBST(root2)}")        # False
    print(f"Inorder-based: {sol.isBSTInorder(root2)}")  # False

    # Test 3: Edge case - single node
    print("\nTest 3: Single node")
    root3 = Node(42)
    print(f"Range-based: {sol.isBST(root3)}")        # True
    print(f"Inorder-based: {sol.isBSTInorder(root3)}")  # True

    # Test 4: Edge case - empty tree
    print("\nTest 4: Empty tree")
    root4 = None
    print(f"Range-based: {sol.isBST(root4)}")        # True
    print(f"Inorder-based: {sol.isBSTInorder(root4)}")  # True

    # Test 5: Invalid BST (duplicate values)
    print("\nTest 5: Tree with duplicates")
    #         10
    #        /  \
    #       5    10    (duplicate value)
    root5 = Node(10)
    root5.left = Node(5)
    root5.right = Node(10)

    print(f"Range-based: {sol.isBST(root5)}")        # False
    print(f"Inorder-based: {sol.isBSTInorder(root5)}")  # False
