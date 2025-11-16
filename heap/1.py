"""
Problem: Heap Sort
==================
Sort an array in ascending order using Heap Sort algorithm.

APPROACH:
---------
1. Build a max heap from the unsorted array
2. Repeatedly extract the maximum element (root) and place it at the end
3. Reduce heap size and heapify the root
4. Repeat until array is sorted

INTUITION:
----------
- Max heap property: parent >= children
- Root always contains maximum element
- After extracting max, restore heap property
- Time Complexity: O(n log n) - guaranteed
- Space Complexity: O(log n) - recursion stack (O(1) with iterative heapify)
- In-place sorting algorithm
- NOT stable (relative order of equal elements may change)

FLOWCHART:
----------
Start
  |
  v
Build Max Heap (O(n))
  |
  v
For i = n-1 to 1:
  |
  v
  Swap arr[0] with arr[i]
  (Move current max to its final position)
  |
  v
  Reduce heap size by 1
  |
  v
  Heapify root (index 0) with reduced heap size
  (Restore max heap property)
  |
  v
Repeat until i = 0
  |
  v
Array Sorted!
  |
  v
End

HEAPIFY PROCESS:
----------------
Current node i
  |
  v
Compare with left child (2*i + 1) and right child (2*i + 2)
  |
  v
Find largest among three
  |
  v
Is largest == i?
  |
  +--Yes--> Return (heap property satisfied)
  |
  +--No---> Swap i with largest
            |
            v
            Recursively heapify the affected subtree

INTERVIEW TIPS:
---------------
- Heap sort is comparison-based and in-place
- Preferred when guaranteed O(n log n) is required
- Not stable (unlike merge sort)
- Better space complexity than quicksort (worst case)
- Used in priority queue implementation
"""


class Solution:

    def heapify(self, arr, n, i):
        """
        Maintains the max heap property for subtree rooted at index i.

        Args:
            arr: Array representing the heap
            n: Size of heap (not array length, used during sorting)
            i: Index of root of subtree to heapify

        Time Complexity: O(log n) - height of tree
        """
        largest = i          # Initialize largest as root
        left = 2 * i + 1     # Left child index
        right = 2 * i + 2    # Right child index

        # If left child exists and is greater than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # If right child exists and is greater than current largest
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not root, swap and recursively heapify
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)  # Recursively heapify affected subtree

    def buildHeap(self, arr, n):
        """
        Builds a max heap from an unsorted array.

        Args:
            arr: Unsorted array
            n: Size of array

        Algorithm:
            Start from last non-leaf node and heapify all nodes
            up to the root in bottom-up manner

        Time Complexity: O(n) - tight bound
        """
        # Start from last non-leaf node (n//2 - 1) and move upwards
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

    def HeapSort(self, arr, n):
        """
        Sorts an array using Heap Sort algorithm.

        Args:
            arr: Array to be sorted (modified in-place)
            n: Size of array

        Algorithm:
            1. Build max heap - O(n)
            2. Extract max element n-1 times - O(n log n)
            3. Each extraction: swap root with last element, reduce heap size, heapify

        Time Complexity: O(n log n) - worst, average, and best case
        Space Complexity: O(log n) - recursion stack for heapify
        """
        # Step 1: Build max heap from array
        # After this, arr[0] is the maximum element
        self.buildHeap(arr, n)

        # Step 2: Extract elements from heap one by one
        for i in range(n - 1, 0, -1):
            # Move current root (maximum) to end
            # This places the largest unsorted element in its final position
            arr[0], arr[i] = arr[i], arr[0]

            # Call heapify on the reduced heap
            # Heap size is now i (excluding sorted elements at end)
            self.heapify(arr, i, 0)

        # Array is now sorted in ascending order


# Example usage
if __name__ == "__main__":
    solution = Solution()
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)

    print("Original array:", arr)
    solution.HeapSort(arr, n)
    print("Sorted array:", arr)

    # Expected output: [5, 6, 7, 11, 12, 13]
