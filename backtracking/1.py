"""
N-QUEENS PROBLEM
================

Problem Statement:
-----------------
The N-Queens puzzle is to place N chess queens on an N×N chessboard such that
no two queens attack each other. A queen can attack horizontally, vertically,
and diagonally.

Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration where 'Q' represents a queen
and '.' represents an empty space.

Example:
--------
Input: n = 4
Output: [
 [".Q..",
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",
  "Q...",
  "...Q",
  ".Q.."]
]

Approach:
---------
1. Use Backtracking with column-by-column placement
2. For each column, try placing queen in each row
3. Use three arrays to track conflicts:
   - row[]: Check if queen exists in this row
   - upper_left[]: Check upper-left to lower-right diagonal
   - down_left[]: Check upper-right to lower-left diagonal
4. Diagonal formula:
   - Upper-left diagonal: (col - row + n - 1) gives unique index
   - Lower-left diagonal: (row + col) gives unique index
5. If valid placement found, mark all three arrays and recurse
6. Backtrack by unmarking when exploring other possibilities

Time Complexity: O(N!) - For first queen N positions, second N-1, etc.
Space Complexity: O(N²) - Board storage + O(N) for tracking arrays

Flowchart:
----------
```mermaid
graph TD
    A[Start: col=0] --> B{col == n?}
    B -->|Yes| C[Found solution - Store board]
    C --> D[Return]
    B -->|No| E[Try each row in current column]
    E --> F{Is position safe?}
    F -->|No| G[Try next row]
    G --> E
    F -->|Yes| H[Place Queen at row,col]
    H --> I[Mark row, both diagonals]
    I --> J[Recurse: solve col+1]
    J --> K[Backtrack: Remove Queen]
    K --> L[Unmark row, both diagonals]
    L --> G
    G -->|All rows tried| D
```
"""

from copy import deepcopy


class Solution:

    def solve(self, col, board):
        """
        Recursive function to place queens column by column

        Args:
            col (int): Current column where we need to place a queen
            board (list): Current state of the board
        """
        # Base Case: All queens placed successfully
        if col == self.n:
            # Deep copy to preserve this solution
            self.res.append(deepcopy(board))
            return

        # Try placing queen in each row of current column
        for row in range(self.n):
            # Check if this position is safe from attacks
            # Queen is safe if:
            # 1. No queen in this row
            # 2. No queen in upper-left diagonal
            # 3. No queen in lower-left diagonal
            if (not self.row[row] and
                not self.upper_left[col - row + self.n - 1] and
                not self.down_left[row + col]):

                # Place the queen
                board[row][col] = "Q"

                # Mark this row and diagonals as occupied
                self.row[row] = True
                self.upper_left[col - row + self.n - 1] = True
                self.down_left[row + col] = True

                # Recursively place queens in next columns
                self.solve(col + 1, board)

                # Backtracking: Remove queen and unmark
                board[row][col] = "."
                self.row[row] = False
                self.upper_left[col - row + self.n - 1] = False
                self.down_left[row + col] = False


    def solveNQueens(self, n):
        """
        Main function to solve N-Queens problem

        Args:
            n (int): Size of the board (n x n) and number of queens

        Returns:
            list: All distinct solutions as board configurations
        """
        self.n = n  # Store board size

        # Initialize n x n board with all empty cells
        board = [["." for _ in range(n)] for _ in range(n)]

        # Initialize result list
        self.res = []

        # Tracking arrays for conflicts
        self.row = [False] * n  # Track if queen exists in each row

        # Track diagonals - There are (2*n - 1) diagonals in each direction
        # Upper-left to lower-right diagonals
        self.upper_left = [False] * (2 * n - 1)

        # Upper-right to lower-left diagonals
        self.down_left = [False] * (2 * n - 1)

        # Start solving from column 0
        self.solve(0, board)

        return self.res


# Example Usage and Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: 4-Queens
    print("Test Case 1: 4-Queens")
    solutions = sol.solveNQueens(4)
    for i, solution in enumerate(solutions, 1):
        print(f"\nSolution {i}:")
        for row in solution:
            print("".join(row))

    # Test Case 2: 8-Queens (Classic problem)
    print("\n\nTest Case 2: 8-Queens")
    solutions = sol.solveNQueens(8)
    print(f"Total solutions: {len(solutions)}")
