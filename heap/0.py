"""
Problem: Build Max Heap
=======================
Given an array, convert it into a max heap. A max heap is a complete binary tree where
the value of each node is greater than or equal to the values of its children.

APPROACH:
---------
1. Start from the last non-leaf node (at index n//2 - 1)
2. Apply heapify to each node from bottom to top
3. Heapify ensures the subtree rooted at index i satisfies max heap property

INTUITION:
----------
- Leaf nodes are already valid heaps (single element)
- Build heap bottom-up to ensure parent > children property
- Time Complexity: O(n) - not O(n log n) due to mathematical proof
- Space Complexity: O(log n) - recursion stack depth

FLOWCHART:
----------
Start
  |
  v
Get array length n
  |
  v
Start from last non-leaf node (n//2 - 1)
  |
  v
For each node from (n//2 - 1) to 0:
  |
  v
  +--> Call heapify(arr, n, i)
       |
       v
       Find largest among node, left child, right child
       |
       v
       Is largest != current node?
       |
       +--Yes--> Swap node with largest
       |         |
       |         v
       |         Recursively heapify affected subtree
       |
       +--No---> Return (heap property satisfied)
  |
  v
All nodes heapified?
  |
  v
Max Heap Built!
  |
  v
End

INTERVIEW TIPS:
---------------
- Explain why we start from n//2 - 1 (last non-leaf node)
- Mention that leaf nodes are at indices [n//2, n-1]
- Discuss time complexity proof (sum of heights, not depth)
- For 0-indexed array: left child = 2*i + 1, right child = 2*i + 2
"""


def heapify(arr, n, i):
    """
    Maintains the max heap property for subtree rooted at index i.

    Args:
        arr: The array representing the heap
        n: Size of heap
        i: Index of root of subtree to heapify

    Process:
        1. Assume current node is largest
        2. Compare with left and right children
        3. If a child is larger, swap and recursively heapify
    """
    largest = i          # Initialize largest as root
    left = 2 * i + 1     # Left child index = 2*i + 1
    right = 2 * i + 2    # Right child index = 2*i + 2

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected sub-tree


def buildHeap(arr):
    """
    Builds a max heap from an unsorted array.

    Args:
        arr: Unsorted array to convert to max heap

    Algorithm:
        1. Find the last non-leaf node (n//2 - 1)
        2. Heapify all nodes from last non-leaf to root
        3. This ensures bottom-up heap construction

    Time Complexity: O(n) - tight bound analysis
    Space Complexity: O(log n) - recursion stack
    """
    n = len(arr)

    # Index of last non-leaf node
    # Nodes from index (n//2) to (n-1) are leaf nodes
    idx = n // 2 - 1

    # Perform reverse level order traversal from last non-leaf node
    # and heapify each node
    for i in range(idx, -1, -1):
        heapify(arr, n, i)

    print(arr)


# Example usage
if __name__ == "__main__":
    arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
    print("Original array:", arr)
    print("Max Heap:", end=" ")
    buildHeap(arr)

    # Expected output: [17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1]
    # The largest element (17) is at the root
