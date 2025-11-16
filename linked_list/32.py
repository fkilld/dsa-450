"""
================================================================================
PROBLEM: Delete Nodes Having Greater Value on Right
================================================================================

DESCRIPTION:
Given a singly linked list, remove all nodes which have a node with a strictly
greater value on its right side. In other words, keep only those nodes for which
all nodes to the right have smaller or equal values.

Input:  12 -> 15 -> 10 -> 11 -> 5 -> 6 -> 2 -> 3 -> NULL
Output: 15 -> 11 -> 6 -> 3 -> NULL

Explanation:
- 12 is deleted (15 > 12 exists on right)
- 15 stays (no greater value on right)
- 10 is deleted (11 > 10 exists on right)
- 11 stays (no greater value on right)
- 5 is deleted (6 > 5 exists on right)
- 6 stays (no greater value on right)
- 2 is deleted (3 > 2 exists on right)
- 3 stays (last node, nothing on right)

================================================================================
APPROACH & REASONING:
================================================================================

APPROACH: Reverse, Filter, Reverse Back

Key Insight:
- Checking "greater values on right" is difficult going left to right
- If we reverse the list, we can check "greater values on left" which is easy
- After filtering, reverse again to restore original order

Algorithm Steps:
1. Reverse the linked list
2. Traverse from new head (originally the tail)
3. Keep track of maximum value seen so far
4. Delete nodes with value less than maximum
5. Reverse the list back to original order

Time Complexity: O(n) - three linear passes (2 reversals + 1 filtering)
Space Complexity: O(1) - only using a few pointers

Why this works:
- After reversing: "greater value on right" becomes "greater value on left"
- We can track maximum seen so far in a single pass
- Any node smaller than current maximum has a greater value to its left
  (which was originally to its right)
- Two reversals restore the original order

Alternative Approach:
- Use recursion to process from right to left
- Time: O(n), Space: O(n) for recursion stack

================================================================================
FLOWCHART:
================================================================================

    compute(head)
          |
          v
    +------------------+
    | Reverse the list |
    +------------------+
          |
          v
    Initialize:
    high = head.data (max seen)
    prev = head
    curr = head.next
          |
          v
    +------------------+
    | curr != NULL?    |-----> NO
    +------------------+        |
          |                     |
         YES                    |
          |                     |
          v                     |
    +-------------------+       |
    | curr.data < high? |       |
    +-------------------+       |
       |            |           |
      YES          NO           |
       |            |           |
       v            v           |
    Delete curr  Update high    |
    curr=curr.next  high=curr.data |
    prev.next=curr  prev=curr   |
                   curr=curr.next |
       |            |           |
       +----(Loop)--+           |
                                |
                                v
                         +------------------+
                         | Reverse the list |
                         | back to original |
                         +------------------+
                                |
                                v
                           return head


    VISUAL EXAMPLE:

    Original: 12 -> 15 -> 10 -> 11 -> 5 -> 6 -> 2 -> 3 -> NULL

    Step 1: Reverse
    3 -> 2 -> 6 -> 5 -> 11 -> 10 -> 15 -> 12 -> NULL

    Step 2: Filter (keep track of max from left)
    Node  Value  Max  Action
    3     3      3    Keep (first node)
    2     2      3    Delete (2 < 3)
    6     6      6    Keep, Update max
    5     5      6    Delete (5 < 6)
    11    11     11   Keep, Update max
    10    10     11   Delete (10 < 11)
    15    15     15   Keep, Update max
    12    12     15   Delete (12 < 15)

    After filtering: 3 -> 6 -> 11 -> 15 -> NULL

    Step 3: Reverse back
    15 -> 11 -> 6 -> 3 -> NULL

================================================================================
"""

class Solution:
    """
    Solution class to delete nodes having greater values on their right.
    """

    def reverse(self, head):
        """
        Reverse a singly linked list.

        Args:
            head: Head node of the list to reverse

        Returns:
            New head of the reversed list

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize pointers
        curr = head      # Current node being processed
        next = None      # Temporary storage for next node
        prev = None      # Previous node (becomes next after reversal)

        # Standard iterative reversal
        while curr != None:
            # Save next node before breaking the link
            next = curr.next

            # Reverse the link
            curr.next = prev

            # Move prev and curr one step forward
            prev = curr
            curr = next

        # Return new head (last node of original list)
        return prev

    def compute(self, head):
        """
        Delete all nodes which have a greater value on the right side.

        Args:
            head: Head node of the linked list

        Returns:
            Head of the modified list

        Algorithm:
        1. Reverse the list (right side becomes left side)
        2. Track maximum value seen so far from the new head
        3. Delete any node with value less than this maximum
        4. Reverse the list back to restore original order

        Time Complexity: O(n) - three passes through the list
        Space Complexity: O(1) - only using constant extra space

        Example:
            Input:  12 -> 15 -> 10 -> 11 -> 5 -> 6 -> 2 -> 3
            Output: 15 -> 11 -> 6 -> 3
        """
        # PHASE 1: Reverse the list
        # This transforms "greater on right" to "greater on left"
        head = self.reverse(head)

        # PHASE 2: Filter nodes based on maximum value seen so far
        # Initialize maximum with the first node (was last node originally)
        high = head.data

        # prev tracks the last node we decided to keep
        prev = head
        # curr is the node we're currently examining
        curr = head.next

        # Traverse the reversed list
        while curr != None:
            # Check if current node should be deleted
            # Delete if its value is less than the highest value seen so far
            if curr.data < high:
                # Skip current node (delete it)
                curr = curr.next
                # Link previous node directly to next node
                prev.next = curr
            else:
                # Current node has value >= high, so keep it
                # Update the maximum value seen
                high = curr.data
                # Move prev pointer to current node
                prev = curr
                # Move to next node
                curr = curr.next

        # PHASE 3: Reverse back to original order
        head = self.reverse(head)

        # Return the head of modified list
        return head


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Should we delete nodes with equal values on the right? (Usually no)
   - Can we modify the list in place? (Usually yes)
   - What should we return for an empty list? (Usually None/NULL)
   - Is the data always numeric? (Usually yes, but ask)

2. Edge Cases to Consider:
   - Empty list (return None)
   - Single node (return as-is, no greater value on right)
   - List in strictly increasing order (keep only last node)
   - List in strictly decreasing order (keep all nodes)
   - All nodes have same value (keep all nodes)
   - Two nodes only

3. Common Mistakes to Avoid:
   - Deleting nodes with equal values (problem says "greater", not ">=")
   - Not updating prev pointer correctly when deleting
   - Losing reference to remaining nodes when deleting
   - Forgetting to reverse back at the end
   - Not handling the first node specially in filtering phase

4. Alternative Approaches:

   a) Recursive Approach:
      - Process from right to left using recursion
      - Return maximum value from recursive call
      - Delete current node if it's less than max from right
      - Time: O(n), Space: O(n) for call stack

      def compute_recursive(self, head):
          def helper(node):
              if not node or not node.next:
                  return node, node.data if node else float('-inf')

              new_head, max_right = helper(node.next)

              if node.data < max_right:
                  return new_head, max_right
              else:
                  node.next = new_head
                  return node, max(node.data, max_right)

          result, _ = helper(head)
          return result

   b) Stack-based Approach:
      - Use stack to process from right
      - Time: O(n), Space: O(n) for stack

5. Follow-up Questions You Might Get:
   - Can you do it without reversing?
     (Yes, using recursion or stack, but uses O(n) space)
   - What if we need to delete nodes with greater OR EQUAL values?
     (Change < to <=)
   - Can you count how many nodes were deleted?
     (Yes, maintain a counter)
   - What if the list is doubly linked?
     (Easier! Can traverse from right to left directly)

6. Why This Approach is Optimal:
   - O(n) time with O(1) space
   - In-place modification (no extra list)
   - Handles all edge cases naturally
   - The reverse trick is a common pattern for right-to-left processing

7. Time to Solve: Aim for 15-20 minutes including edge cases

8. Key Insight for Interview:
   - When you need to process from right to left in a singly linked list,
     consider reversing first
   - "Greater value on right" = "Greater value on left after reversal"
   - This pattern appears in many linked list problems

9. Complexity Analysis:
   - Reverse: O(n)
   - Filter: O(n)
   - Reverse back: O(n)
   - Total: O(n) + O(n) + O(n) = O(3n) = O(n)

================================================================================
"""