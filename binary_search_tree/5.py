"""
BINARY SEARCH TREE - POPULATE INORDER SUCCESSOR FOR ALL NODES
===============================================================

Problem Statement:
    Given a BST where each node has an additional 'next' pointer,
    populate each node's next pointer to point to its inorder successor.

    If a node has no inorder successor, the next pointer should be NULL.

Approach:
    Use Reverse Inorder Traversal (Right -> Root -> Left):

    - Regular inorder: Left -> Root -> Right (gives ascending order)
    - Reverse inorder: Right -> Root -> Left (gives descending order)

    Strategy:
    1. Start from rightmost node (largest value)
    2. Keep track of previously visited node
    3. When visiting current node, set prev.next = current
    4. Update prev to current
    5. Continue to left subtree

    Why Reverse Inorder?
    - When we visit a node, the previous node in reverse inorder
      is actually the successor in normal inorder
    - This allows us to set next pointers in a single traversal

Example:
    BST:        50
               /  \
             30    70
            /  \   / \
          20  40 60  80

    Inorder: 20 -> 30 -> 40 -> 50 -> 60 -> 70 -> 80
    After populating next:
        20.next = 30
        30.next = 40
        40.next = 50
        50.next = 60
        60.next = 70
        70.next = 80
        80.next = None

Time Complexity: O(n) - visit each node once
Space Complexity: O(h) - recursive call stack

Flowchart:
    ┌─────────────┐
    │   Start     │
    │ prev = None │
    └──────┬──────┘
           │
           ▼
    ┌──────────────┐
    │ root == None?│──Yes──►Return
    └──────┬───────┘
           │No
           ▼
    ┌──────────────────┐
    │Populate Left     │
    │Subtree Recursively│
    └──────┬───────────┘
           │
           ▼
    ┌──────────────────┐
    │prev != None?     │──Yes──┐
    └──────┬───────────┘       │
           │No                 ▼
           │            ┌──────────────┐
           │            │prev.next=root│
           │            └──────┬───────┘
           │                   │
           └───────────────────┘
           │
           ▼
    ┌──────────────┐
    │ prev = root  │
    └──────┬───────┘
           │
           ▼
    ┌──────────────────┐
    │Populate Right    │
    │Subtree Recursively│
    └───────────────────┘
"""


class Node:
    """
    BST Node with next pointer

    Attributes:
        data: The value stored in the node
        left: Reference to left child
        right: Reference to right child
        next: Reference to inorder successor
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None  # Points to inorder successor


class Solution:
    def populate(self, root):
        """
        Helper function to populate next pointers using inorder traversal

        Uses instance variable self.prev to track the previously visited node.

        Args:
            root: Current node in traversal

        Time: O(n), Space: O(h)
        """
        if root is None:
            return

        # First, populate left subtree
        self.populate(root.left)

        # Set previous node's next to current node
        # This connects the inorder predecessor to current node
        if self.prev is not None:
            self.prev.next = root

        # Update prev to current node for next iteration
        self.prev = root

        # Finally, populate right subtree
        self.populate(root.right)

    def populateNext(self, root):
        """
        Populate next pointer for all nodes in BST

        Each node's next pointer will point to its inorder successor.
        The last node (rightmost) will have next = None.

        Args:
            root: Root of the BST

        Returns:
            Root of the BST with populated next pointers

        Example:
            >>> root = Node(50)
            >>> root.left = Node(30)
            >>> root.right = Node(70)
            >>> sol = Solution()
            >>> root = sol.populateNext(root)
            >>> root.left.next.data  # 30's successor
            50

        Time: O(n), Space: O(h)
        """
        self.prev = None
        self.populate(root)
        return root


def printInorderWithNext(root):
    """Helper function to print inorder traversal with next pointers"""
    if root is None:
        return

    printInorderWithNext(root.left)

    next_val = root.next.data if root.next else None
    print(f"Node: {root.data}, Next: {next_val}")

    printInorderWithNext(root.right)


# Example Usage and Testing
if __name__ == "__main__":
    # Create a BST
    #         50
    #        /  \
    #      30    70
    #     /  \   / \
    #   20  40 60  80

    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)

    print("BST before populating next pointers:")
    print("Inorder: 20, 30, 40, 50, 60, 70, 80")

    # Populate next pointers
    sol = Solution()
    root = sol.populateNext(root)

    print("\nBST after populating next pointers:")
    print("(Each node's next pointer points to its inorder successor)")
    printInorderWithNext(root)

    # Verify specific connections
    print("\nVerification:")
    print(f"20's successor: {root.left.left.next.data if root.left.left.next else 'None'}")  # 30
    print(f"40's successor: {root.left.right.next.data if root.left.right.next else 'None'}")  # 50
    print(f"50's successor: {root.next.data if root.next else 'None'}")  # 60
    print(f"80's successor: {root.right.right.next.data if root.right.right.next else 'None'}")  # None

    # Test with smaller tree
    print("\n\nTest with smaller tree:")
    root2 = Node(10)
    root2.left = Node(5)
    root2.right = Node(15)

    root2 = sol.populateNext(root2)
    printInorderWithNext(root2)
