"""
PROBLEM: Find Distance Between Two Nodes of a Binary Tree
============================================================

Given a binary tree and two nodes a and b, find the distance between them.
Distance is the number of edges in the path connecting the two nodes.

Example:
    Input:
            1
          /   \
         2     3
        /     / \
       4     5   6

    Query: distance(4, 5)
    Output: 4
    Path: 4 -> 2 -> 1 -> 3 -> 5 (4 edges)

    Query: distance(2, 3)
    Output: 2
    Path: 2 -> 1 -> 3 (2 edges)

APPROACH & REASONING:
====================
Use LCA (Lowest Common Ancestor) to break problem into two parts:
1. Distance from LCA to node a
2. Distance from LCA to node b
Total distance = dist(LCA, a) + dist(LCA, b)

WHY LCA?
- Path between any two nodes MUST go through their LCA
- Can compute distances separately from LCA
- Simpler than finding direct path

KEY INSIGHT:
- Distance(a, b) = Distance(LCA, a) + Distance(LCA, b)
- LCA is the "meeting point" of paths from a and b to root
- We count edges, not nodes: so subtract 2 at the end

ALGORITHM STEPS:
1. Find LCA of nodes a and b
2. Find distance from LCA to node a
3. Find distance from LCA to node b
4. Return dist(LCA,a) + dist(LCA,b) - 2

Why subtract 2?
- dist() returns number of nodes (includes both endpoints)
- We want number of edges
- Each path includes LCA, so we count it twice
- Edges = (nodes_to_a - 1) + (nodes_to_b - 1) = nodes_to_a + nodes_to_b - 2

FLOWCHART:
    [Find LCA] → [Dist to a] → [Dist to b] → [Sum - 2] → [Return]

TIME COMPLEXITY: O(N) - LCA + 2 distance searches
SPACE COMPLEXITY: O(H) - recursion depth

INTERVIEW TIPS:
- Explain why we use LCA
- Discuss the -2 adjustment (edges vs nodes)
- Mention alternative: DFS from one node to other
- Common follow-up: Distance in BST (can optimize)
"""

def lca(root, n1, n2):
    """
    Finds Lowest Common Ancestor of n1 and n2.

    Args:
        root: Root of binary tree
        n1: First node value
        n2: Second node value

    Returns:
        Node: LCA of n1 and n2

    Time: O(N), Space: O(H)
    """
    # BASE CASE: Empty tree
    if root is None:
        return None

    # BASE CASE: Found one of target nodes
    if root.data == n1 or root.data == n2:
        return root

    # Search in left and right subtrees
    l = lca(root.left, n1, n2)
    r = lca(root.right, n1, n2)

    # Both found in different subtrees → current is LCA
    if l != None and r != None:
        return root

    # Propagate non-null result
    if l:
        return l
    else:
        return r

def dist(root, a):
    """
    Finds distance (number of nodes) from root to node with value a.

    Args:
        root: Root of subtree
        a: Target node value

    Returns:
        int: Number of nodes in path (0 if not found, 1+ if found)

    Time: O(N), Space: O(H)
    """
    # BASE CASE: Empty node
    if root is None:
        return 0

    # BASE CASE: Found target node
    # Return 1 to indicate this node is in the path
    if root.data == a:
        return 1

    # STEP 1: Search in left subtree
    x = dist(root.left, a)

    # STEP 2: Search in right subtree
    y = dist(root.right, a)

    # STEP 3: If not found in either subtree, return 0
    # If found (x or y is non-zero), return that + 1 (for current node)
    if not x and not y:
        return 0

    # Found in one subtree: add current node to path length
    return x + y + 1

def findDist(root, a, b):
    """
    Finds distance (number of edges) between nodes a and b.

    Args:
        root: Root of binary tree
        a: First node value
        b: Second node value

    Returns:
        int: Number of edges in path between a and b

    Time: O(N), Space: O(H)
    """
    # STEP 1: Find LCA of a and b
    # This is the meeting point of paths from a and b
    lca_node = lca(root, a, b)

    # STEP 2: Find distance (in nodes) from LCA to a
    dist1 = dist(lca_node, a)

    # STEP 3: Find distance (in nodes) from LCA to b
    dist2 = dist(lca_node, b)

    # STEP 4: Total edges = (nodes to a) + (nodes to b) - 2
    # Why -2?
    # - Each distance includes the LCA node
    # - We count LCA twice, so subtract 2
    # - Also converts from node count to edge count
    return dist1 + dist2 - 2
