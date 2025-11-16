"""
PROBLEM: Convert Binary Tree to Doubly Linked List (DLL)
==========================================================

Given a binary tree, convert it to a doubly linked list such that:
- The DLL should be in-order (left -> root -> right)
- left pointer of tree becomes prev pointer of DLL
- right pointer of tree becomes next pointer of DLL

Example:
    Input Tree:
           10
         /    \
        12    15
       /  \   /
      25  30 36

    Inorder: 25, 12, 30, 10, 36, 15
    DLL: 25 <-> 12 <-> 30 <-> 10 <-> 36 <-> 15

APPROACH & REASONING:
====================
1. Get inorder traversal (gives sorted order for BST)
2. Create DLL nodes from inorder traversal

WHY INORDER?
- Inorder traversal of BST gives sorted order
- Natural left-to-right ordering
- Matches DLL structure requirements

KEY INSIGHT:
- Inorder = sorted order for BST
- Build DLL by linking consecutive inorder nodes

ALGORITHM STEPS:
1. Perform iterative inorder traversal to get node sequence
2. Create DLL nodes from traversal
3. Link nodes bidirectionally

FLOWCHART:
    START → [Inorder Traversal] → [Create DLL Nodes] → [Link Nodes] → END

TIME COMPLEXITY: O(N) - visit each node once
SPACE COMPLEXITY: O(N) - store inorder array

INTERVIEW TIPS:
- Mention iterative inorder using stack
- Discuss in-place conversion alternative
- Compare time/space tradeoffs
"""

class dll:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

def bToDLL(root):
    """
    Converts binary tree to doubly linked list using inorder traversal.

    Args:
        root: Root of binary tree

    Returns:
        Head of doubly linked list

    Time: O(N), Space: O(N)
    """
    # STEP 1: Get inorder traversal iteratively
    inorder = []
    stack = []

    # STEP 2: Iterative inorder traversal
    curr = root
    while curr or stack:
        # Go to leftmost node
        if curr != None:
            stack.append(curr)
            curr = curr.left
        else:
            # Process node
            curr = stack.pop()
            inorder.append(curr.data)
            curr = curr.right

    # STEP 3: Create DLL from inorder
    head = dll(inorder[0])
    curr = head

    # STEP 4: Link nodes bidirectionally
    for i in range(1, len(inorder)):
        temp = dll(inorder[i])
        curr.right = temp  # Next link
        temp.left = curr   # Prev link
        curr = temp

    return head
