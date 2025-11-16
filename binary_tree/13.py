"""
PROBLEM: Check if Binary Tree is Balanced
===========================================

Given a binary tree, determine if it is height-balanced.
A binary tree is height-balanced if for every node:
|height(left subtree) - height(right subtree)| <= 1

Example 1 (Balanced):
    Input Tree:
           1
         /   \
        2     3
       / \
      4   5

    Output: True
    Explanation:
        Node 1: |height(left=2) - height(right=1)| = 1 ✓
        Node 2: |height(left=1) - height(right=1)| = 0 ✓
        Node 3: |height(left=0) - height(right=0)| = 0 ✓

Example 2 (Not Balanced):
    Input Tree:
           1
          /
         2
        /
       3

    Output: False
    Explanation:
        Node 1: |height(left=2) - height(right=0)| = 2 > 1 ✗

APPROACH & REASONING:
====================
We need to check balance at EVERY node while computing heights.

WHY THIS APPROACH?
- Check balance condition at each node during height calculation
- Use a global flag to track if any violation is found
- Short-circuit: Once imbalance is found, no need to continue checking
- Compute heights bottom-up (postorder style)

KEY INSIGHT:
- Height of tree = max(left height, right height) + 1
- Balance check: |left height - right height| <= 1
- Must check ALL nodes, not just root
- Use global flag to propagate failure up the tree

ALTERNATIVE APPROACH (Not implemented):
- Return -1 for unbalanced subtree instead of using global variable
- More elegant but less intuitive

ALGORITHM STEPS:
1. Initialize global flag f = True (assume balanced)
2. Define solve(root) to compute height:
   a. If root is None, return 0
   b. Recursively get left height
   c. Recursively get right height
   d. If |lh - rh| > 1, set global flag f = False
   e. Return max(lh, rh) + 1
3. Call solve(root) and return global flag

FLOWCHART:
         START
           |
           v
    [f = True (global)]
           |
           v
    [Call solve(root)]
           |
           v
    [Return f]

    solve(root):
         START
           |
           v
    <Is root None?>----YES----> [Return 0]
           |
          NO
           |
           v
    [lh = solve(root.left)]
           |
           v
    [rh = solve(root.right)]
           |
           v
    <Is |lh - rh| > 1?>----YES----> [Set f = False]
           |                               |
          NO                               |
           |<------------------------------
           v
    [Return max(lh, rh) + 1]

TIME COMPLEXITY: O(N) where N is the number of nodes
    - Visit each node exactly once
    - Even with early termination, worst case is O(N)

SPACE COMPLEXITY: O(H) where H is height
    - Recursion call stack depth equals height
    - In worst case (skewed tree): O(N)
    - In best case (balanced tree): O(log N)

INTERVIEW TIPS:
- Explain what "balanced" means clearly (height difference <= 1 at ALL nodes)
- Mention this checks EVERY node, not just root
- Discuss the global flag approach vs returning -1 for unbalanced
- Highlight that we compute heights during balance check (efficiency)
- Common follow-up: Return height for balanced, -1 for unbalanced
- Mention AVL trees use this property for self-balancing
"""

# Global variable to track if tree is balanced
f = True

def solve(root):
    """
    Computes height of tree and checks if balanced.

    Args:
        root: Root node of the binary tree

    Returns:
        int: Height of the tree rooted at this node

    Side Effects:
        Sets global variable f to False if tree is unbalanced

    Time Complexity: O(N) - visit each node once
    Space Complexity: O(H) - recursion depth
    """
    # BASE CASE: Empty node has height 0
    if root is None:
        return 0

    # STEP 1: Recursively compute height of left subtree
    # This will check balance of entire left subtree
    lh = solve(root.left)

    # STEP 2: Recursively compute height of right subtree
    # This will check balance of entire right subtree
    rh = solve(root.right)

    # STEP 3: Check balance condition at current node
    # Balance requires: |left height - right height| <= 1
    # If violated, mark entire tree as unbalanced
    if abs(lh - rh) > 1:
        global f
        f = False

    # STEP 4: Return height of current subtree
    # Height = max of children heights + 1 (for current node)
    return max(lh, rh) + 1

def isBalanced(root):
    """
    Checks if a binary tree is height-balanced.

    A tree is balanced if at every node:
    |height(left) - height(right)| <= 1

    Args:
        root: Root node of the binary tree

    Returns:
        bool: True if tree is balanced, False otherwise

    Time Complexity: O(N) - check all nodes
    Space Complexity: O(H) - recursion depth
    """
    # STEP 1: Reset global flag to True (assume balanced)
    global f
    f = True

    # STEP 2: Compute heights and check balance at all nodes
    # solve() will set f to False if any imbalance is found
    solve(root)

    # STEP 3: Return the final balance status
    return f
