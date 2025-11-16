"""
================================================================================
PROBLEM: Remove Loop in Linked List
================================================================================

DESCRIPTION:
Given a linked list that contains a loop/cycle, remove the loop by breaking
the cycle and making the last node in the loop point to NULL.

Input:  1 -> 2 -> 3 -> 4 -> 5
                  ^         |
                  |_________|
Output: 1 -> 2 -> 3 -> 4 -> 5 -> NULL (loop removed)

The challenge is to:
1. Detect if a loop exists
2. Find the node where the loop starts
3. Break the loop by setting the appropriate next pointer to NULL

================================================================================
APPROACH & REASONING:
================================================================================

This problem builds on Floyd's Cycle Detection Algorithm with an additional
step to find and remove the loop.

ALGORITHM STEPS:

1. DETECT LOOP (Floyd's Algorithm):
   - Use slow (1 step) and fast (2 steps) pointers
   - If they meet, a loop exists
   - If fast reaches NULL, no loop exists

2. FIND LOOP START:
   Two cases to handle:

   Case A: Loop starts at head (slow == head after detection)
   - Move fast pointer around the loop until fast.next == head
   - Set fast.next = NULL to break the loop

   Case B: Loop starts somewhere in the middle
   - Reset slow to head
   - Move both slow and fast by 1 step until slow.next == fast.next
   - The node at slow.next (or fast.next) is the loop start
   - Set fast.next = NULL to break the loop

3. WHY THIS WORKS (Mathematical Proof):

   Let's say:
   - Distance from head to loop start = a
   - Distance from loop start to meeting point = b
   - Remaining loop distance = c
   - Loop length = L = b + c

   When slow and fast meet:
   - Slow has traveled: a + b
   - Fast has traveled: a + b + kL (k = number of complete loops)
   - Since fast travels twice as fast: 2(a + b) = a + b + kL
   - Simplifying: a + b = kL, so a = kL - b = (k-1)L + c

   This means: Distance from head to start = Distance from meeting point to start
   That's why moving both pointers by 1 makes them meet at loop start!

Time Complexity: O(n) - we traverse the list a constant number of times
Space Complexity: O(1) - only using two pointers

================================================================================
FLOWCHART:
================================================================================

    START
      |
      v
    Initialize:
    slow = head
    fast = head
      |
      v
    +----------------------------------+
    | PHASE 1: DETECT LOOP             |
    +----------------------------------+
      |
      v
    +----------------------------------+
    | fast!=NULL && fast.next!=NULL?  |-----> NO ----> No loop, RETURN
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
    +--------------+
    | slow == fast?|-----> NO ----> Loop back to check
    +--------------+
      |
     YES (Loop detected!)
      |
      v
    +----------------------------------+
    | PHASE 2: FIND & REMOVE LOOP      |
    +----------------------------------+
      |
      v
    +--------------+
    | slow == head?|
    +--------------+
      |         |
     YES       NO
      |         |
      |         v
      |    Reset slow = head
      |         |
      |         v
      |    +---------------------------+
      |    | slow.next != fast.next?   |-----> NO
      |    +---------------------------+         |
      |         |                               |
      |        YES                              |
      |         |                               |
      |         v                               |
      |    slow = slow.next                     |
      |    fast = fast.next                     |
      |         |                               |
      |         +---(Loop back)                 |
      |                                         |
      v                                         v
    Move fast until                       Set fast.next = NULL
    fast.next == head                     (Break the loop!)
      |                                         |
      v                                         v
    Set fast.next = NULL                      END
    (Break the loop!)
      |
      v
    END


    VISUAL EXAMPLE - Case B (Loop in middle):

    Original with loop:
    1 -> 2 -> 3 -> 4 -> 5
              ^         |
              |_________|

    Step 1: Detect loop (slow and fast meet at node 5)

    Step 2: Reset slow to head
    slow at 1, fast at 5

    Step 3: Move both by 1 until slow.next == fast.next
    Iteration 1: slow at 1, fast at 5 (slow.next=2, fast.next=3) ✗
    Iteration 2: slow at 2, fast at 3 (slow.next=3, fast.next=4) ✗
    Iteration 3: slow at 3, fast at 4 (slow.next=4, fast.next=5) ✗
    Iteration 4: slow at 4, fast at 5 (slow.next=5, fast.next=3) ✗
    Iteration 5: slow at 5, fast at 3 (slow.next=3, fast.next=4) ✗
    Iteration 6: slow at 3, fast at 4 (slow.next=4, fast.next=5) ✗

    Wait, let me reconsider...

    After meeting at a point, if we reset slow to head and move both by 1,
    they will meet at the loop start (node 3).
    Then we need to find the node whose next is the loop start.

================================================================================
"""

class Solution:
    """
    Solution class to remove loop from a linked list.
    """

    def delete_loop(self, head):
        """
        Remove loop from a linked list if it exists.

        Args:
            head: The head node of the linked list

        Returns:
            None (modifies the list in-place)

        Algorithm:
        1. Use Floyd's algorithm to detect if loop exists
        2. If loop detected, find the starting node of the loop
        3. Find the node just before the loop start
        4. Set its next pointer to NULL

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1) - only using two pointers

        Special Cases:
        - If loop starts at head: fast.next should point to NULL
        - If loop starts in middle: move both pointers to find loop start
        """

        # PHASE 1: Detect if loop exists using Floyd's Algorithm
        low = head   # Slow pointer (tortoise)
        high = head  # Fast pointer (hare)

        # Move slow by 1 and fast by 2 until they meet or fast reaches end
        while high != None and high.next != None:
            low = low.next           # Move slow by 1 step
            high = high.next.next    # Move fast by 2 steps

            # If they meet, loop exists - break to proceed to removal
            if low == high:
                break

        # PHASE 2: Remove the loop

        # CASE A: Loop starts at head node itself
        # This happens when the last node points back to head
        if low == head:
            # Move high pointer around the loop until we find the node
            # whose next is the head (that's the last node in the loop)
            while high.next != low:
                high = high.next

            # Break the loop by setting last node's next to NULL
            high.next = None

        # CASE B: Loop exists and starts somewhere in the middle
        elif low == high:  # Confirming loop was detected
            # Reset low to head to find the loop start
            low = head

            # Move both pointers by 1 step until their next nodes match
            # When slow.next == fast.next, they're both pointing to the
            # node just before the loop start
            while low.next != high.next:
                low = low.next
                high = high.next

            # Now both low.next and high.next point to the loop start
            # high is the last node in the loop, so break the cycle
            high.next = None


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Should I modify the list in-place or create a new list? (In-place)
   - What should I do if there's no loop? (Return without changes)
   - What if the list is empty? (Return as-is)
   - Can the loop start at the head? (Yes, handle this case)

2. Edge Cases to Consider:
   - Empty list (head is None) → return immediately
   - No loop exists → fast reaches NULL, no changes needed
   - Single node pointing to itself → special case of loop at head
   - Loop starts at head vs loop starts in middle → different logic
   - Two nodes forming a loop

3. Common Mistakes to Avoid:
   - Not checking if loop was actually detected before trying to remove it
   - Forgetting to handle the case where loop starts at head
   - Not moving pointers correctly when finding loop start
   - Trying to access .next without checking for NULL
   - Breaking the loop at wrong position

4. Why Two Cases?
   - Case A (loop at head): The meeting point calculation doesn't work
     when the loop encompasses the entire list
   - Case B (loop in middle): We can use the mathematical property that
     distance from head to start = distance from meeting point to start

5. Follow-up Questions You Might Get:
   Q: Can you also return the starting node of the loop?
   A: Yes, return low.next (or high.next) instead of setting it to NULL

   Q: What if we need to detect AND remove in O(1) space?
   A: This solution already does that!

   Q: Can you find the length of the loop before removing?
   A: Yes, after detecting loop, keep one pointer fixed and move the other
      until they meet again, counting steps

   Q: What if we're allowed to modify node values?
   A: We could mark visited nodes, but pointer approach is better

6. Related Problems:
   - Problem 2: Detect loop (this is step 1 of current problem)
   - Problem 4: Find first node of loop (similar approach, different output)
   - Remove cycle in directed graph (similar concept)

7. Time to Solve: Aim for 15-20 minutes including both cases and edge cases

8. Interview Strategy:
   - Start by explaining Floyd's algorithm for detection
   - Draw the two cases on whiteboard to visualize
   - Explain the mathematical reasoning for Case B
   - Code and test both cases
   - Discuss edge cases

9. Key Points to Mention:
   - This is a two-phase algorithm: detect, then remove
   - The mathematical property that makes finding loop start work
   - Why we need to handle loop-at-head as a special case
   - Time complexity is still O(n) despite looking like nested loops
     (we traverse the list at most 3 times)

================================================================================
"""
