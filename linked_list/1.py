"""
================================================================================
PROBLEM: Reverse a Linked List in Groups of Given Size
================================================================================

DESCRIPTION:
Given a linked list and a positive integer k, reverse the nodes of the list
k at a time and return the modified list.

Input:  1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> NULL, k = 3
Output: 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 9 -> 8 -> 7 -> NULL

If the number of nodes is not a multiple of k, then left-out nodes in the end
should be reversed as well.

================================================================================
APPROACH & REASONING:
================================================================================

RECURSIVE APPROACH (Elegant and Interview-Friendly):

Key Insight:
- We can break this problem into smaller subproblems
- Reverse the first k nodes, then recursively reverse the remaining nodes
- Connect the reversed first group to the recursively reversed rest

Algorithm Steps:
1. Reverse the first k nodes (similar to basic list reversal)
2. Recursively call the function for the remaining nodes
3. Connect the first group's tail to the head of reversed remaining list
4. Return the new head (which was the k-th node of original list)

Time Complexity: O(n) - visit each node exactly once
Space Complexity: O(n/k) - recursive stack depth (number of groups)

Why this works:
- Each recursive call handles exactly one group of k nodes
- The recursion naturally handles the connection between groups
- Base case: when head is None, return None

================================================================================
FLOWCHART:
================================================================================

    reverse(head, k)
          |
          v
    +-------------+
    | head==NULL? |-----> YES ----> return NULL
    +-------------+
          |
         NO
          |
          v
    Initialize:
    curr = head
    prev = NULL
    next = NULL
    count = 0
          |
          v
    +------------------------+
    | curr!=NULL && count<k? |-----> NO
    +------------------------+         |
          |                           |
         YES                          |
          |                           |
          v                           |
    next = curr.next                  |
    curr.next = prev                  |
    prev = curr                       |
    curr = next                       |
    count++                           |
          |                           |
          +---(Loop back)              |
                                      |
                                      v
                              +-------------+
                              | next!=NULL? |-----> NO
                              +-------------+        |
                                    |                |
                                   YES               |
                                    |                |
                                    v                v
                          Recursive call:       return prev
                          head.next = reverse(next, k)
                                    |
                                    v
                              return prev


    VISUAL EXAMPLE (k=3):

    Original: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> NULL

    Step 1: Reverse first 3 nodes
    3 -> 2 -> 1    4 -> 5 -> 6 -> 7 -> NULL
    ^              ^
    prev          next
    (new head)    (recursively process this)

    Step 2: Recursively process remaining (4->5->6->7)
    3 -> 2 -> 1    6 -> 5 -> 4    7 -> NULL
                   ^              ^
                   prev          next

    Step 3: Connect and return
    3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 7 -> NULL
    ^
    Return this as new head

================================================================================
"""

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    """
    LinkedList class with method to reverse nodes in groups of size k.

    Attributes:
        head: Reference to the first node in the list
    """
    def __init__(self):
        self.head = None

    def push(self, data):
        """
        Insert a new node at the beginning of the linked list.

        Args:
            data: Value to be stored in the new node

        Time Complexity: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self, head, k):
        """
        Reverse the linked list in groups of size k using recursion.

        Args:
            head: The head node of the list/sublist to reverse
            k: The group size - number of nodes to reverse together

        Returns:
            The new head of the reversed list

        Algorithm:
        1. Reverse first k nodes iteratively
        2. Recursively reverse the remaining nodes
        3. Connect the first group to the reversed remaining list
        4. Return the new head

        Time Complexity: O(n) where n is the total number of nodes
        Space Complexity: O(n/k) for recursion stack

        Example:
            Input:  1->2->3->4->5->6, k=2
            Output: 2->1->4->3->6->5
        """
        # Base case: empty list
        if head == None:
            return None

        # Initialize pointers for reversing first k nodes
        curr = head      # Current node being processed
        next = None      # Temporary storage for next node
        prev = None      # Previous node (becomes next after reversal)
        count = 0        # Counter to track k nodes

        # PHASE 1: Reverse first k nodes
        # This is similar to standard list reversal, but limited to k nodes
        while curr != None and count < k:
            # Save next node before we lose reference
            next = curr.next

            # Reverse the link
            curr.next = prev

            # Move prev and curr one step forward
            prev = curr
            curr = next

            # Increment counter
            count += 1

        # After the loop:
        # - 'prev' points to the new head of this reversed group (k-th node)
        # - 'next' points to the (k+1)-th node (start of next group)
        # - 'head' points to what is now the tail of this reversed group

        # PHASE 2: Recursively reverse the remaining nodes
        # Connect the tail of current group to the head of reversed remaining list
        if next != None:
            # 'head' is now the last node of current reversed group
            # Connect it to the result of reversing remaining nodes
            head.next = self.reverse(next, k)

        # PHASE 3: Return the new head
        # 'prev' is the last node we processed (k-th node), which is now the head
        return prev

    def printList(self):
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
    llist = LinkedList()

    # Build list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
    # (push adds to front, so we push in reverse order)
    llist.push(9)
    llist.push(8)
    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)

    print("Original List:")
    llist.printList()  # Output: 1 2 3 4 5 6 7 8 9

    # Reverse in groups of 3
    k = 3
    print(f"\nReversed in groups of {k}:")
    llist.head = llist.reverse(llist.head, k)
    llist.printList()  # Output: 3 2 1 6 5 4 9 8 7

"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - What should happen if the last group has fewer than k nodes?
     (Usually: reverse them as well)
   - Should we modify the original list or create a new one?
     (Usually: modify in-place)
   - What if k is 1 or k > length of list?
     (k=1: no change needed, k>n: reverse entire list)

2. Edge Cases to Consider:
   - Empty list (return None)
   - Single node (return as-is)
   - k = 1 (no reversal needed)
   - k >= list length (reverse entire list)
   - Last group has fewer than k nodes

3. Common Mistakes to Avoid:
   - Forgetting to connect groups after reversal
   - Not handling the case when remaining nodes < k
   - Losing reference to the next group before reversing current group
   - Not updating head pointer to return the correct value

4. Alternative Approaches:
   - Iterative with stack: Use stack to reverse each group (O(k) extra space)
   - Pure iterative: More complex pointer manipulation but O(1) space

5. Follow-up Questions:
   - Can you do it iteratively? (Yes, but more complex)
   - What if we need to reverse alternate groups? (Modify recursion logic)
   - How would you handle a doubly linked list? (Swap next and prev)

6. Time to Solve: Aim for 15-20 minutes including edge cases

7. Key Insight for Interview:
   Explain that this problem combines two concepts:
   - Basic linked list reversal (for each group)
   - Recursion/divide-and-conquer (to handle multiple groups)

================================================================================
"""