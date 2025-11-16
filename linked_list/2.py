"""
================================================================================
PROBLEM: Detect Loop/Cycle in Linked List
================================================================================

DESCRIPTION:
Given a linked list, determine if it has a cycle in it.
A cycle exists if a node's next pointer points back to a previous node,
creating a loop in the list.

Input:  1 -> 2 -> 3 -> 4 -> 5
                  ^         |
                  |_________|
Output: True (there is a cycle)

Input:  1 -> 2 -> 3 -> NULL
Output: False (no cycle)

================================================================================
APPROACH & REASONING:
================================================================================

We'll discuss two approaches:

1. FLOYD'S CYCLE-FINDING ALGORITHM (Tortoise and Hare) - RECOMMENDED
   - Use two pointers: slow (moves 1 step) and fast (moves 2 steps)
   - If there's a cycle, fast will eventually meet slow
   - If there's no cycle, fast will reach NULL

   Time Complexity: O(n)
   Space Complexity: O(1)

   Why this works (Mathematical proof):
   - If there's a cycle, both pointers will eventually enter it
   - Once in the cycle, the fast pointer gains on slow by 1 step each iteration
   - The distance between them decreases by 1 each time
   - They must eventually meet (distance becomes 0)

2. MODIFICATION APPROACH (Less preferred - modifies data):
   - Mark visited nodes by negating their data
   - If we encounter a negative value, we've seen it before
   - This modifies the list, which is generally not acceptable

   Time Complexity: O(n)
   Space Complexity: O(1)
   Drawback: Modifies original data, doesn't work with all data types

================================================================================
FLOWCHART - FLOYD'S CYCLE-FINDING ALGORITHM:
================================================================================

           START
             |
             v
    +----------------+
    | head == NULL?  |-----> YES ----> return False
    +----------------+
             |
            NO
             |
             v
    Initialize:
    slow = head
    fast = head
             |
             v
    +----------------------------------+
    | fast!=NULL && fast.next!=NULL?  |-----> NO ----> return False
    +----------------------------------+                 (no cycle)
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
    | slow == fast?|-----> YES ----> return True
    +--------------+                  (cycle detected!)
             |
            NO
             |
             +----(Loop back to condition)


    VISUAL EXAMPLE - Why Fast and Slow Pointers Work:

    List with cycle:  1 -> 2 -> 3 -> 4 -> 5
                                ^         |
                                |_________|

    Iteration 1:  slow at 1, fast at 1
    Iteration 2:  slow at 2, fast at 3
    Iteration 3:  slow at 3, fast at 5
    Iteration 4:  slow at 4, fast at 4  ← MEET! Cycle detected

    Without cycle: 1 -> 2 -> 3 -> 4 -> NULL

    Iteration 1:  slow at 1, fast at 1
    Iteration 2:  slow at 2, fast at 3
    Iteration 3:  slow at 3, fast at NULL  ← fast reaches end, no cycle

================================================================================
"""

class Solution:
    """
    Solution class containing methods to detect loops in a linked list.
    """

    def floyd_cycle(self, head):
        """
        Detect loop using Floyd's Cycle-Finding Algorithm (Tortoise and Hare).

        This is the RECOMMENDED approach for interviews.

        Args:
            head: The head node of the linked list

        Returns:
            True if cycle exists, False otherwise

        Algorithm:
        1. Initialize two pointers (slow and fast) at head
        2. Move slow by 1 step, fast by 2 steps
        3. If they meet, there's a cycle
        4. If fast reaches NULL, there's no cycle

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1) - only two pointers used

        Why it's called Tortoise and Hare:
        - Slow pointer is the tortoise (moves slowly, 1 step)
        - Fast pointer is the hare (moves quickly, 2 steps)
        - If there's a circular track, the hare will lap the tortoise
        """
        # Edge case: empty list has no cycle
        if head is None:
            return False

        # Initialize both pointers at the start
        slow = head  # Tortoise: moves 1 step at a time
        fast = head  # Hare: moves 2 steps at a time

        # Continue until fast pointer reaches the end
        # We check both fast and fast.next to avoid NoneType error
        while fast != None and fast.next != None:
            # Move slow pointer by 1 step
            slow = slow.next

            # Move fast pointer by 2 steps
            fast = fast.next.next

            # If pointers meet, there's a cycle
            if slow == fast:
                return True

        # If fast reached NULL, there's no cycle
        return False

    def detectLoop(self, head):
        """
        Detect loop by modifying node data (marks visited nodes as negative).

        WARNING: This approach modifies the original list data.
        Only use if explicitly allowed in the problem.

        Args:
            head: The head node of the linked list

        Returns:
            True if cycle exists, False otherwise

        Algorithm:
        1. Traverse the list
        2. Mark each visited node by negating its data
        3. If we encounter a negative value, it's already visited (cycle!)
        4. If we reach NULL, no cycle exists

        Time Complexity: O(n)
        Space Complexity: O(1)

        Limitations:
        - Modifies original data (usually not acceptable)
        - Doesn't work if data can naturally be negative
        - Doesn't work with non-numeric data
        """
        curr = head

        # Traverse the list
        while curr is not None:
            # Check if this node was already visited
            # (indicated by negative data value)
            if curr.data > 0:
                # First visit: mark as visited by negating
                curr.data *= -1
            else:
                # Already negative means we've been here before!
                return True

            # Move to next node
            curr = curr.next

        # Reached end without finding visited node
        return False


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. ALWAYS use Floyd's Cycle-Finding Algorithm unless asked otherwise
   - It doesn't modify the list
   - It works with any data type
   - It's elegant and efficient

2. Clarification Questions to Ask:
   - Can I modify the original list? (Usually NO)
   - What should I return if the list is empty? (Usually False)
   - Should I also find the start of the cycle? (Different problem, but related)

3. Edge Cases to Handle:
   - Empty list (head is None) → return False
   - Single node with no cycle → return False
   - Single node pointing to itself → return True
   - Two nodes forming a cycle → return True

4. Common Mistakes to Avoid:
   - Not checking if fast.next is None before accessing fast.next.next
   - Starting slow and fast at different positions
   - Incrementing pointers before checking if they're equal

5. Follow-up Questions You Might Get:
   Q: Can you find the starting point of the cycle?
   A: Yes, reset slow to head after detection, move both by 1 until they meet

   Q: Can you find the length of the cycle?
   A: Yes, after detecting cycle, keep one pointer fixed and move the other
      until they meet again, counting steps

   Q: What if we can use extra space?
   A: Use a hash set to store visited nodes - simpler but O(n) space

6. Why Floyd's Algorithm is Genius:
   - Inspired by the mathematical concept of periodic sequences
   - Guarantees meeting if there's a cycle (distance decreases by 1 each step)
   - No false positives - can only meet if there's actually a cycle

7. Time to Solve: Aim for 10-12 minutes including edge cases

8. Code Template to Remember:
   ```
   slow = fast = head
   while fast and fast.next:
       slow = slow.next
       fast = fast.next.next
       if slow == fast:
           return True
   return False
   ```

================================================================================
"""