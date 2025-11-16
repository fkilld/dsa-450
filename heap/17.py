"""
Problem: Minimum Sum
=====================
Given an array of size N where each element is a digit (0-9), form two numbers using
all digits such that their sum is minimized.

APPROACH:
---------
Use greedy approach with min heap:
1. Sort digits in ascending order
2. Distribute digits alternately between two numbers
3. Place smaller digits at higher place values to minimize sum

INTUITION:
----------
- To minimize sum, minimize the higher place values
- Distribute smallest digits first between the two numbers
- Alternate distribution ensures balanced numbers
- Example: [6,8,4,5,2,3]
  Sorted: [2,3,4,5,6,8]
  num1 = 2 4 6 = 246
  num2 = 3 5 8 = 358
  Sum = 246 + 358 = 604 (minimum possible)

- Time Complexity: O(n log n) - heapify O(n), extractions O(n log n)
- Space Complexity: O(n) - storing numbers as strings

FLOWCHART:
----------
Start
  |
  v
Convert array to Min Heap
  |
  v
Initialize num1 = "", num2 = ""
Initialize toggle = 0
  |
  v
While heap is not empty:
  |
  v
  +--> Extract minimum digit
       |
       v
       If toggle == 0:
       |    Add digit to num1
       |    toggle = 1
       |
       Else:
            Add digit to num2
            toggle = 0
  |
  v
Convert num1 and num2 to integers
  |
  v
Return num1 + num2
  |
  v
End

WHY THIS WORKS:
---------------
Placing smaller digits at higher significant positions (leftmost)
minimizes the overall value of each number, thus minimizing their sum.

INTERVIEW TIPS:
---------------
- Explain greedy choice: smallest digits first
- Discuss why alternating distribution works
- Handle edge case: array with all zeros
- Mention that this extends to forming K numbers
"""

import heapq


class Solution:

    def solve(self, arr, n):
        """
        Finds minimum sum of two numbers formed using array digits.

        Args:
            arr: Array of digits (0-9)
            n: Size of array

        Returns:
            Minimum possible sum

        Algorithm:
            1. Convert to min heap (sort ascending)
            2. Extract digits one by one
            3. Alternately append to two numbers
            4. Return sum of the two numbers

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        num1 = ""  # First number
        num2 = ""  # Second number

        # Convert array to min heap - O(n)
        heapq.heapify(arr)

        # Toggle between numbers: 0 for num1, 1 for num2
        bi = 0

        # Extract all digits from heap
        while arr:
            if bi == 0:
                # Add smallest remaining digit to num1
                num1 += str(heapq.heappop(arr))
                bi = 1
            else:
                # Add smallest remaining digit to num2
                num2 += str(heapq.heappop(arr))
                bi = 0

        # Convert strings to integers and return sum
        # Handle empty string case (though shouldn't happen with valid input)
        return (int(num1) if len(num1) != 0 else 0) + \
               (int(num2) if len(num2) != 0 else 0)


# Example usage
if __name__ == "__main__":
    solution = Solution()

    arr = [6, 8, 4, 5, 2, 3]
    n = len(arr)

    print(f"Array of digits: {arr}")
    print(f"Minimum sum: {solution.solve(arr.copy(), n)}")

    # Explanation:
    # Sorted: [2, 3, 4, 5, 6, 8]
    # num1 = 246 (digits at positions 0, 2, 4)
    # num2 = 358 (digits at positions 1, 3, 5)
    # Sum = 246 + 358 = 604

    # Try another example
    arr2 = [5, 3, 0, 7, 4]
    print(f"\nArray of digits: {arr2}")
    print(f"Minimum sum: {solution.solve(arr2.copy(), len(arr2))}")

    # Sorted: [0, 3, 4, 5, 7]
    # num1 = 047 = 47
    # num2 = 35 = 35
    # Sum = 47 + 35 = 82
