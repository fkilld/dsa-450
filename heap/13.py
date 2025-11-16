"""
Problem: Minimum Cost of Ropes
===============================
Given N ropes of different lengths, connect them into one rope. The cost to connect
two ropes is the sum of their lengths. Find the minimum cost to connect all ropes.

APPROACH:
---------
Use Min Heap - always connect the two shortest ropes first (Greedy approach).

INTUITION:
----------
- Connecting shorter ropes first minimizes overall cost
- Each connection creates a new rope (sum of two ropes)
- Min heap efficiently gives us two smallest ropes
- Classic greedy algorithm (similar to Huffman coding)
- Time Complexity: O(n log n) - n-1 operations, each O(log n)
- Space Complexity: O(n) - heap storage

WHY GREEDY WORKS:
-----------------
- Longer ropes should be connected later to avoid repeated costs
- Example: ropes [4, 3, 2, 6]
  Wrong: (4+6=10) + (10+3=13) + (13+2=15) = 10+13+15 = 38
  Right: (2+3=5) + (4+5=9) + (6+9=15) = 5+9+15 = 29

FLOWCHART:
----------
Start
  |
  v
Convert array to Min Heap
  |
  v
Initialize cost = 0
  |
  v
While heap has more than 1 element:
  |
  v
  +--> Extract two smallest ropes (a, b)
       |
       v
       cost += (a + b)
       |
       v
       Push new rope (a + b) back to heap
  |
  v
All ropes connected?
  |
  v
Return total cost
  |
  v
End

INTERVIEW TIPS:
---------------
- Explain why greedy works (optimal substructure)
- Mention connection to Huffman coding
- Discuss why sorting once doesn't work
- Compare with dynamic programming (unnecessary here)
"""

import heapq as heap


class Solution:

    def minCost(self, arr):
        """
        Finds minimum cost to connect all ropes.

        Args:
            arr: Array of rope lengths

        Returns:
            Minimum cost to connect all ropes

        Algorithm:
            1. Convert array to min heap
            2. Repeatedly extract two smallest ropes
            3. Add their sum to cost
            4. Push combined rope back to heap
            5. Repeat until one rope remains

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        # Convert array to min heap - O(n)
        heap.heapify(arr)

        cost = 0  # Total cost of joining all ropes

        # Continue until only one rope remains
        while len(arr) > 1:
            # Extract two smallest ropes - O(log n) each
            a = heap.heappop(arr)
            b = heap.heappop(arr)

            # Cost to connect these two ropes
            cost += (a + b)

            # Push the new combined rope back - O(log n)
            heap.heappush(arr, a + b)

        return cost


# Example usage
if __name__ == "__main__":
    solution = Solution()

    ropes = [4, 3, 2, 6]
    print(f"Rope lengths: {ropes}")
    print(f"Minimum cost: {solution.minCost(ropes.copy())}")

    # Step-by-step:
    # [2, 3, 4, 6] → connect 2+3=5, cost=5  → [4, 5, 6]
    # [4, 5, 6]    → connect 4+5=9, cost=14 → [6, 9]
    # [6, 9]       → connect 6+9=15, cost=29
    # Expected output: 29
