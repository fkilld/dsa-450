"""
BINARY SEARCH TREE - DELETION OF A NODE
========================================

Problem Statement:
    Delete a node with a given key from a Binary Search Tree (BST) while
    maintaining the BST properties.

Approach:
    Deletion in BST has three cases:

    1. Node is a leaf (no children):
       - Simply remove the node

    2. Node has one child:
       - Replace node with its child

    3. Node has two children:
       - Find inorder successor (smallest node in right subtree)
       - Replace node's value with inorder successor's value
       - Delete the inorder successor (which will be case 1 or 2)

    Inorder Successor:
    - The smallest node in the right subtree
    - Found by going to right child, then traversing left until we can't go further
    - It's guaranteed to have at most one child (right child only)

Why Inorder Successor?
    - Inorder traversal of BST gives sorted order
    - Inorder successor is the next larger element
    - Replacing with it maintains BST property

Time Complexity: O(h) where h is height of tree
    - Best case: O(log n) for balanced BST
    - Worst case: O(n) for skewed BST

Space Complexity: O(h) due to recursive call stack

Flowchart:
    ┌─────────────┐
    │   Start     │
    └──────┬──────┘
           │
           ▼
    ┌──────────────┐
    │ root == None?│──Yes──┐
    └──────┬───────┘       │
           │No             ▼
           ▼          ┌────────┐
    ┌──────────────┐ │ Return │
    │Find the node │ │  None  │
    │  with key    │ └────────┘
    └──────┬───────┘
           │
           ▼
    ┌──────────────────┐
    │  Node found?     │
    └──────┬───────────┘
           │
     ┌─────┴──────────────┐
     │                    │
     ▼                    ▼
┌─────────┐         ┌──────────┐
│Only left│         │Only right│
│ child?  │         │ child?   │
└────┬────┘         └────┬─────┘
     │Yes                │Yes
     ▼                   ▼
┌──────────┐       ┌──────────┐
│Return    │       │Return    │
│left child│       │right     │
└──────────┘       │child     │
                   └──────────┘
           │
           │Both children exist
           ▼
    ┌────────────────────┐
    │Find inorder succ   │
    │(leftmost in right) │
    └──────┬─────────────┘
           │
           ▼
    ┌────────────────────┐
    │Replace node's value│
    │with successor value│
    └──────┬─────────────┘
           │
           ▼
    ┌────────────────────┐
    │Delete successor    │
    │from right subtree  │
    └────────────────────┘
"""


class TreeNode:
    """
    TreeNode class representing each node in the BST

    Attributes:
        val: The value stored in the node
        left: Reference to left child
        right: Reference to right child
    """
    def __init__(self, data):
        self.val = data
        self.right = None
        self.left = None


class Solution:
    def inorderSucc(self, root):
        """
        Find the inorder successor (minimum value node) in a subtree

        The inorder successor is the leftmost node in the right subtree,
        which is the smallest value greater than the current node.

        Args:
            root: Root of the subtree to search

        Returns:
            The node with minimum value in the subtree

        Example:
            For tree:    50
                        /  \
                      30   70
                          /  \
                        60   80
            inorderSucc(70) returns node with value 60
        """
        curr = root
        # Keep going left to find the smallest value
        while curr.left is not None:
            curr = curr.left
        return curr

    def deleteNode(self, root, key):
        """
        Delete a node with given key from BST

        Args:
            root: Root of the BST (or current node in recursion)
            key: Value of the node to delete

        Returns:
            Root of the modified BST

        Example:
            >>> root = TreeNode(50)
            >>> root.left = TreeNode(30)
            >>> root.right = TreeNode(70)
            >>> sol = Solution()
            >>> root = sol.deleteNode(root, 30)
            # Node with value 30 is deleted
        """
        # Base case: empty tree
        if root is None:
            return None

        # STEP 1: Find the node to delete using BST property
        # Key is in right subtree
        if root.val < key:
            root.right = self.deleteNode(root.right, key)

        # Key is in left subtree
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)

        # STEP 2: Node found, now delete it
        else:
            # Case 1: Node has only right child (or no left child)
            if root.left is None:
                temp = root.right
                root = None  # Delete current node
                return temp

            # Case 2: Node has only left child (or no right child)
            if root.right is None:
                temp = root.left
                root = None  # Delete current node
                return temp

            # Case 3: Node has both left and right children
            # Find inorder successor (smallest in right subtree)
            temp = self.inorderSucc(root.right)

            # Copy inorder successor's value to current node
            root.val = temp.val

            # Delete the inorder successor (it will have at most one child)
            root.right = self.deleteNode(root.right, temp.val)

        return root


def inorder(root, result):
    """Helper function to perform inorder traversal for testing"""
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)


# Example Usage and Testing
if __name__ == "__main__":
    # Create a BST
    #         50
    #        /  \
    #      30    70
    #     /  \   / \
    #   20  40 60  80

    root = TreeNode(50)
    root.left = TreeNode(30)
    root.right = TreeNode(70)
    root.left.left = TreeNode(20)
    root.left.right = TreeNode(40)
    root.right.left = TreeNode(60)
    root.right.right = TreeNode(80)

    sol = Solution()

    print("Original BST (inorder):")
    result = []
    inorder(root, result)
    print(result)  # [20, 30, 40, 50, 60, 70, 80]

    # Test Case 1: Delete leaf node
    print("\nDeleting leaf node (20):")
    root = sol.deleteNode(root, 20)
    result = []
    inorder(root, result)
    print(result)  # [30, 40, 50, 60, 70, 80]

    # Test Case 2: Delete node with one child
    print("\nDeleting node with one child (30):")
    root = sol.deleteNode(root, 30)
    result = []
    inorder(root, result)
    print(result)  # [40, 50, 60, 70, 80]

    # Test Case 3: Delete node with two children
    print("\nDeleting node with two children (70):")
    root = sol.deleteNode(root, 70)
    result = []
    inorder(root, result)
    print(result)  # [40, 50, 60, 80]

    # Test Case 4: Delete root
    print("\nDeleting root (50):")
    root = sol.deleteNode(root, 50)
    result = []
    inorder(root, result)
    print(result)  # [40, 60, 80]
