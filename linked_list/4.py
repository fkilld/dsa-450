"""
================================================================================
PROBLEM: Find First Node of Loop in Linked List
================================================================================

DESCRIPTION:
Given a linked list, determine if it has a cycle. If a cycle exists, return
a pointer to the first node of the cycle. If no cycle exists, return NULL.

Input:  1 -> 2 -> 3 -> 4 -> 5
                  ^         |
                  |_________|
Output: Pointer to node 3 (first node of the loop)

Input:  1 -> 2 -> 3 -> NULL
Output: NULL (no cycle exists)

This is different from just detecting a loop - we need to identify the exact
node where the cycle begins.

================================================================================
APPROACH & REASONING:
================================================================================

This problem uses Floyd's Cycle Detection Algorithm with an extension to
find the starting node of the cycle.

ALGORITHM STEPS:

1. DETECT LOOP (Floyd's Algorithm):
   - Use slow (1 step) and fast (2 steps) pointers
   - If they meet, a loop exists
   - If fast reaches NULL, no loop exists - return NULL

2. FIND LOOP START:
   After detecting a loop, there are two special cases:

   Case A: Loop starts at head (slow == head after detection)
   - Simply return head as it's the first node of the loop

   Case B: Loop starts somewhere in the middle
   - Reset slow to head (keep fast at meeting point)
   - Move both slow and fast by 1 step
   - When slow.next == fast.next, both point to node before loop start
   - Return slow.next (or fast.next) as the first node of loop

3. WHY THIS WORKS (Mathematical Proof):

   Let's define:
   - a = distance from head to loop start
   - b = distance from loop start to meeting point
   - c = remaining distance in loop (from meeting point to loop start)
   - L = loop length = b + c

   When slow and fast meet:
   - Slow traveled: a + b
   - Fast traveled: a + b + kL (where k >= 1, number of complete loops)
   - Since fast moves twice as fast: 2(a + b) = a + b + kL

   Solving:
   2a + 2b = a + b + kL
   a + b = kL
   a = kL - b = (k-1)L + (L - b) = (k-1)L + c

   This proves: Distance from head to loop start (a) equals
                Distance from meeting point to loop start (c)

   Therefore, if we move one pointer from head and another from meeting point,
   both moving one step at a time, they will meet at the loop start!

Time Complexity: O(n) - we traverse the list at most twice
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
    | fast!=NULL && fast.next!=NULL?  |-----> NO ----> return NULL
    +----------------------------------+                (no loop)
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
    | PHASE 2: FIND LOOP START         |
    +----------------------------------+
      |
      v
    +--------------+
    | slow == head?|-----> YES ----> return head
    +--------------+                  (loop starts at head)
      |
     NO
      |
      v
    Reset slow = head
    (keep fast at meeting point)
      |
      v
    +---------------------------+
    | slow.next != fast.next?   |-----> NO ----> return slow.next
    +---------------------------+                (found loop start!)
      |
     YES
      |
      v
    slow = slow.next
    fast = fast.next
      |
      +---(Loop back to check)


    VISUAL EXAMPLE - Case B (Loop in middle):

    Original with loop:
    1 -> 2 -> 3 -> 4 -> 5 -> 6
              ^              |
              |______________|

    Let a=2, b=2, c=2 (loop length L=4)

    Step 1: Detect loop using Floyd's algorithm
    - Slow and fast will meet somewhere in the loop

    Trace:
    Start:      slow=1, fast=1
    Move 1:     slow=2, fast=3
    Move 2:     slow=3, fast=5
    Move 3:     slow=4, fast=3  (fast wrapped around)
    Move 4:     slow=5, fast=5  ← MEET!

    Step 2: Find loop start
    Reset slow to head: slow=1, fast=5

    Move both by 1:
    Move 1:     slow=2, fast=6 (slow.next=3, fast.next=3) ✓
    Both next pointers point to node 3!

    Step 3: Return slow.next = node 3 (loop start)

    Verification: a = 2 (head to 3), c = 2 (node 5 to 3), a = c ✓

================================================================================
"""

class Solution:
    """
    Solution class to find the first node of a loop in a linked list.
    """

    def first_node(self, head):
        """
        Find and return the first node of the loop if it exists.

        Args:
            head: The head node of the linked list

        Returns:
            Pointer to the first node of the loop, or NULL if no loop exists

        Algorithm:
        1. Use Floyd's algorithm to detect if loop exists
        2. If no loop, return NULL
        3. If loop detected at head, return head
        4. If loop in middle, reset slow to head and move both by 1
           until slow.next == fast.next, then return slow.next

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1) - only using two pointers

        Example:
            Input:  1 -> 2 -> 3 -> 4 -> 5
                              ^         |
                              |_________|
            Output: node 3 (first node where cycle begins)
        """

        # PHASE 1: Detect if loop exists using Floyd's Algorithm
        low = head   # Slow pointer (tortoise)
        high = head  # Fast pointer (hare)

        # Move slow by 1 and fast by 2 until they meet or fast reaches end
        # Note: Check high.next first to avoid accessing .next.next on NULL
        while high.next != None and high != None:
            low = low.next           # Move slow by 1 step
            high = high.next.next    # Move fast by 2 steps

            # If they meet, loop exists - break to find start
            if low == high:
                break

        # PHASE 2: Find the first node of the loop

        # CASE A: Loop starts at head node itself
        # This happens when after detection, slow pointer is still at head
        # (only possible if entire list is one big loop)
        if low == head:
            return head

        # CASE B: Loop detected and starts somewhere in the middle
        elif low == high:  # Confirming loop was detected
            # Reset low to head to utilize the mathematical property:
            # Distance from head to loop start = Distance from meeting point to loop start
            low = head

            # Move both pointers by 1 step until their NEXT pointers match
            # When slow.next == fast.next, both are pointing to the node
            # just before the loop start
            while low.next != high.next:
                low = low.next
                high = high.next

            # Now both low.next and high.next point to the first node of loop
            # Return this node
            return high.next

        # CASE C: No loop detected (fast reached end of list)
        # If we reach here, the while loop exited because fast hit NULL
        return None


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - What should I return if there's no loop? (NULL/None)
   - What should I return if the list is empty? (NULL/None)
   - Should I return the node itself or just its value? (The node pointer)
   - Can the loop start at the head? (Yes, handle this case)

2. Edge Cases to Consider:
   - Empty list (head is None) → return None
   - Single node with no loop → return None
   - Single node pointing to itself → return that node (loop at head)
   - Two nodes forming a loop → could be loop at head or at second node
   - No loop exists → return None
   - Loop encompasses entire list vs loop in middle

3. Common Mistakes to Avoid:
   - Not checking if loop was actually detected before trying to find start
   - Accessing .next or .next.next without NULL checks
   - Forgetting the special case where loop starts at head
   - Returning the wrong node (node before loop start vs actual loop start)
   - Not handling the case when no loop exists

4. The Mathematical Insight (Interview Gold!):
   When explaining in interview, draw this diagram:

   head -> ... -> loop_start -> ... -> meeting_point -> ... -> loop_start
           |<-a->|            |<-b->|                |<-c->|

   - Slow travels: a + b
   - Fast travels: a + b + kL (k loops)
   - Since fast is 2x speed: 2(a+b) = a+b+kL
   - Therefore: a = kL - b = c (modulo loop length)

   This is why resetting to head and moving both by 1 works!

5. Follow-up Questions You Might Get:
   Q: Can you also remove the loop after finding it?
   A: Yes, continue from the node before loop start and set its next to NULL

   Q: What if we want to find the length of the loop?
   A: Keep fast at meeting point, move slow until it meets fast again, count steps

   Q: Can you solve this with extra space?
   A: Yes, use a hash set to track visited nodes (O(n) space, simpler logic)

   Q: What if list is very large and we want to optimize?
   A: This solution is already optimal - O(n) time and O(1) space

6. Related Problems:
   - Problem 2: Detect loop (this uses that as first phase)
   - Problem 3: Remove loop (this + one more step to remove)
   - Happy Number problem (uses similar cycle detection)
   - Linked List Cycle II (LeetCode 142 - same problem)

7. Time to Solve: Aim for 12-15 minutes including edge cases and explanation

8. Interview Strategy:
   - Start with Floyd's detection algorithm explanation
   - Draw the diagram showing a, b, c distances
   - Prove mathematically why resetting to head works
   - Code with clear comments for both cases
   - Test with examples: loop at head, loop in middle, no loop

9. Why This Problem is Important:
   - Tests understanding of two-pointer technique
   - Tests ability to prove algorithmic correctness
   - Common in FAANG interviews (Amazon, Microsoft especially)
   - Shows mathematical reasoning skills

10. Code Template to Remember:
    ```
    # Detect loop
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # Find start
    if slow == head:
        return head
    elif slow == fast:
        slow = head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        return slow.next
    return None
    ```

================================================================================
"""
