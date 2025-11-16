"""
================================================================================
PROBLEM: Quick Sort on Linked List
================================================================================

DESCRIPTION:
Sort the given linked list using Quick Sort algorithm. Quick Sort takes O(n²)
time in worst case and O(n log n) in average and best cases.

Input:  4 -> 2 -> 1 -> 3 -> NULL
Output: 1 -> 2 -> 3 -> 4 -> NULL

Note: Quick Sort is generally not the best choice for linked lists (Merge Sort
is preferred), but it's an important algorithm to understand and can be used
when random access is not critical.

================================================================================
APPROACH & REASONING:
================================================================================

QUICK SORT ALGORITHM (Divide and Conquer):

Quick Sort works by:
1. Choosing a pivot element (here: last element)
2. Partitioning the list around the pivot
3. Recursively sorting the sublists

Time Complexity:
- Best/Average Case: O(n log n) - when partition divides evenly
- Worst Case: O(n²) - when list is already sorted or reverse sorted
- For linked lists, finding pivot position takes O(n) time

Space Complexity: O(log n) to O(n)
- Recursion stack depth
- Best case: O(log n) when balanced partitions
- Worst case: O(n) when unbalanced partitions

Why Quick Sort is challenging for Linked Lists:
- Linked lists don't support random access
- Partitioning requires sequential traversal
- Merge Sort is generally preferred for linked lists
- However, Quick Sort can work with proper implementation

Key Components:
1. partition(): Rearranges list so elements < pivot come before pivot
2. sort(): Recursively sorts sublists before and after pivot
3. quick_sort(): Main function that initiates the sort

Algorithm Steps:
1. Choose last element as pivot
2. Partition list: move elements < pivot to left, >= pivot to right
3. Recursively sort left sublist (before pivot)
4. Recursively sort right sublist (after pivot)

================================================================================
FLOWCHART:
================================================================================

    quick_sort(head)
          |
          v
    Initialize:
    start = head
    end = head
          |
          v
    Find last node:
    while end.next != NULL:
        end = end.next
          |
          v
    Call sort(start, end)
          |
          v
         END


    sort(start, end)
          |
          v
    +--------------------------------+
    | start==NULL or start==end or   |-----> YES ----> return
    | start==end.next?               |                 (base case)
    +--------------------------------+
          |
         NO
          |
          v
    Partition around pivot:
    pivot_prev = partition(start, end)
          |
          v
    Recursively sort left part:
    sort(start, pivot_prev)
          |
          v
    +-------------------------+
    | pivot_prev != NULL?     |
    +-------------------------+
          |                   |
         YES                 NO
          |                   |
          v                   v
    +--------------------------+
    | pivot_prev == start?     |
    +--------------------------+
          |              |
         YES            NO
          |              |
          v              v
    sort(pivot_prev    sort(pivot_prev.next.next, end)
         .next, end)
          |              |
          +------+-------+
                 v
            return


    partition(start, end)
          |
          v
    +--------------------------------+
    | start==end or start==NULL or   |-----> YES ----> return start
    | end==NULL?                     |
    +--------------------------------+
          |
         NO
          |
          v
    Initialize:
    pivot_prev = start
    curr = start
    pivot = end.data
          |
          v
    +--------------------+
    | start != end?      |-----> NO
    +--------------------+         |
          |                        |
         YES                       |
          |                        |
          v                        |
    +-------------------------+    |
    | start.data < pivot?     |    |
    +-------------------------+    |
          |              |         |
         YES            NO         |
          |              |         |
          v              |         |
    pivot_prev = curr    |         |
    swap(curr.data,      |         |
         start.data)     |         |
    curr = curr.next     |         |
          |              |         |
          +------+-------+         |
                 |                 |
                 v                 |
    start = start.next             |
          |                        |
          +----(Loop back)         |
                                   |
                                   v
                          swap(curr.data, end.data)
                          return pivot_prev


    VISUAL EXAMPLE:

    Original: 4 -> 2 -> 1 -> 3  (pivot = 3)

    Partition step:
    - Compare 4 with 3: 4 >= 3, don't move
    - Compare 2 with 3: 2 < 3, move to left
    - Compare 1 with 3: 1 < 3, move to left

    After partition: 2 -> 1 -> 3 -> 4
                          pivot_prev^

    Recursively sort:
    Left: 2 -> 1  becomes  1 -> 2
    Right: 4 (single element, already sorted)

    Final: 1 -> 2 -> 3 -> 4

================================================================================
"""

def partition(start, end):
    """
    Partition the linked list around a pivot element.

    The partition rearranges the list so that all elements less than the
    pivot come before it, and all elements greater than or equal to the
    pivot come after it.

    Args:
        start: First node of the sublist to partition
        end: Last node of the sublist (chosen as pivot)

    Returns:
        Node before the pivot after partitioning

    Algorithm:
    1. Choose end.data as pivot value
    2. Use two pointers: curr (tracks position for next small element)
                         start (scans through list)
    3. When we find element < pivot, swap it with curr and move curr
    4. Finally, place pivot in correct position

    Time Complexity: O(n) where n is number of nodes between start and end
    Space Complexity: O(1)

    Example:
        Input: 4->2->1->3 (pivot=3)
        After partition: 2->1->3->4
    """
    # Base case: if sublist is empty or has one element
    if start == end or start == None or end == None:
        return start

    # Initialize pointers
    pivot_prev = start  # Tracks the node before pivot's final position
    curr = start        # Marks position where next small element should go
    pivot = end.data    # Pivot value (last element)

    # Partition: move all elements < pivot to the left
    while start != end:
        # If current element is less than pivot
        if start.data < pivot:
            # Update pivot_prev to current position
            pivot_prev = curr

            # Swap current element with element at curr position
            # This moves smaller elements to the left
            curr.data, start.data = start.data, curr.data

            # Move curr pointer forward (ready for next small element)
            curr = curr.next

        # Move to next element
        start = start.next

    # Place pivot in its correct position
    # Swap pivot (at end) with element at curr
    curr.data, end.data = end.data, curr.data

    # Return the node before pivot
    # This helps in recursive calls to know where to split
    return pivot_prev


def sort(start, end):
    """
    Recursively sort the linked list using Quick Sort.

    Args:
        start: First node of the sublist to sort
        end: Last node of the sublist to sort

    Algorithm:
    1. Base case: if start >= end, sublist has 0 or 1 element (sorted)
    2. Partition the list around a pivot
    3. Recursively sort the left part (before pivot)
    4. Recursively sort the right part (after pivot)

    Time Complexity:
    - Best/Average: O(n log n)
    - Worst: O(n²)

    Space Complexity: O(log n) to O(n) for recursion stack
    """
    # Base cases: empty, single element, or invalid range
    if start == None or start == end or start == end.next:
        return

    # Partition the list and get node before pivot
    pivot_prev = partition(start, end)

    # Recursively sort the left part (before pivot)
    # Sort from start to pivot_prev
    sort(start, pivot_prev)

    # Recursively sort the right part (after pivot)
    # Need to handle two cases based on where pivot ended up

    if pivot_prev != None and pivot_prev == start:
        # If pivot_prev is same as start, pivot is at start.next
        # Sort from pivot.next (which is start.next.next) to end
        sort(pivot_prev.next, end)
    elif pivot_prev != None and pivot_prev.next != None:
        # Normal case: sort from node after pivot to end
        # pivot is at pivot_prev.next, so sort from pivot_prev.next.next
        sort(pivot_prev.next.next, end)


def quick_sort(head):
    """
    Main function to perform Quick Sort on a linked list.

    Args:
        head: Head of the linked list to be sorted

    Algorithm:
    1. Find the last node of the list (will be used as pivot)
    2. Call the recursive sort function with start and end

    Time Complexity:
    - Best/Average: O(n log n)
    - Worst: O(n²) when list is already sorted

    Space Complexity: O(log n) to O(n) for recursion

    Example:
        Input: 4->2->1->3
        Output: 1->2->3->4 (list is sorted in-place)
    """
    # Initialize pointers to head
    start = head
    end = head

    # Find the last node of the list
    # This will be used as the initial pivot
    while end.next != None:
        end = end.next

    # Call the recursive sort function
    # Sorts the list in-place from start to end
    sort(start, end)


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Should we use Quick Sort specifically, or can we choose the algorithm?
     (Usually Merge Sort is better for linked lists)
   - What should be the pivot selection strategy?
     (Last element, first element, random, median-of-three?)
   - Can we modify the list in-place? (Yes, for Quick Sort)
   - What's the expected input? (Sorted, random, reverse sorted?)
   - Are there duplicate elements? (Yes, handle them properly)

2. Edge Cases to Consider:
   - Empty list → return immediately
   - Single node → already sorted
   - Two nodes → partition and done
   - All elements the same → should handle gracefully
   - Already sorted list → worst case O(n²)
   - Reverse sorted list → worst case O(n²)

3. Common Mistakes to Avoid:
   - Not handling the base cases properly
   - Infinite recursion due to incorrect partition logic
   - Off-by-one errors in recursive calls
   - Not properly swapping elements during partition
   - Forgetting to handle the case when pivot_prev is None
   - Not checking for null pointers before accessing .next

4. Quick Sort vs Merge Sort for Linked Lists:

   Quick Sort:
   - In-place sorting (no extra space except stack)
   - Worst case: O(n²) time
   - Not stable (relative order may change)
   - Requires sequential access for partitioning

   Merge Sort:
   - Guaranteed O(n log n) time
   - Stable sort
   - Better for linked lists (no random access needed)
   - RECOMMENDED for linked lists

5. Follow-up Questions You Might Get:
   Q: Why is Merge Sort preferred over Quick Sort for linked lists?
   A: Linked lists lack random access, making partitioning less efficient.
      Merge Sort's sequential merge is more natural for lists.

   Q: How would you optimize Quick Sort for linked lists?
   A: Use randomized pivot, median-of-three, or hybrid with insertion sort
      for small sublists.

   Q: What's the worst case for Quick Sort?
   A: Already sorted or reverse sorted list with last element as pivot.

   Q: Can you make it stable?
   A: Quick Sort is inherently unstable, but can be modified (complex).

   Q: How to avoid worst case?
   A: Use randomized pivot selection or median-of-three method.

6. Time to Solve: Aim for 20-25 minutes including partition logic

7. Key Points to Mention in Interview:
   - Explain why Quick Sort is not ideal for linked lists
   - Discuss the partition strategy and pivot selection
   - Walk through the swapping mechanism during partition
   - Mention the worst-case scenario and how to avoid it
   - Compare with Merge Sort and justify algorithm choice

8. Optimization Strategies:
   - Use randomized pivot to avoid worst case
   - Implement median-of-three for pivot selection
   - Switch to insertion sort for small sublists (< 10 nodes)
   - Use iterative approach to reduce stack space (complex)

9. When to Use Quick Sort on Linked Lists:
   - When space is extremely constrained (in-place sorting)
   - When input is known to be random (not sorted)
   - When average case performance is acceptable
   - When stability is not required

10. Alternative Approaches:
    - Merge Sort: O(n log n) guaranteed, better for linked lists
    - Insertion Sort: O(n²) but good for small lists
    - Convert to array, sort, convert back: Easier but O(n) space

================================================================================
"""
