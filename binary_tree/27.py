"""
PROBLEM: Find Largest Subtree Sum in a Binary Tree
====================================================

Given a binary tree, find the maximum sum among all subtrees.
A subtree's sum includes the root node plus all descendants.

Example:
    Input:
            1
          /   \
         -2    3
        / \   / \
       4   5 -6  2

    Subtree sums:
        - Subtree at 4: sum = 4
        - Subtree at 5: sum = 5
        - Subtree at -2: sum = -2 + 4 + 5 = 7
        - Subtree at -6: sum = -6
        - Subtree at 2: sum = 2
        - Subtree at 3: sum = 3 + (-6) + 2 = -1
        - Entire tree: sum = 1 + 7 + (-1) = 7

    Output: 7 (maximum sum)

APPROACH & REASONING:
====================
Use postorder traversal to compute subtree sums bottom-up.

WHY POSTORDER?
- Need child sums before computing parent sum
- Natural bottom-up computation
- Can track maximum while computing sums

KEY INSIGHT:
- Each subtree's sum = node.data + left_sum + right_sum
- Track global maximum during traversal
- Return sum to parent for its calculation

ALGORITHM STEPS:
1. If null → return 0
2. Recursively get left subtree sum
3. Recursively get right subtree sum
4. Current sum = node + left + right
5. Update global maximum
6. Return current sum to parent

FLOWCHART:
    [Get left sum] → [Get right sum] → [Calc sum] → [Update max] → [Return sum]

TIME COMPLEXITY: O(N) - visit each node once
SPACE COMPLEXITY: O(H) - recursion depth

INTERVIEW TIPS:
- Explain postorder necessity
- Discuss global maximum tracking
- Mention handling negative values
- Compare with maximum path sum problem
"""

class newNode:
    def __init__(self, data):
        """Node for binary tree."""
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def solve(self, root):
        """
        Computes subtree sum and tracks maximum.

        Args:
            root: Root of current subtree

        Returns:
            int: Sum of this entire subtree

        Side Effects:
            Updates self.ans with maximum sum found

        Time: O(N), Space: O(H)
        """
        # BASE CASE: Null node contributes 0
        if root is None:
            return 0

        # STEP 1: Compute current subtree sum (postorder)
        # Sum = current node + left subtree + right subtree
        val = root.data + self.solve(root.left) + self.solve(root.right)

        # STEP 2: Update global maximum if current sum is larger
        self.ans = max(val, self.ans)

        # STEP 3: Return sum to parent for its calculation
        return val

    def largest_sum(self, root):
        """
        Finds the maximum sum among all subtrees.

        Args:
            root: Root of binary tree

        Returns:
            int: Maximum subtree sum

        Time: O(N), Space: O(H)
        """
        # EDGE CASE: Empty tree
        if root is None:
            return 0

        # Initialize maximum to negative infinity (handle negative sums)
        self.ans = float('-inf')

        # Compute all subtree sums and track maximum
        self.solve(root)

        return self.ans


# Driver code
'''
            1
          /   \
         /      \
        -2       3
        / \     / \
        / \     / \
       4   5  -6   2
'''
root = newNode(1)
root.left = newNode(-2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(-6)
root.right.right = newNode(2)

solution = Solution()
print(solution.largest_sum(root))  # Expected: 7
