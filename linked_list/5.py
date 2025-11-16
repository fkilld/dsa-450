"""
================================================================================
PROBLEM: Remove Duplicates from Sorted Linked List
================================================================================

DESCRIPTION:
Given a sorted singly linked list, delete all duplicate nodes such that each
element appears only once.

Input:  1 -> 1 -> 2 -> 3 -> 3 -> 3 -> 4 -> 5 -> 5 -> NULL
Output: 1 -> 2 -> 3 -> 4 -> 5 -> NULL

Since the list is already sorted, all duplicate values will be adjacent to
each other, making the problem simpler than the unsorted case.

================================================================================
APPROACH & REASONING:
================================================================================

Since the list is sorted, we can use a single-pass approach with one pointer.

KEY INSIGHT:
- All duplicates are consecutive (list is sorted)
- We can compare each node with its next node
- If values are equal, skip the next node
- If values are different, move to next node

ALGORITHM:

1. Start from head
2. For each node:
   - If current.data == current.next.data:
     * Skip the next node by doing: current.next = current.next.next
     * Don't move current pointer (there might be more duplicates)
   - Else:
     * Move to next node: current = current.next
3. Continue until we reach the end

WHY THIS WORKS:
- Sorted order guarantees duplicates are adjacent
- By comparing only with the next node, we can identify duplicates
- Skipping nodes removes them from the list
- Not moving current when we find a duplicate allows us to handle
  multiple consecutive duplicates

Time Complexity: O(n) - single pass through the list
Space Complexity: O(1) - only using one pointer, no extra space

EXAMPLE TRACE:
Input: 1 -> 1 -> 1 -> 2 -> 3 -> 3 -> NULL

Step 1: curr at 1, next is 1 (duplicate!)
        Skip: 1 -> 1 -> 2 -> 3 -> 3 -> NULL
              curr stays here

Step 2: curr at 1, next is 1 (duplicate!)
        Skip: 1 -> 2 -> 3 -> 3 -> NULL
              curr stays here

Step 3: curr at 1, next is 2 (different!)
        Move: curr = curr.next
              1 -> 2 -> 3 -> 3 -> NULL
                   curr

Step 4: curr at 2, next is 3 (different!)
        Move: curr = curr.next
              1 -> 2 -> 3 -> 3 -> NULL
                        curr

Step 5: curr at 3, next is 3 (duplicate!)
        Skip: 1 -> 2 -> 3 -> NULL
                        curr stays

Step 6: curr at 3, next is NULL
        Done!

================================================================================
FLOWCHART:
================================================================================

    START
      |
      v
    Initialize:
    curr = head
      |
      v
    +-------------------+
    | curr.next != NULL?|-----> NO ----> END (reached end of list)
    +-------------------+
      |
     YES
      |
      v
    +-------------------------------+
    | curr.data == curr.next.data?  |
    +-------------------------------+
      |                    |
     YES                  NO
      |                    |
      v                    v
    DUPLICATE!         UNIQUE!
    Skip next:         Move forward:
    curr.next =        curr = curr.next
    curr.next.next          |
      |                     |
      +---------------------+
      |
      +---(Loop back to condition)


    VISUAL EXAMPLE:

    Input:  1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5 -> NULL

    Step 1: [1] -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5 -> NULL
            curr  next (different, move curr)

    Step 2: 1 -> [2] -> 2 -> 3 -> 4 -> 4 -> 4 -> 5 -> NULL
                 curr  next (same, skip next)

    Step 3: 1 -> [2] -> 3 -> 4 -> 4 -> 4 -> 5 -> NULL
                 curr  next (different, move curr)

    Step 4: 1 -> 2 -> [3] -> 4 -> 4 -> 4 -> 5 -> NULL
                      curr  next (different, move curr)

    Step 5: 1 -> 2 -> 3 -> [4] -> 4 -> 4 -> 5 -> NULL
                           curr  next (same, skip)

    Step 6: 1 -> 2 -> 3 -> [4] -> 4 -> 5 -> NULL
                           curr  next (same, skip)

    Step 7: 1 -> 2 -> 3 -> [4] -> 5 -> NULL
                           curr  next (different, move)

    Step 8: 1 -> 2 -> 3 -> 4 -> [5] -> NULL
                                curr  next=NULL (done!)

    Output: 1 -> 2 -> 3 -> 4 -> 5 -> NULL

================================================================================
"""

class Solution:
    """
    Solution class to remove duplicates from a sorted linked list.
    """

    def remove(self, head):
        """
        Remove all duplicate nodes from a sorted linked list.

        Args:
            head: The head node of the sorted linked list

        Returns:
            None (modifies the list in-place)

        Algorithm:
        1. Start with current pointer at head
        2. For each node, compare with next node
        3. If values are equal, skip the next node
        4. If values are different, move to next node
        5. Continue until end of list

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1) - only using one pointer

        Example:
            Input:  1 -> 1 -> 2 -> 3 -> 3 -> NULL
            Output: 1 -> 2 -> 3 -> NULL

        Note: This function modifies the list in-place and doesn't return
              anything. The head reference remains unchanged.
        """

        # Start from the head of the list
        curr = head

        # Traverse the list until we reach the end
        # We check curr.next != None because we compare curr with curr.next
        while curr.next != None:

            # Check if current node has same value as next node
            if curr.data == curr.next.data:
                # DUPLICATE FOUND!
                # Skip the next node by linking current to the node after next
                # This effectively removes the duplicate node from the list
                curr.next = curr.next.next
                # Don't move curr - there might be more duplicates ahead

            else:
                # UNIQUE VALUE!
                # Values are different, so move to the next node
                curr = curr.next


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Is the list sorted? (Yes, which makes the problem easier)
   - Should I keep the first occurrence or last? (First - standard approach)
   - Should I modify in-place or create a new list? (In-place)
   - What should I do with an empty list? (Return as-is)
   - Can the list have all duplicates? (Yes, result would be single node)

2. Edge Cases to Consider:
   - Empty list (head is None) → would cause error, need to check first
   - Single node → no duplicates possible, return as-is
   - All nodes have same value → keep only first node
   - No duplicates → list remains unchanged
   - Two nodes with same value → keep first, remove second
   - Duplicates at beginning, middle, and end

3. Common Mistakes to Avoid:
   - Moving current pointer when duplicate found (might miss consecutive dups)
   - Not checking if curr.next is None before accessing curr.next.data
   - Trying to modify head pointer unnecessarily
   - Creating new nodes instead of modifying in-place
   - Not handling empty list (would crash on curr.next)

4. Why This is Easier Than Unsorted Version:
   - Sorted: Only compare adjacent nodes, O(1) space
   - Unsorted: Need to track all seen values, O(n) space (hash set)
   - Sorted: Single pass is sufficient
   - Unsorted: Might need multiple passes or additional data structure

5. Follow-up Questions You Might Get:
   Q: What if list is unsorted?
   A: Use hash set to track seen values (Problem 6)

   Q: What if we want to remove all occurrences of duplicates (keep none)?
   A: Need different approach - use dummy node and track previous node

   Q: Can you do this recursively?
   A: Yes, but iterative is more efficient (no call stack overhead)

   Q: What's the space complexity?
   A: O(1) - we're only using one pointer, no additional data structures

6. Recursive Alternative (for discussion):
   ```python
   def remove_recursive(self, head):
       if not head or not head.next:
           return head
       if head.data == head.next.data:
           head.next = head.next.next
           return self.remove_recursive(head)
       else:
           self.remove_recursive(head.next)
           return head
   ```
   Note: This uses O(n) space for recursion stack

7. Related Problems:
   - Remove Duplicates from Sorted Array (similar logic)
   - Remove Duplicates from Unsorted Linked List (Problem 6)
   - Remove All Duplicate Nodes (keep none, not just one)

8. Time to Solve: Aim for 8-10 minutes including edge cases

9. Interview Strategy:
   - Clarify that list is sorted (changes approach significantly)
   - Draw a simple example on whiteboard
   - Explain why we don't move curr when duplicate found
   - Code with clear comments
   - Test with edge cases: all same, no duplicates, empty list

10. Key Points to Mention:
    - "The sorted property is crucial - it allows O(1) space solution"
    - "We skip duplicates rather than deleting to avoid memory management"
    - "Not moving current pointer handles consecutive duplicates elegantly"
    - "This is a greedy approach - we make local decisions (skip vs move)"

11. Code Optimization Note:
    The current code doesn't handle the case when head is None.
    In production code, you'd add:
    ```python
    if head is None:
        return
    ```

================================================================================
"""
