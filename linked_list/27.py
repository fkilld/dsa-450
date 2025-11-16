"""
================================================================================
PROBLEM: Flattening a Linked List
================================================================================

DESCRIPTION:
Given a Linked List of size N, where every node represents a sub-linked-list
and contains two pointers:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.

Each of the sub-linked-lists is in sorted order. Flatten the Link List such
that all the nodes appear in a single level while maintaining the sorted order.

Note: The flattened list should use the bottom pointer instead of the next
pointer.

Input:
    5 -> 10 -> 19 -> 28
    |    |     |     |
    7    20    22    35
    |          |     |
    8          50    40
    |                |
    30               45

Output: 5 -> 7 -> 8 -> 10 -> 19 -> 20 -> 22 -> 28 -> 30 -> 35 -> 40 -> 45 -> 50

Explanation: All nodes are connected using bottom pointer in sorted order.

================================================================================
APPROACH & REASONING:
================================================================================

OPTIMAL APPROACH: Recursive Merge (Similar to Merge Sort)

Key Insight:
- This problem is similar to merging K sorted lists
- We can recursively merge two sorted sub-lists at a time
- Each sub-list (connected by bottom pointer) is already sorted
- Use merge operation similar to merging two sorted linked lists

Algorithm Steps:
1. Base case: If root is NULL or root.next is NULL, return root
2. Recursively flatten the list starting from root.next
3. Merge the current list (root) with the flattened result
4. Return the merged list

Merge Operation:
1. Compare the data of two lists' heads
2. Choose the smaller one as the result
3. Recursively merge the chosen node's bottom with the other list
4. Set the next pointer to NULL (we only use bottom pointers in result)

Time Complexity: O(N * M) where:
   - N is the number of nodes in the main list (next direction)
   - M is the average number of nodes in each sub-list (bottom direction)
   - Total nodes = N * M, and we visit each once

Space Complexity: O(N) for recursion stack
   - Recursion depth equals number of main list nodes

Why this works:
- Each sub-list is already sorted, so we just need to merge them
- Recursive approach handles the merging systematically
- Similar to merge sort's merge operation
- The bottom pointer creates the final flattened list

================================================================================
FLOWCHART:
================================================================================

    flatten(root)
          |
          v
    +------------------------+
    | root==NULL ||          |-----> YES ----> return root
    | root.next==NULL?       |
    +------------------------+
          |
         NO
          |
          v
    Recursive call:
    root = merge(root, flatten(root.next))
          |
          v
    return root


    merge(h1, h2)
          |
          v
    +-------------+
    | h1 == NULL? |-----> YES ----> return h2
    +-------------+
          |
         NO
          |
          v
    +-------------+
    | h2 == NULL? |-----> YES ----> return h1
    +-------------+
          |
         NO
          |
          v
    +------------------+
    | h1.data < h2.data?|
    +------------------+
          |         |
         YES       NO
          |         |
          v         v
    res = h1    res = h2
    res.bottom =   res.bottom =
    merge(h1.bottom, h2)   merge(h1, h2.bottom)
          |         |
          +---------+
                |
                v
          res.next = NULL
                |
                v
          return res


    VISUAL EXAMPLE:

    Original Structure:
        5 -> 10 -> 19
        |    |     |
        7    20    22
        |
        8

    Step 1: Flatten from the right
        Flatten(19):
        19 -> 22 (using bottom)

    Step 2: Merge 10 with result
        Merge(10->20, 19->22):
        10 -> 19 -> 20 -> 22

    Step 3: Merge 5 with result
        Merge(5->7->8, 10->19->20->22):
        5 -> 7 -> 8 -> 10 -> 19 -> 20 -> 22

    Final: All nodes connected via bottom pointer in sorted order

================================================================================
"""

class Node:
    """
    Node class for flattened linked list.

    Attributes:
        data: The value stored in the node
        next: Reference to the next node in the main list (horizontal)
        bottom: Reference to the next node in the sub-list (vertical)
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None

class Solution:
    """
    Solution class containing methods to flatten a multi-level linked list.
    """

    def merge(self, h1, h2):
        """
        Merge two sorted linked lists (connected by bottom pointers).

        This is similar to merging two sorted arrays or linked lists.
        The merge is done using the bottom pointer, and next is set to NULL.

        Args:
            h1: Head of first sorted list
            h2: Head of second sorted list

        Returns:
            Head of the merged sorted list

        Algorithm:
        1. Base cases: If either list is NULL, return the other
        2. Compare data of both heads
        3. Choose the smaller one as result
        4. Recursively merge the chosen node's bottom with the other list
        5. Set next to NULL (we only use bottom in flattened list)
        6. Return the result

        Time Complexity: O(m + n) where m and n are lengths of the two lists
        Space Complexity: O(m + n) for recursion stack

        Example:
            h1: 5 -> 7 -> 8
            h2: 10 -> 20

            Compare 5 and 10: 5 is smaller
            Result starts with 5
            Recursively merge (7->8) with (10->20)
            ...
            Final: 5 -> 7 -> 8 -> 10 -> 20
        """
        # Base case 1: If first list is empty, return second list
        if h1 == None:
            return h2

        # Base case 2: If second list is empty, return first list
        if h2 == None:
            return h1

        # Variable to store the result
        res = None

        # Compare the data of both nodes and choose smaller one
        if h1.data < h2.data:
            # h1 has smaller data, so it becomes part of result
            res = h1

            # Recursively merge h1's bottom list with h2
            # This ensures all nodes are considered in sorted order
            res.bottom = self.merge(h1.bottom, h2)
        else:
            # h2 has smaller or equal data, so it becomes part of result
            res = h2

            # Recursively merge h1 with h2's bottom list
            res.bottom = self.merge(h1, h2.bottom)

        # Important: Set next to NULL because flattened list uses bottom pointer
        # The final list should be a single vertical chain
        res.next = None

        return res

    def flatten(self, root):
        """
        Flatten a multi-level linked list into a single sorted list.

        The input is a linked list where each node has:
        - next: pointer to the next node in the main list (horizontal)
        - bottom: pointer to a sub-list (vertical), which is sorted

        The output should be a single list using bottom pointers, sorted.

        Args:
            root: Head of the multi-level linked list

        Returns:
            Head of the flattened sorted list (using bottom pointers)

        Algorithm:
        1. Base case: If root is NULL or no next node, return root
        2. Recursively flatten the rest of the list (root.next onwards)
        3. Merge current node's sub-list with the flattened rest
        4. Return the merged result

        Time Complexity: O(N * M) where N is nodes in main list,
                         M is average nodes in sub-lists
        Space Complexity: O(N) for recursion stack

        Example:
            Input:
                5 -> 10 -> 19
                |    |     |
                7    20    22
                |
                8

            Process:
            1. Flatten(19) → 19 -> 22
            2. Merge(10->20, 19->22) → 10 -> 19 -> 20 -> 22
            3. Merge(5->7->8, 10->19->20->22) → 5->7->8->10->19->20->22

            Output: 5 -> 7 -> 8 -> 10 -> 19 -> 20 -> 22 (using bottom)
        """
        # Base case: If root is NULL or it's the last node in main list
        # In both cases, just return root as-is
        if root == None or root.next == None:
            return root

        # Step 1: Recursively flatten the list starting from next node
        # This processes from right to left in the main list
        # After this call, root.next will point to the flattened result
        # of all nodes to the right
        root.next = self.flatten(root.next)

        # Step 2: Merge current node's sub-list with the flattened result
        # root contains the current node and its bottom chain
        # root.next contains the flattened result of remaining nodes
        root = self.merge(root, root.next)

        # Step 3: Return the merged and flattened list
        return root


# ============================================================================
# EXAMPLE USAGE (Conceptual - requires building the structure)
# ============================================================================

"""
To test this solution, you would need to:

1. Create the multi-level structure:
    root = Node(5)
    root.bottom = Node(7)
    root.bottom.bottom = Node(8)
    root.next = Node(10)
    root.next.bottom = Node(20)
    root.next.next = Node(19)
    root.next.next.bottom = Node(22)

2. Flatten it:
    solution = Solution()
    flattened = solution.flatten(root)

3. Print the result (traversing using bottom pointer):
    current = flattened
    while current:
        print(current.data, end=' ')
        current = current.bottom

Expected Output: 5 7 8 10 19 20 22
"""

"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Are the sub-lists (bottom chains) guaranteed to be sorted? (Usually yes)
   - Should the final list use bottom or next pointers? (Usually bottom)
   - What should we return for an empty list? (NULL/None)
   - Can sub-lists be empty (node with no bottom)? (Yes, handle this)
   - Should we preserve the original structure or modify in-place? (Usually modify)
   - Are there any cycles in the structure? (Usually no)

2. Edge Cases to Consider:
   - Empty list (root is NULL) → return NULL
   - Single node with no bottom or next → return as-is
   - All nodes in one vertical chain (no next pointers) → already flattened
   - All nodes in one horizontal chain (no bottom pointers) → simple case
   - Nodes with NULL bottom pointers → handle gracefully in merge
   - Unequal length sub-lists → merge handles this automatically

3. Common Mistakes to Avoid:
   - Forgetting to set res.next = NULL in merge
     (Critical! The flattened list should only use bottom)
   - Not handling NULL cases in merge function
   - Infinite recursion due to not checking base cases
   - Mixing up next and bottom pointers
   - Not understanding that recursion processes right to left
   - Assuming all sub-lists have same length

4. Key Insights for Interview:
   This problem beautifully combines:
   - Merge operation (from merge sort)
   - Recursion (to handle multiple lists)
   - Linked list manipulation (two types of pointers)
   - Understanding of sorted data structures

5. Why Recursion Works Well Here:
   - Natural way to process from right to left
   - Each recursive call handles one main node
   - Merge operation is naturally recursive
   - Stack handles the "return and merge" pattern

6. Alternative Approaches:
   a) Iterative using priority queue/min-heap: O((N*M) log N)
      - Extract all heads into min-heap
      - Build result by repeatedly extracting minimum
      - More complex but doesn't use recursion stack

   b) Collect all nodes, sort, rebuild: O((N*M) log(N*M))
      - Simple but doesn't use the sorted property
      - Extra space for array

   c) Current recursive merge: O(N*M) time, O(N) space
      - OPTIMAL: Uses sorted property
      - Clean and elegant code

7. Follow-up Questions:
   - Can you do it iteratively?
     (Yes, but more complex - would need to track merge state)
   - What if the sub-lists weren't sorted?
     (Would need to sort first, or use different approach)
   - How would you flatten if next should be used instead of bottom?
     (Simple modification: use next in merge instead of bottom)
   - Can you optimize space to O(1)?
     (Difficult with recursion; would need iterative approach)

8. Time to Solve: Aim for 20-25 minutes including:
   - Understanding the structure: 5 minutes
   - Discussing approach: 5 minutes
   - Coding merge function: 5 minutes
   - Coding flatten function: 3 minutes
   - Testing with examples: 2-5 minutes

9. Comparison with Similar Problems:
   - Merge K Sorted Lists: Very similar concept
   - Flatten Binary Tree to Linked List: Similar flattening concept
   - Merge Two Sorted Lists: Core operation used here

10. Testing Strategy:
    Draw the structure on paper and trace through:
    - Empty list
    - Single node
    - Two nodes horizontally (next)
    - Two nodes vertically (bottom)
    - The full example structure
    - Unequal sub-list lengths
    - Some nodes with NULL bottom

11. Key Points to Mention in Interview:
    - The problem uses TWO types of pointers (next and bottom)
    - We're essentially merging K sorted lists (K = number of main nodes)
    - The recursive approach processes from right to left
    - The merge operation is the heart of the solution
    - Final structure uses only bottom pointers

12. Common Interview Follow-up:
    Q: "Why do we set res.next = NULL in merge?"
    A: Because the flattened list should be a single vertical chain using
       only bottom pointers. Setting next to NULL ensures we don't have
       dangling horizontal pointers.

================================================================================
"""
