"""
PROBLEM: Minimum Swaps to Convert Binary Tree to BST
======================================================

Given an array representation of a binary tree, find minimum swaps
needed to convert it to a Binary Search Tree (BST).

Array representation: arr[i] has children at arr[2*i+1] and arr[2*i+2]

Example:
    Input: arr = [5, 6, 7, 8, 9, 10, 11]
    Tree:
           5
         /   \
        6     7
       / \   / \
      8   9 10 11

    Inorder: 8, 6, 9, 5, 10, 7, 11 (not sorted)
    To make BST, need minimum swaps to sort inorder

APPROACH & REASONING:
====================
KEY INSIGHT:
- Inorder traversal of BST is SORTED
- Problem reduces to: minimum swaps to sort array
- Get inorder of current tree, then count swaps to sort it

ALGORITHM:
1. Get inorder traversal of tree
2. Find minimum swaps to sort this array
3. That's the answer!

MINIMUM SWAPS TO SORT ARRAY:
1. Create (value, index) pairs
2. Sort by value
3. Use cycle detection:
   - Each swap fixes one element
   - Count swaps in each cycle
   - Answer = Σ(cycle_size - 1)

FLOWCHART:
    [Get Inorder] → [Min Swaps to Sort] → [Return count]

TIME COMPLEXITY: O(N log N) - sorting dominates
SPACE COMPLEXITY: O(N) - arrays

INTERVIEW TIPS:
- Explain why inorder of BST is sorted
- Show how cycle detection works
- Draw example of swapping cycles
- Mention this is classic array problem adapted to trees
"""

# Inorder traversal for array-based tree
def inorder(arr, n, index):
    """
    Gets inorder traversal of binary tree stored as array.

    Args:
        arr: Array representation of tree
        n: Size of array
        index: Current node index

    Side Effects:
        Appends to global variable v
    """
    # BASE CASE: Index out of bounds
    if index >= n:
        return

    # STEP 1: Traverse left subtree (2*index + 1)
    inorder(arr, n, 2*index + 1)

    # STEP 2: Process current node
    global v
    v.append(arr[index])

    # STEP 3: Traverse right subtree (2*index + 2)
    inorder(arr, n, 2*index + 2)

def minSwaps(v):
    """
    Finds minimum swaps needed to sort array using cycle detection.

    Args:
        v: Array to sort

    Returns:
        Minimum number of swaps needed

    Time: O(N log N), Space: O(N)
    """
    # STEP 1: Create (value, original_index) pairs
    arrpos = []
    n = len(v)
    for i in range(n):
        arrpos.append([v[i], i])

    # STEP 2: Sort by value (correct positions)
    arrpos = sorted(arrpos)

    # STEP 3: Track visited elements for cycle detection
    vis = [False for i in range(n)]
    ans = 0

    # STEP 4: Find cycles and count swaps
    for i in range(n):
        # Skip if already visited or already in correct position
        if vis[i] or arrpos[i][1] == i:
            continue

        # STEP 5: Trace the cycle starting from i
        j = i
        cycle_size = 0

        while not vis[j]:
            vis[j] = True
            j = arrpos[j][1]  # Next element in cycle
            cycle_size += 1

        # STEP 6: Add swaps for this cycle
        # Cycle of size k needs (k-1) swaps
        if cycle_size != 0:
            ans += (cycle_size - 1)

    return ans

# LOGIC:
# The inorder traversal of a BST is sorted
# So: get inorder of current tree, then find min swaps to sort it

# Driver code
v = []
# a = [5, 6, 7, 8, 9, 10, 11]
a = [1, 2, 3]
n = len(a)
inorder(a, n, 0)
print(minSwaps(v))
