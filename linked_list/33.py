"""
================================================================================
PROBLEM: Segregate Even and Odd Nodes in a Linked List
================================================================================

DESCRIPTION:
Given a linked list, rearrange it such that all even-valued nodes appear
before all odd-valued nodes. The relative order within even nodes and within
odd nodes should be maintained.

Input:  17 -> 15 -> 8 -> 12 -> 10 -> 5 -> 4 -> 1 -> 7 -> 6 -> NULL
Output: 8 -> 12 -> 10 -> 4 -> 6 -> 17 -> 15 -> 5 -> 1 -> 7 -> NULL
        [Even nodes first]      [Odd nodes follow]

Input:  1 -> 3 -> 5 -> 7 -> NULL  (all odd)
Output: 1 -> 3 -> 5 -> 7 -> NULL

Input:  2 -> 4 -> 6 -> 8 -> NULL  (all even)
Output: 2 -> 4 -> 6 -> 8 -> NULL

================================================================================
APPROACH & REASONING:
================================================================================

APPROACH: Two Separate Lists (Even and Odd)

Key Insight:
- Maintain two separate linked lists: one for even nodes, one for odd nodes
- Traverse original list and append nodes to appropriate list
- Finally, connect the even list to the odd list

Algorithm Steps:
1. Create two dummy lists: even_list and odd_list
2. Traverse the original list
3. For each node, check if value is even or odd
4. Append to corresponding list (even or odd)
5. Connect even list's tail to odd list's head
6. Return even list's head (or odd if no even nodes)

Time Complexity: O(n) - single pass through the list
Space Complexity: O(1) - only using pointers, no extra nodes created

Why this works:
- Separating nodes into two lists naturally maintains relative order
- Each node is visited exactly once
- No need to swap or rearrange - just redirect pointers
- Joining at the end gives us the desired arrangement

Important Note:
- We're segregating by VALUE (even/odd), not by POSITION
- This is different from "separate even/odd positioned nodes"

================================================================================
FLOWCHART:
================================================================================

    divide(N, head)
          |
          v
    Initialize:
    even = None, odd = None
    e = None (tail of even list)
    o = None (tail of odd list)
          |
          v
    +------------------+
    | head != NULL?    |-----> NO
    +------------------+        |
          |                     |
         YES                    |
          |                     |
          v                     |
    +-------------------+       |
    | head.data % 2==0? |       |
    +-------------------+       |
       |            |           |
      YES          NO           |
    (Even)       (Odd)          |
       |            |           |
       v            v           |
    Add to even  Add to odd     |
    list         list           |
       |            |           |
       +-----+------+           |
             |                  |
             v                  |
    head = head.next            |
             |                  |
             +---(Loop back)    |
                                |
                                v
                         Terminate both lists:
                         e.next = None
                         o.next = None
                                |
                                v
                         Connect lists:
                         e.next = odd
                                |
                                v
                         Return even (or odd if no even)


    VISUAL EXAMPLE:

    Original: 17 -> 15 -> 8 -> 12 -> 10 -> 5 -> 4 -> 1 -> 7 -> 6

    During traversal:
    Even list: 8 -> 12 -> 10 -> 4 -> 6 -> NULL
    Odd list:  17 -> 15 -> 5 -> 1 -> 7 -> NULL

    After connecting:
    Result: 8 -> 12 -> 10 -> 4 -> 6 -> 17 -> 15 -> 5 -> 1 -> 7 -> NULL

================================================================================
"""

class node:
    """
    Node class representing a single element in the linked list.

    Attributes:
        data: The value stored in the node
        next: Reference to the next node in the list
    """
    def __init__(self) -> None:
        self.data = None
        self.next = None

class Solution:
    """
    Solution class to segregate even and odd valued nodes.
    """

    def divide(self, N, head):
        """
        Segregate even and odd nodes such that all even nodes come first.

        Args:
            N: Total number of nodes in the list (not used in logic but provided)
            head: Head node of the original linked list

        Returns:
            Head of the rearranged list with even nodes before odd nodes

        Algorithm:
        1. Create two separate lists for even and odd values
        2. Traverse original list and distribute nodes
        3. Terminate both lists properly
        4. Connect even list to odd list
        5. Return head of even list (or odd if no even nodes)

        Time Complexity: O(n) where n is number of nodes
        Space Complexity: O(1) - only using pointers

        Example:
            Input:  1 -> 2 -> 3 -> 4 -> 5
            Output: 2 -> 4 -> 1 -> 3 -> 5
        """
        # Initialize heads of even and odd lists
        even = None  # Head of even-valued nodes list
        odd = None   # Head of odd-valued nodes list

        # Initialize tail pointers for both lists
        e = None     # Tail pointer for even list
        o = None     # Tail pointer for odd list

        # Traverse the original list
        while head != None:
            # Check if current node has even value
            if head.data % 2 == 0:
                # Add to even list
                if even == None:
                    # First even node - initialize even list
                    even = head
                    e = even
                else:
                    # Append to existing even list
                    e.next = head
                    e = e.next  # Move tail pointer
            else:
                # Add to odd list
                if odd == None:
                    # First odd node - initialize odd list
                    odd = head
                    o = odd
                else:
                    # Append to existing odd list
                    o.next = head
                    o = o.next  # Move tail pointer

            # Move to next node in original list
            head = head.next

        # Terminate both lists properly to avoid cycles
        if e:
            e.next = None  # Terminate even list

        if o:
            o.next = None  # Terminate odd list

        # Connect even list to odd list
        if even:
            # If there are even nodes, connect to odd list
            if e:
                e.next = odd
            return even
        else:
            # No even nodes, return odd list head
            return odd


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Are we segregating by VALUE (even/odd numbers) or POSITION (even/odd indices)?
     (This problem is by VALUE)
   - Should relative order be maintained? (Usually yes)
   - Can the list have negative numbers? (Yes, -2 is even, -1 is odd)
   - What if all nodes are even or all are odd? (Return as-is)
   - Can we use extra space? (This solution uses O(1) extra space)

2. Edge Cases to Consider:
   - Empty list (return None)
   - Single node (return as-is)
   - All even nodes (return the list, no odd section)
   - All odd nodes (return the list)
   - Alternating even-odd pattern
   - Two nodes only (one even, one odd)

3. Common Mistakes to Avoid:
   - Not terminating the even or odd lists (causes cycles!)
   - Forgetting to handle case when one list is empty
   - Confusing value-based segregation with position-based
   - Not maintaining relative order within each group
   - Memory leaks by creating new nodes instead of reusing

4. Alternative Approaches:

   a) In-place Swapping:
      - Use two pointers and swap values
      - More complex, may not preserve relative order
      - Time: O(n), Space: O(1)

   b) Using Extra Space:
      - Create new lists instead of rearranging
      - Simpler logic but uses O(n) extra space
      - Time: O(n), Space: O(n)

   c) Single Pass with Even/Odd Heads:
      - Similar to current approach but slightly different pointer management
      - Time: O(n), Space: O(1)

5. Follow-up Questions You Might Get:
   - What if we need odd nodes first, then even?
     (Swap the logic - connect odd to even instead)
   - Can you segregate into three groups: divisible by 3, remainder 1, remainder 2?
     (Extend to three lists)
   - What if we want to segregate by position instead of value?
     (Different algorithm: alternate between two lists)
   - Can you do this for a doubly linked list?
     (Similar approach, but also update prev pointers)

6. Why This Approach is Good:
   - O(n) time with single pass
   - O(1) space - no extra nodes created
   - Maintains relative order within groups
   - Clean and easy to understand
   - Handles all edge cases naturally

7. Time to Solve: Aim for 12-15 minutes including edge cases

8. Key Insight for Interview:
   - Creating separate lists is a powerful pattern
   - Remember to terminate lists to avoid cycles
   - The pattern: traverse -> distribute -> connect
   - This technique applies to many "partition" problems

9. Testing Strategy:
   - Test with all even: [2, 4, 6]
   - Test with all odd: [1, 3, 5]
   - Test mixed: [1, 2, 3, 4]
   - Test single node: [5]
   - Test empty: []

10. Common Variations:
    - Segregate positive and negative
    - Segregate less than k and greater than k
    - Segregate vowels and consonants (for character lists)
    - Three-way partitioning (like Dutch National Flag)

================================================================================
"""