"""
================================================================================
PROBLEM: Sort a K-Sorted Doubly Linked List
================================================================================

DESCRIPTION:
Given a doubly linked list containing n nodes, where each node is at most k
positions away from its target position in the sorted list. Sort the given
doubly linked list efficiently.

A k-sorted list means that each element is at most k positions away from where
it would be in a fully sorted list.

Input:  3 <-> 6 <-> 2 <-> 12 <-> 56 <-> 8, k = 2
Output: 2 <-> 3 <-> 6 <-> 8 <-> 12 <-> 56

Explanation: Each element is at most 2 positions away from its target:
- 3 is at index 0, should be at index 1 (distance = 1)
- 6 is at index 1, should be at index 2 (distance = 1)
- 2 is at index 2, should be at index 0 (distance = 2)
etc.

================================================================================
APPROACH & REASONING:
================================================================================

OPTIMAL APPROACH: Min-Heap (Priority Queue)

Key Insight:
- Since each element is at most k positions away from its sorted position,
  the smallest element must be within the first k+1 elements
- We can use a min-heap of size k+1 to efficiently find and place elements
- This is much better than O(n log n) sorting when k << n

Algorithm Steps:
1. Create a min-heap and insert first k+1 elements
2. Extract minimum from heap (this is the first element in sorted order)
3. Add next element from list to heap
4. Repeat step 2-3 until all elements are processed
5. Empty remaining elements from heap

Time Complexity: O(n log k) where n is number of nodes
   - We process n elements
   - Each heap operation (insert/extract) takes O(log k)
   - Total: O(n log k)

Space Complexity: O(k) for the heap

Why this works:
- The smallest element is guaranteed to be in the first k+1 elements
- After placing it, the next smallest is in the next k+1 elements window
- Min-heap efficiently maintains the minimum among k+1 elements
- This is optimal when k << n (much better than O(n log n) full sort)

Alternative Approach - Full Sort: O(n log n)
- Convert to array, sort, rebuild list
- Works but doesn't utilize the k-sorted property

================================================================================
FLOWCHART:
================================================================================

    sort(head, k)
          |
          v
    +-------------+
    | head==NULL? |-----> YES ----> return NULL
    +-------------+
          |
         NO
          |
          v
    Create min-heap (size k+1)
          |
          v
    Insert first (k+1) elements
    into heap
          |
          v
    Initialize:
    newHead = NULL
    curr = NULL
          |
          v
    +------------------+
    | heap not empty?  |-----> NO ----> return newHead
    +------------------+
          |
         YES
          |
          v
    Extract min from heap
          |
          v
    +------------------+
    | newHead == NULL? |-----> YES ----> newHead = extracted node
    +------------------+               curr = newHead
          |
         NO
          |
          v
    curr.next = extracted node
    extracted.prev = curr
    curr = curr.next
          |
          v
    +--------------------+
    | more nodes in list?|-----> YES ----> Insert next node
    +--------------------+                  into heap
          |
         NO
          |
          +----(Loop back to "heap not empty?")


    VISUAL EXAMPLE (k = 2):

    Original: 3 <-> 6 <-> 2 <-> 12 <-> 56 <-> 8

    Step 1: Insert first k+1=3 elements into heap
            Heap: [2, 3, 6]
            Remaining: 12 <-> 56 <-> 8

    Step 2: Extract min (2), add next (12)
            Sorted: 2
            Heap: [3, 6, 12]
            Remaining: 56 <-> 8

    Step 3: Extract min (3), add next (56)
            Sorted: 2 <-> 3
            Heap: [6, 12, 56]
            Remaining: 8

    Step 4: Extract min (6), add next (8)
            Sorted: 2 <-> 3 <-> 6
            Heap: [8, 12, 56]
            Remaining: (empty)

    Step 5: Extract remaining from heap
            Sorted: 2 <-> 3 <-> 6 <-> 8 <-> 12 <-> 56

================================================================================
"""

# Getting the priority queue (min-heap implementation)
from queue import PriorityQueue

class Node:
    """
    Node class for doubly linked list.

    Attributes:
        data: The value stored in the node
        next: Reference to the next node
        prev: Reference to the previous node
    """
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """
    DoublyLinkedList class with method to sort k-sorted list efficiently.

    Attributes:
        head: Reference to the first node in the list
    """
    def __init__(self):
        self.head = None

    def push(self, data):
        """
        Insert a new node at the beginning of the doubly linked list.

        Args:
            data: Value to be stored in the new node

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Create new node with given data
        temp = Node(data)

        # If list is empty, new node becomes the head
        if self.head == None:
            self.head = temp
        else:
            # Insert at the beginning
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    def printList(self):
        """
        Print all elements in the doubly linked list.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        temp = self.head
        res = ""
        while temp != None:
            res += str(temp.data) + " "
            temp = temp.next
        print(res)

    def sort(self, head, k):
        """
        Sort a k-sorted doubly linked list using min-heap.

        A k-sorted list is one where each element is at most k positions
        away from its target position in the sorted list.

        Args:
            head: The head node of the doubly linked list
            k: Maximum distance any element is from its sorted position

        Returns:
            The head of the sorted doubly linked list

        Algorithm:
        1. Create a min-heap (priority queue) of size k+1
        2. Insert first k+1 elements into the heap
        3. Extract minimum and build sorted list
        4. For each extracted element, add next element to heap
        5. Continue until all elements are processed

        Time Complexity: O(n log k) where n is the number of nodes
            - Each of n elements is inserted and extracted from heap: O(n)
            - Each heap operation takes O(log k)
            - Total: O(n log k)

        Space Complexity: O(k) for the heap

        Example:
            Input: 3 <-> 6 <-> 2 <-> 12 <-> 56 <-> 8, k = 2

            Heap operations:
            - Insert 3, 6, 2 → heap = [2, 3, 6]
            - Extract 2, insert 12 → heap = [3, 6, 12]
            - Extract 3, insert 56 → heap = [6, 12, 56]
            - Extract 6, insert 8 → heap = [8, 12, 56]
            - Extract 8, 12, 56 in order

            Output: 2 <-> 3 <-> 6 <-> 8 <-> 12 <-> 56
        """
        # Edge case: empty list
        if head == None:
            return None

        # Create a priority queue (min-heap) with capacity k+1
        # Why k+1? Because the minimum element is guaranteed to be
        # among the first k+1 elements in a k-sorted list
        pq = PriorityQueue(k + 1)

        i = 0
        # Phase 1: Insert first k+1 elements into the priority queue
        # We store tuples (data, node) because PriorityQueue compares
        # by the first element (data) for priority
        while i <= k and head != None:
            # Insert tuple: (priority_value, node_object)
            # The queue will order by data value
            pq.put((head.data, head))
            head = head.next
            i += 1

        # Initialize pointers for building the sorted list
        newHead = None  # Will be the head of sorted list
        curr = None     # Current position in sorted list

        # Phase 2: Process remaining elements
        # Continue until heap is empty
        while not pq.empty():
            # Extract the node with minimum data value
            min_node = pq.get()[1]  # Get node from tuple (data, node)

            if newHead == None:
                # First node in sorted list
                newHead = min_node
                newHead.prev = None  # First node has no previous
                curr = newHead
            else:
                # Append to sorted list
                curr.next = min_node
                min_node.prev = curr
                curr = curr.next

            # If there are more nodes in original list, add next one to heap
            # This maintains the window of k+1 elements in the heap
            if head != None:
                pq.put((head.data, head))
                head = head.next

        # Mark the end of the sorted list
        curr.next = None

        return newHead


# ============================================================================
# EXAMPLE EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Create a new doubly linked list
    dll = DoublyLinkedList()

    # Build k-sorted list: 3 <-> 6 <-> 2 <-> 12 <-> 56 <-> 8
    # (push adds to front, so we push in reverse order)
    dll.push(8)
    dll.push(56)
    dll.push(12)
    dll.push(2)
    dll.push(6)
    dll.push(3)

    print("Before sort:")
    dll.printList()  # Output: 3 6 2 12 56 8

    # Sort with k=2 (each element is at most 2 positions away)
    k = 2
    print(f"\nAfter sorting (k={k}):")
    dll.head = dll.sort(dll.head, k)
    dll.printList()  # Output: 2 3 6 8 12 56

"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - What is the value of k relative to n? (If k ≈ n, might as well use full sort)
   - Are all elements distinct or can there be duplicates? (Doesn't affect algorithm)
   - What should we return for an empty list? (NULL/None)
   - Is k guaranteed to be less than n? (Usually yes, but handle edge cases)
   - Should we modify in-place or create a new list? (Usually in-place is preferred)
   - What's the range of data values? (Affects heap implementation choice)

2. Edge Cases to Consider:
   - Empty list (head is NULL) → return NULL
   - Single node → already sorted, return as-is
   - k = 0 → list is already sorted
   - k >= n-1 → equivalent to fully unsorted, O(n log n) sorting
   - All elements are the same → still works correctly
   - k = 1 → almost sorted, very efficient with this approach

3. Common Mistakes to Avoid:
   - Using heap size k instead of k+1
     (The minimum is in first k+1 elements, not k!)
   - Forgetting to set prev pointers when building sorted list
   - Not setting newHead.prev = NULL and curr.next = NULL
   - Not handling the case when k >= n
   - Forgetting to extract remaining elements from heap after list is exhausted

4. Why This Approach is Better Than Full Sort:
   - Full sort: O(n log n)
   - K-sorted sort: O(n log k)
   - When k << n (e.g., k = 10, n = 1000000):
     * Full sort: O(1000000 × log 1000000) ≈ O(20 million operations)
     * K-sort: O(1000000 × log 10) ≈ O(3.3 million operations)
     * About 6x faster!

5. Alternative Approaches:
   a) Insertion Sort: O(nk) - good when k is very small
   b) Full Sort: O(n log n) - simpler but doesn't use k-sorted property
   c) Min-Heap: O(n log k) - OPTIMAL, current approach
   d) Merge Sort with k-way merge: O(n log k) - similar complexity

6. Follow-up Questions:
   - What if we can't use extra space?
     (Insertion sort with O(nk) time, O(1) space)
   - What if k is very large (close to n)?
     (Use standard O(n log n) sort instead)
   - Can you do it in-place without heap?
     (Yes, but O(nk) time with insertion sort)
   - How would you verify the list is k-sorted?
     (Check each element's distance from sorted position)

7. Key Insight for Interview:
   The beauty of this problem is recognizing that:
   - The k-sorted property gives us valuable information
   - We can use a sliding window of size k+1
   - Min-heap perfectly maintains the minimum in this window
   - This transforms an O(n log n) problem into O(n log k)

8. Time to Solve: Aim for 15-20 minutes including:
   - Understanding the problem: 3-5 minutes
   - Discussing approach: 5 minutes
   - Coding: 8-10 minutes
   - Testing with examples: 2-5 minutes

9. Python-Specific Notes:
   - queue.PriorityQueue is thread-safe but slower
   - For interviews, you could also use heapq module:
     ```python
     import heapq
     heap = []
     heapq.heappush(heap, (data, node))
     min_item = heapq.heappop(heap)
     ```

10. Complexity Trade-offs:
    - Time: O(n log k) - optimal for k-sorted lists
    - Space: O(k) - acceptable for most use cases
    - If k is constant, this becomes O(n) which is optimal!

================================================================================
"""
