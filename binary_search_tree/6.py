"""
BINARY SEARCH TREE - LOWEST COMMON ANCESTOR (LCA)
==================================================

Problem Statement:
    Find the Lowest Common Ancestor (LCA) of two nodes in a BST.

    LCA Definition:
    The lowest common ancestor of two nodes n1 and n2 is the lowest node
    that has both n1 and n2 as descendants (a node can be a descendant of itself).

Approach:
    BST property allows us to find LCA efficiently:

    Key Insight:
    - If both n1 and n2 are smaller than current node → LCA is in left subtree
    - If both n1 and n2 are greater than current node → LCA is in right subtree
    - Otherwise, current node is the LCA (split point)

    The split point is where the paths to n1 and n2 diverge.

    Why this works:
    - In BST, values are ordered
    - If node's value is between n1 and n2, it must be their LCA
    - If both values are on same side, LCA must be deeper

Example:
    BST:        20
               /  \
             10    30
            /  \   / \
           5  15 25  35

    LCA(5, 15) = 10   (both in left subtree of 20, split at 10)
    LCA(5, 25) = 20   (5 < 20 < 25, split at root)
    LCA(25, 35) = 30  (both in right subtree of 20, split at 30)

Time Complexity: O(h) where h is height
    - Best: O(log n) for balanced BST
    - Worst: O(n) for skewed BST

Space Complexity:
    - Iterative: O(1)
    - Recursive: O(h)

Flowchart - Iterative:
    ┌─────────────┐
    │   Start     │
    │ curr = root │
    └──────┬──────┘
           │
           ▼
    ┌──────────────────────┐
    │curr.data < n1 AND    │──Yes──┐
    │curr.data < n2?       │       │
    └──────┬───────────────┘       │
           │No                     ▼
           ▼                ┌──────────────┐
    ┌──────────────────────┐│curr = curr.  │
    │curr.data > n1 AND    ││   right      │
    │curr.data > n2?       │└──────┬───────┘
    └──────┬───────────────┘       │
           │No (found LCA!)        │
           ▼                       │
    ┌──────────────┐               │
    │Return curr   │◄──────────────┘
    └──────────────┘

Flowchart - Recursive:
    ┌─────────────┐
    │   Start     │
    └──────┬──────┘
           │
           ▼
    ┌──────────────┐
    │ root == None?│──Yes──►Return None
    └──────┬───────┘
           │No
           ▼
    ┌──────────────────────┐
    │root.data > n1 AND    │──Yes──┐
    │root.data > n2?       │       │
    └──────┬───────────────┘       │
           │No                     ▼
           ▼                ┌──────────────┐
    ┌──────────────────────┐│Return LCA of │
    │root.data < n1 AND    ││ left subtree │
    │root.data < n2?       │└──────────────┘
    └──────┬───────────────┘
           │No (found LCA!)
           ▼
    ┌──────────────┐
    │Return root   │
    └──────────────┘
"""


class Node:
    """
    BST Node class

    Attributes:
        data: The value stored in the node
        left: Reference to left child
        right: Reference to right child
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lca_itr(root, n1, n2):
    """
    Find LCA using iterative approach (RECOMMENDED for interviews)

    This approach is preferred because:
    - No recursion overhead
    - Constant space O(1)
    - Easy to understand and implement
    - Clear logic flow

    Args:
        root: Root of the BST
        n1: First node value
        n2: Second node value

    Returns:
        Node that is the LCA of n1 and n2, or None if not found

    Example:
        >>> root = Node(20)
        >>> root.left = Node(10)
        >>> root.right = Node(30)
        >>> lca = lca_itr(root, 10, 30)
        >>> lca.data
        20

    Time: O(h), Space: O(1)
    """
    curr = root
    ans = None

    while curr is not None:
        # Both values are smaller than current node
        # LCA must be in left subtree
        if curr.data > n1 and curr.data > n2:
            curr = curr.left

        # Both values are greater than current node
        # LCA must be in right subtree
        elif curr.data < n1 and curr.data < n2:
            curr = curr.right

        # We found the split point!
        # Current node is between n1 and n2 (or equal to one)
        else:
            ans = curr
            break

    return ans


def lca_recur(root, n1, n2):
    """
    Find LCA using recursive approach

    Args:
        root: Root of the BST (or current node in recursion)
        n1: First node value
        n2: Second node value

    Returns:
        Node that is the LCA of n1 and n2, or None if not found

    Example:
        >>> root = Node(20)
        >>> root.left = Node(10)
        >>> root.right = Node(30)
        >>> lca = lca_recur(root, 10, 30)
        >>> lca.data
        20

    Time: O(h), Space: O(h)
    """
    # Base case: empty tree
    if root is None:
        return None

    # Both values greater than root → search right
    if root.data < n1 and root.data < n2:
        return lca_recur(root.right, n1, n2)

    # Both values smaller than root → search left
    elif root.data > n1 and root.data > n2:
        return lca_recur(root.left, n1, n2)

    # Split point found: root is the LCA
    else:
        return root


# Example Usage and Testing
if __name__ == "__main__":
    # Create a BST
    #         20
    #        /  \
    #      10    30
    #     /  \   / \
    #    5  15 25  35
    #       /
    #      12

    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)
    root.left.right = Node(15)
    root.right.left = Node(25)
    root.right.right = Node(35)
    root.left.right.left = Node(12)

    print("BST Structure:")
    print("         20")
    print("        /  \\")
    print("      10    30")
    print("     /  \\   / \\")
    print("    5  15 25  35")
    print("       /")
    print("      12")

    # Test cases
    test_cases = [
        (5, 15, 10),    # Both in left subtree
        (5, 25, 20),    # Different subtrees
        (25, 35, 30),   # Both in right subtree
        (12, 15, 15),   # One is ancestor of other
        (5, 35, 20),    # Root is LCA
        (12, 25, 20),   # Across different subtrees
    ]

    print("\nTest Results:")
    print("=" * 50)

    for n1, n2, expected in test_cases:
        # Test iterative version
        lca_it = lca_itr(root, n1, n2)
        result_itr = lca_it.data if lca_it else None

        # Test recursive version
        lca_rec = lca_recur(root, n1, n2)
        result_rec = lca_rec.data if lca_rec else None

        print(f"\nLCA({n1}, {n2}):")
        print(f"  Iterative: {result_itr} (Expected: {expected})")
        print(f"  Recursive: {result_rec} (Expected: {expected})")
        print(f"  {'✓ PASS' if result_itr == expected == result_rec else '✗ FAIL'}")

    # Edge case: single node
    print("\n" + "=" * 50)
    print("Edge Case - Single Node:")
    single = Node(42)
    lca = lca_itr(single, 42, 42)
    print(f"LCA(42, 42) = {lca.data if lca else None}")
