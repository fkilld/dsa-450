"""
================================================================================
PROBLEM: Sort Linked List of 0s, 1s and 2s
================================================================================

DESCRIPTION:
Given a linked list of N nodes where nodes can contain values 0, 1, or 2 only.
The task is to segregate 0s, 1s, and 2s in the linked list such that all zeros
are at the head, 2s at the end, and 1s in the middle of 0s and 2s.

Input:  1 -> 2 -> 2 -> 1 -> 2 -> 0 -> 2 -> 2
Output: 0 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 2

Input:  2 -> 2 -> 0 -> 1
Output: 0 -> 1 -> 2 -> 2

Note: This is similar to the Dutch National Flag problem for arrays.

================================================================================
APPROACH & REASONING:
================================================================================

We'll implement TWO approaches:

APPROACH 1: Count and Replace (Simpler but modifies data)
- Count occurrences of 0, 1, and 2
- Traverse again and fill with 0s, then 1s, then 2s
- Time: O(n), Space: O(1)
- Drawback: Modifies node data (not always acceptable)

APPROACH 2: Link Rearrangement (Better - preserves nodes)
- Create three separate lists for 0, 1, and 2
- Traverse original list and attach nodes to respective lists
- Connect the three lists: 0s -> 1s -> 2s
- Time: O(n), Space: O(1)
- Advantage: Only changes links, preserves original nodes

RECOMMENDED: Approach 2 (Link Rearrangement)
- Doesn't modify node data
- Only rearranges pointers
- More general solution (works even if nodes have complex data)

================================================================================
FLOWCHART - APPROACH 1 (Count and Replace):
================================================================================

    segregate(head)
          |
          v
    Count occurrences:
    count[0] = count[1] = count[2] = 0
          |
          v
    Traverse list:
    count each 0, 1, 2
          |
          v
    Traverse again:
    Fill count[0] nodes with 0
    Fill count[1] nodes with 1
    Fill count[2] nodes with 2
          |
          v
    return head


    VISUAL EXAMPLE:
    Input:  1 -> 2 -> 2 -> 1 -> 2 -> 0 -> 2 -> 2

    After counting:
    count[0] = 1, count[1] = 2, count[2] = 5

    Replace:
    0 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 2

================================================================================
FLOWCHART - APPROACH 2 (Link Rearrangement):
================================================================================

    segregate_links(head)
          |
          v
    Create dummy heads:
    zero_head = Node(-1)
    one_head = Node(-1)
    two_head = Node(-1)
          |
          v
    Initialize pointers:
    zero = zero_head
    one = one_head
    two = two_head
    curr = head
          |
          v
    +---------------+
    | curr != NULL? |-----> NO
    +---------------+         |
          |                   |
         YES                  |
          |                   |
          v                   |
    +------------------+      |
    | curr.data == 0?  |      |
    +------------------+      |
      |       |        |      |
     YES     NO        |      |
      |       |        |      |
      v       v        v      |
    Attach  Check    Check    |
    to 0s   if 1     if 2     |
    list    attach   attach   |
            to 1s    to 2s    |
      |       |        |      |
      +-------+--------+      |
              |               |
              v               |
        curr = curr.next      |
              |               |
              +----(Loop back)|
                              |
                              v
    Connect lists:
    zero.next = one_head.next if exists else two_head.next
    one.next = two_head.next
    two.next = NULL
          |
          v
    return zero_head.next


    VISUAL EXAMPLE:
    Input:  1 -> 2 -> 2 -> 1 -> 2 -> 0 -> 2 -> 2

    During traversal:
    0s list: -1 -> 0
    1s list: -1 -> 1 -> 1
    2s list: -1 -> 2 -> 2 -> 2 -> 2 -> 2

    After connection:
    0 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 2

================================================================================
"""

class Node:
    """
    Node class for singly linked list.

    Attributes:
        data: The value stored in the node (0, 1, or 2)
        next: Reference to the next node
    """
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Solution:
    """
    Solution class with two approaches to sort 0s, 1s, and 2s.
    """

    def segregate(self, head):
        """
        Sort linked list of 0s, 1s, and 2s using counting approach.

        This approach counts occurrences and then modifies node data.

        Args:
            head: Head of the linked list

        Returns:
            Head of the sorted linked list

        Algorithm:
        1. Count occurrences of 0, 1, and 2
        2. Traverse list again
        3. Fill first count[0] nodes with 0
        4. Fill next count[1] nodes with 1
        5. Fill remaining nodes with 2

        Time Complexity: O(n) - two passes through the list
        Space Complexity: O(1) - only using a count array

        Drawback: Modifies node data (not ideal in some scenarios)

        Example:
            Input:  1 -> 2 -> 2 -> 1 -> 2 -> 0
            Count: {0: 1, 1: 2, 2: 3}
            Output: 0 -> 1 -> 1 -> 2 -> 2 -> 2
        """
        # Initialize pointer to traverse the list
        curr = head

        # Dictionary to count occurrences of each value
        count = {0: 0, 1: 0, 2: 0}

        # Phase 1: Count occurrences of 0, 1, and 2
        while curr != None:
            count[curr.data] += 1
            curr = curr.next

        # Phase 2: Modify node values based on counts
        i = 0  # Current value to fill (0, 1, or 2)
        curr = head

        while curr != None:
            # If all occurrences of current value are used, move to next value
            if count[i] == 0:
                i += 1
            else:
                # Set current node's data to i
                curr.data = i
                # Move to next node
                curr = curr.next
                # Decrement count for value i
                count[i] -= 1

        return head

    def segregate_links(self, head):
        """
        Sort linked list of 0s, 1s, and 2s by rearranging links.

        This approach creates three separate lists and connects them.
        RECOMMENDED: This doesn't modify node data, only rearranges pointers.

        Args:
            head: Head of the linked list

        Returns:
            Head of the sorted linked list

        Algorithm:
        1. Create three dummy heads for 0s, 1s, and 2s
        2. Traverse the original list
        3. Attach each node to its respective list based on value
        4. Connect the three lists: 0s -> 1s -> 2s
        5. Handle edge cases where some lists might be empty

        Time Complexity: O(n) - single pass through the list
        Space Complexity: O(1) - only using a few pointers

        Advantage: Preserves original nodes, only changes links

        Example:
            Input:  2 -> 1 -> 2 -> 0 -> 1

            After segregation:
            0s: -1 -> 0
            1s: -1 -> 1 -> 1
            2s: -1 -> 2 -> 2

            After connection:
            0 -> 1 -> 1 -> 2 -> 2
        """
        # Create dummy head nodes for each value (0, 1, 2)
        # Using -1 as dummy value to distinguish from actual data
        zero_head = Node(-1)
        one_head = Node(-1)
        two_head = Node(-1)

        # Pointers to track current position in each segregated list
        zero = zero_head  # Points to last node in 0s list
        one = one_head    # Points to last node in 1s list
        two = two_head    # Points to last node in 2s list

        # Pointer to traverse the original list
        curr = head

        # Phase 1: Segregate nodes into three lists
        while curr != None:
            if curr.data == 0:
                # Attach current node to 0s list
                zero.next = curr
                zero = zero.next
            elif curr.data == 1:
                # Attach current node to 1s list
                one.next = curr
                one = one.next
            else:  # curr.data == 2
                # Attach current node to 2s list
                two.next = curr
                two = two.next

            # Move to next node in original list
            curr = curr.next

        # Phase 2: Connect the three lists
        # Connect 0s list to 1s list (or 2s list if 1s is empty)
        # one_head.next will be None if there are no 1s
        # two_head.next will be None if there are no 2s
        zero.next = one_head.next if one_head.next else two_head.next

        # Connect 1s list to 2s list
        one.next = two_head.next

        # Mark end of the combined list
        two.next = None

        # The actual head is zero_head.next (skip the dummy node)
        head = zero_head.next

        return head


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

"""
To test these solutions:

1. Create a linked list with 0s, 1s, and 2s:
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(2)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(0)

2. Use either approach:
    solution = Solution()

    # Approach 1: Count and replace
    sorted_head = solution.segregate(head)

    # OR

    # Approach 2: Link rearrangement (RECOMMENDED)
    sorted_head = solution.segregate_links(head)

3. Print the result:
    current = sorted_head
    while current:
        print(current.data, end=' ')
        current = current.next

Expected Output: 0 1 1 2 2 2
"""

"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Can the list contain values other than 0, 1, 2? (Usually no)
   - Should we modify node data or only rearrange links? (Prefer links)
   - What should we return for an empty list? (NULL/None)
   - Should the relative order of equal elements be preserved? (Usually no)
   - Can we use extra space? (Usually O(1) space is expected)
   - Is the list guaranteed to have at least one of each value? (No)

2. Edge Cases to Consider:
   - Empty list (head is NULL) → return NULL
   - Single node → return as-is
   - All nodes have same value (all 0s, all 1s, or all 2s) → return as-is
   - No 0s → list starts with 1s or 2s
   - No 1s → connect 0s directly to 2s
   - No 2s → list ends with 1s
   - List already sorted → return as-is

3. Common Mistakes to Avoid:
   - Not handling empty sub-lists in link rearrangement
   - Forgetting to set two.next = NULL (creates cycle!)
   - Not checking if one_head.next exists before connecting
   - Returning zero_head instead of zero_head.next
   - In counting approach: off-by-one errors in replacement
   - Not considering the case where all values are the same

4. Why Link Rearrangement is Better:
   - Doesn't modify node data
   - Works even if nodes contain complex data structures
   - More general solution
   - Same time and space complexity as counting
   - Demonstrates better understanding of pointer manipulation

5. Comparison of Both Approaches:

   Count and Replace:
   ✓ Simple to understand
   ✓ Easy to implement
   ✗ Modifies node data
   ✗ Doesn't work if data is immutable
   Time: O(n), Space: O(1)

   Link Rearrangement:
   ✓ Doesn't modify data
   ✓ Only rearranges pointers
   ✓ More general solution
   ✗ Slightly more complex
   Time: O(n), Space: O(1)

6. Follow-up Questions:
   - Can you do this with only one pass?
     (Yes, link rearrangement does it in one pass)
   - What if values can be any integers, not just 0, 1, 2?
     (Use general sorting like merge sort)
   - How would you maintain relative order (stable sort)?
     (Current link rearrangement is stable!)
   - Can you do this for an array?
     (Yes, Dutch National Flag algorithm)

7. Relation to Dutch National Flag Problem:
   - This is the linked list version
   - Array version uses three-way partitioning
   - Same concept: partition into three groups
   - Linked list requires different technique (can't swap easily)

8. Time to Solve: Aim for 12-15 minutes including:
   - Understanding the problem: 2-3 minutes
   - Discussing both approaches: 3-4 minutes
   - Coding link rearrangement: 5-6 minutes
   - Testing with examples: 2-3 minutes

9. Testing Strategy:
   Test with these cases:
   - Empty list
   - Single node with each value (0, 1, 2)
   - All same values
   - No 0s: [1, 2, 1, 2]
   - No 1s: [2, 0, 2, 0]
   - No 2s: [0, 1, 0, 1]
   - Already sorted: [0, 1, 2]
   - Reverse sorted: [2, 1, 0]
   - Random: [1, 2, 2, 1, 2, 0, 2, 2]

10. Key Points to Mention in Interview:
    - Both approaches have O(n) time, O(1) space
    - Link rearrangement is preferred as it doesn't modify data
    - The problem is also known as "Dutch National Flag" for linked lists
    - Dummy nodes simplify edge case handling
    - Must remember to set two.next = NULL to avoid cycles

11. Common Interview Follow-up:
    Q: "Which approach would you recommend and why?"
    A: Link rearrangement approach because:
       - Doesn't modify original node data
       - Works in one pass
       - Demonstrates better understanding of pointers
       - More general solution

12. Optimization Notes:
    - Can't do better than O(n) time (must visit each node)
    - Already optimal at O(1) space
    - Single pass is achieved with link rearrangement
    - Stable sorting (relative order preserved) is a bonus

================================================================================
"""
