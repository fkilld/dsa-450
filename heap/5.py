"""
Problem: Merge K Sorted Arrays
===============================
Given K sorted arrays, merge them into one sorted array.

APPROACH:
---------
Use Min Heap to efficiently merge K sorted arrays by always extracting the minimum element.

INTUITION:
----------
- Each array is already sorted
- Need to find minimum among K arrays repeatedly
- Min heap gives minimum in O(log K) time
- Track which array each element came from
- After extracting, add next element from same array
- Time Complexity: O(N*K * log K) where N*K is total elements
- Space Complexity: O(K) for heap + O(N*K) for result

FLOWCHART:
----------
Start
  |
  v
Create Min Heap
  |
  v
Insert first element from each of K arrays
(Store: [value, row_index, col_index])
  |
  v
While heap is not empty:
  |
  v
  +--> Extract minimum (val, row, col)
       |
       v
       Add val to result array
       |
       v
       Is there next element in same array (col+1)?
       |
       +--Yes--> Insert arr[row][col+1] to heap
       |
       +--No---> Skip (array exhausted)
  |
  v
All elements processed?
  |
  v
Return merged sorted array
  |
  v
End

VISUALIZATION (K=3 arrays):
---------------------------
arr = [[1, 3, 5],
       [2, 4, 6],
       [0, 9, 10]]

Step 1: Heap = [0(2,0), 1(0,0), 2(1,0)]  → Extract 0, add 9
Step 2: Heap = [1(0,0), 2(1,0), 9(2,1)]  → Extract 1, add 3
Step 3: Heap = [2(1,0), 3(0,1), 9(2,1)]  → Extract 2, add 4
...

Result: [0, 1, 2, 3, 4, 5, 6, 9, 10]

INTERVIEW TIPS:
---------------
- Discuss why heap is better than comparing all K arrays each time
- Mention it's used in external sorting (merge sort for disk files)
- Can be extended to merge K sorted linked lists
- Python PriorityQueue automatically handles duplicate values
"""

from queue import PriorityQueue as pq


class Solution:

    def mergeKArrays(self, arr, K):
        """
        Merges K sorted arrays into one sorted array.

        Args:
            arr: List of K sorted arrays (each of size K in this problem)
            K: Number of arrays

        Returns:
            Merged sorted array containing all elements

        Algorithm:
            1. Insert first element from each array into min heap
            2. Extract minimum, add to result
            3. Insert next element from same array
            4. Repeat until all elements processed

        Time Complexity: O(N*K * log K) where N*K is total elements
        Space Complexity: O(K) for heap, O(N*K) for result
        """
        ans = []  # Store the merged sorted result
        q = pq()   # Min heap to track smallest elements

        # Step 1: Insert first element from each array
        # Store [value, row_index, column_index]
        # row = which array, col = position in that array
        for i in range(K):
            q.put([arr[i][0], i, 0])

        # Step 2: Extract minimum and add next element from same array
        while not q.empty():
            val, row, col = q.get()  # Get minimum element
            ans.append(val)           # Add to result

            # If current element is not the last in its array
            # add the next element from same array to heap
            if col < K - 1:
                q.put([arr[row][col + 1], row, col + 1])

        return ans


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # K sorted arrays, each of size K
    arr = [
        [1, 3, 5, 7],
        [2, 4, 6, 8],
        [0, 9, 10, 11],
        [12, 13, 14, 15]
    ]
    K = 4

    print("K Sorted Arrays:")
    for i, sub_arr in enumerate(arr):
        print(f"  Array {i}: {sub_arr}")

    result = solution.mergeKArrays(arr, K)
    print(f"\nMerged Sorted Array: {result}")

    # Expected: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
