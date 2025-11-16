"""
================================================================================
PROBLEM: Deletion from a Circular Linked List
================================================================================

DESCRIPTION:
Given a circular linked list and a key, delete the first occurrence of the
key from the circular linked list. The function should maintain the circular
property of the list after deletion.

Input:  1 -> 2 -> 3 -> 4 -> (back to 1), key = 3
Output: 1 -> 2 -> 4 -> (back to 1)

Input:  1 -> 2 -> 3 -> (back to 1), key = 1
Output: 2 -> 3 -> (back to 2)  [head updated]

Input:  5 -> (back to 5), key = 5
Output: None (empty list)

================================================================================
APPROACH & REASONING:
================================================================================

SEQUENTIAL SEARCH AND DELETE APPROACH:

The algorithm handles three cases:
1. Empty list - return immediately
2. Single node with matching key - delete and return None
3. Head node matches key - find last node, update links
4. Non-head node matches key - standard deletion

Algorithm Steps:
1. Handle empty list edge case
2. Check if single node matches key
3. If head matches key, find last node and update
4. Otherwise, traverse to find key
5. Delete node and maintain circular property

Time Complexity: O(n) - may need to traverse entire list
Space Complexity: O(1) - only using pointers

Why this works:
- Circular list needs special handling for head deletion
- Must find last node to maintain circular property
- Regular node deletion is similar to normal linked list

Key Considerations:
- Must maintain circular property after deletion
- Head may need to be updated
- Last node must always point to (new) head
- Single node deletion results in empty list

================================================================================
FLOWCHART:
================================================================================

    delete(head, key)
          |
          v
    +----------------+
    | head == NULL?  |-----> YES ----> return NULL
    +----------------+
          |
         NO
          |
          v
    +--------------------------------+
    | head.data==key &&              |-----> YES ----> head = NULL
    | head.next==head?               |                 return NULL
    +--------------------------------+                 (single node deleted)
          |
         NO
          |
          v
    Initialize:
    curr = head
    prev = NULL
          |
          v
    +----------------------+
    | head.data == key?    |-----> NO (skip to general case)
    +----------------------+
          |
         YES (head needs deletion)
          |
          v
    Find last node:
    while curr.next != head:
        curr = curr.next
    curr.next = head.next
    head = curr.next
          |
          +----> return head
          |
          v
    General case:
    Find node to delete
    while curr.next!=head && curr.next.data!=key:
        curr = curr.next
          |
          v
    +---------------------------+
    | curr.next.data == key?    |-----> YES ----> curr.next = curr.next.next
    +---------------------------+                 return head
          |
         NO (key not found)
          |
          v
    return head (no deletion)


    VISUAL EXAMPLE - DELETE HEAD:

    Original: 1 -> 2 -> 3 -> 4 -> (back to 1), delete 1

    Step 1: Detect head.data == key
    Step 2: Find last node (4)
    Step 3: Update last.next = head.next (4 points to 2)
    Step 4: Update head = 2

    Result: 2 -> 3 -> 4 -> (back to 2)
                          ↑           |
                          |___________|


    VISUAL EXAMPLE - DELETE NON-HEAD:

    Original: 1 -> 2 -> 3 -> 4 -> (back to 1), delete 3

    Step 1: head.data != key, proceed to search
    Step 2: Traverse: curr.next.data != 3? (at node 1, check 2)
                      curr.next.data != 3? (at node 2, check 3) - Found!
    Step 3: curr.next = curr.next.next (2 points to 4)

    Result: 1 -> 2 -> 4 -> (back to 1)
           ↑              |
           |______________|


    VISUAL EXAMPLE - DELETE SINGLE NODE:

    Original: 5 -> (back to 5), delete 5

    Step 1: head.data == key && head.next == head
    Step 2: head = NULL

    Result: NULL (empty list)

================================================================================
"""

class Solution:
    """
    Solution class for deleting a node from a circular linked list.
    """

    def delete(self, head, key):
        """
        Delete the first occurrence of a key from a circular linked list.

        The function handles three main cases:
        1. Empty list or single node deletion
        2. Head node deletion
        3. Non-head node deletion

        Args:
            head: Head of the circular linked list
            key: Value to be deleted

        Returns:
            Updated head of the circular linked list

        Algorithm:
        1. Handle empty list case
        2. Handle single node case
        3. If head matches key, find last node and update links
        4. Otherwise, search for key and delete
        5. Return updated head

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1) - only using pointers

        Example:
            Input: 1->2->3->4->(to 1), key=3
            Output: 1->2->4->(to 1)
        """
        # CASE 1: Empty list
        # If list is empty, nothing to delete
        if head is None:
            return None

        # CASE 2: Single node deletion
        # If only one node and it matches the key
        if head.data == key and head.next == head:
            head = None
            return None

        # Initialize pointers for traversal
        curr = head
        prev = None

        # CASE 3: Head node needs to be removed
        if head.data == key:
            # Find the last node (which points back to head)
            # This is needed to maintain circular property
            while curr.next != head:
                curr = curr.next

            # Update last node to point to new head (head.next)
            curr.next = head.next

            # Update head to the next node
            head = curr.next

            # Return the new head
            return head

        # CASE 4: Non-head node deletion
        # Traverse to find the node with the key
        # We check curr.next (not curr) so we can easily delete
        while curr.next != head and curr.next.data != key:
            curr = curr.next

        # If we found the key (curr.next.data == key)
        if curr.next.data == key:
            # Remove the node by skipping it
            # curr.next.next is the node after the one we're deleting
            curr.next = curr.next.next

        # Return the head (unchanged in this case)
        return head


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Should we delete only first occurrence or all occurrences? (First)
   - What if key is not found? (Return list as-is)
   - What if list becomes empty after deletion? (Return NULL)
   - Should we maintain circular property? (YES - critical)
   - Can there be duplicate values? (Yes, delete first occurrence)

2. Edge Cases to Consider:
   - Empty list (head is None) → return None
   - Single node matching key → return None (empty list)
   - Single node not matching key → return head (no change)
   - Head node matches key → update head and last node
   - Last node matches key → update second-to-last node
   - Middle node matches key → standard deletion
   - Key not found → return list unchanged
   - All nodes have same value as key

3. Common Mistakes to Avoid:
   - Breaking circular property during deletion
   - Not updating head when first node is deleted
   - Not finding last node when deleting head
   - Infinite loop when traversing circular list
   - Not handling single node case
   - Forgetting to check if key exists before deleting

4. Key Insights:
   - Head deletion requires special handling
   - Must find last node to maintain circularity
   - Regular deletion is similar to normal linked list
   - Always maintain circular property (last.next = head)
   - Single node deletion results in empty list

5. Follow-up Questions You Might Get:
   Q: How to delete all occurrences of a key?
   A: Continue traversing after each deletion until we loop back

   Q: How to delete node at a specific position?
   A: Traverse to position-1, then delete similar to key deletion

   Q: What if we need to delete the last node?
   A: Find second-to-last node, update its next to head

   Q: Can you delete without finding last node when deleting head?
   A: No, we need last node to maintain circular property

   Q: How to delete kth node from end?
   A: Count nodes, find position n-k, then delete

6. Time to Solve: Aim for 12-15 minutes including edge cases

7. Key Points to Mention in Interview:
   - Explain the three main cases (empty, head, non-head)
   - Discuss why head deletion needs special handling
   - Emphasize maintaining circular property
   - Walk through how last node is found
   - Mention single node deletion edge case

8. Testing Strategy:
   - Test empty list
   - Test single node (matching and non-matching key)
   - Test deleting head node
   - Test deleting last node
   - Test deleting middle node
   - Test key not found
   - Test list with 2 nodes

9. Why This Problem is Important:
   - Tests understanding of circular linked lists
   - Requires careful pointer manipulation
   - Common in buffer and queue implementations
   - Demonstrates edge case handling skills
   - Shows ability to maintain data structure invariants

10. Related Problems:
    - Insert in circular linked list
    - Check if list is circular
    - Split circular list
    - Merge circular lists
    - Delete node in regular linked list
    - Circular queue implementation

================================================================================
"""
