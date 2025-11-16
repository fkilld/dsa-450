"""
================================================================================
PROBLEM: Count Triplets in Sorted Doubly Linked List with Given Sum
================================================================================

DESCRIPTION:
Given a sorted doubly linked list of distinct nodes and a value x, count all
triplets in the list that sum up to the given value x.

Input:  1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9, x = 17
Output: 2 (Triplets: (2, 6, 9) and (4, 5, 8))

Input:  1 <-> 5 <-> 6, x = 12
Output: 1 (Triplet: (1, 5, 6))

================================================================================
APPROACH & REASONING:
================================================================================

OPTIMAL APPROACH: Fix First Element + Two Pointer Technique

Key Insight:
- Since the list is sorted, we can use the two-pointer technique
- Fix each element one by one as the first element of the triplet
- Use two pointers to find pairs in the remaining list that sum to (x - first)
- This is essentially converting the triplet problem into multiple pair problems

Algorithm Steps:
1. For each node as the first element of triplet:
   - Calculate target = x - current.data
   - Use two pointers (start from current.next, end from tail)
   - Find pairs that sum to target using two-pointer technique

2. Two-pointer pair counting:
   - If first.data + last.data == target: found a pair, move both pointers
   - If sum < target: move first pointer forward (to increase sum)
   - If sum > target: move last pointer backward (to decrease sum)

Time Complexity: O(n²) where n is the number of nodes
   - Outer loop: O(n) to fix first element
   - Inner loop: O(n) for two-pointer pair search
   - Overall: O(n) × O(n) = O(n²)

Space Complexity: O(1) - only using a few pointers

Why this works:
- Sorted property allows two-pointer technique to work efficiently
- By fixing one element, we reduce triplet problem to pair problem
- Two pointers cover all possible pairs without duplicates
- Moving pointers based on comparison guarantees we don't miss any valid pair

================================================================================
FLOWCHART:
================================================================================

    count_triplets(x)
          |
          v
    +-------------+
    | head==NULL? |-----> YES ----> return 0
    +-------------+
          |
         NO
          |
          v
    Initialize:
    current = head
    last = head
    count = 0
          |
          v
    Find last node
    (traverse to end)
          |
          v
    +------------------+
    | current != NULL? |-----> NO ----> return count
    +------------------+
          |
         YES
          |
          v
    first = current.next
    target = x - current.data
          |
          v
    count += count_pairs(first, last, target)
          |
          v
    current = current.next
          |
          +----(Loop back)


    count_pairs(first, last, k)
          |
          v
    Initialize:
    count = 0
          |
          v
    +----------------------------------------+
    | first!=last && last.prev!=first &&     |-----> NO ----> return count
    | first!=NULL && last!=NULL?             |
    +----------------------------------------+
          |
         YES
          |
          v
    +------------------------+
    | first.data + last.data |
    +------------------------+
          |
          +--------+--------+
          |        |        |
         ==k      <k        >k
          |        |        |
          v        v        v
    count++   first++   last--
    first++
    last--
          |        |        |
          +--------+--------+
          |
          +----(Loop back)


    VISUAL EXAMPLE (x = 17):

    List: 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9

    Fix current = 2, target = 17 - 2 = 15
         first = 4, last = 9
         4 + 9 = 13 < 15, move first right
         first = 5, last = 9
         5 + 9 = 14 < 15, move first right
         first = 6, last = 9
         6 + 9 = 15 == target, found (2, 6, 9)! count = 1

    Fix current = 4, target = 17 - 4 = 13
         first = 5, last = 9
         5 + 9 = 14 > 13, move last left
         first = 5, last = 8
         5 + 8 = 13 == target, found (4, 5, 8)! count = 2

    Continue for remaining nodes...
    Final count = 2

================================================================================
"""

class Node:
    """
    Node class for doubly linked list.

    Attributes:
        data: The value stored in the node
        next: Reference to the next node
        prev: Reference to the previous node
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """
    DoublyLinkedList class with methods to count triplets with given sum.

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

    def count_pairs(self, first, last, k):
        """
        Count pairs in sorted doubly linked list with given sum k.
        Uses two-pointer technique to efficiently find pairs.

        Args:
            first: Starting node (left pointer)
            last: Ending node (right pointer)
            k: Target sum for the pair

        Returns:
            Number of pairs that sum to k

        Algorithm:
        1. Use two pointers: first from start, last from end
        2. If sum matches k, increment count and move both pointers
        3. If sum < k, move first forward to increase sum
        4. If sum > k, move last backward to decrease sum
        5. Continue until pointers meet or cross

        Time Complexity: O(n) where n is distance between first and last
        Space Complexity: O(1)

        Example:
            List: 1 <-> 2 <-> 4 <-> 5, k = 6
            first=1, last=5: 1+5=6 (match!) count=1
            first=2, last=4: 2+4=6 (match!) count=2
            Result: 2 pairs
        """
        count = 0

        # Continue until pointers meet or cross
        # Multiple conditions to handle all edge cases:
        # - first != last: pointers haven't met yet
        # - last.prev != first: pointers haven't crossed
        # - first != None and last != None: valid pointers
        while first != last and last.prev != first and first != None and last != None:
            # Calculate sum of current pair
            current_sum = first.data + last.data

            if current_sum == k:
                # Found a valid pair
                count += 1
                # Move both pointers to find more pairs
                first = first.next
                last = last.prev

            elif current_sum < k:
                # Sum too small, need larger values
                # Move first pointer right (towards larger values)
                first = first.next

            else:  # current_sum > k
                # Sum too large, need smaller values
                # Move last pointer left (towards smaller values)
                last = last.prev

        return count

    def count_triplets(self, x):
        """
        Count all triplets in sorted doubly linked list with sum equal to x.

        Args:
            x: Target sum for triplets

        Returns:
            Number of triplets that sum to x

        Algorithm:
        1. Handle edge case: empty list returns 0
        2. Find the last node of the list
        3. Fix each node as the first element of triplet
        4. For remaining nodes, find pairs that sum to (x - first element)
        5. Add count of such pairs to total count

        Time Complexity: O(n²) where n is the number of nodes
            - O(n) to iterate through each node as first element
            - O(n) for count_pairs for each iteration
            - Overall: O(n²)

        Space Complexity: O(1) - only using pointers

        Example:
            List: 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9, x = 17

            Fix 1: find pairs in [2...9] summing to 16 → 0 pairs
            Fix 2: find pairs in [4...9] summing to 15 → 1 pair (6,9)
            Fix 4: find pairs in [5...9] summing to 13 → 1 pair (5,8)
            Fix 5: find pairs in [6...9] summing to 12 → 0 pairs
            ...
            Result: 2 triplets
        """
        # Edge case: empty list has no triplets
        if self.head == None:
            return 0

        # Initialize pointers
        current = self.head  # Will be fixed as first element of triplet
        first = None         # Start of pair search range
        last = self.head     # Will point to last node
        count = 0            # Total triplet count

        # Step 1: Find the last node of the list
        while last.next != None:
            last = last.next

        # Step 2: Fix each node as first element and find pairs in remaining list
        while current != None:
            # The search range for pairs starts from next node
            first = current.next

            # Calculate target sum for the pair
            # If current + pair = x, then pair = x - current
            target = x - current.data

            # Count pairs in remaining list that sum to target
            # These pairs, combined with current, form valid triplets
            count += self.count_pairs(first, last, target)

            # Move to next node as first element
            current = current.next

        return count


# ============================================================================
# EXAMPLE EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Create a new doubly linked list
    dll = DoublyLinkedList()

    # Build list: 1 <-> 5 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
    # (push adds to front, so we push in reverse order)
    dll.push(9)
    dll.push(8)
    dll.push(6)
    dll.push(5)
    dll.push(4)
    dll.push(5)
    dll.push(1)

    print("Doubly Linked List:")
    dll.printList()  # Output: 1 5 4 5 6 8 9

    # Note: For this algorithm to work optimally, list should be sorted
    # The example list is not fully sorted, but demonstrates the algorithm

    target_sum = 17
    print(f"\nNumber of triplets with sum {target_sum}:")
    result = dll.count_triplets(target_sum)
    print(result)

"""
================================================================================
INTERVIEW TIPS:
================================================================================

1. Clarification Questions to Ask:
   - Is the doubly linked list guaranteed to be sorted? (Usually yes)
   - Can the list contain duplicate values? (May affect counting)
   - Should we count distinct triplets or all combinations?
   - What should we return for an empty list or list with < 3 nodes? (0)
   - Are the triplets ordered (a, b, c where a < b < c)? (Usually yes)
   - What's the range of values and the target sum? (Check for overflow)

2. Edge Cases to Consider:
   - Empty list → return 0
   - List with fewer than 3 nodes → return 0
   - No triplets exist with given sum → return 0
   - All elements are the same → handle duplicates carefully
   - Target sum is too small or too large → no valid triplets
   - List has exactly 3 nodes → check if they sum to target

3. Common Mistakes to Avoid:
   - Forgetting to check both first != last AND last.prev != first
     (prevents counting the same element twice)
   - Not handling NULL pointers in count_pairs
   - Forgetting that list must be sorted for two-pointer approach
   - Not updating both pointers when sum matches
   - Integer overflow with large sums (though Python handles this)

4. Alternative Approaches:
   a) Brute Force: O(n³) - three nested loops to check all triplets
   b) Hash Set: O(n²) space and time - store all elements, fix two and lookup third
   c) Current approach: O(n²) time, O(1) space - OPTIMAL for sorted list

5. Follow-up Questions:
   - Can you find the actual triplets instead of just counting?
     (Yes, store them in a list when found)
   - What if the list is singly linked?
     (Would need O(n) space to store nodes for backward traversal)
   - Can you do it in less than O(n²) time?
     (Not possible as we must check O(n²) pairs in worst case)
   - How would you handle an unsorted doubly linked list?
     (Sort it first O(n log n), then apply same algorithm)

6. Key Insight for Interview:
   This problem brilliantly combines:
   - Fixing one element to reduce problem complexity
   - Two-pointer technique on sorted sequence
   - Properties of doubly linked list (bidirectional traversal)

7. Time to Solve: Aim for 20-25 minutes including:
   - Understanding the problem: 3-5 minutes
   - Discussing approach: 5 minutes
   - Coding: 10 minutes
   - Testing with examples: 5 minutes

8. Optimization Notes:
   - Could optimize by stopping early in outer loop when remaining nodes < 2
   - Could skip duplicate values to avoid counting same triplets
   - For very large lists, consider parallel processing of different ranges

================================================================================
"""
