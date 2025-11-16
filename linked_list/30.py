"""
================================================================================
PROBLEM: Merge K Sorted Linked Lists
================================================================================

DESCRIPTION:
Given K sorted linked lists of different sizes, merge them into a single
sorted linked list. All lists are sorted in ascending order.

Input:
    K = 3
    List 1: 1 -> 3 -> 5 -> 7
    List 2: 2 -> 4 -> 6 -> 8
    List 3: 0 -> 9 -> 10 -> 11

Output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11

Constraints:
- Each individual list is sorted
- K can be any positive integer
- Lists can have different lengths
- Total number of nodes across all lists = N

================================================================================
APPROACH & REASONING:
================================================================================

OPTIMAL APPROACH: Divide and Conquer (Pair-wise Merging)

Key Insight:
- Instead of merging all K lists at once, merge them pair by pair
- Similar to merge sort's merge operation
- Reduces K lists to K/2, then K/4, and so on until one list remains

Algorithm Steps:
1. Start with K lists in an array
2. While more than one list remains:
   - Pair up lists and merge each pair
   - First with last, second with second-last, etc.
   - This reduces the number of lists by half
3. Continue until only one merged list remains

Time Complexity: O(N log K) where:
   - N is the total number of nodes across all lists
   - K is the number of lists
   - We have log K levels of merging
   - Each level processes all N nodes

Space Complexity: O(1) if we don't count recursion in merge
   - Only using pointers for merging
   - In-place modification of list links

Why this works:
- Each merge operation combines two sorted lists into one sorted list
- By pairing and merging, we systematically reduce the number of lists
- Similar to tournament bracket structure
- Optimal because we minimize comparisons

Alternative Approaches:
1. Sequential Merging: O(NK) - merge lists one by one (inefficient)
2. Min-Heap: O(N log K) - same complexity but uses O(K) extra space
3. Divide & Conquer: O(N log K) - OPTIMAL with O(1) space

================================================================================
FLOWCHART:
================================================================================

    mergeKLists(arr, K)
          |
          v
    Initialize:
    last = K - 1
          |
          v
    +-------------+
    | last != 0?  |-----> NO ----> return arr[0]
    +-------------+
          |
         YES
          |
          v
    Initialize:
    i = 0
    j = last
          |
          v
    +----------+
    | i < j?   |-----> NO ----> last = j
    +----------+                   |
          |                        |
         YES                       |
          |                        |
          v                        |
    Merge arr[i] and arr[j]       |
    Store result in arr[i]        |
    i++, j--                      |
          |                        |
          v                        |
    +----------+                   |
    | i >= j?  |-----> NO          |
    +----------+       |           |
          |           (Loop back)  |
         YES                       |
          |                        |
          +----(Continue outer loop)


    merge(h1, h2)
          |
          v
    +-------------+
    | h1 == NULL? |-----> YES ----> return h2
    +-------------+
          |
         NO
          |
          v
    +-------------+
    | h2 == NULL? |-----> YES ----> return h1
    +-------------+
          |
         NO
          |
          v
    +------------------+
    | h1.data < h2.data?|
    +------------------+
      |              |
     YES            NO
      |              |
      v              v
    res = h1      res = h2
    res.next =    res.next =
    merge(h1.next, h2)   merge(h1, h2.next)
      |              |
      +--------------+
            |
            v
      return res


    VISUAL EXAMPLE (K=4):

    Initial: [1->4, 2->5, 3->6, 7->8]

    Round 1: Pair and merge
        Merge arr[0] and arr[3]: 1->4 with 7->8 → 1->4->7->8
        Merge arr[1] and arr[2]: 2->5 with 3->6 → 2->3->5->6
        Result: [1->4->7->8, 2->3->5->6]

    Round 2: Pair and merge
        Merge arr[0] and arr[1]: 1->4->7->8 with 2->3->5->6
        Result: [1->2->3->4->5->6->7->8]

    Final: 1->2->3->4->5->6->7->8

    Levels of merging: log₂(4) = 2
    Total comparisons: O(N log K)

================================================================================
"""

class Node:
    """
    Node class for singly linked list.

    Attributes:
        data: The value stored in the node
        next: Reference to the next node
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    """
    Solution class to merge K sorted linked lists.
    """

    def merge(self, head1, head2):
        """
        Merge two sorted linked lists into one sorted list.

        This is the fundamental operation used repeatedly in mergeKLists.
        Similar to the merge operation in merge sort.

        Args:
            head1: Head of first sorted linked list
            head2: Head of second sorted linked list

        Returns:
            Head of the merged sorted linked list

        Algorithm:
        1. Base cases: If either list is empty, return the other
        2. Compare heads of both lists
        3. Choose the smaller one as the result
        4. Recursively merge remaining nodes
        5. Return the merged list

        Time Complexity: O(m + n) where m, n are lengths of the two lists
        Space Complexity: O(m + n) for recursion stack

        Example:
            h1: 1 -> 3 -> 5
            h2: 2 -> 4 -> 6

            Compare 1 and 2: 1 is smaller
            Result starts with 1
            Recursively merge (3->5) with (2->4->6)
            ...
            Final: 1 -> 2 -> 3 -> 4 -> 5 -> 6
        """
        # Base case 1: If first list is empty, return second list
        if head1 == None:
            return head2

        # Base case 2: If second list is empty, return first list
        if head2 == None:
            return head1

        # Variable to store the result head
        res = None

        # Compare the data of both heads and choose the smaller one
        if head1.data < head2.data:
            # head1 has smaller data, so it becomes part of result
            res = head1

            # Recursively merge head1's next with head2
            # This ensures all remaining nodes are merged in sorted order
            res.next = self.merge(head1.next, head2)
        else:
            # head2 has smaller or equal data, so it becomes part of result
            res = head2

            # Recursively merge head1 with head2's next
            res.next = self.merge(head1, head2.next)

        return res

    def mergeKLists(self, arr, K):
        """
        Merge K sorted linked lists using divide and conquer approach.

        This function repeatedly pairs and merges lists until only one remains.
        It's efficient because it minimizes the total number of comparisons.

        Args:
            arr: Array of K linked list heads (each list is sorted)
            K: Number of linked lists

        Returns:
            Head of the final merged sorted linked list

        Algorithm:
        1. Use two pointers: i from start, j from end
        2. Merge arr[i] with arr[j], store in arr[i]
        3. Move i forward, j backward
        4. When i >= j, we've completed one round
        5. Update last to j (number of lists reduced)
        6. Repeat until only one list remains (last = 0)

        Time Complexity: O(N log K) where:
            - N is total number of nodes across all lists
            - K is the number of lists
            - log K levels of merging, each level processes N nodes

        Space Complexity: O(1) excluding recursion stack
            - Only using array indices and pointers
            - Recursive merge uses O(log N) stack space

        Example:
            arr = [1->4, 2->5, 3->6], K = 3

            Round 1:
            - Merge arr[0] (1->4) with arr[2] (3->6) → 1->3->4->6
            - arr[1] stays as 2->5
            - last = 1, now we have 2 lists

            Round 2:
            - Merge arr[0] (1->3->4->6) with arr[1] (2->5) → 1->2->3->4->5->6
            - last = 0, only 1 list remains

            Return arr[0] = 1->2->3->4->5->6
        """
        # Initialize last to point to the last list
        last = K - 1

        # Continue merging until only one list remains
        # When last = 0, we have merged all lists into arr[0]
        while last != 0:
            # Initialize two pointers
            i = 0       # Points to start of array
            j = last    # Points to end of array

            # Pair up lists from start and end, merge them
            while i < j:
                # Merge the list at index i with the list at index j
                # Store the merged result back in arr[i]
                arr[i] = self.merge(arr[i], arr[j])

                # Move i forward to next list
                i += 1
                # Move j backward to next list from end
                j -= 1

                # Check if pointers have met or crossed
                # If i >= j, we've completed this round of merging
                if i >= j:
                    # Update last to j
                    # This effectively reduces the number of active lists
                    # After this round, only lists from 0 to j are valid
                    last = j

        # After all merging, arr[0] contains the final merged list
        return arr[0]


class LinkedList:
    """
    Helper class to create and manipulate linked lists for testing.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, x):
        """
        Add a new node with value x to the end of the list.

        Args:
            x: Value to be added

        Time Complexity: O(1)
        """
        if self.head is None:
            # First node in the list
            self.head = Node(x)
            self.tail = self.head
        else:
            # Append to the end
            self.tail.next = Node(x)
            self.tail = self.tail.next

def printList(head):
    """
    Print all elements in a linked list.

    Args:
        head: Head of the linked list

    Time Complexity: O(n)
    """
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk = walk.next
    print()


# ============================================================================
# EXAMPLE EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Read number of test cases
    for _ in range(int(input())):
        # Read number of lists
        n = int(input())

        # Read all input as a single line
        line = [int(x) for x in input().strip().split()]

        # Parse input and create linked lists
        heads = []
        index = 0

        for i in range(n):
            # First number is the size of this list
            size = line[index]
            index += 1

            # Create a new linked list
            newList = LinkedList()

            # Add 'size' number of elements to this list
            for _ in range(size):
                newList.add(line[index])
                index += 1

            # Store the head of this list
            heads.append(newList.head)

        # Merge all K lists
        merged_list = Solution().mergeKLists(heads, n)

        # Print the merged list
        printList(merged_list)

"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Are all K lists guaranteed to be sorted? (Yes)
   - Can any of the lists be empty? (Yes, handle NULL)
   - What should we return if K = 0 or all lists are empty? (NULL)
   - Can we modify the original lists? (Usually yes - in-place)
   - Are the lists sorted in ascending or descending order? (Usually ascending)
   - What's the range of K and N? (Important for complexity analysis)

2. Edge Cases to Consider:
   - K = 0 (no lists) → return NULL
   - K = 1 (single list) → return that list as-is
   - All lists are empty → return NULL
   - Some lists are empty, some are not → handle NULL checks
   - Lists of very different lengths → algorithm handles naturally
   - K = 2 (just two lists) → simple merge

3. Common Mistakes to Avoid:
   - Not handling NULL lists in the merge function
   - Off-by-one errors in the while loop conditions
   - Not updating 'last' correctly after each round
   - Forgetting to check i >= j before updating last
   - Not preserving the merged result in arr[i]
   - Integer overflow if K or N is very large

4. Why Divide & Conquer is Optimal:

   Sequential Merging (merge lists one by one):
   - Merge list1 with list2 → result1
   - Merge result1 with list3 → result2
   - Continue...
   - Time: O(NK) - each list merged with growing result

   Pair-wise Merging (current approach):
   - Merge in pairs simultaneously
   - Reduces K to K/2, then K/4, etc.
   - Time: O(N log K) - optimal!
   - Each level processes all N nodes
   - Number of levels = log K

5. Comparison of Approaches:

   Sequential Merging:
   ✗ O(NK) time complexity
   ✓ Simple to understand
   ✓ O(1) extra space

   Min-Heap Approach:
   ✓ O(N log K) time
   ✗ O(K) extra space for heap
   ✓ Good for external sorting

   Divide & Conquer (Current):
   ✓ O(N log K) time - OPTIMAL
   ✓ O(1) extra space - OPTIMAL
   ✗ Slightly more complex
   ✓ In-place modification

6. Follow-up Questions:
   - Can you do it without recursion?
     (Yes, iterative merge is possible but more complex)
   - What if lists are sorted in descending order?
     (Same algorithm works, just comparison logic changes)
   - How would you handle this if K is very large?
     (Current approach is optimal; min-heap might be clearer)
   - Can you merge K sorted arrays instead?
     (Yes, similar approach works)
   - What if we need to preserve original lists?
     (Create new nodes during merge - O(N) space)

7. Key Insight for Interview:
   This problem beautifully demonstrates:
   - Divide and conquer strategy
   - Reducing problem size systematically
   - Optimal use of the merge operation
   - Balancing time and space complexity
   - Similar to merge sort's merge phase

8. Time to Solve: Aim for 20-25 minutes including:
   - Understanding the problem: 3-4 minutes
   - Discussing approaches: 5-6 minutes
   - Coding merge function: 4-5 minutes
   - Coding mergeKLists: 5-6 minutes
   - Testing with examples: 3-4 minutes

9. Min-Heap Approach (Alternative):
   ```python
   import heapq

   def mergeKListsHeap(lists):
       heap = []
       # Add first node of each list to heap
       for i, head in enumerate(lists):
           if head:
               heapq.heappush(heap, (head.data, i, head))

       dummy = Node(0)
       current = dummy

       while heap:
           val, i, node = heapq.heappop(heap)
           current.next = node
           current = current.next
           if node.next:
               heapq.heappush(heap, (node.next.data, i, node.next))

       return dummy.next
   ```

10. Complexity Analysis Deep Dive:

    For K lists with total N nodes:

    Divide & Conquer:
    - Level 1: K/2 merges, each avg 2N/K nodes → O(N)
    - Level 2: K/4 merges, each avg 4N/K nodes → O(N)
    - ...
    - Level log K: 1 merge with N nodes → O(N)
    - Total: O(N log K)

    This is optimal because we must compare each node at least once.

11. Testing Strategy:
    Test with these cases:
    - K = 0 (no lists)
    - K = 1 (single list)
    - K = 2 (two lists of equal length)
    - K = 2 (two lists of different lengths)
    - K = 4 (power of 2 - clean division)
    - K = 3 (odd number - asymmetric merging)
    - Some empty lists mixed with non-empty
    - All lists empty
    - Lists with duplicate values

12. Real-world Applications:
    - External merge sort (sorting large files)
    - Merging log files from multiple servers
    - Combining sorted data streams
    - Database query optimization
    - Merging sorted chunks in distributed systems

13. Key Points to Mention in Interview:
    - This is a classic divide-and-conquer problem
    - Similar to merge sort but for K lists instead of 2
    - Achieves optimal O(N log K) time complexity
    - Uses O(1) extra space (excluding recursion)
    - Each round halves the number of active lists
    - The merge function is standard 2-way merge

================================================================================
"""
