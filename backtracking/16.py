"""
PRINT ALL POSSIBLE PATHS FROM TOP LEFT TO BOTTOM RIGHT OF A M×N MATRIX
=======================================================================

Problem Statement:
-----------------
Given a M×N matrix, print all possible paths from the top-left corner (0,0)
to the bottom-right corner (M-1, N-1).

You can only move RIGHT or DOWN at any point in time.

Example:
--------
Input:
matrix = [[1, 2, 3],
          [4, 5, 6]]
M = 2, N = 3

Output:
1 2 3 6
1 2 5 6
1 4 5 6

Explanation: Three paths exist from (0,0) to (1,2):
- Path 1: (0,0) -> (0,1) -> (0,2) -> (1,2) : 1 2 3 6
- Path 2: (0,0) -> (0,1) -> (1,1) -> (1,2) : 1 2 5 6
- Path 3: (0,0) -> (1,0) -> (1,1) -> (1,2) : 1 4 5 6

Approach:
---------
1. Use Backtracking to explore all possible paths
2. Start from (0, 0) and try two moves: RIGHT and DOWN
3. Store current element in path array at position pi (path index)
4. Special cases:
   - If we reach last row, fill remaining cells from current column to end
   - If we reach last column, fill remaining cells from current row to end
5. Otherwise, recursively explore both directions:
   - Move DOWN: (i+1, j)
   - Move RIGHT: (i, j+1)
6. Path is printed when we reach destination

Time Complexity: O(2^(M+N)) - Each cell has 2 choices (right/down) until boundary
Space Complexity: O(M+N) - Path array size + recursion depth

Flowchart:
----------
```mermaid
graph TD
    A[Start: i=0, j=0, pi=0] --> B{Reached last row?}
    B -->|Yes| C[Fill remaining columns]
    C --> D[Print path]
    D --> E[Return]
    B -->|No| F{Reached last column?}
    F -->|Yes| G[Fill remaining rows]
    G --> D
    F -->|No| H[Add current cell to path]
    H --> I[Move DOWN: i+1, j]
    I --> J[Move RIGHT: i, j+1]
    J --> E
```
"""


class Solution:

    def solve(self, i, j, pi):
        """
        Recursive function to find and print all paths

        Args:
            i (int): Current row position
            j (int): Current column position
            pi (int): Current position in path array (path index)
        """
        # Special Case 1: Reached last row
        # Fill remaining columns and print path
        if i == self.m - 1:
            # Fill path with remaining elements in this row
            for k in range(j, self.n):
                self.path[pi + k - j] = self.matrix[i][k]

            # Print the complete path
            for l in range(pi + self.n - j):
                print(self.path[l], end=" ")
            print()
            return

        # Special Case 2: Reached last column
        # Fill remaining rows and print path
        if j == self.n - 1:
            # Fill path with remaining elements in this column
            for k in range(i, self.m):
                self.path[pi + k - i] = self.matrix[k][j]

            # Print the complete path
            for l in range(pi + self.m - i):
                print(self.path[l], end=" ")
            print()
            return

        # General Case: Not at boundary
        # Add current element to path
        self.path[pi] = self.matrix[i][j]

        # Explore two directions:

        # 1. Move DOWN (increase row)
        self.solve(i + 1, j, pi + 1)

        # 2. Move RIGHT (increase column)
        self.solve(i, j + 1, pi + 1)

        # Note: If diagonal moves were allowed, add:
        # self.solve(i + 1, j + 1, pi + 1)

    def printAllPath(self, matrix, m, n):
        """
        Main function to print all paths from top-left to bottom-right

        Args:
            matrix (list): M×N matrix
            m (int): Number of rows
            n (int): Number of columns
        """
        self.m = m  # Number of rows
        self.n = n  # Number of columns
        self.matrix = matrix

        # Create path array to store current path
        # Maximum path length is m + n - 1 (all rights then all downs)
        self.path = [0 for _ in range(m + n)]

        # Start from top-left corner (0, 0) with path index 0
        self.solve(0, 0, 0)


# Example Usage and Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: 2×3 matrix
    print("Test Case 1: 2×3 Matrix")
    matrix1 = [[1, 2, 3],
               [4, 5, 6]]
    m1, n1 = 2, 3
    print(f"Matrix:")
    for row in matrix1:
        print(row)
    print(f"\nAll paths from (0,0) to ({m1-1},{n1-1}):")
    sol.printAllPath(matrix1, m1, n1)

    # Test Case 2: 3×3 matrix
    print("\n\nTest Case 2: 3×3 Matrix")
    matrix2 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    m2, n2 = 3, 3
    print(f"Matrix:")
    for row in matrix2:
        print(row)
    print(f"\nAll paths from (0,0) to ({m2-1},{n2-1}):")
    sol.printAllPath(matrix2, m2, n2)

    # Test Case 3: 1×4 matrix (single row)
    print("\n\nTest Case 3: 1×4 Matrix (Single Row)")
    matrix3 = [[1, 2, 3, 4]]
    m3, n3 = 1, 4
    print(f"Matrix: {matrix3[0]}")
    print(f"\nAll paths from (0,0) to ({m3-1},{n3-1}):")
    sol.printAllPath(matrix3, m3, n3)

    # Test Case 4: 4×1 matrix (single column)
    print("\n\nTest Case 4: 4×1 Matrix (Single Column)")
    matrix4 = [[1], [2], [3], [4]]
    m4, n4 = 4, 1
    print(f"Matrix:")
    for row in matrix4:
        print(row)
    print(f"\nAll paths from (0,0) to ({m4-1},{n4-1}):")
    sol.printAllPath(matrix4, m4, n4)

    # Test Case 5: 3×2 matrix
    print("\n\nTest Case 5: 3×2 Matrix")
    matrix5 = [[10, 20],
               [30, 40],
               [50, 60]]
    m5, n5 = 3, 2
    print(f"Matrix:")
    for row in matrix5:
        print(row)
    print(f"\nAll paths from (0,0) to ({m5-1},{n5-1}):")
    sol.printAllPath(matrix5, m5, n5)

    # Test Case 6: 1×1 matrix (edge case)
    print("\n\nTest Case 6: 1×1 Matrix (Edge Case)")
    matrix6 = [[5]]
    m6, n6 = 1, 1
    print(f"Matrix: {matrix6[0]}")
    print(f"\nAll paths from (0,0) to ({m6-1},{n6-1}):")
    sol.printAllPath(matrix6, m6, n6)
