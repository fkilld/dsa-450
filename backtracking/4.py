"""
SUDOKU SOLVER
=============

Problem Statement:
-----------------
Given a partially filled 9×9 2D array grid, the goal is to assign digits
(from 1 to 9) to the empty cells (represented by 0) so that every row,
every column, and every 3×3 sub-grid contains exactly one instance of
the digits from 1 to 9.

Example:
--------
Input:
grid[][] =
[[3, 0, 6, 5, 0, 8, 4, 0, 0],
 [5, 2, 0, 0, 0, 0, 0, 0, 0],
 [0, 8, 7, 0, 0, 0, 0, 3, 1],
 [0, 0, 3, 0, 1, 0, 0, 8, 0],
 [9, 0, 0, 8, 6, 3, 0, 0, 5],
 [0, 5, 0, 0, 9, 0, 6, 0, 0],
 [1, 3, 0, 0, 0, 0, 2, 5, 0],
 [0, 0, 0, 0, 0, 0, 0, 7, 4],
 [0, 0, 5, 2, 0, 6, 3, 0, 0]]

Output: Solved Sudoku grid

Approach:
---------
1. Find an empty cell (value = 0)
2. Try placing digits 1-9 in that cell
3. For each digit, check if it's valid:
   - No same digit in the same row
   - No same digit in the same column
   - No same digit in the same 3x3 sub-grid
4. If valid, place the digit and recursively solve rest
5. If recursion returns True, solution found
6. If recursion returns False, backtrack (reset to 0) and try next digit
7. If no digit works, return False

Time Complexity: O(9^(n*n)) where n=9 - Exponential in worst case
Space Complexity: O(n*n) - Recursion stack depth

Flowchart:
----------
```mermaid
graph TD
    A[Start: Find empty cell 0] --> B{Found empty cell?}
    B -->|No| C[All cells filled - Return True]
    B -->|Yes| D[Try digits 1 to 9]
    D --> E{Is digit valid?}
    E -->|No| F[Try next digit]
    E -->|Yes| G[Place digit in cell]
    G --> H[Recursively solve rest]
    H --> I{Solution found?}
    I -->|Yes| C
    I -->|No| J[Backtrack: Reset cell to 0]
    J --> F
    F -->|All digits tried| K[Return False]
```
"""


class Solution:

    def isValid(self, val, row, col, grid):
        """
        Check if placing 'val' at grid[row][col] is valid

        Args:
            val (int): Value to place (1-9)
            row (int): Row index
            col (int): Column index
            grid (list): Current Sudoku grid

        Returns:
            bool: True if placement is valid, False otherwise
        """
        # Check the entire row and column in one loop
        for i in range(9):
            # Check if 'val' already exists in the same row
            if grid[row][i] == val:
                return False

            # Check if 'val' already exists in the same column
            if grid[i][col] == val:
                return False

            # Check if 'val' exists in the 3x3 sub-grid
            # Formula to check all 9 cells of the 3x3 box:
            # - 3 * (row // 3) gives top-left row of the box
            # - i // 3 iterates through 3 rows (0, 0, 0, 1, 1, 1, 2, 2, 2)
            # - 3 * (col // 3) gives top-left column of the box
            # - i % 3 iterates through 3 columns (0, 1, 2, 0, 1, 2, ...)
            if grid[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == val:
                return False

        return True


    def SolveSudoku(self, grid):
        """
        Solve Sudoku using backtracking

        Args:
            grid (list): 9x9 Sudoku grid (0 represents empty cell)

        Returns:
            bool: True if solution found, False otherwise
        """
        # Iterate through each cell in the grid
        for i in range(9):
            for j in range(9):

                # Found an empty cell (represented by 0)
                if grid[i][j] == 0:

                    # Try placing digits 1 through 9
                    for val in range(1, 10):

                        # Check if current value is valid at this position
                        if self.isValid(val, i, j, grid):
                            # Place the value
                            grid[i][j] = val

                            # Recursively solve the rest of the grid
                            if self.SolveSudoku(grid):
                                return True  # Solution found
                            else:
                                # Backtracking: Current placement didn't work
                                # Reset to 0 and try next value
                                grid[i][j] = 0

                    # If no value from 1-9 works at this position
                    # This path doesn't lead to solution
                    return False

        # All cells filled successfully
        return True


    def printGrid(self, grid):
        """Helper function to print the Sudoku grid"""
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(grid[i][j], end=" ")
            print()


# Example Usage and Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Easy Sudoku
    grid1 = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    print("Original Sudoku:")
    sol.printGrid(grid1)

    if sol.SolveSudoku(grid1):
        print("\nSolved Sudoku:")
        sol.printGrid(grid1)
    else:
        print("\nNo solution exists")
