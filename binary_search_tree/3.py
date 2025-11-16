"""
BINARY SEARCH TREE - INORDER SUCCESSOR AND PREDECESSOR
=======================================================

Problem Statement:
    Find the inorder successor and inorder predecessor of a given key in a BST.

    - Inorder Successor: The next node in inorder traversal (smallest node greater than key)
    - Inorder Predecessor: The previous node in inorder traversal (largest node smaller than key)

Approach:
    Understanding Inorder Traversal:
    For BST:        50
                   /  \
                 30    70
                /  \   / \
              20  40 60  80

    Inorder: 20, 30, 40, 50, 60, 70, 80 (always sorted for BST)

    CASE 1: Key exists in the tree
    ----------------
    Successor:
    - If node has right subtree: successor is the leftmost node in right subtree
    - Otherwise: successor is the ancestor where we last took a left turn

    Predecessor:
    - If node has left subtree: predecessor is the rightmost node in left subtree
    - Otherwise: predecessor is the ancestor where we last took a right turn

    CASE 2: Key doesn't exist
    ----------------
    - While searching for key, track potential successor/predecessor
    - When going left: current node could be successor
    - When going right: current node could be predecessor

Time Complexity: O(h) where h is height of tree
    - Best: O(log n) for balanced BST
    - Worst: O(n) for skewed BST

Space Complexity: O(h) for recursive approach

Flowchart:
    ┌─────────────┐
    │   Start     │
    └──────┬──────┘
           │
           ▼
    ┌──────────────┐
    │Find node with│
    │    key       │
    └──────┬───────┘
           │
      ┌────┴────┐
      │         │
      ▼         ▼
  ┌────────┐ ┌────────┐
  │Key ==  │ │Key !=  │
  │root.key│ │root.key│
  └───┬────┘ └───┬────┘
      │          │
      ▼          ▼
  ┌────────────────┐
  │Node has left?  │──Yes──┐
  └───┬────────────┘       │
      │No                  ▼
      │              ┌──────────────┐
      ▼              │Pred=rightmost│
  ┌────────────────┐│in left tree  │
  │Node has right? │└──────────────┘
  └───┬────────────┘
      │Yes
      ▼
  ┌──────────────┐
  │Succ=leftmost │
  │in right tree │
  └──────────────┘

Example:
    BST:        50
               /  \
             30    70
            /  \   / \
          20  40 60  80

    For key=50:
    - Predecessor: 40 (rightmost in left subtree)
    - Successor: 60 (leftmost in right subtree)

    For key=30:
    - Predecessor: 20 (leftmost in left subtree, actually rightmost)
    - Successor: 40 (rightmost in right subtree, actually leftmost)
"""


class Node:
    """
    Node class for BST

    Attributes:
        key: The value stored in the node
        left: Reference to left child
        right: Reference to right child
    """
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


def inorderPredecessor(root):
    """
    Find the inorder predecessor (maximum value) in a subtree

    The predecessor is the rightmost node (maximum) in the given subtree.

    Args:
        root: Root of the subtree

    Returns:
        Node with maximum value in subtree

    Time: O(h), Space: O(1)
    """
    curr = root
    # Keep moving right to find the largest value
    while curr.right is not None:
        curr = curr.right
    return curr


def inorderSuccessor(root):
    """
    Find the inorder successor (minimum value) in a subtree

    The successor is the leftmost node (minimum) in the given subtree.

    Args:
        root: Root of the subtree

    Returns:
        Node with minimum value in subtree

    Time: O(h), Space: O(1)
    """
    curr = root
    # Keep moving left to find the smallest value
    while curr.left is not None:
        curr = curr.left
    return curr


def findPredSucc(root, key):
    """
    Find both predecessor and successor of a given key in BST

    Args:
        root: Root of the BST
        key: The value whose predecessor and successor we need to find

    Returns:
        Tuple (predecessor, successor) - both can be None if they don't exist

    Example:
        >>> root = Node(50)
        >>> root.left = Node(30)
        >>> root.right = Node(70)
        >>> root.left.left = Node(20)
        >>> root.left.right = Node(40)
        >>> pred, succ = findPredSucc(root, 30)
        >>> pred.key if pred else None
        20
        >>> succ.key if succ else None
        40

    Time: O(h), Space: O(h)
    """
    pred = None
    succ = None

    # Search for the key and find predecessor/successor
    curr = root

    while curr is not None:
        if curr.key == key:
            # Key found!

            # Predecessor: rightmost node in left subtree
            if curr.left:
                pred = inorderPredecessor(curr.left)

            # Successor: leftmost node in right subtree
            if curr.right:
                succ = inorderSuccessor(curr.right)

            break

        elif key < curr.key:
            # Key is in left subtree
            # Current node could be the successor (we're going left)
            succ = curr
            curr = curr.left

        else:  # key > curr.key
            # Key is in right subtree
            # Current node could be the predecessor (we're going right)
            pred = curr
            curr = curr.right

    return pred, succ


def findPredSuccRecursive(root, pred, succ, key):
    """
    Recursive version to find predecessor and successor

    NOTE: This implementation uses mutable list to pass pred/succ by reference

    Args:
        root: Current node in recursion
        pred: List containing predecessor node [pred_node]
        succ: List containing successor node [succ_node]
        key: The value to find pred/succ for

    Returns:
        None (modifies pred and succ lists)

    Example:
        >>> root = Node(50)
        >>> pred, succ = [None], [None]
        >>> findPredSuccRecursive(root, pred, succ, 30)
        >>> pred[0].key if pred[0] else None
        >>> succ[0].key if succ[0] else None
    """
    if root is None:
        return

    # Key found at root
    if root.key == key:
        # Predecessor is the maximum in left subtree
        if root.left:
            pred[0] = inorderPredecessor(root.left)

        # Successor is the minimum in right subtree
        if root.right:
            succ[0] = inorderSuccessor(root.right)

        return

    # Key is greater than root, search in right subtree
    elif key > root.key:
        # Root could be predecessor (we're moving right)
        pred[0] = root
        findPredSuccRecursive(root.right, pred, succ, key)

    # Key is smaller than root, search in left subtree
    else:
        # Root could be successor (we're moving left)
        succ[0] = root
        findPredSuccRecursive(root.left, pred, succ, key)


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

    # Test 1: Find pred/succ of root (50)
    print("Test 1: Key = 50 (root)")
    pred, succ = findPredSucc(root, 50)
    print(f"Predecessor: {pred.key if pred else None}")  # 40
    print(f"Successor: {succ.key if succ else None}")    # 60

    # Test 2: Find pred/succ of 30
    print("\nTest 2: Key = 30")
    pred, succ = findPredSucc(root, 30)
    print(f"Predecessor: {pred.key if pred else None}")  # 20
    print(f"Successor: {succ.key if succ else None}")    # 40

    # Test 3: Find pred/succ of 20 (leftmost - no predecessor)
    print("\nTest 3: Key = 20 (leftmost)")
    pred, succ = findPredSucc(root, 20)
    print(f"Predecessor: {pred.key if pred else None}")  # None
    print(f"Successor: {succ.key if succ else None}")    # 30

    # Test 4: Find pred/succ of 80 (rightmost - no successor)
    print("\nTest 4: Key = 80 (rightmost)")
    pred, succ = findPredSucc(root, 80)
    print(f"Predecessor: {pred.key if pred else None}")  # 70
    print(f"Successor: {succ.key if succ else None}")    # None

    # Test 5: Find pred/succ of non-existing key 65
    print("\nTest 5: Key = 65 (doesn't exist)")
    pred, succ = findPredSucc(root, 65)
    print(f"Predecessor: {pred.key if pred else None}")  # 60
    print(f"Successor: {succ.key if succ else None}")    # 70

    # Test recursive version
    print("\nTest 6: Recursive version for key = 40")
    pred_list, succ_list = [None], [None]
    findPredSuccRecursive(root, pred_list, succ_list, 40)
    print(f"Predecessor: {pred_list[0].key if pred_list[0] else None}")  # 30
    print(f"Successor: {succ_list[0].key if succ_list[0] else None}")    # 50
