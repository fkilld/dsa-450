"""
================================================================================
PROBLEM: Find Pairs with Given Sum in Doubly Linked List
================================================================================

DESCRIPTION:
Given a sorted doubly linked list and a target sum k, find all pairs of
nodes whose values add up to k.

Input:  1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9, k = 7
Output: [[1, 6], [2, 5]]

Input:  1 <-> 2 <-> 3 <-> 4, k = 5
Output: [[1, 4], [2, 3]]

Note: The doubly linked list is sorted in ascending order. Each pair should
be counted only once, and pairs should be in order of their first element.

================================================================================
APPROACH & REASONING:
================================================================================

TWO-POINTER APPROACH (Optimal for Sorted List):

The key insight is to use the doubly linked property to traverse from both
ends simultaneously, similar to the two-pointer technique for sorted arrays.

Algorithm Steps:
1. Set first pointer at head (smallest element)
2. Set second pointer at tail (largest element)
3. While first and second haven't crossed:
   - If sum equals k, add pair and move both pointers
   - If sum is less than k, move first forward (increase sum)
   - If sum is greater than k, move second backward (decrease sum)
4. Return all found pairs

Time Complexity: O(n) - single pass with two pointers
Space Complexity: O(1) - only using two pointers (excluding result storage)

Why this works:
- List is sorted, so smallest is at start, largest at end
- If current sum < k, we need a larger number (move first forward)
- If current sum > k, we need a smaller number (move second backward)
- Doubly linked list allows backward traversal (using prev pointer)

Alternative Approaches:
1. Hash Set: O(n) time, O(n) space - works for unsorted lists
2. Nested loops: O(n²) time, O(1) space - inefficient
3. Current approach: O(n) time, O(1) space - optimal for sorted lists

================================================================================
FLOWCHART:
================================================================================

    pairsum(k)
          |
          v
    Initialize:
    first = head (smallest)
    second = head
    res = []
          |
          v
    Find last node (second):
    while second.next != NULL:
        second = second.next
          |
          v
    +------------------------------------+
    | first != second &&                 |-----> NO ----> return res
    | second.next != first?              |
    +------------------------------------+
          |
         YES
          |
          v
    sum = first.data + second.data
          |
          v
    +------------------+
    | sum == k?        |
    +------------------+
          |         |
         YES       NO
          |         |
          v         v
    Add pair    +------------------+
    to res      | sum < k?         |
    Move first  +------------------+
    forward           |         |
    Move second      YES       NO
    backward          |         |
          |           v         v
          |      Move first  Move second
          |      forward     backward
          |           |         |
          +----+------+---------+
               |
               v
          (Loop back to condition)


    VISUAL EXAMPLE:

    List: 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9, k = 7

    Initial:
    first -> 1, second -> 9
    sum = 10 > 7, move second backward

    Step 1:
    first -> 1, second -> 8
    sum = 9 > 7, move second backward

    Step 2:
    first -> 1, second -> 6
    sum = 7 == 7, found pair [1, 6]
    Move both: first -> 2, second -> 5

    Step 3:
    first -> 2, second -> 5
    sum = 7 == 7, found pair [2, 5]
    Move both: first -> 4, second -> 4

    Step 4:
    first == second, stop

    Result: [[1, 6], [2, 5]]


    KEY INSIGHT - Why pointers won't miss pairs:

    Since list is sorted:
    - If sum < k, increasing first (smaller value) is only way to increase sum
    - If sum > k, decreasing second (larger value) is only way to decrease sum
    - We explore all valid combinations without duplication

================================================================================
"""

class Node:
    """
    Node class representing a single element in the doubly linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """
    DoublyLinkedList class with methods to find pairs with given sum.
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

        # If list is empty, make new node the head
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

    def pairsum(self, k):
        """
        Find all pairs in a sorted doubly linked list that sum to k.

        Uses two-pointer technique from both ends of the list.

        Args:
            k: Target sum

        Returns:
            List of pairs [a, b] where a + b = k, or -1 if no pairs found

        Algorithm:
        1. Initialize first at head, second at tail
        2. While pointers haven't crossed:
           - If sum == k: add pair, move both inward
           - If sum < k: move first forward (need larger value)
           - If sum > k: move second backward (need smaller value)
        3. Return all found pairs

        Time Complexity: O(n) - single traversal with two pointers
        Space Complexity: O(1) - excluding result storage

        Example:
            Input: 1<->2<->4<->5<->6, k=7
            Output: [[1, 6], [2, 5]]
        """
        # List to store result pairs
        res = []

        # Initialize first pointer at the beginning (smallest element)
        first = self.head

        # Initialize second pointer at the beginning
        # We'll move it to the end in the next step
        second = self.head

        # PHASE 1: Find the last node (largest element)
        # Move second pointer to the tail of the list
        while second.next != None:
            second = second.next

        # PHASE 2: Two-pointer approach to find pairs
        # Continue until pointers meet or cross
        # Conditions:
        # 1. first != second: pointers haven't met
        # 2. second.next != first: pointers haven't crossed
        while first != second and second.next != first:
            # Calculate sum of current pair
            current_sum = first.data + second.data

            # CASE 1: Found a pair that sums to k
            if current_sum == k:
                # Add pair to result
                res.append([first.data, second.data])

                # Move first pointer forward (to next larger element)
                first = first.next

                # Move second pointer backward (to next smaller element)
                second = second.prev

            # CASE 2: Sum is less than k
            # Need to increase sum, so move first forward
            elif current_sum < k:
                first = first.next

            # CASE 3: Sum is greater than k
            # Need to decrease sum, so move second backward
            else:
                second = second.prev

        # Return result or -1 if no pairs found
        return res if len(res) > 0 else -1


# ============================================================================
# EXAMPLE EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Create a new doubly linked list
    dll = DoublyLinkedList()

    # Build list: 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
    # (push adds to front, so we push in reverse order)
    dll.push(9)
    dll.push(8)
    dll.push(6)
    dll.push(5)
    dll.push(4)
    dll.push(2)
    dll.push(1)

    # Print the list
    dll.printList()  # Output: 1 2 4 5 6 8 9

    # Find pairs with sum = 7
    print(dll.pairsum(7))  # Output: [[1, 6], [2, 5]]


"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Is the list sorted? (Critical for O(n) solution)
   - Can there be duplicate values? (Yes, handle them)
   - Should pairs be unique? (Yes, each pair counted once)
   - What if no pairs found? (Return empty list or -1)
   - Can a number be paired with itself? (Only if two instances exist)
   - What format for result? (List of pairs usually)

2. Edge Cases to Consider:
   - Empty list → return -1
   - Single node → return -1 (can't make pair)
   - Two nodes (sum equals k) → return that pair
   - Two nodes (sum doesn't equal k) → return -1
   - No pairs sum to k → return -1
   - All pairs sum to k → return all pairs
   - Duplicate values in list

3. Common Mistakes to Avoid:
   - Forgetting that list is sorted (enables two-pointer approach)
   - Not moving both pointers when sum equals k
   - Infinite loop due to not moving pointers correctly
   - Counting same pair twice
   - Not checking if pointers have crossed
   - Not handling the case when first == second

4. Why Two-Pointer Approach Works:

   Key Properties:
   - List is sorted: smallest at start, largest at end
   - If sum < k: must increase sum (move left pointer right)
   - If sum > k: must decrease sum (move right pointer left)
   - If sum == k: found pair, explore other possibilities

   Why it doesn't miss pairs:
   - We systematically check all valid combinations
   - Pointers move inward, covering all possibilities
   - No pair is counted twice

5. Follow-up Questions You Might Get:
   Q: What if list is not sorted?
   A: Use hash set approach - O(n) time, O(n) space

   Q: How to find triplets that sum to k?
   A: Fix one element, use two-pointer for remaining

   Q: What if we need all pairs, not just count?
   A: Current implementation returns all pairs

   Q: Can you do this for singly linked list?
   A: Yes, but O(n²) or convert to array first

   Q: How to handle duplicates differently?
   A: Modify to skip duplicates or count all occurrences

6. Time to Solve: Aim for 12-15 minutes including edge cases

7. Key Points to Mention in Interview:
   - Explain why sorting enables O(n) solution
   - Discuss the two-pointer technique clearly
   - Mention that doubly linked list enables backward traversal
   - Walk through sum comparisons and pointer movements
   - Compare with hash set approach for unsorted lists

8. Comparison with Array Approach:

   Doubly Linked List:
   - Two pointers from ends
   - O(n) time, O(1) space
   - Need to find tail first
   - Use prev pointer for backward movement

   Array:
   - Two pointers (indices) from ends
   - O(n) time, O(1) space
   - Direct access to both ends
   - Simpler implementation

9. Alternative Approaches:

   Hash Set (works for unsorted):
   ```python
   seen = set()
   for node in list:
       complement = k - node.data
       if complement in seen:
           add [complement, node.data] to result
       seen.add(node.data)
   ```
   Time: O(n), Space: O(n)

   Nested Loops (brute force):
   ```python
   for each node i:
       for each node j after i:
           if i.data + j.data == k:
               add pair
   ```
   Time: O(n²), Space: O(1)

10. Related Problems:
    - Two sum in array
    - Three sum problem
    - Four sum problem
    - Pair with given difference
    - Count pairs with given sum
    - Find pair in BST with given sum
    - Two pointers technique problems

================================================================================
"""
