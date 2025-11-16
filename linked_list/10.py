"""
================================================================================
PROBLEM: Intersection of Two Sorted Linked Lists
================================================================================

DESCRIPTION:
Given two sorted linked lists, create and return a new linked list representing
the intersection of the two lists. The intersection should contain only the
common elements that appear in both lists.

The new list should be made with its own memory - the original lists should
not be changed.

Input:  First:  1 -> 2 -> 3 -> 4 -> 6 -> NULL
        Second: 2 -> 4 -> 6 -> 8 -> NULL
Output:         2 -> 4 -> 6 -> NULL

Input:  First:  1 -> 2 -> 3 -> NULL
        Second: 4 -> 5 -> 6 -> NULL
Output:         NULL (no common elements)

The result should also be sorted and contain no duplicates.

================================================================================
APPROACH & REASONING:
================================================================================

Since both lists are SORTED, we can use a two-pointer technique to find
common elements efficiently.

KEY INSIGHT:
- Both lists are sorted in increasing order
- We can traverse both lists simultaneously
- When values match, it's part of the intersection
- When values don't match, advance the pointer with smaller value

ALGORITHM (Two-Pointer Merge):

1. Initialize two pointers: i for first list, j for second list
2. Initialize result list: res = None
3. While both pointers are not None:
   a. If i.data == j.data:
      - Found common element
      - Create new node and add to result
      - Move both pointers forward
   b. Else if i.data < j.data:
      - First list value is smaller
      - Move i forward (skip this element)
   c. Else (i.data > j.data):
      - Second list value is smaller
      - Move j forward (skip this element)
4. Return result list

WHY THIS WORKS:
- Sorted property allows us to skip non-matching elements
- When i.data < j.data, we know i.data won't match anything ahead in second
  list (because second list is sorted and increasing)
- Similar logic for j.data < i.data
- Only need one pass through each list

Time Complexity: O(n + m) where n, m are lengths of the two lists
Space Complexity: O(min(n, m)) for result list (worst case: all elements match)

COMPARISON WITH UNSORTED LISTS:
If lists were unsorted, we'd need:
- Hash set approach: O(n + m) time, O(n) space
- Nested loops: O(n × m) time, O(1) space
Sorted property makes this much more efficient!

================================================================================
FLOWCHART:
================================================================================

    START
      |
      v
    Initialize:
    i = first
    j = second
    res = None (result head)
    curr = None (current result node)
      |
      v
    +-------------------------+
    | i != NULL AND j != NULL?|-----> NO ----> return res
    +-------------------------+                 (done!)
      |
     YES
      |
      v
    +------------------+
    | i.data == j.data?|
    +------------------+
      |              |
     YES            NO
      |              |
      v              v
    MATCH!      +------------------+
    Create      | i.data < j.data? |
    new node    +------------------+
      |              |         |
      |             YES       NO
      |              |         |
      |              v         v
      |         i is      j is
      |         smaller   smaller
      |         i=i.next  j=j.next
      |              |         |
      |              +---------+
      |                   |
      v                   |
    Add to result         |
    Move both:            |
    i = i.next            |
    j = j.next            |
      |                   |
      +-------------------+
      |
      +---(Loop back to condition)


    VISUAL EXAMPLE:

    First:  1 -> 2 -> 3 -> 4 -> 6 -> NULL
    Second: 2 -> 4 -> 6 -> 8 -> NULL

    Step 1: i=1, j=2
            1 < 2, move i
            i=2, j=2

    Step 2: i=2, j=2
            2 == 2, MATCH! Add 2 to result
            Result: 2 -> NULL
            i=3, j=4

    Step 3: i=3, j=4
            3 < 4, move i
            i=4, j=4

    Step 4: i=4, j=4
            4 == 4, MATCH! Add 4 to result
            Result: 2 -> 4 -> NULL
            i=6, j=6

    Step 5: i=6, j=6
            6 == 6, MATCH! Add 6 to result
            Result: 2 -> 4 -> 6 -> NULL
            i=NULL, j=8

    Step 6: i=NULL
            Stop (one list exhausted)

    Output: 2 -> 4 -> 6 -> NULL


    TRACE WITH NO INTERSECTION:

    First:  1 -> 3 -> 5 -> NULL
    Second: 2 -> 4 -> 6 -> NULL

    Step 1: i=1, j=2 → 1<2, i=3, j=2
    Step 2: i=3, j=2 → 3>2, i=3, j=4
    Step 3: i=3, j=4 → 3<4, i=5, j=4
    Step 4: i=5, j=4 → 5>4, i=5, j=6
    Step 5: i=5, j=6 → 5<6, i=NULL, j=6
    Step 6: i=NULL → Stop

    Output: NULL (no matches)

================================================================================
"""

class Node:
    """
    Node class representing a single element in the linked list.
    """
    def __init__(self, data):
        self.data = data  # Value stored in node
        self.next = None  # Pointer to next node

class Solution:
    """
    Solution class to find intersection of two sorted linked lists.
    """

    def intersection(self, first, second):
        """
        Find the intersection of two sorted linked lists.

        Args:
            first: Head of the first sorted linked list
            second: Head of the second sorted linked list

        Returns:
            Head of a new linked list containing the intersection
            (common elements), or None if no common elements

        Algorithm:
        Two-pointer technique:
        1. Compare elements from both lists
        2. If equal: add to result, advance both pointers
        3. If first < second: advance first pointer
        4. If first > second: advance second pointer
        5. Continue until one list exhausted

        Time Complexity: O(n + m) where n, m are list lengths
        Space Complexity: O(min(n, m)) for result list

        Example:
            Input:  first = 1->2->3->6, second = 2->4->6->8
            Output: 2->6 (common elements)

        Note: Creates new nodes, doesn't modify original lists
        """

        # Initialize pointers for traversing both lists
        i = first   # Pointer for first list
        j = second  # Pointer for second list

        # Initialize result list
        res = None   # Head of result list
        curr = None  # Current node in result list

        # Traverse both lists simultaneously
        while i != None and j != None:

            # CASE 1: Elements match - part of intersection
            if i.data == j.data:
                # Create new node with the common value
                temp = Node(i.data)

                # Add to result list
                if res == None:
                    # First node in result
                    res = temp
                else:
                    # Link to previous node
                    curr.next = temp

                # Move curr to newly added node
                curr = temp

                # Advance both pointers (skip this common element in both)
                i = i.next
                j = j.next

            # CASE 2: First list element is smaller
            # This element from first list won't match anything in second list
            # (because second list is sorted and all remaining values are >= j.data)
            elif i.data < j.data:
                # Skip this element in first list
                i = i.next

            # CASE 3: Second list element is smaller
            # This element from second list won't match anything in first list
            # (because first list is sorted and all remaining values are >= i.data)
            else:
                # Skip this element in second list
                j = j.next

        # Return the head of intersection list
        # Will be None if no common elements found
        return res


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Are both lists sorted? (Yes - crucial for this approach)
   - Should I modify the original lists? (No - create new list)
   - Can lists have duplicates? (Usually yes, but we only add unique to result)
   - What if one or both lists are empty? (Return None/empty)
   - Should result be sorted? (Yes, naturally sorted by our approach)
   - What if no common elements? (Return None/empty list)

2. Edge Cases to Consider:
   - Empty lists: [] ∩ [1,2,3] = []
   - No common elements: [1,3,5] ∩ [2,4,6] = []
   - All elements common: [1,2,3] ∩ [1,2,3] = [1,2,3]
   - One element each: [5] ∩ [5] = [5]
   - Different lengths: [1,2,3,4,5] ∩ [2,4] = [2,4]
   - Duplicates in input: handled by == condition

3. Common Mistakes to Avoid:
   - Modifying original lists instead of creating new nodes
   - Not handling empty list case
   - Wrong pointer advancement (moving wrong pointer when values differ)
   - Not checking for None before accessing .data
   - Forgetting to link nodes in result list
   - Not initializing res and curr properly

4. Why Two-Pointer Approach Works:
   - Sorted lists mean we can skip elements intelligently
   - When i.data < j.data, we know i won't match any future j values
   - Single pass through each list is sufficient
   - No need for nested loops or hash sets
   - Time complexity is linear, not quadratic

5. Follow-up Questions You Might Get:
   Q: What if lists aren't sorted?
   A: Use hash set - add all elements from first to set, traverse second
      and add to result if in set. O(n+m) time, O(n) space.
      Code:
      ```python
      seen = set()
      curr = first
      while curr:
          seen.add(curr.data)
          curr = curr.next
      # Then traverse second and check membership
      ```

   Q: Can you do it without creating new nodes?
   A: Problem requires new list, but could return array of common values

   Q: What about union instead of intersection?
   A: Use merge algorithm, include all unique elements from both

   Q: What if we want to modify first list to be the intersection?
   A: More complex - need to track prev pointer and remove nodes

   Q: How to handle duplicates in result?
   A: Current solution handles it - move both pointers on match

6. Comparison: Sorted vs Unsorted:
   ```
   SORTED (This problem):
   - Two pointers, one pass each
   - O(n+m) time, O(1) extra space (besides result)
   - Simple, elegant

   UNSORTED:
   - Hash set approach
   - O(n+m) time, O(n) extra space
   - More memory usage
   ```

7. Related Problems:
   - Merge Two Sorted Lists (similar two-pointer technique)
   - Intersection of Two Arrays (same concept, different data structure)
   - Union of Two Sorted Lists (include all, not just common)
   - Find common elements in k sorted lists

8. Time to Solve: Aim for 10-12 minutes including edge cases

9. Interview Strategy:
   - Clarify that lists are sorted (changes everything)
   - Draw simple example on whiteboard
   - Explain why we can skip elements (sorted property)
   - Code with clear variable names (i, j, res)
   - Test with: matching elements, no matches, empty list

10. Key Points to Mention:
    - "Sorted property allows linear time solution"
    - "Two pointers avoid nested loops"
    - "Skip smaller element because it won't match anything ahead"
    - "Create new nodes - don't modify original lists"
    - "Result is naturally sorted"

11. Alternative Implementation (More Pythonic):
    ```python
    def intersection(self, first, second):
        # Convert to sets and find intersection
        set1 = {node.data for node in self.to_list(first)}
        set2 = {node.data for node in self.to_list(second)}
        common = sorted(set1 & set2)
        return self.create_list(common)
    ```
    But two-pointer is preferred for interviews (shows algorithm skills)

12. Memory Consideration:
    - Input lists: O(n) + O(m)
    - Result list: O(k) where k = number of common elements
    - Algorithm extra space: O(1) - just pointers
    - Total space: O(k) for result

13. Testing Strategy:
    Test these cases:
    - [1,2,3] ∩ [2,3,4] = [2,3]
    - [1,3,5] ∩ [2,4,6] = []
    - [] ∩ [1,2,3] = []
    - [5] ∩ [5] = [5]
    - [1,2,2,3] ∩ [2,2,4] = [2]

14. Optimization Notes:
    - Can't do better than O(n+m) - must examine all elements
    - Space for result is unavoidable (problem requires new list)
    - Current solution is optimal for this problem

15. Set Theory Context:
    This problem implements set intersection (A ∩ B):
    - Elements that belong to BOTH sets
    - Different from union (A ∪ B): elements in EITHER set
    - Different from difference (A - B): elements in A but not B

================================================================================
"""
