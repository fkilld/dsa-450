"""
================================================================================
PROBLEM: Merge Sort for Linked List
================================================================================

DESCRIPTION:
Given a pointer/reference to the head of a linked list, sort the linked list
using Merge Sort algorithm.

Input:  4 -> 2 -> 1 -> 3 -> NULL
Output: 1 -> 2 -> 3 -> 4 -> NULL

Note: If the length of linked list is odd, then the extra node should go in
the first list while splitting.

================================================================================
APPROACH & REASONING:
================================================================================

MERGE SORT ALGORITHM (Divide and Conquer):

Merge Sort is ideal for linked lists because:
1. No random access needed (unlike Quick Sort)
2. No extra space for auxiliary arrays
3. Stable sort (maintains relative order of equal elements)
4. Guaranteed O(n log n) time complexity

Algorithm Overview:
1. DIVIDE: Split the list into two halves using slow/fast pointer technique
2. CONQUER: Recursively sort both halves
3. COMBINE: Merge the two sorted halves into one sorted list

Time Complexity: O(n log n)
- Dividing the list takes O(log n) levels
- Merging at each level takes O(n) time
- Total: O(n log n)

Space Complexity: O(log n)
- Recursive call stack depth is O(log n)
- No auxiliary arrays needed (in-place for linked lists)

Why Merge Sort works for Linked Lists:
- Linked lists don't support random access, making Quick Sort less efficient
- Merge operation is naturally efficient with linked lists (just pointer manipulation)
- No need to shift elements like in arrays

Key Components:
1. find_middle(): Uses slow/fast pointer to find the middle
2. merge(): Merges two sorted lists into one sorted list
3. mergeSort(): Main recursive function that divides and conquers

================================================================================
FLOWCHART:
================================================================================

    mergeSort(head)
          |
          v
    +-------------------------+
    | head==NULL or           |-----> YES ----> return head
    | head.next==NULL?        |                 (base case)
    +-------------------------+
          |
         NO
          |
          v
    Find middle using
    slow/fast pointers:
    middle = find_middle(head)
          |
          v
    Split the list:
    middleNext = middle.next
    middle.next = NULL
          |
          v
    Recursively sort left half:
    left = mergeSort(head)
          |
          v
    Recursively sort right half:
    right = mergeSort(middleNext)
          |
          v
    Merge sorted halves:
    head = merge(left, right)
          |
          v
    return head


    MERGE PROCESS:

    merge(first, second)
          |
          v
    +-----------------+
    | first == NULL?  |-----> YES ----> return second
    +-----------------+
          |
    +-----------------+
    | second == NULL? |-----> YES ----> return first
    +-----------------+
          |
         NO
          |
          v
    +---------------------------+
    | first.data <= second.data?|
    +---------------------------+
          |                    |
         YES                  NO
          |                    |
          v                    v
    answer = first        answer = second
    answer.next =         answer.next =
    merge(first.next,     merge(first,
          second)               second.next)
          |                    |
          +--------------------+
                    |
                    v
              return answer


    VISUAL EXAMPLE:

    Original:  4 -> 2 -> 1 -> 3

    Split:     4 -> 2    |    1 -> 3
                |        |      |
    Split:    4 | 2      |    1 | 3
                |  |     |      |  |
    Merge:    2->4       |    1->3
                |        |      |
    Merge:    1 -> 2 -> 3 -> 4

    Detailed merge example:
    Merge(2->4, 1->3):
      1 < 2, so pick 1: 1 -> merge(2->4, 3)
        2 < 3, so pick 2: 2 -> merge(4, 3)
          3 < 4, so pick 3: 3 -> merge(4, NULL)
            return 4
        Result: 3 -> 4
      Result: 2 -> 3 -> 4
    Final: 1 -> 2 -> 3 -> 4

================================================================================
"""

class Solution:
    """
    Solution class implementing Merge Sort for linked lists.
    """

    def find_middle(self, curr):
        """
        Find the middle node of a linked list using slow/fast pointer technique.

        Args:
            curr: Head of the linked list

        Returns:
            Middle node of the list

        Algorithm:
        - Use two pointers: slow (moves 1 step) and fast (moves 2 steps)
        - When fast reaches end, slow is at middle
        - For odd length: slow at exact middle
        - For even length: slow at end of first half

        Time Complexity: O(n)
        Space Complexity: O(1)

        Example:
            1->2->3->4->5: returns node 3
            1->2->3->4: returns node 2
        """
        # Initialize slow pointer at head
        slow = curr

        # Initialize fast pointer one step ahead
        # This ensures for even-length lists, slow stops at end of first half
        fast = curr.next

        # Move fast by 2 steps and slow by 1 step
        # When fast reaches end, slow is at middle
        while fast != None:
            fast = fast.next  # Move fast one step
            if fast != None:
                slow = slow.next  # Move slow only if fast hasn't reached end
                fast = fast.next  # Move fast second step

        # slow now points to the middle node
        return slow

    def merge(self, first, second):
        """
        Merge two sorted linked lists into one sorted list.

        Args:
            first: Head of first sorted linked list
            second: Head of second sorted linked list

        Returns:
            Head of the merged sorted list

        Algorithm:
        - Compare first nodes of both lists
        - Pick the smaller one and recursively merge the rest
        - Base cases: if one list is empty, return the other

        Time Complexity: O(n + m) where n, m are lengths of the lists
        Space Complexity: O(n + m) due to recursion stack

        Example:
            first: 1->3->5
            second: 2->4->6
            Result: 1->2->3->4->5->6
        """
        answer = None

        # Base case 1: If first list is empty, return second list
        if not first:
            return second
        # Base case 2: If second list is empty, return first list
        elif not second:
            return first

        # Recursive case: Compare and merge
        if first.data <= second.data:
            # First element is smaller
            answer = first
            # Recursively merge rest of first with entire second
            answer.next = self.merge(first.next, second)
        else:
            # Second element is smaller
            answer = second
            # Recursively merge entire first with rest of second
            answer.next = self.merge(first, second.next)

        return answer

    def mergeSort(self, head):
        """
        Sort a linked list using Merge Sort algorithm.

        Args:
            head: Head of the unsorted linked list

        Returns:
            Head of the sorted linked list

        Algorithm:
        1. Base case: If list is empty or has one node, it's already sorted
        2. Find the middle of the list
        3. Split the list into two halves
        4. Recursively sort both halves
        5. Merge the sorted halves

        Time Complexity: O(n log n)
        - O(log n) levels of recursion
        - O(n) work at each level for finding middle and merging

        Space Complexity: O(log n)
        - Recursion stack depth

        Example:
            Input: 4->2->1->3
            Output: 1->2->3->4
        """
        # Base case: Empty list or single node is already sorted
        if not head or not head.next:
            return head

        # STEP 1: Find the middle of the list
        # This will be the end of the first half
        middle = self.find_middle(head)

        # STEP 2: Split the list into two halves
        # Save the start of second half
        middleNext = middle.next
        # Break the link to split the list
        middle.next = None

        # STEP 3: Recursively sort the left half
        # Sort from head to middle
        left = self.mergeSort(head)

        # STEP 4: Recursively sort the right half
        # Sort from middleNext to end
        right = self.mergeSort(middleNext)

        # STEP 5: Merge the two sorted halves
        head = self.merge(left, right)

        # Return the head of the sorted list
        return head


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Should the sort be stable? (Merge sort is naturally stable)
   - Can we modify the original list or create a new one? (Usually modify)
   - What should we do with an empty list? (Return None/NULL)
   - Are there duplicate values? (Yes, handle them)
   - What's the expected size of the list? (Helps decide algorithm)

2. Edge Cases to Consider:
   - Empty list (head is None) → return None
   - Single node → return head (already sorted)
   - Two nodes → split and merge correctly
   - All elements are the same → return list as-is
   - Already sorted list (ascending or descending)
   - Odd vs even number of nodes (affects middle splitting)

3. Common Mistakes to Avoid:
   - Forgetting to break the link when splitting (middle.next = None)
   - Not handling the base case properly
   - Infinite recursion due to incorrect middle finding
   - Not considering odd/even length lists when finding middle
   - Memory leaks (in languages with manual memory management)

4. Why Merge Sort over Quick Sort for Linked Lists:
   - Quick Sort requires random access for efficient partitioning
   - Linked lists don't support O(1) random access
   - Merge operation is naturally efficient with pointers
   - Guaranteed O(n log n) time (Quick Sort can be O(n²) worst case)

5. Follow-up Questions You Might Get:
   Q: Can you implement iterative merge sort?
   A: Yes, use bottom-up approach with multiple passes

   Q: How would you optimize space complexity?
   A: Already optimal for linked lists (O(log n) stack only)

   Q: What if the list is already sorted?
   A: Still O(n log n) - Merge Sort doesn't adapt to sorted input

   Q: Can you sort in descending order?
   A: Yes, change comparison in merge() from <= to >=

   Q: How does this compare to sorting an array?
   A: Arrays need O(n) extra space, linked lists don't

6. Time to Solve: Aim for 20-25 minutes including all helper functions

7. Key Points to Mention in Interview:
   - Explain the divide-and-conquer paradigm
   - Draw the recursion tree to show O(n log n) complexity
   - Mention why find_middle uses fast.next (for even-length lists)
   - Explain why merge sort is preferred over quick sort for lists
   - Walk through a small example step by step

8. Alternative Approaches:
   - Bottom-up iterative merge sort: O(1) extra space but more complex
   - Convert to array, sort, convert back: O(n) space, simpler
   - Insertion sort: O(n²) but good for small or nearly sorted lists

9. Optimization Tips:
   - For small sublists (< 10 nodes), insertion sort might be faster
   - Can combine with insertion sort for hybrid approach
   - The fast.next initialization is crucial for correct middle finding

10. Related Problems:
    - Sort a K-sorted linked list (use min-heap)
    - Merge K sorted lists (use priority queue)
    - Find median of sorted linked lists

================================================================================
"""
