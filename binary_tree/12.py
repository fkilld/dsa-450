"""
PROBLEM: ZigZag (Spiral) Tree Traversal
========================================

Given a binary tree, perform zigzag level order traversal.
Zigzag traversal alternates direction at each level:
- Level 0: Left to Right
- Level 1: Right to Left
- Level 2: Left to Right
- And so on...

Example 1:
    Input Tree:
               1
             /   \
            2     3
           / \   / \
          4   5 6   7

    Output: [1, 3, 2, 4, 5, 6, 7]
    Explanation:
        Level 0 (L->R): 1
        Level 1 (R->L): 3, 2
        Level 2 (L->R): 4, 5, 6, 7

Example 2:
    Input Tree:
           1
         /   \
        2     3

    Output: [1, 3, 2]

APPROACH & REASONING:
====================
This is a modified BFS where we need to control the order of children insertion.

WHY THIS APPROACH (TWO DEQUES)?
- Use two deques: curr_level and next_level
- Use a boolean flag to track direction
- When going L->R: Add children normally (left first, then right) to FRONT of next_level
- When going R->L: Add children reversed (right first, then left) to FRONT of next_level
- Swap deques when current level is exhausted

KEY INSIGHT:
- appendleft() is the trick - it reverses the natural order
- When reverse=True (L->R level):
  * We add left child first to front, then right child to front
  * Result: right child ends up at front, processed first next iteration (R->L)
- When reverse=False (R->L level):
  * We add right child first to front, then left child to front
  * Result: left child ends up at front, processed first next iteration (L->R)

ALGORITHM STEPS:
1. Handle edge case: if root is None, return empty list
2. Initialize:
   - curr_level deque with root
   - empty next_level deque
   - reverse flag = True (start with L->R, need children R->L)
   - empty result list
3. While curr_level is not empty:
   a. Pop node from curr_level
   b. Add node data to result
   c. If reverse (current level L->R, next level should be R->L):
      - Add left child first (to front of next_level)
      - Then add right child (to front of next_level)
      This makes right at front, so next level processes R->L
   d. Else (current level R->L, next level should be L->R):
      - Add right child first (to front of next_level)
      - Then add left child (to front of next_level)
      This makes left at front, so next level processes L->R
   e. When curr_level empty: toggle reverse, swap deques
4. Return result

FLOWCHART:
         START
           |
           v
    <Is root None?>----YES----> [Return []]
           |
          NO
           |
           v
    [Initialize curr_level=[root], next_level=[]]
           |
           v
    [reverse=True, ans=[]]
           |
           v
    <Is curr_level empty?>----YES----> [Return ans]
           |
          NO
           |
           v
    [Pop node from curr_level]
           |
           v
    [Add node.data to ans]
           |
           v
    <Is reverse True?>----YES----> [appendleft left, then right]
           |                              |
          NO                              |
           |<-----------------------------
           v
    [appendleft right, then left]
           |
           v
    <Is curr_level empty?>----YES----> [Toggle reverse, swap deques]
           |                                  |
          NO                                  |
           |<---------------------------------
           v
    [Go back to curr_level check]

TIME COMPLEXITY: O(N) where N is the number of nodes
    - Visit each node exactly once
    - appendleft is O(1) for deque

SPACE COMPLEXITY: O(W) where W is the maximum width
    - Two deques hold at most all nodes at widest level
    - In worst case: O(N)

INTERVIEW TIPS:
- Explain the two-deque approach and why it works
- Emphasize the appendleft trick for reversing
- Mention alternative: Single queue with level size tracking + reverse
- Discuss the reverse flag - why it starts True
- Common follow-up: Implement with single queue
- Highlight that this is also called "Spiral Order Traversal"
"""

from collections import deque

def zigZagTraversal(root):
    """
    Performs zigzag (spiral) level order traversal of binary tree.

    Args:
        root: Root node of the binary tree

    Returns:
        List containing node values in zigzag order

    Time Complexity: O(N) - visit each node once
    Space Complexity: O(W) - two deques hold at most W nodes
    """
    # EDGE CASE: If tree is empty, return empty list
    if root is None:
        return []

    # STEP 1: Initialize current level deque with root
    # This holds nodes at current level being processed
    curr_level = deque([root])

    # STEP 2: Initialize next level deque (empty initially)
    # This will hold nodes for the next level
    next_level = deque([])

    # STEP 3: Initialize reverse flag
    # True means: current level is L->R, so prepare next level for R->L
    # We start with True because level 0 goes L->R
    reverse = True

    # STEP 4: Initialize result list
    ans = []

    # STEP 5: Process all levels
    while len(curr_level) != 0:
        # STEP 6: Pop node from current level (left end, FIFO)
        node = curr_level.popleft()

        # STEP 7: Add current node's data to result
        ans.append(node.data)

        # STEP 8: Add children to next_level based on current direction
        if reverse:
            # Current level is L->R, next level should be R->L
            # Add children with appendleft to reverse their order
            # Add LEFT first (to front), then RIGHT (to front)
            # Result: RIGHT ends up at front, will be processed first (R->L)
            if node.left != None:
                next_level.appendleft(node.left)
            if node.right != None:
                next_level.appendleft(node.right)
        else:
            # Current level is R->L, next level should be L->R
            # Add children with appendleft to reverse their order
            # Add RIGHT first (to front), then LEFT (to front)
            # Result: LEFT ends up at front, will be processed first (L->R)
            if node.right != None:
                next_level.appendleft(node.right)
            if node.left != None:
                next_level.appendleft(node.left)

        # STEP 9: When current level is exhausted, move to next level
        if len(curr_level) == 0:
            # STEP 10: Toggle direction for next level
            reverse = not reverse

            # STEP 11: Swap deques - next_level becomes curr_level
            # Python's elegant tuple swap
            curr_level, next_level = next_level, curr_level

    # STEP 12: Return complete zigzag traversal
    return ans
