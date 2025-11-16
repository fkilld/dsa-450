"""
================================================================================
PROBLEM: Remove Duplicates from Unsorted Linked List
================================================================================

DESCRIPTION:
Given an unsorted singly linked list, remove all duplicate nodes such that
each element appears only once. The order of first occurrence should be
preserved.

Input:  5 -> 2 -> 2 -> 4 -> 5 -> 1 -> 4 -> NULL
Output: 5 -> 2 -> 4 -> 1 -> NULL

Unlike the sorted version (Problem 5), duplicates are not necessarily adjacent,
so we need a different approach to track which values we've already seen.

================================================================================
APPROACH & REASONING:
================================================================================

Since the list is UNSORTED, we cannot rely on adjacent comparisons.
We need to remember all values we've seen so far.

APPROACH: Hash Set (Dictionary) Method

KEY INSIGHT:
- Use a hash set to track values we've encountered
- For each node, check if its value is in the set
- If not in set: add it and move forward
- If in set: it's a duplicate, skip this node

ALGORITHM:

1. Create an empty hash set to store seen values
2. Initialize prev = head, curr = head.next
3. Add head's value to the set (first node is never a duplicate)
4. For each subsequent node:
   - If curr.data is already in set:
     * It's a duplicate, skip it: prev.next = curr.next
     * Don't move prev (it still points to last unique node)
   - Else:
     * It's unique, add curr.data to set
     * Move prev forward: prev = curr
   - Always move curr forward: curr = curr.next
5. Continue until curr is None

WHY THIS WORKS:
- Hash set provides O(1) lookup time
- We maintain prev pointer to remove duplicates
- First occurrence is always kept
- Subsequent occurrences are removed

Time Complexity: O(n) - single pass, O(1) hash set operations
Space Complexity: O(n) - hash set stores up to n unique values

ALTERNATIVE APPROACH (O(1) space but O(n²) time):
- For each node, scan remaining list to find duplicates
- Remove duplicates as found
- No extra space needed, but slower

================================================================================
FLOWCHART:
================================================================================

    START
      |
      v
    Check if list empty?
      |      |
     YES    NO
      |      |
      v      v
    return  Initialize:
    head    nodes = {head.data}
            prev = head
            curr = head.next
                 |
                 v
    +-------------------+
    | curr != NULL?     |-----> NO ----> return head (done!)
    +-------------------+
      |
     YES
      |
      v
    +-------------------------+
    | curr.data in nodes set? |
    +-------------------------+
      |              |
     YES            NO
      |              |
      v              v
    DUPLICATE!    UNIQUE!
    Skip node:    Add to set:
    prev.next =   nodes[curr.data] = 1
    curr.next     prev = curr
      |              |
      +------+-------+
             |
             v
      Move curr forward:
      curr = curr.next
             |
             +---(Loop back to condition)


    VISUAL EXAMPLE:

    Input:  5 -> 2 -> 2 -> 4 -> 5 -> 1 -> NULL

    Step 0: Initialize
            nodes = {5}
            prev = 5, curr = 2

    Step 1: Check 2
            [5] -> (2) -> 2 -> 4 -> 5 -> 1 -> NULL
            prev   curr
            2 not in {5}, add it: nodes = {5, 2}
            Move: prev = 2, curr = 2

    Step 2: Check 2 (second occurrence)
            5 -> [2] -> (2) -> 4 -> 5 -> 1 -> NULL
                 prev   curr
            2 in {5, 2}, DUPLICATE!
            Skip: prev.next = curr.next
            5 -> [2] -> 4 -> 5 -> 1 -> NULL
                 prev  curr (moved to 4)

    Step 3: Check 4
            5 -> [2] -> (4) -> 5 -> 1 -> NULL
                 prev   curr
            4 not in {5, 2}, add it: nodes = {5, 2, 4}
            Move: prev = 4, curr = 5

    Step 4: Check 5 (second occurrence)
            5 -> 2 -> [4] -> (5) -> 1 -> NULL
                      prev   curr
            5 in {5, 2, 4}, DUPLICATE!
            Skip: prev.next = curr.next
            5 -> 2 -> [4] -> 1 -> NULL
                      prev  curr (moved to 1)

    Step 5: Check 1
            5 -> 2 -> [4] -> (1) -> NULL
                      prev   curr
            1 not in {5, 2, 4}, add it: nodes = {5, 2, 4, 1}
            Move: prev = 1, curr = NULL

    Step 6: curr = NULL, done!
            Result: 5 -> 2 -> 4 -> 1 -> NULL

================================================================================
"""

class Solution:
    """
    Solution class to remove duplicates from an unsorted linked list.
    """

    def removeDuplicates(self, head):
        """
        Remove all duplicate nodes from an unsorted linked list.

        Args:
            head: The head node of the unsorted linked list

        Returns:
            head: The head of the modified list (unchanged reference)

        Algorithm:
        1. Use hash set to track seen values
        2. Keep first occurrence, remove subsequent duplicates
        3. Maintain prev pointer to remove nodes

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(n) for the hash set storing unique values

        Example:
            Input:  5 -> 2 -> 2 -> 4 -> 5 -> NULL
            Output: 5 -> 2 -> 4 -> NULL

        Note: This preserves the order of first occurrences.
        """

        # Edge case: empty list
        if head is None:
            return head

        # Initialize hash set with head's value
        # Dictionary in Python works as hash set (keys are unique)
        # We use {value: 1} format, though we only care about keys
        prev = head
        nodes = {head.data: 1}  # Track seen values

        # Start checking from second node
        curr = head.next

        # Traverse the list
        while curr != None:

            # Check if current value has been seen before
            if curr.data in nodes:
                # DUPLICATE FOUND!
                # Remove this node by skipping it
                # prev.next points to the node after curr
                prev.next = curr.next
                # Don't move prev - it should still point to last unique node

            else:
                # UNIQUE VALUE!
                # Add this value to our set of seen values
                nodes[curr.data] = 1

                # Move prev forward to this node
                # (curr is the new "last unique node")
                prev = curr

            # Always move curr forward to next node
            curr = curr.next

        # Return the head (list has been modified in-place)
        return head


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Is the list sorted? (NO - that's the key difference from Problem 5)
   - Should I preserve the order of first occurrences? (Yes, usually)
   - Can I use extra space? (Yes, hash set is acceptable and optimal)
   - What should I return for empty list? (The head itself)
   - Should I modify in-place or create new list? (In-place preferred)

2. Edge Cases to Consider:
   - Empty list (head is None) → return None
   - Single node → no duplicates, return as-is
   - All nodes are duplicates → keep only first
   - No duplicates → list unchanged
   - Duplicates are far apart (not adjacent)
   - Large list with many duplicates

3. Common Mistakes to Avoid:
   - Trying to use sorted-list approach (only works for adjacent duplicates)
   - Moving prev pointer when duplicate is found (wrong!)
   - Forgetting to add head.data to initial set
   - Not checking for empty list (would crash)
   - Starting curr from head instead of head.next
   - Modifying head pointer unnecessarily

4. Space vs Time Trade-off:
   - Hash Set Approach: O(n) time, O(n) space ← RECOMMENDED
   - Nested Loop Approach: O(n²) time, O(1) space
   - Sort First: O(n log n) time, O(1) space (but changes order)

5. Follow-up Questions You Might Get:
   Q: Can you solve without extra space?
   A: Yes, use nested loops - for each node, scan rest to remove duplicates
      (O(n²) time). Code:
      ```python
      curr = head
      while curr:
          runner = curr
          while runner.next:
              if runner.next.data == curr.data:
                  runner.next = runner.next.next
              else:
                  runner = runner.next
          curr = curr.next
      ```

   Q: What if list was sorted?
   A: Much simpler - just compare adjacent nodes (Problem 5, O(1) space)

   Q: Can you use a different data structure?
   A: Could use set instead of dict, or even a sorted array with binary search
      (but hash set is optimal for this use case)

   Q: What if we can modify node values?
   A: Still need hash set to track which values to keep

6. Why Hash Set is Optimal:
   - O(1) lookup time to check if value seen before
   - O(1) insertion time to add new value
   - Python dict/set uses hash table internally
   - Total time: O(n) - can't do better than reading each node once
   - Space: O(k) where k = number of unique values ≤ n

7. Related Problems:
   - Problem 5: Remove duplicates from SORTED list (easier, O(1) space)
   - Remove duplicates from array (similar concept)
   - Two Sum problem (also uses hash set)

8. Time to Solve: Aim for 10-12 minutes including edge cases

9. Interview Strategy:
   - First mention the O(1) space approach exists but is slower
   - Explain why hash set is better for unsorted list
   - Draw diagram showing why we can't just compare adjacent nodes
   - Code with clear comments
   - Test with example where duplicates are far apart

10. Key Points to Mention:
    - "Unlike sorted version, duplicates can be anywhere, need to track all"
    - "Hash set gives O(1) lookup, making this O(n) overall"
    - "We keep first occurrence and remove later ones"
    - "prev pointer is crucial for removing nodes without losing list"

11. Comparison with Sorted Version:
    ```
    SORTED (Problem 5):
    - Compare only adjacent nodes
    - O(1) space (just one pointer)
    - Simpler logic

    UNSORTED (Problem 6):
    - Must track all seen values
    - O(n) space (hash set)
    - Need prev pointer to remove nodes
    ```

12. Python-Specific Notes:
    - Can use set() instead of dict: `nodes = set(); nodes.add(val)`
    - Can use `if val in nodes` for both set and dict
    - Dict notation {val: 1} is fine if you prefer key-value pairs

================================================================================
"""
