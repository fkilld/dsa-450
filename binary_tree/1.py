"""
PROBLEM: Reverse Level Order Traversal of Binary Tree
====================================================

Given a binary tree, return the reverse level order traversal.
This means we visit nodes from bottom to top, and at each level from left to right.

Example:
    Input Tree:
           1
         /   \
        2     3
       / \
      4   5

    Output: [4, 5, 2, 3, 1]
    Explanation:
        Level 2: [4, 5]
        Level 1: [2, 3]
        Level 0: [1]
        Reverse order: [4, 5, 2, 3, 1]

APPROACH & REASONING:
====================
This problem is a variation of standard level order traversal with a twist.
We need the output in reverse order (bottom-up instead of top-down).

KEY INSIGHT:
Instead of appending values to the end of result, we insert them at the beginning.
This reverses the order naturally as we process from top to bottom.

TWO APPROACHES:
1. Do normal level order, then reverse the result (2 passes)
2. Use deque.appendleft() to build result in reverse (1 pass) ✓ Better

IMPORTANT DETAIL:
Since we're building the result in reverse, we need to process RIGHT child
before LEFT child. This ensures that when we insert at the beginning,
left nodes appear before right nodes in the final result.

ALGORITHM STEPS:
1. Initialize a queue for BFS traversal
2. Initialize a deque for result (allows efficient insertion at front)
3. Process nodes level by level using BFS
4. For each node, insert RIGHT child first, then LEFT child
5. Insert current node's value at the BEGINNING of result
6. Return the reversed level order

FLOWCHART:
         START
           |
           v
    [Initialize BFS queue with root]
           |
           v
    [Initialize result deque]
           |
           v
    <Is queue empty?>----YES----> [Return result]
           |
          NO
           |
           v
    [Dequeue front node]
           |
           v
    <Is node NULL?>----YES----> [Continue loop]
           |
          NO
           |
           v
    [Insert node.data at FRONT of result]
           |
           v
    [Enqueue RIGHT child first (if exists)]
           |
           v
    [Enqueue LEFT child second (if exists)]
           |
           v
    [Go back to queue check]

WHY RIGHT BEFORE LEFT?
    Processing right before left ensures that when we reverse,
    left appears before right in the final output.

    Example: At level with nodes [2, 3]
    - We process 2 first, add right(none), left(4,5)
    - We process 3, no children
    - Result building: insert 2 -> [2], insert 3 -> [3, 2]
    - When processing children: insert 5 -> [5, 3, 2], insert 4 -> [4, 5, 3, 2]
    - Wait, this gives wrong order... Actually we need to reconsider.

CORRECTED UNDERSTANDING:
    We insert at the front (appendleft), and we process right before left
    in the queue, so they get inserted in the correct left-to-right order
    when reversed.

TIME COMPLEXITY: O(N) where N is the number of nodes
    - Visit each node exactly once
    - appendleft() on deque is O(1)

SPACE COMPLEXITY: O(N)
    - Queue can hold up to N/2 nodes (last level of complete tree)
    - Result deque holds all N node values
    - Overall: O(N)

INTERVIEW TIPS:
- Explain the difference from normal level order
- Mention why we use appendleft instead of append + reverse
- Discuss the importance of processing right before left
- Be ready to implement using stack instead of deque
"""

from collections import deque

def reverseLevelOrder(root):
    """
    Performs reverse level order traversal on a binary tree.

    Args:
        root: Root node of the binary tree

    Returns:
        Deque containing node values in reverse level order
    """
    # STEP 1: Initialize queue for BFS traversal
    q = deque()
    q.append(root)

    # STEP 2: Initialize result deque (allows O(1) insertion at front)
    ans = deque()

    # STEP 3: Process all nodes using BFS
    while len(q) != 0:
        # STEP 4: Dequeue the front node
        node = q.popleft()

        # STEP 5: Process only valid nodes
        if node != None:
            # STEP 6: Insert current node's value at the BEGINNING
            # This reverses the level order naturally
            ans.appendleft(node.data)

            # STEP 7: Add RIGHT child first to the queue
            # When reversed, this ensures left appears before right
            if node.right != None:
                q.append(node.right)

            # STEP 8: Add LEFT child second to the queue
            if node.left != None:
                q.append(node.left)

    # STEP 9: Return the reverse level order traversal
    return ans