"""
================================================================================
PROBLEM: Find Nth Node from End of Linked List
================================================================================

DESCRIPTION:
Given a linked list and a number n, find the value of the nth node from the
end of the linked list. If n is greater than the size of the list, return -1.

Input:  1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> NULL, n = 2
Output: 8 (2nd node from end is 8)

Input:  1 -> 2 -> 3 -> 4 -> 5 -> NULL, n = 5
Output: 1 (5th node from end is the first node)

Input:  1 -> 2 -> 3 -> NULL, n = 5
Output: -1 (n is greater than list length)

Note: Indexing is 1-based from the end. The last node is the 1st from end.

================================================================================
APPROACH & REASONING:
================================================================================

We'll discuss two approaches:

1. TWO-PASS APPROACH (Current Implementation):
   - First pass: Calculate the length of the list
   - Second pass: Move (length - n) steps from the beginning
   - Return the data at that position

   Time Complexity: O(n) - two passes through the list
   Space Complexity: O(1) - only using a few variables

   Why this works:
   - The nth node from end is the (length - n + 1)th node from beginning
   - We need length to calculate this position
   - After finding length, we can directly navigate to the target

2. TWO-POINTER APPROACH (More Elegant - One Pass):
   - Use two pointers: fast and slow
   - Move fast pointer n steps ahead
   - Then move both pointers together until fast reaches end
   - Slow pointer will be at nth node from end

   Time Complexity: O(n) - single pass
   Space Complexity: O(1)

   Why this works:
   - Maintaining a gap of n nodes between pointers
   - When fast reaches the end, slow is n nodes behind (from end)
   - This is a classic linked list technique

================================================================================
FLOWCHART - TWO-PASS APPROACH:
================================================================================

    getNthFromLast(head, n)
              |
              v
    PHASE 1: Calculate Length
    Initialize: l = 0, curr = head
              |
              v
    +------------------+
    | curr != NULL?    |-----> NO (length calculated)
    +------------------+        |
              |                 |
             YES                |
              |                 |
              v                 |
         l += 1                 |
         curr = curr.next       |
              |                 |
              +---(Loop)        |
                                |
                                v
                         +-------------+
                         | n > l ?     |-----> YES ----> return -1
                         +-------------+
                                |
                               NO
                                |
                                v
                         PHASE 2: Find Node
                         temp = head
                         Loop (l - n) times:
                            temp = temp.next
                                |
                                v
                         return temp.data


    VISUAL EXAMPLE:

    List: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> NULL
          Find 2nd node from end (n=2)

    Phase 1: Count length
    Length = 9

    Phase 2: Calculate position
    Position from start = length - n = 9 - 2 = 7
    (7th node from start is 2nd node from end)

    Move 7 steps:
    1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
                                        ^
                                    7th node = 8

================================================================================
FLOWCHART - TWO-POINTER APPROACH (ALTERNATIVE):
================================================================================

    getNthFromLast_TwoPointer(head, n)
              |
              v
    Initialize:
    fast = head
    slow = head
              |
              v
    Move fast n steps ahead
    for i in range(n):
        if fast == NULL:
            return -1 (n > length)
        fast = fast.next
              |
              v
    +-------------------------+
    | fast != NULL?           |-----> NO
    +-------------------------+        |
              |                        |
             YES                       |
              |                        |
              v                        |
    slow = slow.next                  |
    fast = fast.next                  |
              |                        |
              +---(Loop)               |
                                       |
                                       v
                                return slow.data


    VISUAL EXAMPLE - TWO POINTER:

    List: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> NULL
          Find 2nd from end (n=2)

    Step 1: Move fast 2 steps ahead
    slow
     v
     1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> NULL
               ^
              fast

    Step 2: Move both until fast reaches end
                                        slow
                                         v
     1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> NULL
                                              ^
                                             fast

    slow is at 8 (2nd from end) ✓

================================================================================
"""

def getNthFromLast(head, n):
    """
    Find the nth node from the end of a linked list using two-pass approach.

    Args:
        head: Head node of the linked list
        n: Position from the end (1-based indexing)

    Returns:
        Data value of the nth node from end, or -1 if n > length

    Algorithm:
    1. First pass: Calculate the total length of the list
    2. Check if n is valid (n <= length)
    3. Second pass: Move (length - n) steps from head
    4. Return the data at that position

    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(1) - only using constant extra space

    Example:
        List: 1 -> 2 -> 3 -> 4 -> 5, n = 2
        Result: 4 (2nd from end)
    """
    # PHASE 1: Calculate the length of the linked list
    l = 0        # Length counter
    curr = head  # Pointer for traversal

    # Traverse entire list to count nodes
    while curr != None:
        l += 1              # Increment counter
        curr = curr.next    # Move to next node

    # VALIDATION: Check if n is within valid range
    # If n > length, the nth node from end doesn't exist
    if n > l:
        return -1

    # PHASE 2: Navigate to the nth node from end
    # The nth node from end is at position (l - n) from start
    # Example: If length=5 and n=2, we need node at position 5-2=3 from start
    temp = head

    # Move (l - n) steps from the beginning
    for i in range(l - n):
        temp = temp.next

    # temp now points to the nth node from end
    return temp.data


def getNthFromLast_TwoPointer(head, n):
    """
    Find the nth node from end using two-pointer technique (one-pass solution).

    This is an alternative, more elegant approach that uses only one pass.

    Args:
        head: Head node of the linked list
        n: Position from the end (1-based indexing)

    Returns:
        Data value of the nth node from end, or -1 if n > length

    Algorithm:
    1. Initialize two pointers: fast and slow at head
    2. Move fast pointer n steps ahead
    3. Move both pointers together until fast reaches end
    4. Slow pointer will be at nth node from end

    Time Complexity: O(n) - single pass
    Space Complexity: O(1)

    Example:
        List: 1 -> 2 -> 3 -> 4 -> 5, n = 2
        After moving fast 2 steps: fast at 3, slow at 1
        After moving both: fast at None, slow at 4
        Result: 4
    """
    # Initialize both pointers at head
    fast = head
    slow = head

    # PHASE 1: Move fast pointer n steps ahead
    for i in range(n):
        # If fast becomes None before n steps, n > length
        if fast == None:
            return -1
        fast = fast.next

    # PHASE 2: Move both pointers until fast reaches end
    # Maintain gap of n nodes between them
    while fast != None:
        slow = slow.next
        fast = fast.next

    # Now slow is at nth node from end
    return slow.data


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Is n 1-based or 0-based? (Usually 1-based: last node is 1st from end)
   - What should we return if n > length? (Usually -1 or None)
   - What if the list is empty? (Return -1)
   - Should we return the node or just the data? (Usually data)
   - Can n be 0 or negative? (Usually no, but clarify)

2. Edge Cases to Consider:
   - Empty list (return -1)
   - n = 1 (last node)
   - n = length (first node)
   - n > length (return -1)
   - n = 0 or negative (usually invalid, return -1)
   - Single node list with n = 1 (return that node)

3. Common Mistakes to Avoid:
   - Off-by-one errors in counting (1-based vs 0-based)
   - Not checking if fast becomes None in two-pointer approach
   - Confusing "from end" with "from beginning"
   - Not handling case when n > length
   - Moving the wrong number of steps

4. Why Two-Pointer Approach is Better:
   - Single pass instead of two passes
   - More elegant and interview-friendly
   - Demonstrates understanding of pointer manipulation
   - Same time complexity but better constant factor
   - Common pattern in many linked list problems

5. Follow-up Questions You Might Get:
   - Can you do it in one pass? (Yes, two-pointer approach)
   - What if you need to delete the nth node from end?
     (Use two pointers with n+1 gap, or find and delete)
   - How would you find the middle node?
     (Two pointers with 2x speed difference)
   - What if the list is doubly linked?
     (Can traverse from tail, simpler)
   - Can you do this without calculating length?
     (Yes, two-pointer approach)

6. Related Problems:
   - Remove nth node from end (LeetCode 19)
   - Find middle of linked list
   - Detect cycle in linked list (Floyd's algorithm)
   - Rotate list by k positions

7. Time to Solve: Aim for 10-12 minutes including edge cases

8. Which Approach to Present in Interview:
   - Start with two-pass approach (simpler to explain)
   - If asked for optimization, present two-pointer approach
   - Or directly present two-pointer and explain both
   - Discuss trade-offs (both are O(n) time, O(1) space)

9. Key Insight:
   - Two-pointer technique with fixed gap is powerful
   - "nth from end" = "maintain gap of n, move together"
   - This pattern appears in many problems

10. Implementation Tips:
    - Always validate input (n > 0, n <= length)
    - Use clear variable names (fast/slow or lead/follow)
    - Handle None checks carefully
    - Test with small examples first

================================================================================
"""
