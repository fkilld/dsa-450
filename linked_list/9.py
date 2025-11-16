"""
================================================================================
PROBLEM: Add Two Numbers Represented by Linked Lists
================================================================================

DESCRIPTION:
Given two numbers represented by two linked lists, return a sum list which is
the linked list representation of the addition of the two input numbers.

The most significant digit is at the head of each list.

Input:  First:  3 -> 4 -> 5 -> NULL  (represents 345)
        Second: 5 -> 6 -> 7 -> NULL  (represents 567)
Output:         9 -> 1 -> 2 -> NULL  (represents 912, since 345 + 567 = 912)

Input:  First:  9 -> 9 -> NULL  (represents 99)
        Second: 1 -> NULL       (represents 1)
Output:         1 -> 0 -> 0 -> NULL  (represents 100, since 99 + 1 = 100)

The lists may have different lengths, and carry propagation must be handled.

================================================================================
APPROACH & REASONING:
================================================================================

This is similar to adding two numbers on paper - we start from the rightmost
(least significant) digits and propagate carry leftward.

KEY INSIGHT:
- Addition is performed from LEAST to MOST significant digits (right to left)
- But the lists are ordered from MOST to LEAST significant (left to right)
- We need to process from the end of both lists

APPROACH: Reverse, Add with Carry, Reverse

ALGORITHM:

1. REVERSE both input lists
   - Now least significant digits are at the heads
2. ADD digits with carry propagation:
   - Traverse both lists simultaneously
   - For each position: sum = digit1 + digit2 + carry
   - Current digit = sum % 10
   - Carry = sum // 10
   - Create new node with current digit
   - Continue until both lists exhausted
3. Handle remaining carry:
   - If carry exists after both lists done, create new node
4. REVERSE the result list
   - Restore most-significant-first order
5. Return the result head

WHY THIS WORKS:
- Reversing allows natural left-to-right processing
- Carry propagation is straightforward
- Different length lists handled by treating missing digits as 0
- Final reverse restores expected output format

Time Complexity: O(max(n, m)) where n, m are lengths of the two lists
Space Complexity: O(max(n, m)) for the result list (unavoidable)

SPECIAL CASES:
- Lists of different lengths (99 + 1 = 100)
- All 9s with carry (99 + 99 = 198)
- One or both lists empty
- Carry at the end (9 + 9 = 18, need extra digit)

================================================================================
FLOWCHART:
================================================================================

    START
      |
      v
    PHASE 1: Reverse both lists
    first = reverse(first)
    second = reverse(second)
      |
      v
    PHASE 2: Initialize for addition
    carry = 0
    sum = 0
    res = None (result list)
    curr = None (current node in result)
      |
      v
    +------------------------------+
    | first != NULL or             |-----> NO  -----> Check final carry
    | second != NULL?              |                   |
    +------------------------------+                   v
      |                                      +------------------+
     YES                                     | carry > 0?       |
      |                                      +------------------+
      v                                           |          |
    Calculate sum:                               YES        NO
    sum = carry +                                 |          |
          (first.data if first else 0) +          v          v
          (second.data if second else 0)    New node   Skip to
      |                                      carry      reverse
      v                                           |          |
    Extract digit and carry:                      +----------+
    digit = sum % 10                              |
    carry = sum // 10                             v
      |                                      PHASE 3: Reverse result
      v                                      res = reverse(res)
    Create node with digit                        |
    Add to result list                            v
      |                                      return res
      v                                            |
    Move pointers:                                 v
    if first: first = first.next                  END
    if second: second = second.next
      |
      +---(Loop back to condition)


    VISUAL EXAMPLE:

    Input:  First:  3 -> 4 -> 5 -> NULL  (345)
            Second: 5 -> 6 -> 7 -> NULL  (567)

    Step 1: Reverse both lists
            First:  5 -> 4 -> 3 -> NULL
            Second: 7 -> 6 -> 5 -> NULL

    Step 2: Add digit by digit

    Position 0 (rightmost):
            5 + 7 + 0(carry) = 12
            digit = 2, carry = 1
            Result: 2 -> NULL

    Position 1:
            4 + 6 + 1(carry) = 11
            digit = 1, carry = 1
            Result: 2 -> 1 -> NULL

    Position 2:
            3 + 5 + 1(carry) = 9
            digit = 9, carry = 0
            Result: 2 -> 1 -> 9 -> NULL

    Both lists exhausted, carry = 0

    Step 3: Reverse result
            9 -> 1 -> 2 -> NULL

    Output: 912 ✓ (345 + 567 = 912)


    EXAMPLE WITH CARRY AT END:

    Input:  First:  9 -> 9 -> NULL  (99)
            Second: 9 -> 9 -> NULL  (99)

    After reverse:
            First:  9 -> 9 -> NULL
            Second: 9 -> 9 -> NULL

    Addition:
    9 + 9 + 0 = 18, digit = 8, carry = 1
    9 + 9 + 1 = 19, digit = 9, carry = 1
    0 + 0 + 1 = 1,  digit = 1, carry = 0

    Result before reverse: 8 -> 9 -> 1 -> NULL
    Result after reverse:  1 -> 9 -> 8 -> NULL

    Output: 198 ✓ (99 + 99 = 198)

================================================================================
"""

class Node:
    """
    Node class representing a single digit in a number.
    """
    def __init__(self, data):
        self.data = data  # Single digit (0-9)
        self.next = None  # Pointer to next digit

class Solution:
    """
    Solution class to add two numbers represented as linked lists.
    """

    def reverse(self, head):
        """
        Helper function to reverse a linked list.

        Args:
            head: The head node of the list to reverse

        Returns:
            The new head of the reversed list

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        curr = head
        prev = None
        next = None

        # Standard iterative reversal
        while curr != None:
            next = curr.next      # Save next node
            curr.next = prev      # Reverse the link
            prev = curr           # Move prev forward
            curr = next           # Move curr forward

        return prev  # New head

    def add_two_ll(self, first, second):
        """
        Add two numbers represented by linked lists.

        Args:
            first: Head of first number's linked list
            second: Head of second number's linked list

        Returns:
            Head of the result linked list (sum of the two numbers)

        Algorithm:
        1. Reverse both input lists
        2. Add corresponding digits with carry
        3. Build result list
        4. Reverse result list
        5. Return result head

        Time Complexity: O(max(n, m)) where n, m are list lengths
        Space Complexity: O(max(n, m)) for result list

        Example:
            Input:  first = 1->2->3, second = 9->8
            Output: 2->2->1 (123 + 98 = 221)
        """

        # PHASE 1: Reverse both lists to process from least significant digit
        first = self.reverse(first)
        second = self.reverse(second)

        # PHASE 2: Add the numbers digit by digit
        c = 0   # carry
        s = 0   # sum of current digits plus carry

        res = None   # Result list head
        curr = None  # Current node in result list

        # Process while either list has digits remaining
        while first != None or second != None:

            # Calculate sum of current digits plus carry
            # If a list is exhausted, treat its digit as 0
            s = c + (first.data if first else 0) + (second.data if second else 0)

            # Determine carry for next position
            c = 1 if s >= 10 else 0

            # Current digit is the remainder after removing carry
            s = s % 10

            # Create new node for current digit
            temp = Node(s)

            # Add node to result list
            if res == None:
                # First node in result
                res = temp
            else:
                # Link previous node to current node
                curr.next = temp

            # Move curr to the newly added node
            curr = temp

            # Move pointers in input lists (if not exhausted)
            if first:
                first = first.next
            if second:
                second = second.next

        # PHASE 3: Handle remaining carry
        # If there's a carry after processing all digits, add new node
        if c > 0:
            temp = Node(c)
            curr.next = temp
            curr = temp

        # PHASE 4: Reverse the result to get most-significant-first order
        res = self.reverse(res)

        return res


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Which end has the most significant digit? (Usually head)
   - Can the lists be different lengths? (Yes)
   - Can either list be empty? (Yes, treat as 0)
   - Can the numbers have leading zeros? (Usually no)
   - Should I modify the original lists? (No, create new result list)
   - How should I handle overflow? (Return result as-is, don't worry about max int)

2. Edge Cases to Consider:
   - Empty lists: None + 123 = 123
   - Different lengths: 99 + 1 = 100
   - Carry at the end: 99 + 99 = 198
   - All zeros: 0 + 0 = 0
   - Large numbers: should work with any size
   - Single digit each: 9 + 9 = 18

3. Common Mistakes to Avoid:
   - Not handling different length lists
   - Forgetting final carry (99 + 1 should be 100, not 00)
   - Not checking if list pointers are null before accessing .data
   - Forgetting to reverse result back
   - Not initializing carry to 0
   - Memory leak - not properly managing new nodes

4. Alternative Approaches:

   A) WITHOUT REVERSING (Using Stack - O(n) space):
   ```python
   # Push all digits onto stacks
   # Pop and add with carry
   # Build result directly in correct order
   ```

   B) WITHOUT REVERSING (Using Recursion):
   ```python
   # Recursively add from the end
   # Pass carry back up the recursion
   # More complex to handle different lengths
   ```

   C) IF DIGITS ARE ALREADY REVERSED (Least significant first):
   ```python
   # Skip all reverse operations
   # Direct addition from head
   # Much simpler!
   ```

5. Follow-up Questions You Might Get:
   Q: What if digits are stored in reverse order (least significant first)?
   A: Much easier! Skip all reverse operations, add directly from heads

   Q: Can you do this without reversing?
   A: Yes, using stack or recursion, but adds complexity

   Q: What about subtraction instead?
   A: More complex - need to handle borrowing and negative results

   Q: What if we have k lists to add?
   A: Generalize to process k lists simultaneously with same logic

   Q: How would you optimize for very large numbers?
   A: Current solution is already optimal O(n), can't do better

6. Why Reverse Approach Works Best:
   - Simplest to understand and implement
   - Clean handling of different lengths
   - Natural carry propagation
   - Reuses standard reverse function
   - O(1) extra space (besides result)

7. Related Problems:
   - Add Two Numbers (LeetCode 2) - digits in reverse order (easier!)
   - Add Two Numbers II (LeetCode 445) - this problem exactly
   - Multiply Two Numbers (more complex)
   - Add Strings (same concept, different data structure)

8. Time to Solve: Aim for 18-20 minutes including edge cases

9. Interview Strategy:
   - Draw example showing why we reverse
   - Explain carry propagation clearly
   - Show example with different length lists
   - Code reverse helper first
   - Test with: same length, different length, carry at end

10. Key Points to Mention:
    - "Addition is right-to-left, but lists are left-to-right"
    - "Reversing makes the algorithm natural and simple"
    - "Handle different lengths by treating missing digits as 0"
    - "Don't forget final carry - 99+1 needs 3 digits"
    - "Time complexity is O(max(n,m)) - must process all digits"

11. Code Quality Tips:
    - Use meaningful variable names (carry, sum, not c, s)
    - Comment each phase clearly
    - Handle edge cases at the start
    - Test incrementally

12. Testing Strategy:
    Test these cases:
    - 0 + 0 = 0
    - 99 + 1 = 100 (different lengths, carry)
    - 123 + 456 = 579 (same length, no carry at end)
    - 999 + 999 = 1998 (carry at end)
    - 5 + 5 = 10 (single digits with carry)

13. Comparison with Problem 8 (Add 1):
    ```
    Add 1 (Problem 8):
    - Only one list
    - Adding constant (1)
    - Simpler edge cases

    Add Two Lists (Problem 9):
    - Two lists to manage
    - Different lengths possible
    - More complex carry handling
    - More general solution
    ```

14. Memory Consideration:
    The result list must be created (can't modify input).
    Space: O(max(n,m)) for result, O(1) for algorithm itself.

================================================================================
"""
