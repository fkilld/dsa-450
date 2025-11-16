"""
BINARY SEARCH TREE - SEARCH AND INSERTION
==========================================

Problem Statement:
    Implement search and insertion operations in a Binary Search Tree (BST).

    A Binary Search Tree is a binary tree with the following properties:
    - The left subtree of a node contains only nodes with keys less than the node's key
    - The right subtree of a node contains only nodes with keys greater than the node's key
    - Both left and right subtrees are also binary search trees
    - No duplicate nodes

Approach:
    1. SEARCH OPERATION:
       - Start from the root node
       - If the key matches current node's data, return the node
       - If key is smaller, search in left subtree
       - If key is larger, search in right subtree
       - If we reach None, key doesn't exist

    2. INSERTION OPERATION:
       - Find the correct position using BST property
       - If tree is empty, create new node as root
       - If key already exists, return (no duplicates)
       - If key is smaller than current node, go left
       - If key is larger than current node, go right
       - Insert new node when we reach None position

Time Complexity:
    - Search: O(h) where h is height of tree
      * Best case: O(log n) for balanced BST
      * Worst case: O(n) for skewed BST
    - Insert: O(h) where h is height of tree
      * Best case: O(log n) for balanced BST
      * Worst case: O(n) for skewed BST

Space Complexity:
    - O(h) due to recursive call stack
    - O(1) for iterative approach (can be implemented)

Flowchart - SEARCH:
    ┌─────────────┐
    │   Start     │
    └──────┬──────┘
           │
           ▼
    ┌──────────────────┐
    │ root == None or  │──Yes──┐
    │ root.data == key?│       │
    └──────┬───────────┘       │
           │No                 │
           ▼                   ▼
    ┌──────────────────┐  ┌────────────┐
    │ root.data < key? │  │Return root │
    └──────┬───────────┘  └────────────┘
           │
     ┌─────┴─────┐
     │Yes        │No
     ▼           ▼
┌─────────┐  ┌──────────┐
│Search in│  │Search in │
│  right  │  │   left   │
│ subtree │  │ subtree  │
└─────────┘  └──────────┘

Flowchart - INSERT:
    ┌─────────────┐
    │   Start     │
    └──────┬──────┘
           │
           ▼
    ┌──────────────┐
    │ root == None?│──Yes──┐
    └──────┬───────┘       │
           │No             ▼
           ▼          ┌────────────┐
    ┌──────────────┐ │Create Node │
    │root.data==key│ │Return Node │
    └──────┬───────┘ └────────────┘
           │
     ┌─────┴─────┐
     │Yes        │No
     ▼           ▼
┌──────────┐  ┌──────────────┐
│Return    │  │root.data<key?│
│  root    │  └──────┬───────┘
└──────────┘         │
                ┌────┴────┐
                │Yes      │No
                ▼         ▼
           ┌─────────┐ ┌──────────┐
           │Insert in│ │Insert in │
           │  right  │ │   left   │
           │ subtree │ │ subtree  │
           └─────────┘ └──────────┘
"""


class Node:
    """
    Node class representing each node in the Binary Search Tree

    Attributes:
        data: The value stored in the node
        left: Reference to left child node
        right: Reference to right child node
    """
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def search(root, key):
    """
    Search for a key in the Binary Search Tree

    Args:
        root: Root node of the BST (or current node in recursion)
        key: The value to search for

    Returns:
        The node containing the key if found, None otherwise

    Example:
        >>> root = Node(50)
        >>> root.left = Node(30)
        >>> root.right = Node(70)
        >>> result = search(root, 30)
        >>> result.data
        30
    """
    # Base case: empty tree or key found
    if root is None or root.data == key:
        return root

    # Key is greater than current node's data, search in right subtree
    if root.data < key:
        return search(root.right, key)

    # Key is smaller than current node's data, search in left subtree
    return search(root.left, key)


def insert(root, key):
    """
    Insert a new key into the Binary Search Tree

    Args:
        root: Root node of the BST (or current node in recursion)
        key: The value to insert

    Returns:
        The root node of the modified BST

    Example:
        >>> root = None
        >>> root = insert(root, 50)
        >>> root = insert(root, 30)
        >>> root = insert(root, 70)
        >>> root.data
        50
        >>> root.left.data
        30
        >>> root.right.data
        70
    """
    # Base case: found the position to insert
    if root is None:
        return Node(key)

    # Key already exists, return without inserting (no duplicates)
    if root.data == key:
        return root

    # Key is greater than current node, insert in right subtree
    elif root.data < key:
        root.right = insert(root.right, key)

    # Key is smaller than current node, insert in left subtree
    else:
        root.left = insert(root.left, key)

    # Return the unchanged root pointer
    return root


# Example Usage and Testing
if __name__ == "__main__":
    # Create a BST
    root = None

    # Insert nodes
    print("Inserting nodes: 50, 30, 20, 40, 70, 60, 80")
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    # BST Structure:
    #         50
    #        /  \
    #      30    70
    #     /  \   / \
    #   20  40 60  80

    # Search for existing keys
    print("\nSearching for key 40:")
    result = search(root, 40)
    if result:
        print(f"Found: {result.data}")
    else:
        print("Not found")

    # Search for non-existing key
    print("\nSearching for key 100:")
    result = search(root, 100)
    if result:
        print(f"Found: {result.data}")
    else:
        print("Not found")

    # Try to insert duplicate
    print("\nTrying to insert duplicate key 30:")
    root = insert(root, 30)
    print("No duplicate inserted (BST maintains uniqueness)")
