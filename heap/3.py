"""
Problem: K Largest Elements in an Array
========================================
Given an array of N positive integers, find K largest elements from the array.
The output elements should appear in decreasing order.

APPROACH:
---------
Use Max Heap to efficiently extract the K largest elements.

INTUITION:
----------
- Max heap keeps largest element at root
- Extract from heap K times to get K largest elements
- Python's PriorityQueue is min heap by default
- Multiply by -1 to simulate max heap behavior
- Time Complexity: O(n + k log n) - heapify O(n), k extractions O(k log n)
- Space Complexity: O(n) - storing all elements in heap

ALTERNATIVE APPROACH:
---------------------
Use Min Heap of size K (more space efficient):
- Maintain heap of size K
- If new element > heap top, replace
- Time: O(n log k), Space: O(k)

FLOWCHART:
----------
Start
  |
  v
Create Max Heap (PriorityQueue)
  |
  v
For each element in array:
  |
  v
  Insert element * (-1) into heap
  (Negative to simulate max heap)
  |
  v
All elements inserted
  |
  v
Initialize result array
  |
  v
Extract K elements from heap:
  |
  v
  +--> Get top element (multiply by -1 to get original)
       |
       v
       Add to result array
       |
       v
       Decrement K
  |
  v
K elements extracted?
  |
  v
Return result array
  |
  v
End

INTERVIEW TIPS:
---------------
- Clarify if duplicates should be included
- Ask if order matters (descending or any order)
- Discuss space-time tradeoff: O(n) space vs O(k) space
- For k ≈ n, sorting might be simpler: O(n log n)
- For small k, min heap of size k is optimal
"""

from queue import PriorityQueue as pq


class Solution:

    def kLargest(self, arr, n, k):
        """
        Returns K largest elements from array in descending order.

        Args:
            arr: Input array of positive integers
            n: Size of array
            k: Number of largest elements to find

        Returns:
            List of k largest elements in descending order

        Algorithm:
            1. Insert all elements into max heap (use negative values)
            2. Extract top K elements from heap
            3. Return in descending order

        Time Complexity: O(n + k log n)
        Space Complexity: O(n)
        """
        q = pq()  # Min heap by default

        # Insert all elements into heap
        # Multiply by -1 to convert min heap to max heap
        for el in arr:
            q.put(-1 * el)

        ans = []  # Store K largest elements
        i = 0

        # Extract K largest elements
        while i < k:
            # Get top element and convert back to positive
            ans.append(-1 * q.get())
            i += 1

        return ans


# Example usage
if __name__ == "__main__":
    solution = Solution()
    arr = [12, 5, 787, 1, 23]
    n = len(arr)
    k = 2

    print(f"Array: {arr}")
    print(f"K = {k}")
    print(f"{k} largest elements: {solution.kLargest(arr, n, k)}")

    # Expected output: [787, 23]