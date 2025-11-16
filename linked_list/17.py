"""
================================================================================
PROBLEM: Check if Linked List is Palindrome
================================================================================

DESCRIPTION:
Given a singly linked list of integers, check if it is a palindrome.
A palindrome reads the same forwards and backwards.

Input:  1 -> 2 -> 3 -> 2 -> 1 -> NULL
Output: 1 (True - it's a palindrome)

Input:  1 -> 2 -> 3 -> 4 -> NULL
Output: 0 (False - not a palindrome)

Input:  1 -> 2 -> 2 -> 1 -> NULL
Output: 1 (True - it's a palindrome)

================================================================================
APPROACH & REASONING:
================================================================================

REVERSE SECOND HALF APPROACH (Optimal):

The key insight is to find the middle, reverse the second half, and then
compare the first half with the reversed second half.

Algorithm Steps:
1. Find the middle of the linked list using slow/fast pointers
2. Reverse the second half of the list
3. Compare first half with reversed second half
4. If all nodes match, it's a palindrome

Time Complexity: O(n) - single pass to find middle, reverse, and compare
Space Complexity: O(1) - only using pointers, no extra data structures

Why this works:
- Palindrome property: first half mirrors second half
- By reversing second half, we can compare node by node
- If all values match, the list is a palindrome

Alternative Approaches:
1. Stack-based: Push first half to stack, compare with second half (O(n) space)
2. Array conversion: Convert to array, use two pointers (O(n) space)
3. Recursive: Use recursion to compare ends (O(n) space for call stack)

Current approach is optimal: O(n) time, O(1) space

================================================================================
FLOWCHART:
================================================================================

    palindrome(head)
          |
          v
    PHASE 1: Find middle
    Initialize:
    slow = head
    fast = head
          |
          v
    +---------------------------+
    | fast!=NULL &&             |-----> NO (middle found)
    | fast.next!=NULL?          |
    +---------------------------+
          |
         YES
          |
          v
    slow = slow.next
    fast = fast.next.next
          |
          +----(Loop back)
          |
          v
    PHASE 2: Reverse second half
    curr = slow
    prev = NULL
          |
          v
    +------------------+
    | curr != NULL?    |-----> NO (reversal done)
    +------------------+
          |
         YES
          |
          v
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
          |
          +----(Loop back)
          |
          v
    PHASE 3: Compare halves
    fast = head
    (prev points to reversed second half)
          |
          v
    +------------------------+
    | prev != NULL?          |-----> NO ----> return 1
    +------------------------+                (palindrome!)
          |
         YES
          |
          v
    +------------------------+
    | prev.data != fast.data?|-----> YES ----> return 0
    +------------------------+                 (not palindrome)
          |
         NO
          |
          v
    fast = fast.next
    prev = prev.next
          |
          +----(Loop back)


    VISUAL EXAMPLE - PALINDROME:

    Original: 1 -> 2 -> 3 -> 2 -> 1

    Step 1: Find middle (slow/fast pointers)
    slow ends at 3, fast at end

    Step 2: Reverse second half (3 -> 2 -> 1)
    After reversal: 1 -> 2
                        ↓
    Reversed second:    1 -> 2 -> 3

    Step 3: Compare
    First:  1 -> 2
    Second: 1 -> 2 (reversed)
    All match → return 1 (palindrome)


    VISUAL EXAMPLE - NOT PALINDROME:

    Original: 1 -> 2 -> 3 -> 4

    Step 1: Find middle
    slow at 3

    Step 2: Reverse second half (3 -> 4)
    Reversed: 4 -> 3

    Step 3: Compare
    First:  1 -> 2
    Second: 4 -> 3 (reversed)
    1 != 4 → return 0 (not palindrome)

================================================================================
"""

class Node:
    """
    Node class representing a single element in the linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    """
    Solution class to check if a linked list is a palindrome.
    """

    def palindrome(self, head):
        """
        Check if a singly linked list is a palindrome.

        Algorithm:
        1. Find the middle of the list using slow/fast pointers
        2. Reverse the second half of the list
        3. Compare first half with reversed second half
        4. Return 1 if all values match, 0 otherwise

        Args:
            head: Head of the linked list

        Returns:
            1 if list is palindrome, 0 otherwise

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1) - only using pointers

        Example:
            Input: 1->2->3->2->1
            Output: 1 (palindrome)

            Input: 1->2->3->4
            Output: 0 (not palindrome)
        """
        # PHASE 1: Find the middle element using slow/fast pointers
        # slow moves 1 step, fast moves 2 steps
        # When fast reaches end, slow is at middle
        slow = head
        fast = head

        # Move slow and fast pointers to find middle
        while fast != None and fast.next != None:
            # Move slow by one step
            slow = slow.next
            # Move fast by two steps
            fast = fast.next.next

        # After this loop, slow points to the middle node
        # For odd length: slow is at exact middle
        # For even length: slow is at start of second half

        # PHASE 2: Reverse the second half of the linked list
        # We'll reverse from slow to end
        curr = slow      # Start of second half
        prev = None      # Will become head of reversed second half
        next = None      # Temporary storage

        # Standard linked list reversal
        while curr != None:
            # Save next node before breaking the link
            next = curr.next

            # Reverse the link
            curr.next = prev

            # Move prev and curr forward
            prev = curr
            curr = next

        # After reversal, 'prev' points to head of reversed second half

        # PHASE 3: Compare the first half with the reversed second half
        # fast pointer is reused to traverse first half
        fast = head

        # prev points to reversed second half
        # Compare node by node
        while prev != None:
            # If any data doesn't match, it's not a palindrome
            if prev.data != fast.data:
                return 0

            # Move both pointers forward
            fast = fast.next
            prev = prev.next

        # If we've compared all nodes without mismatch, it's a palindrome
        return 1


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Can we modify the original list? (Reversing second half modifies it)
   - What should we return? (Usually 1/0 or True/False)
   - What if list is empty? (Empty is considered palindrome)
   - What if list has one node? (Single node is palindrome)
   - Should we restore the list after checking? (Usually not required)

2. Edge Cases to Consider:
   - Empty list → return 1 (palindrome by definition)
   - Single node → return 1 (palindrome)
   - Two nodes (same) → return 1
   - Two nodes (different) → return 0
   - Odd length palindrome (e.g., 1->2->1)
   - Even length palindrome (e.g., 1->2->2->1)
   - Not a palindrome

3. Common Mistakes to Avoid:
   - Not handling empty or single node cases
   - Off-by-one errors in finding middle
   - Not properly reversing second half
   - Comparing wrong number of nodes
   - Not checking fast.next before fast.next.next
   - Infinite loops in reversal or comparison

4. Why This Approach is Optimal:
   - O(n) time: single pass through list
   - O(1) space: no extra data structures needed
   - Efficient for interviews
   - Demonstrates multiple linked list techniques

5. Follow-up Questions You Might Get:
   Q: Can you solve without modifying the list?
   A: Yes, use a stack (O(n) space) or recursion (O(n) call stack)

   Q: How would you restore the list after checking?
   A: Reverse the second half again before returning

   Q: Can you do it with recursion?
   A: Yes, but requires O(n) space for call stack

   Q: What if we can use extra space?
   A: Copy to array and use two pointers (simpler but O(n) space)

   Q: How to handle doubly linked list?
   A: Use two pointers from both ends, compare until they meet

6. Time to Solve: Aim for 15-18 minutes including edge cases

7. Key Points to Mention in Interview:
   - Explain the three-phase approach clearly
   - Draw diagrams showing middle finding and reversal
   - Discuss why this is O(1) space (no auxiliary structures)
   - Mention that we're modifying the list
   - Walk through both palindrome and non-palindrome examples

8. Alternative Approaches and Trade-offs:

   Stack-based (O(n) space):
   - Push first half to stack
   - Pop and compare with second half
   - Simpler but uses extra space

   Array conversion (O(n) space):
   - Convert list to array
   - Use two pointers from ends
   - Easiest to implement but requires extra space

   Recursive (O(n) space):
   - Use recursion to reach end
   - Compare on way back
   - Elegant but uses call stack

   Current approach (O(1) space):
   - Best space complexity
   - Requires understanding of multiple techniques
   - Preferred in interviews when space is constrained

9. Testing Strategy:
   - Test empty list
   - Test single node
   - Test two nodes (same and different)
   - Test odd-length palindrome (1->2->1)
   - Test even-length palindrome (1->2->2->1)
   - Test non-palindrome
   - Test all same values (1->1->1->1)

10. Related Problems:
    - Reverse linked list
    - Find middle of linked list
    - Check if array is palindrome
    - Valid palindrome (with characters)
    - Longest palindromic substring

================================================================================
"""
