"""
================================================================================
PROBLEM: Intersection Point in Y Shaped Linked Lists
================================================================================

DESCRIPTION:
Given two singly linked lists of size N and M, find the point where two linked
lists intersect each other. If the lists don't intersect, return -1.

Visual Representation:
    List 1:  1 -> 2 -> 3 \
                          \
                           6 -> 7 -> 8 -> NULL
                          /
    List 2:      4 -> 5 /

    Intersection point: Node with value 6

Note: The intersection is based on reference/pointer, not value.
After intersection, both lists share the same nodes in memory.

================================================================================
APPROACH & REASONING:
================================================================================

We'll discuss two approaches:

1. LENGTH DIFFERENCE APPROACH (Implemented) - RECOMMENDED:
   - Calculate lengths of both linked lists
   - Find the difference in lengths
   - Advance the pointer of the longer list by the difference
   - Now both pointers are equidistant from the intersection point
   - Move both pointers together until they meet

   Time Complexity: O(N + M) where N and M are lengths of the two lists
   Space Complexity: O(1) - only using pointers

   Why this works:
   - The key insight is that after the intersection, both lists share nodes
   - If we align the starting positions (by skipping extra nodes in longer list)
   - Both pointers will meet exactly at the intersection point
   - If lists don't intersect, both will reach NULL together

2. TWO-POINTER CYCLE APPROACH (Alternative):
   - Use two pointers starting from each head
   - When a pointer reaches end, redirect it to the other list's head
   - Both will meet at intersection (or NULL if no intersection)

   Time Complexity: O(N + M)
   Space Complexity: O(1)

   Why this works:
   - Both pointers travel the same total distance: (N + M)
   - They sync up at the intersection point after traversing both lists

================================================================================
FLOWCHART - LENGTH DIFFERENCE APPROACH:
================================================================================

    START
      |
      v
    Initialize:
    ptr1 = head1
    ptr2 = head2
    c1 = 0, c2 = 0
      |
      v
    +--------------------+
    | Calculate length   |
    | of first list (c1) |
    | ptr1 = head1       |
    | while ptr1:        |
    |   c1++             |
    |   ptr1 = ptr1.next |
    +--------------------+
      |
      v
    +--------------------+
    | Calculate length   |
    | of second list(c2) |
    | ptr2 = head2       |
    | while ptr2:        |
    |   c2++             |
    |   ptr2 = ptr2.next |
    +--------------------+
      |
      v
    Reset pointers:
    ptr1 = head1
    ptr2 = head2
    diff = |c1 - c2|
      |
      v
    +----------------+
    | c1 > c2?       |-----> YES ----> Advance ptr1 by diff steps
    +----------------+
      |
     NO
      |
      v
    +----------------+
    | c2 > c1?       |-----> YES ----> Advance ptr2 by diff steps
    +----------------+
      |
     NO (equal lengths)
      |
      v
    +-----------------------+
    | ptr1 != ptr2?         |-----> NO (found intersection!)
    +-----------------------+         |
      |                               v
     YES                        return ptr1.data
      |
      v
    Move both forward:
    ptr1 = ptr1.next
    ptr2 = ptr2.next
      |
      +----(Loop back)


    VISUAL EXAMPLE:

    List 1: 1 -> 2 -> 3 -> 6 -> 7 -> 8     (length = 6)
    List 2:           4 -> 5 -> 6 -> 7 -> 8 (length = 5)
                           ^
                           Intersection at 6

    Step 1: Calculate lengths (c1=6, c2=5, diff=1)
    Step 2: Move ptr1 ahead by 1 (skip node 1)

    Aligned position:
    ptr1:  2 -> 3 -> 6 -> 7 -> 8
    ptr2:  4 -> 5 -> 6 -> 7 -> 8

    Step 3: Move both together until they meet at node 6

================================================================================
"""

class Solution:
    """
    Solution class to find intersection point of two linked lists.
    """

    def intersect(self, head1, head2):
        """
        Find the intersection point of two singly linked lists.

        Args:
            head1: Head of the first linked list
            head2: Head of the second linked list

        Returns:
            Data value of the intersection node, or -1 if no intersection

        Algorithm:
        1. Calculate the length of both linked lists
        2. Find the difference in lengths
        3. Advance the pointer of the longer list by the difference
        4. Move both pointers together until they meet
        5. Return the intersection point or -1

        Time Complexity: O(N + M) where N and M are lengths of the lists
        Space Complexity: O(1) - only using constant extra space

        Example:
            List1: 1->2->3->6->7
            List2: 4->5->6->7
            Output: 6 (intersection point)
        """
        # Initialize pointers to traverse both lists
        ptr1 = head1
        ptr2 = head2

        # Counters to store lengths of both lists
        c1, c2 = 0, 0

        # PHASE 1: Calculate the length of first linked list
        # Traverse entire first list and count nodes
        while ptr1:
            c1 += 1  # Increment counter for each node
            ptr1 = ptr1.next  # Move to next node

        # PHASE 2: Calculate the length of second linked list
        # Traverse entire second list and count nodes
        while ptr2:
            c2 += 1  # Increment counter for each node
            ptr2 = ptr2.next  # Move to next node

        # PHASE 3: Reset pointers to the beginning of both lists
        # We need to traverse again to find intersection
        ptr1 = head1
        ptr2 = head2

        # Calculate absolute difference in lengths
        # This tells us how many extra nodes the longer list has
        diff = abs(c1 - c2)

        # PHASE 4: Bring both lists to the same level
        # Advance the pointer of the longer list by 'diff' steps
        # After this, both pointers will be equidistant from intersection

        if c1 > c2:
            # First list is longer - skip 'diff' nodes
            for i in range(diff):
                ptr1 = ptr1.next
        elif c2 > c1:
            # Second list is longer - skip 'diff' nodes
            for i in range(diff):
                ptr2 = ptr2.next

        # PHASE 5: Move both pointers together until they meet
        # Since they're now equidistant from intersection, they'll meet there
        # If no intersection, both will reach None together
        while ptr1 != ptr2:
            ptr1 = ptr1.next  # Move first pointer forward
            ptr2 = ptr2.next  # Move second pointer forward

        # PHASE 6: Return result
        # If ptr1 is not None, we found intersection - return its data
        # If ptr1 is None, lists don't intersect - return -1
        if ptr1:
            return ptr1.data
        return -1


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Are we looking for intersection by reference or by value?
     (Usually by reference - same node in memory)
   - Can the lists have different lengths? (Yes, usually)
   - What should we return if there's no intersection? (Usually -1 or None)
   - Can the lists be empty? (Yes, handle this edge case)
   - Can we modify the original lists? (Usually no)

2. Edge Cases to Consider:
   - One or both lists are empty → return -1
   - Lists don't intersect → return -1
   - Intersection at the first node (heads are same) → return immediately
   - One list is much longer than the other
   - Lists have same length but no intersection
   - Lists intersect at the last node

3. Common Mistakes to Avoid:
   - Comparing node values instead of node references
   - Not handling the case when lists have different lengths
   - Forgetting to reset pointers after calculating lengths
   - Off-by-one errors when advancing pointers
   - Not checking for NULL/None before accessing .next

4. Alternative Approaches to Discuss:
   - Hash Set approach: Store nodes of one list in set, check second list
     (O(N) space but simpler to implement)
   - Two-pointer cycle approach: Redirect pointers to opposite heads
     (Same complexity but different technique)
   - Difference in lengths: Current approach (Most intuitive)

5. Follow-up Questions You Might Get:
   Q: Can you solve it without calculating lengths?
   A: Yes, use two-pointer approach where pointers swap lists at end

   Q: What if we can use extra space?
   A: Use hash set to store visited nodes from one list

   Q: How would you handle circular linked lists?
   A: Different algorithm needed (Floyd's cycle detection)

   Q: Can you return the node instead of the value?
   A: Yes, just return ptr1 instead of ptr1.data

6. Time to Solve: Aim for 15-20 minutes including edge cases and testing

7. Key Points to Mention in Interview:
   - Explain why length difference approach works
   - Draw a diagram to visualize the Y-shaped intersection
   - Mention that intersection is by reference, not value
   - Walk through both the length calculation and alignment phases
   - Discuss time and space complexity clearly

8. Optimization Notes:
   - This is already optimal: O(N+M) time, O(1) space
   - Cannot do better than O(N+M) as we must examine all nodes at least once
   - The alternative approaches have same complexity but different constants

================================================================================
"""
