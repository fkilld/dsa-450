"""
Problem: Merge Two Binary Max Heaps
====================================
Given two binary max heaps as arrays, merge them to form a new max heap.

APPROACH:
---------
1. Merge both arrays into one
2. Build max heap on the merged array using heapify

INTUITION:
----------
- Simply combining two max heaps doesn't guarantee heap property
- Building heap from scratch ensures correctness
- Heapify is O(n), so total time is O(n + m) where n, m are sizes
- Time Complexity: O(n + m) - linear time to build heap
- Space Complexity: O(1) - in-place if we can modify input

FLOWCHART:
----------
Start
  |
  v
Concatenate array 'a' and array 'b'
  |
  v
merged_array = a + b, n = length
  |
  v
Start from last non-leaf node (n//2 - 1)
  |
  v
For i from (n//2 - 1) down to 0:
  |
  v
  +--> Heapify at index i
       |
       v
       Find largest among node, left, right children
       |
       v
       If largest != current node: Swap and recurse
  |
  v
Return merged max heap
  |
  v
End
"""


class Solution():

    def heapify(self, arr, idx, n):
        """
        Maintains max heap property for subtree rooted at idx.

        Args:
            arr: Array representing the heap
            idx: Index of current node to heapify
            n: Size of heap
        """
        largest = idx       # Assume current node is largest
        left = 2 * idx + 1  # Left child index
        right = 2 * idx + 2 # Right child index

        # Check if left child exists and is greater
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child exists and is greater
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not current node, swap and recurse
        if largest != idx:
            arr[largest], arr[idx] = arr[idx], arr[largest]
            self.heapify(arr, largest, n)

    def mergeHeaps(self, a, b, n, m):
        """
        Merges two binary max heaps.

        Time Complexity: O(n + m)
        Space Complexity: O(n + m)
        """
        # Merge both arrays
        a = a + b
        n = len(a)

        # Build max heap from merged array
        # Start from last non-leaf node
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(a, i, n)

        return a
