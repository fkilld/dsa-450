"""
================================================================================
PROBLEM: Add 1 to a Number Represented as Linked List
================================================================================

DESCRIPTION:
Given a singly linked list where each node represents a digit of a number,
add 1 to the number and return the resulting linked list.

The most significant digit is at the head of the list.

Input:  1 -> 2 -> 3 -> NULL  (represents 123)
Output: 1 -> 2 -> 4 -> NULL  (represents 124)

Input:  9 -> 9 -> 9 -> NULL  (represents 999)
Output: 1 -> 0 -> 0 -> 0 -> NULL  (represents 1000)

The challenge is handling carry propagation, especially when all digits are 9.

================================================================================
APPROACH & REASONING:
================================================================================

The problem mimics addition: when adding 1 to the least significant digit,
we might get a carry that propagates leftward.

KEY INSIGHT:
- Addition starts from the LEAST significant digit (rightmost)
- But our list starts from MOST significant digit (leftmost)
- We need to access nodes from right to left

APPROACH: Reverse, Add, Reverse

ALGORITHM:

1. REVERSE the linked list (now least significant digit is at head)
2. ADD 1 with carry propagation:
   - Start from head (least significant digit)
   - Add 1 to first digit
   - Propagate carry through the list:
     * If digit is 9 and we have carry: digit becomes 0, carry continues
     * If digit < 9 and we have carry: digit += 1, carry stops
   - Special case: If all digits are 9, we need a new node at the end
3. REVERSE the list again to restore original order
4. Return the new head

WHY THIS WORKS:
- Reversing allows us to process from least to most significant digit
- Carry propagation is natural when processing left to right after reversal
- Second reversal restores the expected output format

Time Complexity: O(n) - three O(n) operations (reverse + add + reverse)
Space Complexity: O(1) - only using pointers, no extra data structures

SPECIAL CASES:
- Single digit (0-8): Simply increment and return
- Single digit 9: Becomes 1 -> 0
- All 9s: New node prepended, all become 0s
- Leading zeros: Shouldn't exist in input, but handled naturally

================================================================================
FLOWCHART:
================================================================================

    START
      |
      v
    PHASE 1: Reverse the list
    head = reverse(head)
      |
      v
    PHASE 2: Add 1 with carry
    curr = head
    carry = 1 (we're adding 1)
      |
      v
    +-------------------+
    | curr != NULL?     |-----> NO  -----> Check if carry left
    +-------------------+                   |
      |                                     v
     YES                          +------------------+
      |                           | carry > 0?       |
      v                           +------------------+
    +-----------------------+           |        |
    | curr.next == NULL     |          YES      NO
    | AND curr.data == 9?   |           |        |
    +-----------------------+           v        v
      |              |          New node    Return
     YES            NO          needed!    (done)
      |              |
      v              v
    Last node    Calculate:
    is 9!        sum = curr.data + carry
      |          carry = 1 if sum >= 10 else 0
      v          curr.data = sum % 10
    curr.data = 1         |
    New node: 0           v
    Add to head     curr = curr.next
      |                   |
      +-------------------+
      |
      v
    PHASE 3: Reverse again
    head = reverse(head)
      |
      v
    return head
      |
      v
    END


    VISUAL EXAMPLE 1: Simple case (no all-9s)

    Input: 1 -> 2 -> 3 -> NULL (123)

    Step 1: Reverse
            3 -> 2 -> 1 -> NULL

    Step 2: Add 1
            Start: curr = 3, carry = 1
            3 + 1 = 4, no carry
            4 -> 2 -> 1 -> NULL
            curr moves to 2, but carry = 0, so we're done

    Step 3: Reverse
            1 -> 2 -> 4 -> NULL

    Output: 124 ✓


    VISUAL EXAMPLE 2: All 9s case

    Input: 9 -> 9 -> 9 -> NULL (999)

    Step 1: Reverse
            9 -> 9 -> 9 -> NULL

    Step 2: Add 1
            Iteration 1: curr = 9 (first), carry = 1
                        curr.next = 9, curr.data = 9
                        Not last, so: data = 0, carry = 1
                        0 -> 9 -> 9 -> NULL

            Iteration 2: curr = 9 (second), carry = 1
                        curr.next = 9, curr.data = 9
                        Not last, so: data = 0, carry = 1
                        0 -> 0 -> 9 -> NULL

            Iteration 3: curr = 9 (third/last), carry = 1
                        curr.next = NULL, curr.data = 9
                        Last node AND 9!
                        curr.data = 1, create new node 0
                        0 -> 0 -> 0 -> 1 -> NULL

    Step 3: Reverse
            1 -> 0 -> 0 -> 0 -> NULL

    Output: 1000 ✓

================================================================================
"""

class Node:
    """
    Node class representing a single digit in the number.
    """
    def __init__(self, data) -> None:
        self.data = data  # Stores a single digit (0-9)
        self.next = None  # Pointer to next digit

class Solution:
    """
    Solution class to add 1 to a number represented as a linked list.
    """

    def add_llist(self, head):
        """
        Add 1 to the number represented by the linked list.

        Args:
            head: The head node of the linked list (most significant digit)

        Returns:
            head: The head of the resulting linked list

        Algorithm:
        1. Reverse the list to access least significant digit first
        2. Add 1 and handle carry propagation
        3. Reverse the list back to original order
        4. Return new head

        Time Complexity: O(n) where n is the number of digits
        Space Complexity: O(1) - only using pointers

        Example:
            Input:  9 -> 9 -> 9 -> NULL (999)
            Output: 1 -> 0 -> 0 -> 0 -> NULL (1000)
        """

        def reverse(head):
            """
            Helper function to reverse a linked list.

            Returns the new head of the reversed list.
            """
            curr = head
            next = None
            prev = None

            # Standard list reversal
            while curr != None:
                next = curr.next      # Save next
                curr.next = prev      # Reverse link
                prev = curr           # Move prev
                curr = next           # Move curr

            return prev  # New head

        # PHASE 1: Reverse the list
        # Now least significant digit is at head
        head = reverse(head)

        # PHASE 2: Add 1 with carry propagation
        curr = head

        # Traverse and add 1 (with carry)
        while curr != None:

            # SPECIAL CASE: Last node with value 9
            # This means we need to add a new digit at the front
            # Example: 999 + 1 = 1000 (need extra digit)
            if curr.next == None and curr.data == 9:
                # Set current node to 1 (this will be second digit after reverse)
                curr.data = 1

                # Create new node with 0 (will be last digit after reverse)
                temp = Node(0)
                temp.next = head
                head = temp

                # Move curr to process the new node
                curr = curr.next

            # CASE: Current digit is 9 (but not last node)
            # 9 + 1 = 10, so digit becomes 0 and carry continues
            elif curr.data == 9:
                curr.data = 0  # 9 + 1 = 10, keep 0, carry 1
                curr = curr.next  # Continue to propagate carry

            # CASE: Current digit is 0-8
            # Simply add 1 and stop (no carry)
            else:
                curr.data += 1  # Add the 1
                curr = curr.next
                break  # No more carry, stop processing

        # PHASE 3: Reverse back to original order
        # Most significant digit returns to head
        head = reverse(head)

        return head


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Which end is the most significant digit? (Usually head/first)
   - Can the number have leading zeros? (Usually no)
   - What's the maximum number of digits? (Affects if we can use int conversion)
   - Should I handle negative numbers? (Usually no, just positive)
   - Can I modify the original list? (Yes, expected)

2. Edge Cases to Consider:
   - Single digit 0-8: Simple increment (e.g., 5 -> 6)
   - Single digit 9: Needs new node (9 -> 1 -> 0)
   - All 9s: Needs new leading digit (999 -> 1000)
   - Large numbers: Should work with any size
   - No leading zeros in input (but output might start with 1 if all 9s)

3. Common Mistakes to Avoid:
   - Not handling the all-9s case (missing new digit)
   - Forgetting to reverse back after addition
   - Not properly handling carry propagation
   - Trying to convert to integer (fails for large numbers)
   - Not breaking when carry becomes 0
   - Edge case: single node with value 9

4. Alternative Approaches:

   A) RECURSIVE (more elegant but O(n) space):
   ```python
   def addOne(head):
       carry = add_helper(head)
       if carry:
           new_head = Node(1)
           new_head.next = head
           return new_head
       return head

   def add_helper(node):
       if not node:
           return 1  # Base: add 1
       carry = add_helper(node.next)
       total = node.data + carry
       node.data = total % 10
       return total // 10
   ```

   B) THREE-POINTER (without reversing, but complex):
   - Find length, traverse to last node
   - Process backwards using recursion or stack
   - More complex, not recommended for interviews

5. Follow-up Questions You Might Get:
   Q: Can you do this without reversing?
   A: Yes, using recursion or stack, but reversing is simpler and O(1) space

   Q: What if we need to add a number k instead of 1?
   A: Similar approach, but start with carry = k and propagate

   Q: What if digits are in reverse order (least significant first)?
   A: Even easier - skip the reverse steps, directly add!

   Q: Can you handle subtraction?
   A: More complex - need to handle borrowing instead of carrying

6. Why Reverse Approach is Best:
   - Simple to understand and implement
   - O(1) space (recursion uses O(n) stack)
   - Handles all edge cases naturally
   - Reuses standard reverse logic
   - Easy to extend to adding any number, not just 1

7. Related Problems:
   - Add Two Numbers (LeetCode 2) - similar but two lists
   - Plus One (LeetCode 66) - same problem but with array
   - Multiply Strings (LeetCode 43) - more complex arithmetic

8. Time to Solve: Aim for 15-18 minutes including edge cases

9. Interview Strategy:
   - Start by explaining why we reverse (access from right)
   - Draw example with all 9s to show the challenge
   - Code the reverse helper function first
   - Carefully handle the three cases in addition phase
   - Test with: simple case, all 9s, single 9

10. Key Points to Mention:
    - "Addition works right to left, but list is left to right"
    - "Reversing makes carry propagation natural"
    - "Special case when all digits are 9 - need extra digit"
    - "Time is still O(n) despite reversing twice"

11. Optimization Note:
    The current code has a subtle issue in the all-9s case.
    A cleaner version:
    ```python
    # After first reverse
    carry = 1
    curr = head
    while curr and carry:
        total = curr.data + carry
        curr.data = total % 10
        carry = total // 10
        if curr.next is None and carry:
            # Need new digit
            curr.next = Node(carry)
            carry = 0
        curr = curr.next
    ```

12. Testing Strategy:
    Test cases to verify:
    - 0 -> 1
    - 5 -> 6
    - 9 -> 1 -> 0
    - 1 -> 2 -> 9 -> 1 -> 3 -> 0
    - 9 -> 9 -> 9 -> 1 -> 0 -> 0 -> 0

================================================================================
"""
