"""
================================================================================
PROBLEM: Rotate Doubly Linked List by N Nodes
================================================================================

DESCRIPTION:
Given a doubly linked list and a number N, rotate the doubly linked list
counter-clockwise by N nodes. Rotating by N nodes means that the first N
nodes move to the end of the list.

Input:  a <-> b <-> c <-> d <-> e, N = 2
Output: c <-> d <-> e <-> a <-> b

Explanation: The first 2 nodes (a, b) are moved to the end.

Input:  1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6, N = 3
Output: 4 <-> 5 <-> 6 <-> 1 <-> 2 <-> 3

================================================================================
APPROACH & REASONING:
================================================================================

OPTIMAL APPROACH: Break and Reconnect

Key Insight:
- We need to identify three key positions:
  1. The (N+1)th node - this becomes the new head
  2. The Nth node - this will become the new tail
  3. The original tail - needs to connect to the original head

Algorithm Steps:
1. Find the (N+1)th node which will be the new head
2. The Nth node will be the new tail (end of the rotated list)
3. Find the current tail of the list
4. Connect current tail to original head
5. Break the link at Nth node
6. Set (N+1)th node as new head

Time Complexity: O(n) where n is the number of nodes
   - O(n) to find the Nth node
   - O(n) to find the tail
   - O(1) for reconnections
   - Overall: O(n)

Space Complexity: O(1) - only using a few pointers

Why this works:
- Rotation is essentially moving a portion from start to end
- Doubly linked list allows us to easily reconnect in both directions
- We just need to carefully update the next and prev pointers

================================================================================
FLOWCHART:
================================================================================

    rotate(N)
          |
          v
    Initialize:
    newHead = head
    prev = NULL
          |
          v
    Loop N times:
    +----------------+
    | i < N?         |-----> NO
    +----------------+         |
          |                    |
         YES                   |
          |                    |
          v                    |
    prev = newHead             |
    newHead = newHead.next     |
    i++                        |
          |                    |
          +---(Loop back)      |
                               |
                               v
    prev.next = NULL (cut after Nth node)
    newHead.prev = NULL (new head has no prev)
          |
          v
    Find tail:
    curr = newHead
    while curr.next != NULL:
          curr = curr.next
          |
          v
    Connect tail to old head:
    curr.next = head
    head.prev = curr
          |
          v
    Update head:
    head = newHead
          |
          v
         END


    VISUAL EXAMPLE (N = 2):

    Original: a <-> b <-> c <-> d <-> e
              ^         ^              ^
              head    newHead       tail

    Step 1: Identify positions after N iterations
            prev = b (Nth node)
            newHead = c (N+1th node)

    Step 2: Break the link at Nth node
            a <-> b    c <-> d <-> e
            ^          ^
            head     newHead

    Step 3: Find current tail (e)
            and connect to original head
            a <-> b <-+
            ^         |
            |         |
            +-> e <---+
                ^
                |
            c <-> d

    Step 4: Reconnect
            c <-> d <-> e <-> a <-> b
            ^
            new head

    Final: c <-> d <-> e <-> a <-> b

================================================================================
"""

class Node:
    """
    Node class for doubly linked list.

    Attributes:
        data: The value stored in the node
        next: Reference to the next node
        prev: Reference to the previous node
    """
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """
    DoublyLinkedList class with method to rotate by N nodes.

    Attributes:
        head: Reference to the first node in the list
    """
    def __init__(self):
        self.head = None

    def push(self, data):
        """
        Insert a new node at the beginning of the doubly linked list.

        Args:
            data: Value to be stored in the new node

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Create new node with given data
        temp = Node(data)

        # If list is empty, new node becomes the head
        if self.head == None:
            self.head = temp
        else:
            # Insert at the beginning
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    def printList(self):
        """
        Print all elements in the doubly linked list.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        temp = self.head
        res = ""
        while temp != None:
            res += str(temp.data) + " "
            temp = temp.next
        print(res)

    def rotate(self, n):
        """
        Rotate the doubly linked list counter-clockwise by N nodes.

        Rotation means the first N nodes are moved to the end of the list.
        The (N+1)th node becomes the new head.

        Args:
            n: Number of nodes to rotate (move from start to end)

        Algorithm:
        1. Traverse N nodes to find the new head (N+1th node)
        2. The Nth node (prev) will be the new tail
        3. Break the link: prev.next = NULL, newHead.prev = NULL
        4. Find the current tail of the remaining list
        5. Connect tail to original head
        6. Update head to newHead

        Time Complexity: O(n) where n is the number of nodes
            - O(n) to find the (N+1)th node
            - O(n-N) to find the tail
            - Overall: O(n)

        Space Complexity: O(1) - only using pointers

        Example:
            Input:  a <-> b <-> c <-> d <-> e, N = 2

            Step-by-step:
            1. newHead = c (3rd node)
            2. prev = b (2nd node, new tail)
            3. Break: a <-> b    c <-> d <-> e
            4. Find tail: e
            5. Connect: e.next = a, a.prev = e
            6. Result: c <-> d <-> e <-> a <-> b
        """
        # Initialize newHead to current head
        newHead = self.head
        prev = None

        # Phase 1: Find the (N+1)th node by moving N steps forward
        # After this loop:
        # - prev points to Nth node (will be new tail)
        # - newHead points to (N+1)th node (will be new head)
        for i in range(n):
            prev = newHead
            newHead = newHead.next  # Move to next node

        # Phase 2: Break the connection at Nth node
        # Nth node (prev) becomes the end of rotated portion
        prev.next = None

        # (N+1)th node (newHead) becomes start of new list
        # Remove its backward link to the first N nodes
        newHead.prev = None

        # Phase 3: Find the tail of the remaining list
        # Start from newHead and traverse to the end
        curr = newHead
        while curr.next != None:
            curr = curr.next

        # Phase 4: Connect the tail to the original head
        # This creates: (N+1 to end) <-> (1 to N)
        curr.next = self.head
        self.head.prev = curr

        # Phase 5: Update head to the new starting node
        self.head = newHead


# ============================================================================
# EXAMPLE EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Create a new doubly linked list
    dll = DoublyLinkedList()

    # Build list: a <-> b <-> c <-> d <-> e
    # (push adds to front, so we push in reverse order)
    dll.push('e')
    dll.push('d')
    dll.push('c')
    dll.push('b')
    dll.push('a')

    print("Before rotating:")
    dll.printList()  # Output: a b c d e

    # Rotate by 2 positions
    n = 2
    dll.rotate(n)

    print(f"After rotating by {n}:")
    dll.printList()  # Output: c d e a b

"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - What should happen if N = 0? (No rotation, return as-is)
   - What if N >= length of list? (Usually N = N % length)
   - Should we rotate left (counter-clockwise) or right? (Specify direction)
   - What if the list is empty or has one node? (Return as-is)
   - Can N be negative? (Negative means rotate in opposite direction)
   - Should we modify in-place or create new list? (Usually in-place)

2. Edge Cases to Consider:
   - Empty list (head is NULL) → no rotation needed
   - Single node → no rotation needed
   - N = 0 → no rotation needed
   - N = length of list → back to original (full rotation)
   - N > length of list → use N % length
   - N = 1 → second node becomes head, first node becomes tail

3. Common Mistakes to Avoid:
   - Not breaking the link at the Nth node (prev.next = NULL)
   - Not removing backward link (newHead.prev = NULL)
   - Forgetting to connect tail to original head
   - Not updating both next AND prev pointers
   - Accessing newHead.next when newHead is NULL (if N = length)
   - Off-by-one errors in counting N nodes

4. Alternative Approaches:
   a) Make circular, then break: O(n) time, O(1) space
      - Connect tail to head to make circular
      - Find new tail and break there
   b) Current approach: O(n) time, O(1) space - cleaner
   c) Using array: O(n) time, O(n) space - simpler but uses extra space

5. Optimization Considerations:
   - If N > length, compute N = N % length first
   - Could find length first, then handle N % length
   - For multiple rotations, consider making list circular temporarily

6. Follow-up Questions:
   - How would you rotate right instead of left?
     (Rotate by (length - N) nodes left, or traverse from end)
   - What if it's a singly linked list?
     (Same approach but can't set prev pointers)
   - Can you rotate in O(k) where k < n?
     (Yes, if we know the length in advance, we can optimize)
   - How would you handle N > length?
     (Find length first, then N = N % length)

7. Key Insight for Interview:
   Rotation is really about:
   - Identifying the break point (Nth node)
   - Making the connection circular
   - Breaking at the new tail position
   - The doubly linked structure makes reconnection easier

8. Time to Solve: Aim for 12-15 minutes including:
   - Understanding the problem: 2-3 minutes
   - Discussing approach: 3-4 minutes
   - Coding: 5-6 minutes
   - Testing with examples: 2-3 minutes

9. Comparison with Singly Linked List:
   Doubly Linked List:
   - Easier to maintain connections
   - Need to update both next and prev
   - Same time complexity O(n)

   Singly Linked List:
   - Only next pointers to update
   - Can't traverse backward
   - Same algorithm works

10. Real-world Applications:
    - Circular buffers
    - Round-robin scheduling
    - Playlist rotation
    - Token ring networks
    - Carousel/slideshow implementations

11. Testing Strategy:
    Test with these cases:
    - Empty list
    - Single node
    - N = 0
    - N = 1
    - N = length - 1
    - N = length
    - N > length
    - List with 2 nodes, N = 1

================================================================================
"""
