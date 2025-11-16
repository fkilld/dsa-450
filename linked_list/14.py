"""
================================================================================
PROBLEM: Middle of the Linked List
================================================================================

DESCRIPTION:
Given a non-empty, singly linked list with head node, return the middle node
of the linked list. If there are two middle nodes, return the second middle node.

Input:  1 -> 2 -> 3 -> 4 -> 5 -> NULL
Output: Node 3 (middle node)

Input:  1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
Output: Node 4 (second middle node when there are two middle nodes)

================================================================================
APPROACH & REASONING:
================================================================================

We'll discuss two approaches:

1. SLOW/FAST POINTER APPROACH (Tortoise and Hare) - RECOMMENDED:
   - Use two pointers: slow (moves 1 step) and fast (moves 2 steps)
   - When fast reaches the end, slow will be at the middle
   - For odd-length lists: slow is at exact middle
   - For even-length lists: slow is at the second middle

   Time Complexity: O(n) - single pass through the list
   Space Complexity: O(1) - only using two pointers

   Why this works:
   - Fast pointer covers twice the distance as slow pointer
   - When fast reaches end (or can't move further), slow is at middle
   - This is because slow moves at half the speed of fast

2. TWO-PASS APPROACH (Less efficient):
   - First pass: count total nodes
   - Second pass: traverse to position n/2
   - Return the node at n/2

   Time Complexity: O(n) - two passes through the list
   Space Complexity: O(1)

   Why slow/fast is better:
   - Only one pass needed
   - More elegant solution
   - Same time complexity but better constant factor

================================================================================
FLOWCHART - SLOW/FAST POINTER APPROACH:
================================================================================

    START
      |
      v
    Initialize:
    slow = head
    fast = head.next
      |
      v
    +----------------------------------+
    | fast != NULL &&                  |-----> NO ----> return slow
    | fast.next != NULL?               |                (middle found!)
    +----------------------------------+
      |
     YES
      |
      v
    Move pointers:
    slow = slow.next (1 step)
    fast = fast.next.next (2 steps)
      |
      v
    (Loop back to condition)


    VISUAL EXAMPLE - ODD LENGTH LIST:

    List: 1 -> 2 -> 3 -> 4 -> 5 -> NULL

    Initial:    slow    fast
                 ↓       ↓
                 1   ->  2  -> 3 -> 4 -> 5 -> NULL

    Step 1:          slow         fast
                      ↓             ↓
                 1 -> 2 -> 3 -> 4 -> 5 -> NULL

    Step 2:               slow              fast
                           ↓                 ↓
                 1 -> 2 -> 3 -> 4 -> 5 -> NULL

    fast.next is NULL, so stop. slow is at 3 (middle).


    VISUAL EXAMPLE - EVEN LENGTH LIST:

    List: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL

    Initial:    slow    fast
                 ↓       ↓
                 1   ->  2  -> 3 -> 4 -> 5 -> 6 -> NULL

    Step 1:          slow         fast
                      ↓             ↓
                 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL

    Step 2:               slow              fast
                           ↓                 ↓
                 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL

    Step 3:                    slow                   fast
                                ↓                      ↓
                 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL

    fast is NULL, so stop. slow is at 4 (second middle).


    KEY INSIGHT - Why fast starts at head.next:
    - If fast starts at head: returns first middle for even-length lists
    - If fast starts at head.next: returns second middle for even-length lists
    - Problem asks for second middle, so we use fast = head.next

================================================================================
"""

class Solution:
    """
    Solution class to find the middle node of a linked list.
    """

    def middle(self, head):
        """
        Find the middle node of a singly linked list using slow/fast pointers.

        Args:
            head: Head of the linked list (non-empty)

        Returns:
            The middle node of the list
            - For odd-length lists: the exact middle node
            - For even-length lists: the second middle node

        Algorithm:
        1. Initialize slow pointer at head
        2. Initialize fast pointer at head.next (to get second middle for even length)
        3. Move slow by 1 step, fast by 2 steps
        4. When fast reaches end, slow is at middle

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1) - only two pointers used

        Example:
            Input: 1->2->3->4->5
            Output: Node 3

            Input: 1->2->3->4->5->6
            Output: Node 4 (second middle)
        """
        # Initialize slow pointer at the head
        # This pointer will eventually point to the middle
        slow = head

        # Initialize fast pointer one step ahead
        # Starting at head.next ensures we get second middle for even-length lists
        # If we started at head, we'd get first middle for even-length lists
        fast = head.next

        # Move both pointers until fast reaches the end
        # Fast moves 2x faster than slow, so when fast reaches end,
        # slow will be at middle
        while fast != None and fast.next != None:
            # Move slow pointer by one step
            slow = slow.next

            # Move fast pointer by two steps
            fast = fast.next.next

        # When loop ends, slow is at the middle node
        # For odd length (n=5): slow at position 3 (exact middle)
        # For even length (n=6): slow at position 4 (second middle)
        return slow


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - What should be returned for empty list? (Problem states non-empty)
   - For even-length lists, which middle? First or second? (Usually second)
   - Should we return the node or just the value? (Usually the node)
   - Can we modify the list? (Not needed for this problem)
   - What if list has only one node? (Return that node)

2. Edge Cases to Consider:
   - Single node list → return that node
   - Two node list → return the second node
   - Three node list → return the middle (second) node
   - Very long list → algorithm still works efficiently
   - Note: Problem states non-empty list, so no need to handle NULL

3. Common Mistakes to Avoid:
   - Starting fast at head instead of head.next (gives wrong middle for even length)
   - Not checking fast.next before accessing fast.next.next
   - Checking conditions in wrong order (fast.next before fast)
   - Returning slow.next instead of slow
   - Infinite loop due to not moving pointers correctly

4. Variations of This Problem:
   - Find first middle for even-length list: start fast at head
   - Find node at position n/3: use three-speed pointers
   - Delete middle node: keep track of slow's previous node
   - Check if list has cycle: similar two-pointer technique

5. Follow-up Questions You Might Get:
   Q: How would you get the first middle for even-length lists?
   A: Start both slow and fast at head instead of fast at head.next

   Q: How to find the node at position n/3?
   A: Use three pointers with different speeds (1x, 2x, 3x)

   Q: Can you do it without the fast pointer?
   A: Yes, count nodes first, then traverse to n/2 (less efficient)

   Q: How to delete the middle node?
   A: Keep prev pointer, when slow reaches middle, do prev.next = slow.next

   Q: What if we want to split list at middle?
   A: Keep prev of slow, set prev.next = None to split

6. Time to Solve: Aim for 5-10 minutes including edge cases

7. Key Points to Mention in Interview:
   - Explain why slow/fast pointer technique works
   - Discuss why fast starts at head.next (for second middle)
   - Draw a diagram showing pointer movements
   - Mention this is O(n) time with single pass
   - Compare with two-pass approach (less elegant)

8. Related Techniques:
   - Floyd's cycle detection: Similar slow/fast pointer concept
   - Finding nth node from end: Use gap between pointers
   - Partitioning list: Use slow/fast to find middle
   - Merge sort on linked list: Uses this to split list

9. Why This Technique is Important:
   - Fundamental pattern for linked list problems
   - Used in many advanced algorithms (merge sort, cycle detection)
   - Demonstrates understanding of pointer manipulation
   - Shows ability to solve in one pass

10. Code Template to Remember:
    ```
    slow = head
    fast = head.next  # or head, depending on requirement
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    ```

================================================================================
"""
