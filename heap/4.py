"""
Problem: Kth Smallest Element
==============================
Find the Kth smallest element in an array.

APPROACH:
---------
Use Min Heap to efficiently find the Kth smallest element.

INTUITION:
----------
- Min heap keeps smallest element at root
- After heapifying, extract minimum k-1 times
- The root becomes the kth smallest element
- Time Complexity: O(n + k log n) - heapify O(n), k-1 extractions O(k log n)
- Space Complexity: O(1) - in-place heapification

OPTIMIZED APPROACH:
-------------------
Use Max Heap of size K:
- Maintain heap of size K with K smallest elements
- Keep removing largest when heap size > K
- Time: O(n log k), Space: O(k)
- Better when k << n

FLOWCHART:
----------
Start
  |
  v
Convert array to Min Heap
  |
  v
Extract minimum (k-1) times:
  |
  v
  +--> Pop root (smallest element)
       |
       v
       Heapify to maintain min heap property
       |
       v
       Decrement k
  |
  v
k-1 elements extracted?
  |
  v
Return current root (kth smallest)
  |
  v
End

INTERVIEW TIPS:
---------------
- Clarify if k is 0-indexed or 1-indexed
- Discuss QuickSelect algorithm: O(n) average case
- For multiple queries, consider sorting: O(n log n) once
- Max heap of size k is memory efficient for small k
"""

import heapq


class Solution:

    def kthSmallest(self, arr, l, r, k):
        """
        Returns the Kth smallest element in the array.

        Args:
            arr: Input array
            l: Left index (usually 0)
            r: Right index (usually n-1)
            k: Find kth smallest (1-indexed)

        Returns:
            Kth smallest element

        Algorithm:
            1. Convert array to min heap
            2. Pop k-1 smallest elements
            3. Root is now kth smallest

        Time Complexity: O(n + k log n)
        Space Complexity: O(1) - in-place
        """
        # Convert array to min heap in O(n) time
        heapq.heapify(arr)

        # Extract minimum element (k-1) times
        # After this, the root will be the kth smallest
        for i in range(k - 1):
            heapq.heappop(arr)

        # Return the root (kth smallest element)
        return arr[0]


# Example usage
if __name__ == "__main__":
    solution = Solution()
    arr = [7, 10, 4, 3, 20, 15]
    k = 3

    print(f"Array: {arr}")
    print(f"K = {k}")
    print(f"{k}th smallest element: {solution.kthSmallest(arr, 0, len(arr) - 1, k)}")

    # Expected output: 7 (sorted: [3, 4, 7, 10, 15, 20])


# Alternative approach using Max Heap of size K (more space efficient)
class SolutionOptimized:

    def kthSmallest(self, arr, l, r, k):
        """
        Optimized approach using max heap of size k.

        Time Complexity: O(n log k)
        Space Complexity: O(k)
        """
        # Create max heap of first k elements (negate for max heap)
        max_heap = [-x for x in arr[:k]]
        heapq.heapify(max_heap)

        # Process remaining elements
        for i in range(k, len(arr)):
            if arr[i] < -max_heap[0]:  # If current element is smaller than max
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, -arr[i])

        # Root of max heap is kth smallest
        return -max_heap[0]
