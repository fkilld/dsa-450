"""
================================================================================
PROBLEM: Reverse Doubly Linked List in Groups of Given Size
================================================================================

DESCRIPTION:
Given a doubly linked list and a positive integer k, reverse the nodes of the
list k at a time and return the modified list. If the number of nodes is not
a multiple of k, the left-out nodes at the end should also be reversed.

Input:  10 <-> 8 <-> 4 <-> 2, k = 2
Output: 8 <-> 10 <-> 2 <-> 4

Input:  1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6, k = 3
Output: 3 <-> 2 <-> 1 <-> 6 <-> 5 <-> 4

================================================================================
APPROACH & REASONING:
================================================================================

OPTIMAL APPROACH: Recursive Group Reversal with Pointer Swapping

Key Insight:
- For doubly linked lists, we can reverse by swapping next and prev pointers
- Process in groups of k nodes using recursion
- Each group is reversed independently, then connected to the next reversed group

Algorithm Steps:
1. For current group of k nodes:
   - Swap next and prev pointers for each node
   - Keep track of the first and last nodes of the group
2. Recursively reverse the remaining groups
3. Connect the current group to the result of the recursive call
4. Return the new head (which was the kth node of the current group)

Time Complexity: O(n) where n is the number of nodes
   - Visit each node exactly once
   - Constant work per node (pointer swapping)

Space Complexity: O(n/k) for recursion stack
   - Number of recursive calls = number of groups = n/k
   - Each call uses constant space

Why this works:
- Swapping next and prev pointers reverses the direction in doubly linked list
- Recursion handles the grouping naturally
- Connection between groups is maintained through proper pointer updates

Doubly vs Singly Linked List Reversal:
- Singly: Reverse the next pointers only
- Doubly: Swap next and prev pointers for each node
- Doubly requires updating both directions but makes reversal more elegant

================================================================================
FLOWCHART:
================================================================================

    reverse_by_k(head, k)
          |
          v
    +-------------+
    | head==NULL? |-----> YES ----> return NULL
    +-------------+
          |
         NO
          |
          v
    head.prev = NULL
    Initialize:
    curr = head
    next = NULL
    prev = NULL
    count = 0
          |
          v
    +-------------------------+
    | count<k && curr!=NULL?  |-----> NO
    +-------------------------+         |
          |                            |
         YES                           |
          |                            |
          v                            |
    Save next:                         |
    prev = curr                        |
    next = curr.next                   |
    Swap pointers:                     |
    curr.next = curr.prev              |
    curr.prev = next                   |
    Move forward:                      |
    curr = next                        |
    count++                            |
          |                            |
          +---(Loop back)              |
                                       |
                                       v
                              +---------------+
                              | next != NULL? |-----> NO ----> return prev
                              +---------------+
                                       |
                                      YES
                                       |
                                       v
                              Recursive call:
                              head.next = reverse_by_k(next, k)
                              head.next.prev = head
                                       |
                                       v
                                  return prev


    VISUAL EXAMPLE (k = 3):

    Original: 24 <-> 45 <-> 10 <-> 8 <-> 4 <-> 2

    Group 1: Reverse first 3 nodes
            Before: 24 <-> 45 <-> 10    8 <-> 4 <-> 2
            After:  10 <-> 45 <-> 24    8 <-> 4 <-> 2
                    ^                   ^
                    prev (new head)    next (recursively process)

    After swapping in first group:
            prev = 10 (was 3rd node, now head of group)
            head = 24 (was 1st node, now tail of group)
            next = 8 (start of next group)

    Group 2: Recursively process remaining (8 <-> 4 <-> 2)
            After:  2 <-> 4 <-> 8

    Connect groups:
            10 <-> 45 <-> 24 <-> 2 <-> 4 <-> 8
            ^
            Return this as new head

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
    DoublyLinkedList class with method to reverse in groups of size k.

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

    def reverse_by_k(self, head, k):
        """
        Reverse the doubly linked list in groups of size k using recursion.

        This is the doubly linked list version of group reversal. Unlike singly
        linked lists, we swap both next and prev pointers for each node.

        Args:
            head: The head node of the list/sublist to reverse
            k: The group size - number of nodes to reverse together

        Returns:
            The new head of the reversed list

        Algorithm:
        1. Set head.prev = NULL (head of sublist has no previous)
        2. For k nodes or until end of list:
           - Save next node reference
           - Swap curr.next and curr.prev (reverses the node)
           - Move to next node
        3. If more nodes exist, recursively reverse them
        4. Connect current group's tail to the reversed remaining groups
        5. Return the new head of current group

        Time Complexity: O(n) where n is the total number of nodes
        Space Complexity: O(n/k) for recursion stack depth

        Example:
            Input:  24 <-> 45 <-> 10 <-> 8 <-> 4 <-> 2, k = 3

            Group 1: [24, 45, 10]
            - Swap pointers: 10 <-> 45 <-> 24
            - prev = 10, head = 24, next = 8

            Group 2: [8, 4, 2] (recursive call)
            - Swap pointers: 2 <-> 4 <-> 8

            Connect:
            - 24.next = 2, 2.prev = 24

            Output: 10 <-> 45 <-> 24 <-> 2 <-> 4 <-> 8
        """
        # Base case: empty list
        if head == None:
            return None

        # The head of this sublist should have no previous node
        head.prev = None

        # Initialize pointers for reversing current group
        curr = head      # Current node being processed
        next = None      # Next node in original order
        prev = None      # Will track the new head of reversed group
        count = 0        # Counter to track k nodes

        # Phase 1: Reverse first k nodes by swapping next and prev pointers
        # This is the key difference from singly linked list reversal
        while count < k and curr != None:
            # Save current and next references before swapping
            prev = curr
            next = curr.next

            # SWAP POINTERS: This reverses the node's direction
            # Original: ... <-> curr <-> next <-> ...
            # After swap: ... <-> curr.prev <- curr -> curr.next
            # The swap makes curr point backward instead of forward
            curr.next = curr.prev  # Point to previous node
            curr.prev = next       # Previous pointer becomes next

            # Move to next node in original order
            curr = next
            count += 1

        # After the loop:
        # - 'prev' points to the last reversed node (new head of this group)
        # - 'head' points to what is now the tail of this reversed group
        # - 'next' points to the first node of the next group (or NULL)

        # Phase 2: Recursively reverse the remaining nodes
        if next != None:
            # Recursively reverse the next group
            # 'head' is now the tail of current group, connect it to next group's head
            head.next = self.reverse_by_k(next, k)

            # Maintain bidirectional link
            head.next.prev = head

        # Phase 3: Return the new head of this reversed group
        # 'prev' is the kth node of the original group, now the head
        return prev


# ============================================================================
# EXAMPLE EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Create a new doubly linked list
    dll = DoublyLinkedList()

    # Build list: 24 <-> 45 <-> 10 <-> 8 <-> 4 <-> 2
    # (push adds to front, so we push in reverse order)
    dll.push(2)
    dll.push(4)
    dll.push(8)
    dll.push(10)
    dll.push(45)
    dll.push(24)

    print("Original List:")
    dll.printList()  # Output: 24 45 10 8 4 2

    # Reverse in groups of 3
    k = 3
    print(f"\nReversed in groups of {k}:")
    dll.head = dll.reverse_by_k(dll.head, k)
    dll.printList()  # Output: 10 45 24 2 4 8

"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - What should happen if the last group has fewer than k nodes?
     (Usually: reverse them as well)
   - Should we modify the original list or create a new one?
     (Usually: modify in-place)
   - What if k is 1? (No change needed, return original list)
   - What if k >= length of list? (Reverse entire list)
   - Can k be 0 or negative? (Usually no, but handle edge case)
   - Is the list guaranteed to be non-empty? (Clarify before coding)

2. Edge Cases to Consider:
   - Empty list (head is NULL) → return NULL
   - Single node → return as-is
   - k = 1 → no reversal needed
   - k >= list length → reverse entire list
   - k = 2 with even/odd number of nodes
   - Last group has fewer than k nodes → still reverse them

3. Common Mistakes to Avoid:
   - Forgetting to set head.prev = NULL at the start
   - Not swapping BOTH next and prev pointers
   - Losing reference to the next group before processing current group
   - Forgetting to connect groups bidirectionally (both next and prev)
   - Not handling the last group when it has fewer than k nodes
   - Confusing singly and doubly linked list reversal logic

4. Key Differences from Singly Linked List:

   Singly Linked List Reversal:
   ```
   next = curr.next
   curr.next = prev
   prev = curr
   curr = next
   ```

   Doubly Linked List Reversal:
   ```
   prev = curr
   next = curr.next
   curr.next = curr.prev  # Swap
   curr.prev = next       # Swap
   curr = next
   ```

5. Alternative Approaches:
   a) Iterative with stack: O(k) extra space for each group
   b) Pure iterative: More complex pointer manipulation, O(1) space
   c) Recursive: O(n/k) stack space - current approach, most elegant

6. Follow-up Questions:
   - Can you do it iteratively?
     (Yes, but more complex with doubly linked lists)
   - What's the space complexity of your solution?
     (O(n/k) due to recursion, could be O(1) with iteration)
   - How would you reverse alternate groups?
     (Track group number, reverse only odd/even groups)
   - How is this different from singly linked list reversal?
     (Must swap both next and prev pointers instead of just next)

7. Key Insight for Interview:
   The beauty of this problem for doubly linked lists:
   - Swapping next and prev effectively reverses direction
   - Each node's reversal is independent within a group
   - Recursion elegantly handles multiple groups
   - Must maintain bidirectional links between groups

8. Time to Solve: Aim for 15-20 minutes including:
   - Understanding the problem: 3-4 minutes
   - Discussing approach: 5 minutes
   - Coding: 8-10 minutes
   - Testing with examples: 2-3 minutes

9. Testing Strategy:
   Test with these cases:
   - Empty list
   - Single node, k = 1
   - List: [1,2], k = 2
   - List: [1,2,3], k = 2 (last group smaller)
   - List: [1,2,3,4,5,6], k = 3 (perfect groups)
   - k = 1 (no reversal)
   - k > length (full reversal)

10. Verification Steps:
    After implementing, verify:
    - Forward traversal gives correct order
    - Backward traversal (using prev) also works
    - No broken links (NULL pointer exceptions)
    - First node's prev is NULL
    - Last node's next is NULL

11. Common Interview Follow-ups:
    Q: "Why use recursion instead of iteration?"
    A: Recursion is more elegant for group processing, but iteration
       would save stack space (O(1) vs O(n/k))

    Q: "Can you reverse the groups themselves (not the nodes)?"
    A: Yes, would need to reverse at group level first, then node level

    Q: "What if we want to reverse only alternate groups?"
    A: Add a boolean parameter to track whether to reverse current group

================================================================================
"""
