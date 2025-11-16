"""
================================================================================
PROBLEM: Split a Circular Linked List into Two Halves
================================================================================

DESCRIPTION:
Given a circular linked list of size N, split it into two halves. Both
resulting lists should also be circular lists (not linear lists).

If there are odd number of nodes, the first list should have one node more
than the second list.

Input:  1 -> 2 -> 3 -> 4 -> 5 -> (back to 1)  [5 nodes - odd]
Output:
    List 1: 1 -> 2 -> 3 -> (back to 1)  [3 nodes]
    List 2: 4 -> 5 -> (back to 4)       [2 nodes]

Input:  1 -> 2 -> 3 -> 4 -> (back to 1)  [4 nodes - even]
Output:
    List 1: 1 -> 2 -> (back to 1)  [2 nodes]
    List 2: 3 -> 4 -> (back to 3)  [2 nodes]

================================================================================
APPROACH & REASONING:
================================================================================

SLOW/FAST POINTER APPROACH:

The algorithm uses the slow/fast pointer technique to find the middle of the
circular linked list, then splits it while maintaining the circular property.

Algorithm Steps:
1. Find the middle of the circular list using slow/fast pointers
2. For odd-length: fast.next == head (fast completes one round)
3. For even-length: fast.next.next == head
4. Split the list at the middle
5. Make both halves circular

Time Complexity: O(n) - single pass to find middle
Space Complexity: O(1) - only using pointers

Why this works:
- Slow/fast pointers help find middle in one traversal
- For circular list, we check when fast completes the circle
- After finding middle, we carefully adjust pointers to:
  * Make first half circular (slow.next = head)
  * Make second half circular (fast.next = slow.next)

Key Considerations:
- Both halves MUST be circular (not linear)
- Odd length: first half gets extra node
- Even length: both halves have equal nodes
- Empty list: handle gracefully

================================================================================
FLOWCHART:
================================================================================

    split(head1, head2)
          |
          v
    +------------------+
    | self.head==NULL? |-----> YES ----> return
    +------------------+
          |
         NO
          |
          v
    Initialize:
    slow = self.head
    fast = self.head
          |
          v
    +----------------------------------------+
    | fast.next != self.head &&              |-----> NO (middle found)
    | fast.next.next != self.head?           |
    +----------------------------------------+
          |
         YES
          |
          v
    Move pointers:
    slow = slow.next
    fast = fast.next.next
          |
          +----(Loop back)
          |
          v
    +---------------------------+
    | fast.next.next == head?   |-----> YES (even length)
    +---------------------------+         |
          |                               |
         NO (odd length)                  v
          |                          fast = fast.next
          +------------+-------------+
                       |
                       v
            Set up two circular lists:
            head1 = self.head
            head2 = slow.next (if exists)
            fast.next = slow.next
            slow.next = self.head
                       |
                       v
                     return


    VISUAL EXAMPLE - ODD LENGTH (5 nodes):

    Original: 1 -> 2 -> 3 -> 4 -> 5 -> (back to 1)

    Finding middle:
    Initial:  slow,fast at 1
    Step 1:   slow at 2, fast at 3
    Step 2:   slow at 3, fast at 5
    fast.next == head, stop

    After split:
    List 1: 1 -> 2 -> 3 -> (back to 1)
                     ↑     |
                     |_____|
    List 2: 4 -> 5 -> (back to 4)
                ↑    |
                |____|


    VISUAL EXAMPLE - EVEN LENGTH (4 nodes):

    Original: 1 -> 2 -> 3 -> 4 -> (back to 1)

    Finding middle:
    Initial:  slow,fast at 1
    Step 1:   slow at 2, fast at 3
    fast.next.next == head, stop
    Move fast to 4

    After split:
    List 1: 1 -> 2 -> (back to 1)
               ↑     |
               |_____|
    List 2: 3 -> 4 -> (back to 3)
               ↑     |
               |_____|

================================================================================
"""

class Node:
    """
    Node class representing a single element in the circular linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    """
    CircularLinkedList class with methods to manage a circular linked list
    and split it into two halves.
    """
    def __init__(self):
        self.head = None

    def push(self, data):
        """
        Insert a new node at the beginning of the circular linked list.

        Args:
            data: Value to be stored in the new node

        Algorithm:
        1. Create new node
        2. If list is empty, make it point to itself
        3. Otherwise, find last node and update pointers

        Time Complexity: O(n) - need to find last node
        Space Complexity: O(1)
        """
        # Create new node with given data
        ptr = Node(data)
        temp = self.head

        # Make new node point to current head
        # (will be correct even if list becomes circular)
        ptr.next = self.head

        # If list is not empty, find the last node
        if self.head is not None:
            # Traverse to find the last node (whose next is head)
            while temp.next != self.head:
                temp = temp.next
            # Update last node to point to new node
            temp.next = ptr
        else:
            # List is empty - make new node point to itself
            ptr.next = ptr

        # Update head to new node
        self.head = ptr

    def split(self, head1, head2):
        """
        Split the circular linked list into two circular halves.

        For odd number of nodes, first list gets the extra node.
        Both resulting lists are circular (not linear).

        Args:
            head1: Will store head of first half (passed by reference)
            head2: Will store head of second half (passed by reference)

        Algorithm:
        1. Use slow/fast pointers to find the middle
        2. For odd length: fast.next == head when middle found
        3. For even length: fast.next.next == head when middle found
        4. Split and make both halves circular

        Time Complexity: O(n) where n is number of nodes
        Space Complexity: O(1)

        Example:
            Input: 1->2->3->4->5->(to 1)
            Output: head1: 1->2->3->(to 1), head2: 4->5->(to 4)
        """
        # Edge case: empty list
        if self.head is None:
            return

        # Initialize slow and fast pointers
        slow = self.head
        fast = self.head

        # PHASE 1: Find the middle of the circular list
        # For odd nodes: fast.next will be head when slow is at middle
        # For even nodes: fast.next.next will be head when slow is at middle
        while fast.next != self.head and fast.next.next != self.head:
            # Move slow by one step
            slow = slow.next
            # Move fast by two steps
            fast = fast.next.next

        # PHASE 2: Adjust for even-length list
        # If even number of nodes, move fast to the actual last node
        if fast.next.next == self.head:
            fast = fast.next

        # PHASE 3: Set up the first half
        # First half starts at original head
        head1 = self.head

        # PHASE 4: Set up the second half
        # Second half starts after slow (the middle node)
        if self.head.next != self.head:
            # Only create second half if there's more than one node
            head2 = slow.next

        # PHASE 5: Make second half circular
        # Last node of original list (fast) should point to start of second half
        fast.next = slow.next

        # PHASE 6: Make first half circular
        # Middle node (slow) should point back to head
        slow.next = self.head


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - For odd-length lists, which half gets extra node? (Usually first half)
   - Should both resulting lists be circular? (YES - critical requirement)
   - What if list is empty? (Return without doing anything)
   - What if list has only one node? (First half gets it, second is empty)
   - Should we modify original list or create new lists? (Modify is fine)

2. Edge Cases to Consider:
   - Empty list → return immediately
   - Single node → first half gets it, second half empty
   - Two nodes → each half gets one node
   - Odd number of nodes → first half gets extra
   - Even number of nodes → equal split
   - Very large circular list

3. Common Mistakes to Avoid:
   - Making resulting lists linear instead of circular
   - Not handling odd vs even length correctly
   - Infinite loop in slow/fast pointer logic
   - Not checking for head.next != head condition
   - Forgetting to make fast point to last node for even length
   - Off-by-one errors in pointer assignments

4. Key Insights:
   - The condition fast.next != head detects odd length
   - The condition fast.next.next != head detects even length
   - Must make BOTH halves circular (not just one)
   - For odd length, slow naturally stops at middle
   - For even length, need to move fast one more step

5. Follow-up Questions You Might Get:
   Q: How would you split into three parts?
   A: Find nodes at n/3 and 2n/3 positions, split there

   Q: What if we want linear lists instead?
   A: Just set last nodes of each half to NULL instead of making circular

   Q: How to verify both halves are circular?
   A: Traverse each list and check if you return to head

   Q: Can you merge two circular lists?
   A: Yes, find last nodes of each, connect them appropriately

   Q: What if first half should be smaller for odd length?
   A: Adjust the slow/fast initialization or move slow one more step

6. Time to Solve: Aim for 15-20 minutes including making both halves circular

7. Key Points to Mention in Interview:
   - Explain slow/fast pointer technique for finding middle
   - Discuss difference between odd and even length handling
   - Emphasize that both halves MUST be circular
   - Walk through pointer adjustments carefully
   - Draw diagrams to show before/after states

8. Testing Strategy:
   - Test with empty list
   - Test with single node
   - Test with two nodes
   - Test with odd length (3, 5, 7 nodes)
   - Test with even length (4, 6, 8 nodes)
   - Verify circularity of both resulting lists

9. Why This Problem is Important:
   - Tests understanding of circular linked lists
   - Combines multiple concepts (slow/fast pointers, circular lists)
   - Requires careful pointer manipulation
   - Common in systems programming (buffer management)

10. Related Problems:
    - Find middle of circular list
    - Merge two circular lists
    - Convert circular to linear list
    - Detect if list is circular
    - Rotate circular list

================================================================================
"""
