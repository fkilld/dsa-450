"""
================================================================================
PROBLEM: Move Last Element to Front of Linked List
================================================================================

DESCRIPTION:
Given a singly linked list, move the last element to the front of the list
and return the new head.

Input:  1 -> 2 -> 3 -> 4 -> 5 -> NULL
Output: 5 -> 1 -> 2 -> 3 -> 4 -> NULL

This is essentially a rotation operation - we're rotating the list to the
right by one position.

================================================================================
APPROACH & REASONING:
================================================================================

This is a straightforward pointer manipulation problem.

KEY INSIGHT:
- We need to find the last node and second-to-last node
- Disconnect the last node from the list
- Make it point to the current head
- Update head to the last node

ALGORITHM:

1. Handle edge cases (empty list, single node)
2. Traverse to find the last and second-to-last nodes:
   - Use curr and prev pointers
   - Move until curr.next is None
   - At this point: prev is second-to-last, curr is last
3. Disconnect last node:
   - Set prev.next = None (remove last node from list)
4. Move last node to front:
   - Set curr.next = head (last node points to old head)
   - Set head = curr (last node becomes new head)
5. Return new head

WHY THIS WORKS:
- We only need to modify two pointers:
  1. Second-to-last node's next (to None)
  2. Last node's next (to old head)
- No complex operations needed, just find and move

Time Complexity: O(n) - traverse entire list once to find last node
Space Complexity: O(1) - only using two pointers

VISUAL EXAMPLE:

Before:  1 -> 2 -> 3 -> 4 -> 5 -> NULL
         ^                   ^
        head               last

After:   5 -> 1 -> 2 -> 3 -> 4 -> NULL
         ^
      new head

================================================================================
FLOWCHART:
================================================================================

    START
      |
      v
    +---------------------+
    | head == NULL or     |-----> YES ----> return head
    | head.next == NULL?  |                 (nothing to move)
    +---------------------+
      |
     NO
      |
      v
    Initialize:
    curr = head
    prev = None
      |
      v
    +--------------------+
    | curr.next != NULL? |-----> NO  (found last node)
    +--------------------+         |
      |                            |
     YES                           |
      |                            |
      v                            |
    prev = curr                    |
    curr = curr.next               |
      |                            |
      +---(Loop back)              |
                                   |
                                   v
                          Disconnect last:
                          prev.next = NULL
                                   |
                                   v
                          Move to front:
                          curr.next = head
                          head = curr
                                   |
                                   v
                          return head
                                   |
                                   v
                                  END


    DETAILED VISUAL TRACE:

    Input: 1 -> 2 -> 3 -> 4 -> 5 -> NULL

    Step 1: Find last and second-to-last
            Start: curr = 1, prev = None

            Iteration 1:
            prev = 1, curr = 2
            1 -> [2] -> 3 -> 4 -> 5 -> NULL

            Iteration 2:
            prev = 2, curr = 3
            1 -> 2 -> [3] -> 4 -> 5 -> NULL

            Iteration 3:
            prev = 3, curr = 4
            1 -> 2 -> 3 -> [4] -> 5 -> NULL

            Iteration 4:
            prev = 4, curr = 5
            1 -> 2 -> 3 -> 4 -> [5] -> NULL
            curr.next = NULL, stop!

    Step 2: Disconnect last node
            prev.next = None
            1 -> 2 -> 3 -> 4 -> NULL    5
                              ^         ^
                            prev      curr

    Step 3: Move last to front
            curr.next = head
            5 -> 1 -> 2 -> 3 -> 4 -> NULL
            ^
          curr

    Step 4: Update head
            head = curr
            5 -> 1 -> 2 -> 3 -> 4 -> NULL
            ^
          head (returned)

================================================================================
"""

class Solution:
    """
    Solution class to move the last element to the front of a linked list.
    """

    def move(self, head):
        """
        Move the last node to the front of the linked list.

        Args:
            head: The head node of the linked list

        Returns:
            head: The new head of the list (which was the last node)

        Algorithm:
        1. Traverse to find last and second-to-last nodes
        2. Disconnect last node by setting second-to-last.next = None
        3. Make last node point to old head
        4. Update head to last node
        5. Return new head

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1) - only using two pointers

        Example:
            Input:  1 -> 2 -> 3 -> 4 -> 5 -> NULL
            Output: 5 -> 1 -> 2 -> 3 -> 4 -> NULL

        Edge Cases:
            - Empty list: return None
            - Single node: return as-is (already at front)
        """

        # Edge case: empty list or single node
        # In both cases, there's nothing to move
        if head is None or head.next is None:
            return head

        # Initialize pointers to traverse the list
        curr = head  # Will eventually point to last node
        prev = None  # Will eventually point to second-to-last node

        # Traverse until we reach the last node
        # Last node is when curr.next is None
        while curr.next != None:
            prev = curr          # Save current node as previous
            curr = curr.next     # Move to next node

        # At this point:
        # - curr points to the last node
        # - prev points to the second-to-last node

        # Step 1: Disconnect the last node from the list
        # Make the second-to-last node the new last node
        prev.next = None

        # Step 2: Make the last element point to the current head
        # This connects the old last node to the front of the list
        curr.next = head

        # Step 3: Update head to point to the old last node
        # The last node is now the first node
        head = curr

        # Return the new head
        return head


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Should I return the new head? (Yes)
   - What if the list is empty? (Return None/head as-is)
   - What if there's only one node? (Return as-is, nothing to move)
   - Should I modify in-place? (Yes)
   - What if we need to move last k elements? (Different problem, needs k nodes)

2. Edge Cases to Consider:
   - Empty list (head is None) → return None
   - Single node → return as-is
   - Two nodes → swap them
   - Very long list → same logic applies
   - List with duplicate values → doesn't matter, move by position

3. Common Mistakes to Avoid:
   - Not handling empty list (would crash on curr.next)
   - Not handling single node case
   - Forgetting to disconnect last node (prev.next = None)
   - Forgetting to update head pointer
   - Not returning the new head
   - Trying to use complex logic when simple pointer manipulation suffices

4. Follow-up Questions You Might Get:
   Q: What if we need to move last k elements to front?
   A: Find the (n-k)th node, split list there, reconnect pieces
      Example code:
      ```python
      # Find length, find (n-k)th node
      # Split: temp = node(n-k).next
      # Connect: node(n-k).next = None
      # Find new last: traverse temp to end
      # Connect: last.next = head
      # Return: temp as new head
      ```

   Q: Can you rotate right by k positions?
   A: Move last element k times, or optimize using above approach

   Q: What about rotating left instead of right?
   A: Move first element to end (simpler - no need to find prev)

   Q: Can you do this recursively?
   A: Yes, but iterative is simpler and more efficient for this problem

   Q: How would you optimize if called multiple times?
   A: Keep reference to last node (circular buffer concept)

5. Variations of This Problem:
   - Rotate right by k positions
   - Rotate left by k positions
   - Move first element to end (easier - no prev needed)
   - Swap first and last elements
   - Reverse the list (different problem)

6. Related Problems:
   - Rotate Array (similar concept)
   - Rotate List (LeetCode 61 - rotate by k positions)
   - Reverse Linked List (Problem 0)

7. Time to Solve: Aim for 8-10 minutes including edge cases

8. Interview Strategy:
   - Draw the before and after states
   - Identify what pointers need to change
   - Explain why we need prev pointer
   - Code with clear variable names
   - Test with examples: 2 nodes, 3 nodes, empty

9. Key Points to Mention:
   - "This is essentially a rotation by 1 position"
   - "We need prev pointer because we can't go backwards in singly linked list"
   - "Only two pointer updates needed: disconnect and reconnect"
   - "Time is O(n) because we must traverse to find last node"

10. Alternative Approach (Using Tail Pointer):
    If the list class maintains a tail pointer:
    ```python
    # O(1) solution with tail pointer
    tail.next = head
    head = tail
    # Find new tail (second-to-last)
    new_tail = head
    while new_tail.next != tail:
        new_tail = new_tail.next
    new_tail.next = None
    tail = new_tail
    ```
    But standard singly linked list doesn't have tail pointer

11. Why This Problem Matters:
    - Tests understanding of pointer manipulation
    - Common operation in circular buffers and queues
    - Foundation for more complex rotation problems
    - Shows importance of tracking prev pointer in singly linked lists

12. Code Simplification:
    The current code could be slightly simplified:
    ```python
    if not head or not head.next:
        return head

    prev, curr = None, head
    while curr.next:
        prev, curr = curr, curr.next

    prev.next = None
    curr.next = head
    return curr
    ```

================================================================================
"""
