"""
================================================================================
PROBLEM: Clone Linked List with Next and Random Pointer
================================================================================

DESCRIPTION:
Given a linked list where each node contains:
- data: integer value
- next: pointer to the next node
- random/arb: pointer to any random node in the list or NULL

Create a deep copy (clone) of the linked list. The cloned list should have
completely new nodes with the same data and the same next/random relationships.

Input:
    Node1 (data=1, random=Node3) -> Node2 (data=2, random=Node1) ->
    Node3 (data=3, random=Node3) -> NULL

Output:
    A completely new list with same structure and relationships but different
    node objects in memory.

Note: This is also known as "Copy List with Random Pointer" problem.

================================================================================
APPROACH & REASONING:
================================================================================

OPTIMAL APPROACH: Interleaving Nodes (O(n) time, O(1) space)

Key Insight:
- Challenge: How to map original nodes to cloned nodes for random pointers?
- Solution: Temporarily interleave cloned nodes with original nodes
- This creates a mapping without using extra space (hash map)

Algorithm Steps:
1. Create cloned nodes and insert after each original node
   Original: 1 -> 2 -> 3
   After:    1 -> 1' -> 2 -> 2' -> 3 -> 3'

2. Set random pointers for cloned nodes
   If original.random = X, then clone.random = X.next (X's clone)

3. Separate the two lists
   Restore original: 1 -> 2 -> 3
   Extract clone:    1' -> 2' -> 3'

Time Complexity: O(n) where n is the number of nodes
   - Three passes through the list (create, set random, separate)
   - Each pass is O(n)

Space Complexity: O(1) if we don't count the output list
   - No extra data structure like hash map needed
   - Only a few pointers used

Why this works:
- Interleaving creates implicit mapping: original.next = clone
- Random pointer can be set using: clone.random = original.random.next
- Separation restores original list and extracts clone

Alternative Approach - Hash Map: O(n) time, O(n) space
- First pass: Create all cloned nodes, store in hash map (original -> clone)
- Second pass: Set next and random using hash map lookup
- Simpler but uses O(n) extra space

================================================================================
FLOWCHART:
================================================================================

    copyList(head)
          |
          v
    PHASE 1: Create interleaved list
    +---------------+
    | curr != NULL? |-----> NO
    +---------------+         |
          |                   |
         YES                  |
          |                   |
          v                   |
    Create clone of curr      |
    Insert after curr         |
    curr = clone.next         |
          |                   |
          +---(Loop back)     |
                              |
                              v
    PHASE 2: Set random pointers
    curr = head
    +---------------+
    | curr != NULL? |-----> NO
    +---------------+         |
          |                   |
         YES                  |
          |                   |
          v                   |
    curr.next.arb =           |
    curr.arb.next (if exists) |
    curr = curr.next.next     |
          |                   |
          +---(Loop back)     |
                              |
                              v
    PHASE 3: Separate lists
    original = head
    copy = head.next
    copyHead = head.next
    +------------------------+
    | original != NULL &&    |-----> NO ----> return copyHead
    | copy != NULL?          |
    +------------------------+
          |
         YES
          |
          v
    Restore links:
    original.next = original.next.next
    copy.next = copy.next.next if exists
    Move pointers forward
          |
          +---(Loop back)


    VISUAL EXAMPLE:

    Original List:
        1 (arb->3) -> 2 (arb->1) -> 3 (arb->3)

    Phase 1: Interleave
        1 -> 1' -> 2 -> 2' -> 3 -> 3'
        (arb not set for clones yet)

    Phase 2: Set random pointers
        1.arb = 3, so 1'.arb = 3.next = 3'
        2.arb = 1, so 2'.arb = 1.next = 1'
        3.arb = 3, so 3'.arb = 3.next = 3'

    Phase 3: Separate
        Original: 1 -> 2 -> 3
        Clone:    1' -> 2' -> 3'
        (both with correct random pointers)

================================================================================
"""

class Node:
    """
    Node class for linked list with random pointer.

    Attributes:
        data: The value stored in the node
        next: Reference to the next node
        arb: Random/arbitrary pointer to any node in the list
    """
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.arb = None  # Arbitrary/random pointer

class Solution:
    """
    Solution class to clone a linked list with random pointers.
    """

    def copyList(self, head):
        """
        Clone a linked list with next and random (arb) pointers.

        This implementation uses the interleaving technique which is
        optimal in both time O(n) and space O(1).

        Args:
            head: Head of the original linked list

        Returns:
            Head of the cloned linked list

        Algorithm:
        1. Create cloned nodes interleaved with original nodes
        2. Set random pointers for cloned nodes
        3. Separate original and cloned lists

        Time Complexity: O(n) - three passes through the list
        Space Complexity: O(1) - only using pointers (excluding output)

        Example:
            Input: 1(->3) -> 2(->1) -> 3(->3) where (->X) means random to X

            After Phase 1: 1 -> 1' -> 2 -> 2' -> 3 -> 3'
            After Phase 2: Random pointers set for 1', 2', 3'
            After Phase 3: Original: 1 -> 2 -> 3
                          Clone:    1' -> 2' -> 3'
        """
        # PHASE 1: Create cloned nodes and interleave with original list
        # We insert each clone immediately after its original node
        # This creates an implicit mapping: original.next = clone

        curr = head

        while curr != None:
            # Save reference to the next original node
            temp = curr.next

            # Create a clone of current node with same data
            clone = Node(curr.data)

            # Insert clone between current and next original node
            # Pattern: original -> clone -> next_original
            curr.next = clone
            clone.next = temp

            # Move to next original node (skip the clone we just inserted)
            curr = temp

        # PHASE 2: Set random/arbitrary pointers for cloned nodes
        # Now that clones are interleaved, we can easily set their random pointers
        # For each original node, its clone is original.next
        # If original.arb points to X, then clone.arb should point to X's clone (X.next)

        curr = head

        while curr != None:
            # curr is an original node
            # curr.next is its clone

            # Set clone's arbitrary pointer
            # If original has no random pointer, clone shouldn't either
            if curr.arb:
                # curr.arb is the original node that random points to
                # curr.arb.next is the clone of that node
                curr.next.arb = curr.arb.next
            else:
                curr.next.arb = None

            # Move to next original node (skip clone)
            # curr.next is clone, curr.next.next is next original
            curr = curr.next.next

        # PHASE 3: Separate the interleaved list into two lists
        # Restore original list and extract the cloned list

        original = head  # Pointer to traverse original list
        if head:
            copy = head.next  # Pointer to traverse cloned list
        else:
            return None

        copyHead = head.next  # Save head of cloned list to return

        # Separate the lists by restoring proper next pointers
        while original != None and copy != None:
            # Restore original list's next pointer
            # original -> clone -> next_original
            # Should become: original -> next_original
            original.next = original.next.next

            # Set clone's next pointer
            # clone -> next_original -> next_clone
            # Should become: clone -> next_clone
            if copy.next:
                copy.next = copy.next.next
            else:
                copy.next = None

            # Move to next nodes
            original = original.next
            copy = copy.next

        # Return the head of the cloned list
        return copyHead


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

"""
To test this solution:

1. Create a linked list with random pointers:
    head = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    head.next = node2
    node2.next = node3

    head.arb = node3  # 1's random points to 3
    node2.arb = head  # 2's random points to 1
    node3.arb = node3 # 3's random points to itself

2. Clone the list:
    solution = Solution()
    cloned_head = solution.copyList(head)

3. Verify the clone:
    - All nodes should be different objects (different memory addresses)
    - But data and relationships should be identical
    - Modifying clone shouldn't affect original

4. Print to verify:
    current = cloned_head
    while current:
        arb_data = current.arb.data if current.arb else None
        print(f"Node: {current.data}, Random: {arb_data}")
        current = current.next

Expected Output:
    Node: 1, Random: 3
    Node: 2, Random: 1
    Node: 3, Random: 3
"""

"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Can the random pointer point to the node itself? (Yes)
   - Can the random pointer be NULL? (Yes)
   - Should we create new nodes or can we reuse? (Create new - deep copy)
   - What should we return for an empty list? (NULL/None)
   - Can there be cycles in the list via next pointers? (Usually no)
   - Is the list guaranteed to be non-empty? (Handle empty case)

2. Edge Cases to Consider:
   - Empty list (head is NULL) → return NULL
   - Single node with random pointing to itself → clone correctly
   - Single node with random = NULL → handle NULL random
   - All random pointers are NULL → simpler case
   - All random pointers point to head → test mapping
   - Random pointers creating complex relationships → test thorough cloning

3. Common Mistakes to Avoid:
   - Forgetting to handle NULL random pointers
   - Not properly separating the lists (leaving them interleaved)
   - Losing reference to cloned list head before returning
   - Not handling the case when copy.next is NULL in separation phase
   - Modifying original list permanently
   - Shallow copy instead of deep copy (reusing nodes)

4. Why Interleaving is Clever:
   - Creates implicit mapping without hash map
   - O(1) space instead of O(n)
   - Original.next always points to its clone
   - Allows easy random pointer setting: original.random.next is clone of random
   - Can separate lists cleanly afterward

5. Comparison of Approaches:

   Hash Map Approach:
   ✓ Easier to understand
   ✓ Simpler implementation
   ✗ O(n) extra space for hash map
   Time: O(n), Space: O(n)

   Interleaving Approach:
   ✓ O(1) space (optimal)
   ✓ Same time complexity
   ✗ More complex logic
   ✗ Temporarily modifies original list structure
   Time: O(n), Space: O(1)

6. Follow-up Questions:
   - Can you do it without modifying the original list's structure?
     (Yes, but would need hash map - O(n) space)
   - What if there are multiple random pointers per node?
     (Same approach works, just set multiple random fields)
   - How would you verify the clone is correct?
     (Check all nodes are different objects but same relationships)
   - Can you do it recursively?
     (Yes, but might hit stack limit and is more complex)

7. Key Insight for Interview:
   The brilliance of this problem:
   - Shows understanding of pointer manipulation
   - Demonstrates space optimization thinking
   - Tests ability to handle complex data structures
   - Requires careful handling of multiple pointer types

8. Time to Solve: Aim for 15-20 minutes including:
   - Understanding the problem: 3-4 minutes
   - Discussing approach: 4-5 minutes
   - Coding the solution: 6-8 minutes
   - Testing with examples: 2-3 minutes

9. Hash Map Approach (Alternative):
   ```python
   def copyListHashMap(head):
       if not head:
           return None

       # Phase 1: Create all nodes and store mapping
       hashmap = {}
       curr = head
       while curr:
           hashmap[curr] = Node(curr.data)
           curr = curr.next

       # Phase 2: Set next and random using hashmap
       curr = head
       while curr:
           if curr.next:
               hashmap[curr].next = hashmap[curr.next]
           if curr.arb:
               hashmap[curr].arb = hashmap[curr.arb]
           curr = curr.next

       return hashmap[head]
   ```

10. Testing Strategy:
    Test with these cases:
    - Empty list
    - Single node (random = NULL)
    - Single node (random = self)
    - Two nodes with various random configurations
    - List where all randoms are NULL
    - List where all randoms point to head
    - Complex case with varied random pointers
    - Verify original list is unchanged after cloning

11. Key Points to Mention in Interview:
    - This is a deep copy, not shallow copy
    - Challenge is maintaining random pointer relationships
    - Interleaving is a clever space optimization
    - Three distinct phases: create, set random, separate
    - Original list structure is temporarily modified but restored

12. Common Interview Follow-up:
    Q: "Why is O(1) space important here?"
    A: For large lists, a hash map would use significant memory.
       The interleaving technique uses only a few pointers regardless
       of list size, making it more scalable.

13. Debugging Tips:
    - Draw the interleaved structure on paper
    - Trace through each phase with a small example
    - Verify random pointers are set before separation
    - Check that both lists are properly separated
    - Ensure no memory leaks or dangling pointers

================================================================================
"""
