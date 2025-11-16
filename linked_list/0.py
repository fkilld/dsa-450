"""
================================================================================
PROBLEM: Reverse a Linked List
================================================================================

DESCRIPTION:
Given a singly linked list, reverse the order of nodes so that the last node
becomes the first node, and so on.

Input: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
Output: 5 -> 4 -> 3 -> 2 -> 1 -> NULL

================================================================================
APPROACH & REASONING:
================================================================================

We can solve this problem using two approaches:

1. ITERATIVE APPROACH (Recommended for interviews):
   - Use three pointers: prev, current, and next
   - Traverse the list and reverse the links one by one
   - Time Complexity: O(n) - single pass through the list
   - Space Complexity: O(1) - only using three pointers

   Why this works:
   - We need to reverse the 'next' pointer of each node
   - To avoid losing reference to the rest of the list, we save 'next' first
   - Then we can safely reverse the current node's pointer to point to prev
   - Move all pointers one step forward and repeat

2. RECURSIVE APPROACH:
   - Base case: When we reach the last node, make it the new head
   - Recursive case: Reverse the rest of the list, then fix current node's link
   - Time Complexity: O(n) - visit each node once
   - Space Complexity: O(n) - recursive call stack

   Why this works:
   - Recursion naturally processes nodes from end to start
   - Each recursive call handles one node's reversal
   - The last node becomes the new head automatically

================================================================================
FLOWCHART - ITERATIVE APPROACH:
================================================================================

    START
      |
      v
    Initialize:
    prev = NULL
    current = head
    next = NULL
      |
      v
    +-----------------+
    | current != NULL?|-----> NO  ----> Make prev the new head
    +-----------------+                      |
           |                                 v
          YES                              END
           |
           v
    Save next node:
    next = current.next
           |
           v
    Reverse the link:
    current.next = prev
           |
           v
    Move pointers forward:
    prev = current
    current = next
           |
           v
    (Loop back to condition)


    VISUAL EXAMPLE OF ITERATIVE REVERSAL:

    Initial:  NULL  1 -> 2 -> 3 -> 4 -> NULL
              prev  cur  next

    Step 1:   NULL<-1   2 -> 3 -> 4 -> NULL
                   prev cur next

    Step 2:   NULL<-1<-2   3 -> 4 -> NULL
                        prev cur next

    Step 3:   NULL<-1<-2<-3   4 -> NULL
                             prev cur next

    Step 4:   NULL<-1<-2<-3<-4   NULL
                                  prev cur(NULL)

    Final head = prev = 4

================================================================================
FLOWCHART - RECURSIVE APPROACH:
================================================================================

    reverse_recur(current, prev)
              |
              v
    +----------------------+
    | current.next == NULL?|-----> YES ----> Make current the new head
    +----------------------+                 current.next = prev
              |                              RETURN
             NO
              |
              v
    Save next reference:
    next = current.next
              |
              v
    Reverse current node:
    current.next = prev
              |
              v
    Recursive call:
    reverse_recur(next, current)
              |
              v
         RETURN

    RECURSION STACK VISUALIZATION:

    Call Stack (going down):
    reverse(1, NULL)  -> reverse(2, 1)  -> reverse(3, 2)  -> reverse(4, 3)
                                                               (base case)

    Unwinding (coming back up):
    1->NULL <- 2->1 <- 3->2 <- 4->3 (head=4)

================================================================================
"""

class Node:
    """
    Node class representing a single element in the linked list.

    Attributes:
        data: The value stored in the node
        next: Reference to the next node in the list
    """
    def __init__(self, data=0):
        self.data = data
        self.next = None

class LinkedList:
    """
    LinkedList class with methods to reverse the list using both
    iterative and recursive approaches.

    Attributes:
        head: Reference to the first node in the list
    """
    def __init__(self):
        self.head = None

    def reverse_itr(self):
        """
        Reverse the linked list using iterative approach.

        Algorithm:
        1. Initialize three pointers: prev (None), current (head), next (None)
        2. Traverse the list:
           - Save the next node before breaking the link
           - Reverse the current node's pointer to point to previous node
           - Move prev and current one step forward
        3. Update head to prev (which now points to the last node)

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1) - only using constant extra space
        """
        prev_node = None        # Will eventually become the new head
        current_node = self.head  # Start from the beginning
        next_node = None         # Temporary storage for next node

        # Traverse until we reach the end of the list
        while current_node != None:
            # Step 1: Save the next node (before we lose reference to it)
            next_node = current_node.next

            # Step 2: Reverse the link - make current point to previous
            current_node.next = prev_node

            # Step 3: Move prev pointer forward
            prev_node = current_node

            # Step 4: Move current pointer forward
            current_node = next_node

        # After loop, prev_node points to the last node (new head)
        self.head = prev_node

    def reverse_recur(self):
        """
        Reverse the linked list using recursive approach.

        This method is a wrapper that calls the internal recursive function.

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(n) due to recursive call stack
        """

        def _reverse_recur(curr, prev):
            """
            Internal recursive function to reverse the list.

            Args:
                curr: Current node being processed
                prev: Previous node (will become current's next after reversal)

            Base Case: When curr.next is None (last node)
                - Make curr the new head
                - Point curr to prev
                - Return

            Recursive Case:
                - Save next node
                - Reverse current node's link
                - Recursively process the rest of the list
            """
            # Base case: reached the last node
            if curr.next is None:
                # This is the new head of reversed list
                self.head = curr
                # Point this node to the previous node
                curr.next = prev
                return

            # Save reference to next node (before we change curr.next)
            next = curr.next

            # Reverse the link: make current point to previous
            curr.next = prev

            # Recursive call: process the rest of the list
            # 'next' becomes current, 'curr' becomes previous
            _reverse_recur(next, curr)

        # Handle empty list
        if self.head is None:
            return

        # Start recursion from head with no previous node
        _reverse_recur(self.head, None)

    def push(self, data):
        """
        Insert a new node at the beginning of the linked list.

        Args:
            data: Value to be stored in the new node

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Create new node with given data
        new_node = Node(data)

        # Make new node point to current head
        new_node.next = self.head

        # Update head to point to new node
        self.head = new_node

    def print(self):
        """
        Print all elements in the linked list.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        temp = self.head
        result = ""
        while temp:
            result += str(temp.data) + " "
            temp = temp.next
        print(result)


# ============================================================================
# EXAMPLE EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Create a new linked list
    ll = LinkedList()

    # Insert values: Since we're using push (insert at beginning),
    # the list will be built in reverse order
    # After these operations: 25 -> 23 -> 12 -> 10 -> NULL
    ll.push(10)
    ll.push(12)
    ll.push(23)
    ll.push(25)

    # Display original list
    print("Original Order:")
    ll.print()  # Output: 25 23 12 10

    # Reverse using recursive approach
    print("\nReversed Order (using recursive approach):")
    ll.reverse_recur()
    ll.print()  # Output: 10 12 23 25

    # Reverse back using iterative approach
    print("\nReversed Again (using iterative approach):")
    ll.reverse_itr()
    ll.print()  # Output: 25 23 12 10

"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Start with the iterative approach - it's more intuitive and uses O(1) space
2. Always clarify:
   - Should we modify the original list or create a new one? (Usually modify)
   - What should we return? (Usually the new head)
   - What if the list is empty or has only one node? (Return as-is)

3. Common mistakes to avoid:
   - Losing reference to the rest of the list (that's why we save 'next')
   - Forgetting to update the head pointer at the end
   - Not handling edge cases (empty list, single node)

4. Follow-up questions you might get:
   - Can you do it in O(1) space? (Yes, iterative approach)
   - Can you do it recursively? (Yes, but uses O(n) space for call stack)
   - What if it's a doubly linked list? (Swap next and prev pointers)
   - Reverse only a portion of the list? (Modify to take start/end positions)

5. Time to solve: Aim for 10-15 minutes including edge cases and testing
================================================================================
"""