"""
PROBLEM: Sum of the Longest Bloodline (Root to Leaf Path) of a Tree
======================================================================

Given a binary tree, find the sum of the nodes on the longest path from
root to leaf. If multiple paths have the same maximum length, return the
path with maximum sum.

Example:
    Input:
           1
         /   \
        2     3
       / \
      4   5

    Paths:
        1 -> 2 -> 4 (length=3, sum=7)
        1 -> 2 -> 5 (length=3, sum=8)
        1 -> 3      (length=2, sum=4)

    Output: 8 (longest path 1->2->5 with max sum)

APPROACH & REASONING:
====================
Use recursion to track both path length and sum simultaneously.

WHY THIS APPROACH?
- Need to compare paths by length first, then by sum
- Recursion naturally tracks path from leaf to root
- Return [level, sum] pair for comparison

KEY INSIGHT:
- Return [depth, sum] from each subtree
- Compare left and right: prefer longer path
- If equal length: prefer path with larger sum

ALGORITHM STEPS:
1. If null → return [0, 0]
2. Get [level, sum] from left and right subtrees
3. Compare:
   - If left level > right level → choose left
   - If right level > left level → choose right
   - If equal → choose max sum
4. Return [level+1, sum+root.data]

FLOWCHART:
    [Get left result] → [Get right result] → [Compare levels] → [Choose best]
                                                     ↓
                                      [Return [level+1, sum+root]]

TIME COMPLEXITY: O(N) - visit each node once
SPACE COMPLEXITY: O(H) - recursion depth

INTERVIEW TIPS:
- Explain why we return both level and sum
- Discuss tie-breaking by sum
- Mention similarity to tree diameter problem
"""

class Solution:
    def solve(self, root):
        """
        Finds longest path and its sum from this subtree.

        Args:
            root: Root of current subtree

        Returns:
            [level, sum]: Level is path length, sum is path sum

        Time: O(N), Space: O(H)
        """
        # BASE CASE: Null node contributes nothing
        if root is None:
            return [0, 0]  # [level, sum]

        # STEP 1: Get result from left subtree (postorder)
        a = self.solve(root.left)

        # STEP 2: Get result from right subtree (postorder)
        b = self.solve(root.right)

        # STEP 3: Compare paths and choose best
        # CASE 1: Left path is longer → take left
        if a[0] > b[0]:
            return [a[0] + 1, a[1] + root.data]

        # CASE 2: Right path is longer → take right
        elif a[0] < b[0]:
            return [b[0] + 1, b[1] + root.data]

        # CASE 3: Equal length → take path with max sum
        else:
            return [a[0] + 1, max(a[1], b[1]) + root.data]

    def sumOfLongRootToLeafPath(self, root):
        """
        Main function to find sum of longest root-to-leaf path.

        Args:
            root: Root of binary tree

        Returns:
            int: Sum of longest path (max sum if tie)

        Time: O(N), Space: O(H)
        """
        # Get [level, sum] for longest path
        ans = self.solve(root)

        # Return the sum (index 1)
        return ans[1]
