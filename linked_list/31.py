"""
================================================================================
PROBLEM: Multiply Two Linked Lists
================================================================================

DESCRIPTION:
Given two linked lists representing two non-negative numbers. The digits are
stored in their respective linked lists such that the most significant digit
is at the head of the list. Multiply the two numbers and return the result
modulo 10^9 + 7.

Input:  L1 = 3 -> 2 -> NULL  (represents 32)
        L2 = 2 -> 1 -> NULL  (represents 21)
Output: 672 (32 * 21 = 672)

Input:  L1 = 1 -> 0 -> 0 -> NULL  (represents 100)
        L2 = 1 -> 0 -> NULL       (represents 10)
Output: 1000 (100 * 10 = 1000)

================================================================================
APPROACH & REASONING:
================================================================================

APPROACH: String Conversion Method

Key Insight:
- Convert each linked list to its numeric representation
- Multiply the two numbers
- Return result modulo 10^9 + 7

Algorithm Steps:
1. Traverse first linked list and build string representation of number
2. Traverse second linked list and build string representation of number
3. Convert both strings to integers
4. Multiply the integers and return result modulo 10^9 + 7

Time Complexity: O(m + n) where m, n are lengths of the two lists
Space Complexity: O(m + n) for storing the string representations

Why this works:
- Each node contains a single digit
- By traversing from head to tail, we naturally get digits in correct order
- String concatenation preserves digit positions
- Modulo operation prevents integer overflow for large numbers

Alternative Approach (More Optimal):
- Build numbers digit by digit: num = num * 10 + digit
- Apply modulo at each step to prevent overflow
- Time: O(m + n), Space: O(1)

================================================================================
FLOWCHART:
================================================================================

    multiply(head1, head2)
           |
           v
    Initialize:
    mod = 10^9 + 7
    num1 = ""
    num2 = ""
           |
           v
    +------------------+
    | Traverse List 1  |
    | curr1 = head1    |
    +------------------+
           |
           v
    +--------------------+
    | curr1 != NULL?     |-----> NO
    +--------------------+        |
           |                     |
          YES                    |
           |                     |
           v                     |
    Append curr1.data           |
    to num1 string              |
    curr1 = curr1.next          |
           |                     |
           +---(Loop)            |
                                 |
                                 v
                         +------------------+
                         | Traverse List 2  |
                         | curr2 = head2    |
                         +------------------+
                                 |
                                 v
                         +--------------------+
                         | curr2 != NULL?     |-----> NO
                         +--------------------+        |
                                 |                     |
                                YES                    |
                                 |                     |
                                 v                     |
                         Append curr2.data            |
                         to num2 string               |
                         curr2 = curr2.next           |
                                 |                     |
                                 +---(Loop)            |
                                                       |
                                                       v
                                                Convert num1, num2
                                                to integers
                                                       |
                                                       v
                                                Multiply and
                                                return result % mod
                                                       |
                                                       v
                                                      END


    VISUAL EXAMPLE:

    List 1:  3 -> 2 -> NULL
             |    |
             v    v
    num1 = "3" + "2" = "32"

    List 2:  2 -> 1 -> NULL
             |    |
             v    v
    num2 = "2" + "1" = "21"

    Result: int("32") * int("21") = 672
    Return: 672 % (10^9 + 7) = 672

================================================================================
"""

def multiply(head1, head2):
    """
    Multiply two numbers represented by linked lists.

    Args:
        head1: Head node of first linked list
        head2: Head node of second linked list

    Returns:
        Product of the two numbers modulo 10^9 + 7

    Algorithm:
    1. Convert first linked list to string representation of number
    2. Convert second linked list to string representation of number
    3. Convert strings to integers and multiply
    4. Return result modulo 10^9 + 7

    Time Complexity: O(m + n) where m, n are list lengths
    Space Complexity: O(m + n) for string storage

    Example:
        L1: 3 -> 2 -> NULL  (32)
        L2: 2 -> 1 -> NULL  (21)
        Result: 672
    """
    # Modulo value to prevent overflow
    mod = 10**9 + 7

    # Build string representation of first number
    num1 = ""
    curr1 = head1

    # Traverse first linked list
    while curr1 != None:
        # Append current digit to string
        num1 += str(curr1.data)
        # Move to next node
        curr1 = curr1.next

    # Build string representation of second number
    num2 = ""
    curr2 = head2

    # Traverse second linked list
    while curr2 != None:
        # Append current digit to string
        num2 += str(curr2.data)
        # Move to next node
        curr2 = curr2.next

    # Convert strings to integers, multiply, and return with modulo
    return (int(num1) * int(num2)) % mod


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Are the numbers guaranteed to be non-negative? (Usually yes)
   - Can the lists be empty? (Handle as 0)
   - Should we return result modulo some value? (Usually 10^9 + 7)
   - What's the maximum length of the lists? (Important for overflow consideration)
   - Are there leading zeros? (Usually no, except for the number 0 itself)

2. Edge Cases to Consider:
   - One or both lists are empty (treat as 0)
   - Single digit numbers (lists with one node)
   - One of the numbers is 0 (result should be 0)
   - Very large numbers (why we need modulo)
   - Lists of different lengths

3. Common Mistakes to Avoid:
   - Integer overflow for large numbers (use modulo or handle carefully)
   - Not handling empty lists
   - Building the number in reverse order
   - Forgetting to apply modulo operation

4. Alternative Approaches:

   a) Digit-by-Digit Multiplication (More Space Efficient):
      - Build numbers on the fly: num = num * 10 + digit
      - Apply modulo at each step
      - Space: O(1) instead of O(m + n)

      def multiply_optimal(head1, head2):
          mod = 10**9 + 7
          num1 = 0
          while head1:
              num1 = (num1 * 10 + head1.data) % mod
              head1 = head1.next

          num2 = 0
          while head2:
              num2 = (num2 * 10 + head2.data) % mod
              head2 = head2.next

          return (num1 * num2) % mod

   b) School Multiplication Method:
      - Multiply digit by digit like manual multiplication
      - More complex but educational
      - Useful if asked to return result as linked list

5. Follow-up Questions You Might Get:
   - Can you do it without converting to string?
     (Yes, build number digit by digit)
   - What if result should be a linked list?
     (Use digit-by-digit multiplication and build result list)
   - How would you handle negative numbers?
     (Track sign separately, multiply absolute values)
   - Can you optimize space complexity?
     (Yes, use digit-by-digit approach for O(1) space)

6. Key Insights for Interview:
   - This problem tests understanding of:
     * Linked list traversal
     * Number representation
     * Modular arithmetic
     * String/integer conversion
   - The modulo operation is crucial for handling large numbers
   - Always discuss time/space tradeoffs

7. Time to Solve: Aim for 10-15 minutes including edge cases

8. Extension Problems:
   - Add two numbers represented as linked lists
   - Subtract two numbers
   - Divide two numbers
   - Handle decimal numbers

================================================================================
"""