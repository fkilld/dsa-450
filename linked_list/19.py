"""
================================================================================
PROBLEM: Reverse a Doubly Linked List
================================================================================

DESCRIPTION:
Given a doubly linked list, reverse it so that the last node becomes the
first node, and vice versa. Each node has both 'next' and 'prev' pointers.

Input:  NULL <- 1 <-> 2 <-> 3 <-> 4 <-> 5 -> NULL
Output: NULL <- 5 <-> 4 <-> 3 <-> 2 <-> 1 -> NULL

Note: Unlike singly linked list, we have both forward and backward pointers
that need to be swapped.

================================================================================
APPROACH & REASONING:
================================================================================

POINTER SWAPPING APPROACH:

The key insight is that for each node in a doubly linked list, we need to
swap its 'next' and 'prev' pointers. The last node of the original list
becomes the new head.

Algorithm Steps:
1. Handle edge cases (empty list or single node)
2. Traverse to find the last node (new head)
3. For each node, swap its 'next' and 'prev' pointers
4. Return the last node as the new head

Time Complexity: O(n) - single pass through the list
Space Complexity: O(1) - only using pointers

Why this works:
- In a doubly linked list, each node has two pointers
- Reversing means swapping the direction of both pointers
- After swapping all pointers, the last node becomes the first
- This is simpler than singly linked list reversal

Alternative Approach:
- Use three pointers (prev, curr, next) like singly linked list
- Current approach is cleaner for doubly linked lists

================================================================================
FLOWCHART:
================================================================================

    reverse(head)
          |
          v
    Initialize:
    curr = head
          |
          v
    +---------------------------+
    | curr==NULL or             |-----> YES ----> return head
    | curr.next==NULL?          |                 (empty or single node)
    +---------------------------+
          |
         NO
          |
          v
    Find last node:
    while curr.next != NULL:
        curr = curr.next
          |
          v
    head = curr
    (last node is new head)
          |
          v
    Swap pointers for each node:
    while curr != NULL:
        swap(curr.next, curr.prev)
        curr = curr.next (which is old prev)
          |
          v
    return head


    VISUAL EXAMPLE:

    Original:
    NULL <- 1 <-> 2 <-> 3 <-> 4 -> NULL
         head^

    Step 1: Find last node (4)
    new_head = 4

    Step 2: Swap pointers for each node

    At node 4:
    Before: prev=3, next=NULL
    After:  prev=NULL, next=3

    At node 3:
    Before: prev=2, next=4
    After:  prev=4, next=2

    At node 2:
    Before: prev=1, next=3
    After:  prev=3, next=1

    At node 1:
    Before: prev=NULL, next=2
    After:  prev=2, next=NULL

    Result:
    NULL <- 4 <-> 3 <-> 2 <-> 1 -> NULL
         head^


    POINTER SWAPPING DETAIL:

    For each node:
    temp = curr.next
    curr.next = curr.prev
    curr.prev = temp

    This effectively reverses the direction of links.

================================================================================
"""

def reverse(head):
    """
    Reverse a doubly linked list.

    Each node in a doubly linked list has both 'next' and 'prev' pointers.
    To reverse, we swap these pointers for each node and update the head
    to point to the original last node.

    Args:
        head: Head of the doubly linked list

    Returns:
        New head of the reversed doubly linked list

    Algorithm:
    1. Handle edge cases (empty or single node)
    2. Traverse to find the last node
    3. For each node, swap next and prev pointers
    4. Return the last node as new head

    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(1) - only using pointers

    Example:
        Input:  NULL <- 1 <-> 2 <-> 3 -> NULL
        Output: NULL <- 3 <-> 2 <-> 1 -> NULL
    """
    # Initialize current pointer at head
    curr = head

    # EDGE CASE 1: Empty list
    # EDGE CASE 2: Single node
    # In both cases, list is already "reversed"
    if curr == None or curr.next == None:
        return head

    # PHASE 1: Find the last node of the list
    # The last node will become the new head
    while curr.next != None:
        curr = curr.next

    # Update head to point to the last node
    # This is the new head of the reversed list
    head = curr

    # PHASE 2: Swap next and prev pointers for each node
    # Traverse the list and swap pointers
    # Note: After swapping, curr.next becomes old curr.prev
    # So we move "forward" by going to curr.next (which is actually going backward)
    while curr != None:
        # Swap the next and prev pointers
        # This is done using Python's tuple unpacking
        curr.next, curr.prev = curr.prev, curr.next

        # Move to the next node in the original order
        # Since we just swapped, curr.next now points to the previous node
        curr = curr.next

    # Return the new head (which was the last node)
    return head


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Can we modify the original list? (Yes, reverse in-place)
   - Should we return the new head? (Yes, usually)
   - What if list is empty? (Return NULL/None)
   - What if list has one node? (Return as-is)
   - Is it guaranteed to be a valid doubly linked list? (Usually yes)

2. Edge Cases to Consider:
   - Empty list (head is None) → return None
   - Single node → return head (already reversed)
   - Two nodes → swap and update head
   - Very long list → algorithm scales well
   - All nodes have same value → still works

3. Common Mistakes to Avoid:
   - Not finding the last node before starting reversal
   - Forgetting to swap both next and prev pointers
   - Getting confused about traversal direction after swapping
   - Not updating head to the last node
   - Losing reference to nodes during swapping
   - Infinite loop due to incorrect pointer updates

4. Doubly vs Singly Linked List Reversal:

   Doubly Linked List:
   - Simpler: just swap next and prev for each node
   - Must update both pointers
   - Can traverse backward if needed
   - More memory (two pointers per node)

   Singly Linked List:
   - Need three pointers (prev, curr, next)
   - More complex pointer manipulation
   - Can only traverse forward
   - Less memory (one pointer per node)

5. Follow-up Questions You Might Get:
   Q: Can you reverse without finding the last node first?
   A: Yes, swap pointers while traversing, track new head separately

   Q: How would you reverse only a portion of the list?
   A: Pass start and end nodes, reverse between them

   Q: Can you do it recursively?
   A: Yes, but iterative is simpler and uses O(1) space

   Q: How to reverse a circular doubly linked list?
   A: Similar approach but need to handle circular property

   Q: What if some prev pointers are NULL (corrupted list)?
   A: Would need to handle as singly linked list

6. Time to Solve: Aim for 10-12 minutes including edge cases

7. Key Points to Mention in Interview:
   - Explain why we need to find the last node first
   - Discuss the pointer swapping mechanism
   - Mention that this is simpler than singly linked list reversal
   - Walk through the direction change after swapping
   - Emphasize O(1) space complexity

8. Testing Strategy:
   - Test empty list
   - Test single node
   - Test two nodes
   - Test odd-length list (3, 5 nodes)
   - Test even-length list (4, 6 nodes)
   - Verify both forward and backward traversal after reversal

9. Alternative Implementation:
   You can also reverse without finding last node first:

   ```python
   curr = head
   new_head = None
   while curr:
       curr.next, curr.prev = curr.prev, curr.next
       new_head = curr  # Track what will be new head
       curr = curr.prev  # Move to next (now in prev due to swap)
   return new_head
   ```

   This is more concise but less explicit about finding the new head.

10. Related Problems:
    - Reverse singly linked list
    - Reverse in groups of k
    - Reverse between positions m and n
    - Flatten a multilevel doubly linked list
    - Clone a doubly linked list with random pointers
    - LRU Cache implementation (uses doubly linked list)

================================================================================
"""
