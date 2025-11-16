"""
PROBLEM: Print All K-Sum Paths in a Binary Tree
=================================================

Given a binary tree and a number k, print all paths where the sum equals k.
A path can start and end at any node (doesn't need to be root-to-leaf).

Example:
    Input: k = 5
    Tree:
            1
          /   \
         3     -1
        / \     \
       2   1     4
             \   / \
              1 1   2

    K-Sum Paths (sum = 5):
        - [1, 3, 1]
        - [3, 2]
        - [1, 3, 1] (different path)
        - [-1, 4, 2]

APPROACH & REASONING:
====================
Use backtracking to track current path and check all subpaths for sum = k.

WHY BACKTRACKING?
- Need to explore all possible paths
- Path array tracks current path from root
- Can check all suffixes of current path

KEY INSIGHT:
- For each node, check all subpaths ending at this node
- Path[i..current] is a subpath
- Check sum of each subpath
- Use backtracking to restore state

ALGORITHM STEPS:
1. Add current node to path
2. Recursively explore left and right subtrees
3. For each node, check all subpaths ending here:
   - Iterate backwards through path
   - Calculate running sum
   - If sum == k, found a path!
4. Remove current node from path (backtrack)

FLOWCHART:
    [Add to path] → [Recurse children] → [Check subpaths] → [Backtrack]

TIME COMPLEXITY: O(N * H) where H is height
    - Visit each node once: O(N)
    - At each node, check path of length H: O(H)

SPACE COMPLEXITY: O(H) - path array + recursion

INTERVIEW TIPS:
- Explain why we check all subpaths (not just root-to-current)
- Discuss backtracking importance
- Mention path sum variations
- Compare with root-to-leaf path sum
"""

class newNode:
    def __init__(self, data) -> None:
        """Node for binary tree."""
        self.data = data
        self.left = None
        self.right = None


def k_sum_path(root, path, k):
    """
    Finds all paths with sum = k using backtracking.

    Args:
        root: Current node
        path: List tracking current path from root
        k: Target sum

    Side Effects:
        Appends valid paths to global variable 'ans'

    Time: O(N * H), Space: O(H)
    """
    # BASE CASE: Null node
    if root is None:
        return

    # STEP 1: Add current node to path (backtracking - add)
    path.append(root.data)

    # STEP 2: Recursively explore left subtree
    k_sum_path(root.left, path, k)

    # STEP 3: Recursively explore right subtree
    k_sum_path(root.right, path, k)

    # STEP 4: Check all subpaths ending at current node
    # Iterate backwards through path to find all suffixes
    f = 0  # Running sum
    for j in range(len(path) - 1, -1, -1):
        f += path[j]  # Add to sum

        # STEP 5: If sum equals k, found a valid path!
        if f == k:
            global ans
            ans.append(path[j:])  # Add path from index j to end

    # STEP 6: Backtrack - remove current node from path
    path.pop()


# Driver code
root = newNode(1)
root.left = newNode(3)
root.left.left = newNode(2)
root.left.right = newNode(1)
root.left.right.left = newNode(1)
root.right = newNode(-1)
root.right.left = newNode(4)
root.right.left.left = newNode(1)
root.right.left.right = newNode(2)
root.right.right = newNode(5)
root.right.right.right = newNode(2)

k = 5
ans = []  # Global list to store results
path = []  # Current path being explored

k_sum_path(root, path, k)

# Print all k-sum paths
print(*ans)
