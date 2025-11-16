"""
BINARY SEARCH TREE - FIND MINIMUM AND MAXIMUM VALUES
=====================================================

Problem Statement:
    Find the minimum and maximum values in a Binary Search Tree (BST).

Approach:
    The BST property makes this operation very efficient:

    For MINIMUM VALUE:
    - In a BST, smaller values are always on the left
    - Keep traversing left until we can't go further
    - The leftmost node contains the minimum value

    For MAXIMUM VALUE:
    - In a BST, larger values are always on the right
    - Keep traversing right until we can't go further
    - The rightmost node contains the maximum value

    Why this works:
    - BST property: left subtree < node < right subtree
    - Minimum is the leftmost leaf (no smaller values exist)
    - Maximum is the rightmost leaf (no larger values exist)

Time Complexity: O(h) where h is height of tree
    - Best case: O(log n) for balanced BST
    - Worst case: O(n) for skewed BST (e.g., all nodes form a chain)

Space Complexity: O(1) - Iterative approach uses constant space

Flowchart - Find Minimum:
    ┌─────────────┐
    │   Start     │
    │ (root node) │
    └──────┬──────┘
           │
           ▼
    ┌─────────────────┐
    │ minVal = root   │
    └──────┬──────────┘
           │
           ▼
    ┌──────────────────┐
    │minVal.left exists│──No──┐
    └──────┬───────────┘      │
           │Yes               │
           ▼                  ▼
    ┌──────────────────┐ ┌────────────┐
    │minVal=minVal.left│ │Return      │
    └──────┬───────────┘ │minVal      │
           │             └────────────┘
           └─────────────┘
           (Loop back)

Flowchart - Find Maximum:
    ┌─────────────┐
    │   Start     │
    │ (root node) │
    └──────┬──────┘
           │
           ▼
    ┌─────────────────┐
    │ maxVal = root   │
    └──────┬──────────┘
           │
           ▼
    ┌───────────────────┐
    │maxVal.right exists│──No──┐
    └──────┬────────────┘      │
           │Yes                │
           ▼                   ▼
    ┌───────────────────┐ ┌────────────┐
    │maxVal=maxVal.right│ │Return      │
    └──────┬────────────┘ │maxVal      │
           │              └────────────┘
           └──────────────┘
           (Loop back)

Example:
    BST:        50
               /  \
             30    70
            /  \   / \
          20  40 60  80

    Minimum: Start at 50 → go to 30 → go to 20 → can't go left → Min = 20
    Maximum: Start at 50 → go to 70 → go to 80 → can't go right → Max = 80
"""


class Node:
    """
    Node class representing each node in the BST

    Attributes:
        data: The value stored in the node
        left: Reference to left child
        right: Reference to right child
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def min_and_max(root):
    """
    Find both minimum and maximum values in a BST

    Args:
        root: Root node of the BST

    Returns:
        Tuple (minNode, maxNode) containing nodes with min and max values

    Raises:
        AttributeError: If root is None (empty tree)

    Example:
        >>> root = Node(50)
        >>> root.left = Node(30)
        >>> root.right = Node(70)
        >>> root.left.left = Node(20)
        >>> root.right.right = Node(80)
        >>> minNode, maxNode = min_and_max(root)
        >>> minNode.data
        20
        >>> maxNode.data
        80

    Time: O(h), Space: O(1)
    """
    # Initialize pointers to root
    minVal = root
    maxVal = root

    # Find minimum value: keep going left
    while minVal.left is not None:
        minVal = minVal.left

    # Find maximum value: keep going right
    while maxVal.right is not None:
        maxVal = maxVal.right

    return minVal, maxVal


def find_min(root):
    """
    Find only the minimum value in BST

    Args:
        root: Root node of the BST

    Returns:
        Node with minimum value

    Example:
        >>> root = Node(50)
        >>> root.left = Node(30)
        >>> root.left.left = Node(20)
        >>> minNode = find_min(root)
        >>> minNode.data
        20
    """
    if root is None:
        return None

    current = root
    # Traverse to the leftmost node
    while current.left is not None:
        current = current.left

    return current


def find_max(root):
    """
    Find only the maximum value in BST

    Args:
        root: Root node of the BST

    Returns:
        Node with maximum value

    Example:
        >>> root = Node(50)
        >>> root.right = Node(70)
        >>> root.right.right = Node(80)
        >>> maxNode = find_max(root)
        >>> maxNode.data
        80
    """
    if root is None:
        return None

    current = root
    # Traverse to the rightmost node
    while current.right is not None:
        current = current.right

    return current


# Example Usage and Testing
if __name__ == "__main__":
    # Create a BST
    #         50
    #        /  \
    #      30    70
    #     /  \   / \
    #   20  40 60  80
    #  /           \
    # 10           90

    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)
    root.left.left.left = Node(10)
    root.right.right.right = Node(90)

    # Test min_and_max function
    print("Testing min_and_max function:")
    minNode, maxNode = min_and_max(root)
    print(f"Minimum value: {minNode.data}")  # Output: 10
    print(f"Maximum value: {maxNode.data}")  # Output: 90

    # Test individual functions
    print("\nTesting individual functions:")
    minNode = find_min(root)
    maxNode = find_max(root)
    print(f"Minimum value: {minNode.data}")  # Output: 10
    print(f"Maximum value: {maxNode.data}")  # Output: 90

    # Test with smaller tree
    print("\nTesting with smaller tree:")
    small_root = Node(100)
    small_root.left = Node(50)
    small_root.right = Node(150)

    minNode, maxNode = min_and_max(small_root)
    print(f"Minimum value: {minNode.data}")  # Output: 50
    print(f"Maximum value: {maxNode.data}")  # Output: 150

    # Test with single node
    print("\nTesting with single node:")
    single = Node(42)
    minNode, maxNode = min_and_max(single)
    print(f"Minimum value: {minNode.data}")  # Output: 42
    print(f"Maximum value: {maxNode.data}")  # Output: 42
