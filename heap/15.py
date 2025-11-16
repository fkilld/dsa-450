"""
Problem: Convert Min Heap to Max Heap
======================================
Given an array representing a min heap, convert it into a max heap.

APPROACH:
---------
Use heapify operation for max heap on all non-leaf nodes from bottom to top.

INTUITION:
----------
- Min heap and max heap are different organizations of same elements
- Can't just reverse the array
- Apply max-heapify from bottom to ensure heap property
- Time Complexity: O(n) - linear time heapification
- Space Complexity: O(log n) - recursion stack

FLOWCHART:
----------
Start
  |
  v
Input: Min Heap array
  |
  v
Start from last non-leaf node (n//2 - 1)
  |
  v
For i from (n//2 - 1) down to 0:
  |
  v
  +--> Apply Max Heapify at index i
       |
       v
       Find largest among node, left child, right child
       |
       v
       If largest != current node
       |
       v
       Swap and recursively max-heapify
  |
  v
All nodes processed?
  |
  v
Max Heap created!
  |
  v
End

KEY INSIGHT:
------------
The same array can represent different heaps depending on the heap property:
- Min Heap: parent <= children
- Max Heap: parent >= children

We rebuild the heap structure by re-heapifying with max heap property.

INTERVIEW TIPS:
---------------
- Explain why we can't just negate all values
- Discuss that we're rebuilding the heap structure
- Time complexity is O(n), not O(n log n)
- Similar to buildHeap operation
"""


class Solution:

    def heapify(self, idx, arr, n):
        """
        Applies max heapify at given index.

        Args:
            idx: Index to heapify
            arr: Array representing heap
            n: Size of heap

        Process:
            Find largest among node and children,
            swap if needed, recursively heapify affected subtree
        """
        largest = idx       # Assume current is largest
        left = 2 * idx + 1  # Left child
        right = 2 * idx + 2 # Right child

        # Check if left child is larger
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child is larger
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not current node, swap and recurse
        if largest != idx:
            arr[idx], arr[largest] = arr[largest], arr[idx]
            self.heapify(largest, arr, n)

    def convert(self, arr, n):
        """
        Converts min heap to max heap.

        Args:
            arr: Array representing min heap
            n: Size of array

        Returns:
            Same array converted to max heap

        Time Complexity: O(n)
        Space Complexity: O(log n) for recursion
        """
        # Apply max heapify from last non-leaf to root
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i, arr, n)
        return arr


# Example usage
if __name__ == "__main__":
    min_heap = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
    n = len(min_heap)

    obj = Solution()
    print(f"Min Heap : {min_heap}")

    max_heap = obj.convert(min_heap.copy(), n)
    print(f"Max Heap : {max_heap}")

    # Example output: [20, 18, 10, 12, 9, 9, 5, 3, 6, 8]
    # Root (20) is now the largest element
