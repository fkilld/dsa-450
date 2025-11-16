"""
PROBLEM: Check if Two Trees are Isomorphic
============================================

Two trees are isomorphic if one can be obtained from the other by:
- Swapping left and right children of nodes
- The structure can differ but node values at corresponding positions must match

Example 1 (Isomorphic):
    Tree 1:          Tree 2:
         1               1
       /   \           /   \
      2     3         3     2
     / \              \   /
    4   5              5 4

    Output: True
    (Tree2 obtained by flipping children at nodes 1 and 2)

Example 2 (Not Isomorphic):
    Tree 1:          Tree 2:
         1               1
       /   \           /   \
      2     3         3     5

    Output: False
    (Node values don't match: 2 vs 5)

APPROACH & REASONING:
====================
Recursively check two cases:
1. No flip: left1 matches left2, right1 matches right2
2. Flip: left1 matches right2, right1 matches left2

WHY THIS WORKS?
- At each node, children can either match directly or be swapped
- Recursively verify both possibilities
- If either case holds, trees are isomorphic

KEY INSIGHT:
- Trees are isomorphic if:
  * Both empty, OR
  * Same root value AND
    (normal match OR flipped match)
- Short-circuit evaluation avoids unnecessary checks

ALGORITHM STEPS:
1. If both null → isomorphic
2. If one null → not isomorphic
3. If root values differ → not isomorphic
4. Check two cases:
   a. left1 ≅ left2 AND right1 ≅ right2
   b. left1 ≅ right2 AND right1 ≅ left2
5. Return true if either case holds

FLOWCHART:
    [Both null?] → YES → [Return True]
         NO ↓
    [One null?] → YES → [Return False]
         NO ↓
    [Values equal?] → NO → [Return False]
         YES ↓
    [Check normal OR flipped] → [Return result]

TIME COMPLEXITY: O(min(N1, N2))
    - Visit nodes until mismatch or smaller tree exhausted

SPACE COMPLEXITY: O(H)
    - Recursion depth equals height
    - O(min(H1, H2))

INTERVIEW TIPS:
- Draw examples showing both cases
- Explain why we check both orientations
- Mention this is different from "identical" trees
- Common follow-up: Count number of ways to make isomorphic
- Discuss optimization: can memoize subtree comparisons
"""

class Solution:
    def isIsomorphic(self, root1, root2):
        """
        Checks if two binary trees are isomorphic.

        Trees are isomorphic if one can be obtained from other
        by flipping children at any nodes.

        Args:
            root1: Root of first tree
            root2: Root of second tree

        Returns:
            bool: True if isomorphic, False otherwise

        Time: O(min(N1, N2)), Space: O(min(H1, H2))
        """
        # BASE CASE 1: Both trees empty → isomorphic
        if root1 is None and root2 is None:
            return True

        # BASE CASE 2: One tree empty, other not → not isomorphic
        # Trees must have same number of nodes
        if root1 is None or root2 is None:
            return False

        # BASE CASE 3: Root values must match
        # If roots differ, trees can't be isomorphic
        if root1.data != root2.data:
            return False

        # RECURSIVE CASE: Check two possible configurations
        # Configuration 1: No flip - children match directly
        # left1 with left2, right1 with right2
        l1 = self.isIsomorphic(root1.left, root2.left) and \
             self.isIsomorphic(root1.right, root2.right)

        # Configuration 2: Flip - children swapped
        # left1 with right2, right1 with left2
        l2 = self.isIsomorphic(root1.left, root2.right) and \
             self.isIsomorphic(root1.right, root2.left)

        # STEP 4: Trees are isomorphic if EITHER configuration works
        # OR operator means we accept either matching pattern
        return l1 or l2
