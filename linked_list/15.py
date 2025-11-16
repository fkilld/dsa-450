"""
================================================================================
PROBLEM: Check If Circular Linked List
================================================================================

DESCRIPTION:
Given a singly linked list, determine if it is a circular linked list.
A circular linked list is one in which the last node points back to the
first node (head) instead of pointing to NULL.

Input:  1 -> 2 -> 3 -> 4 -> 5 -> (back to 1)
Output: 1 (True - it's circular)

Input:  1 -> 2 -> 3 -> NULL
Output: 0 (False - it's not circular)

Note: An empty linked list is considered circular (returns 1).

================================================================================
APPROACH & REASONING:
================================================================================

SINGLE POINTER TRAVERSAL APPROACH:

The key insight is that in a circular linked list, we will eventually
encounter the head node again while traversing. In a non-circular list,
we will encounter NULL.

Algorithm:
1. Handle edge case: empty list is considered circular
2. Start traversing from head
3. Keep moving to next nodes
4. If we encounter head again → circular
5. If we encounter NULL → not circular

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(1) - only using one pointer

Why this works:
- In a circular list: last node's next points to head
- We traverse the list and check if next == head
- If we find NULL before finding head, it's not circular

Alternative Approach (Not implemented):
- Use Floyd's cycle detection (slow/fast pointers)
- More general (works for any cycle, not just circular)
- Current approach is simpler since we know cycle must be at head

================================================================================
FLOWCHART:
================================================================================

    START
      |
      v
    +---------------+
    | head == NULL? |-----> YES ----> return 1
    +---------------+                 (empty list is circular)
      |
     NO
      |
      v
    Initialize:
    temp = head
      |
      v
    +---------------------+
    | temp.next != head?  |-----> NO (found head) ----> return 1
    +---------------------+                             (circular!)
      |
     YES
      |
      v
    Move to next:
    temp = temp.next
      |
      v
    +--------------+
    | temp == NULL?|-----> YES ----> return 0
    +--------------+                 (not circular)
      |
     NO
      |
      +----(Loop back to "temp.next != head" check)


    VISUAL EXAMPLE - CIRCULAR LIST:

    Circular List: 1 -> 2 -> 3 -> 4
                   ^              |
                   |______________|

    temp = head (node 1)
    Step 1: temp.next = 2 (not head), temp = 2, not NULL
    Step 2: temp.next = 3 (not head), temp = 3, not NULL
    Step 3: temp.next = 4 (not head), temp = 4, not NULL
    Step 4: temp.next = 1 (equals head!) → return 1 (circular)


    VISUAL EXAMPLE - NON-CIRCULAR LIST:

    Non-Circular: 1 -> 2 -> 3 -> NULL

    temp = head (node 1)
    Step 1: temp.next = 2 (not head), temp = 2, not NULL
    Step 2: temp.next = 3 (not head), temp = 3, not NULL
    Step 3: temp.next = NULL (not head), temp = NULL → return 0 (not circular)


    KEY INSIGHT:
    The loop condition checks temp.next != head before moving temp.
    This allows us to detect circularity when we see head as the next node,
    not when we're actually at head (which would be immediate).

================================================================================
"""

def isCircular(head):
    """
    Check if a singly linked list is circular.

    A circular linked list is one where the last node points back to the
    head instead of NULL. An empty list is considered circular by definition.

    Args:
        head: Head of the linked list

    Returns:
        1 if the list is circular, 0 otherwise

    Algorithm:
    1. Empty list is considered circular (return 1)
    2. Traverse the list starting from head
    3. At each step, check if next node is head (circular) or NULL (not circular)
    4. Return 1 for circular, 0 for non-circular

    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(1) - only using one pointer

    Example:
        Input: 1->2->3->(back to 1)
        Output: 1 (circular)

        Input: 1->2->3->NULL
        Output: 0 (not circular)
    """
    # Edge case: An empty linked list is considered circular
    # This is a definition-based edge case
    if head == None:
        return 1

    # Initialize temp pointer to traverse the list
    temp = head

    # Traverse the list until we find either:
    # 1. The next node is head (circular)
    # 2. We encounter NULL (not circular)
    while temp.next != head:
        # Move to the next node
        temp = temp.next

        # If we encounter NULL, list is not circular
        # This means we reached the end without looping back to head
        if temp == None:
            return 0

    # If we exit the loop, it means temp.next == head
    # This indicates the list is circular
    return 1


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Is an empty list considered circular? (Usually yes, return 1)
   - Should we detect any cycle or specifically circular? (Circular = cycle at head)
   - What should we return? (Usually 1/0 or True/False)
   - Can the list have only one node pointing to itself? (Yes, that's circular)
   - Is the list guaranteed to have no other cycles? (Usually yes)

2. Edge Cases to Consider:
   - Empty list (NULL head) → return 1 (considered circular)
   - Single node pointing to itself → circular (return 1)
   - Single node pointing to NULL → not circular (return 0)
   - Two nodes forming a cycle → circular (return 1)
   - Very long circular list → algorithm still works
   - Non-circular list → return 0

3. Common Mistakes to Avoid:
   - Not handling the empty list case
   - Checking temp == NULL before temp.next (will cause error)
   - Infinite loop if not checking for NULL properly
   - Starting traversal incorrectly
   - Confusing circular with general cycle detection
   - Not understanding the while loop condition

4. Circular vs Cycle Detection:

   Circular List:
   - Last node specifically points to head
   - Forms a perfect circle
   - This problem's focus

   Cycle Detection (General):
   - Any node can point back to any previous node
   - Use Floyd's algorithm (slow/fast pointers)
   - More general problem

5. Follow-up Questions You Might Get:
   Q: How would you detect a cycle at any position (not just head)?
   A: Use Floyd's cycle detection with slow/fast pointers

   Q: Can you find the length of the circular list?
   A: Yes, traverse until we reach head again, counting nodes

   Q: What if we want to convert circular to non-circular?
   A: Find the node whose next is head, set its next to NULL

   Q: How to detect if a node points to itself?
   A: Check if head.next == head

   Q: Can you use Floyd's algorithm instead?
   A: Yes, but current approach is simpler for this specific problem

6. Time to Solve: Aim for 8-10 minutes including edge cases

7. Key Points to Mention in Interview:
   - Explain the difference between circular and general cycle
   - Discuss why empty list is considered circular
   - Walk through the loop condition logic
   - Mention that we're checking for NULL during traversal
   - Compare with Floyd's algorithm (more general but complex)

8. Alternative Approaches:
   - Floyd's cycle detection: Use slow/fast pointers (more general)
   - Hash set: Store visited nodes (O(n) space)
   - Modify data: Mark visited nodes (destructive)

   Current approach is best because:
   - Simple and efficient for this specific problem
   - O(1) space complexity
   - Easy to understand and implement

9. Code Walkthrough Example:
   List: 1->2->3->(back to 1)

   - head = node1
   - temp = node1
   - Loop: temp.next = node2 (not head), move temp to node2
   - Loop: temp.next = node3 (not head), move temp to node3
   - Loop: temp.next = node1 (equals head!), exit loop
   - Return 1 (circular)

10. Why This Problem Matters:
    - Tests understanding of linked list structure
    - Demonstrates pointer manipulation skills
    - Shows ability to handle edge cases
    - Foundation for more complex cycle detection problems
    - Common in interviews (especially for circular list operations)

================================================================================
"""
