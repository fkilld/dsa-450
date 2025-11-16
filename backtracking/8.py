"""
KNIGHT'S TOUR PROBLEM
=====================

Problem Statement:
-----------------
Given a N×N chessboard and a Knight at position (0, 0). The knight has to take
exactly N²-1 steps, where each step consists of moving the knight according to
chess rules (L-shaped move: 2 squares in one direction and 1 square perpendicular).

Find a sequence of moves such that the knight visits every square exactly once.
Print the order in which the knight visits each square.

Example:
--------
Input: N = 5
Output: A 5×5 matrix where each cell shows the order of visit

   0  59  38  33  30
  37  34  31  60  39
  58   1  36  41  32
  35  48  61  28  63
   2  57  40  55  26

Explanation: Knight starts at (0,0) marked as 0, then moves to positions marked
1, 2, 3... and eventually visits all 64 squares

Input: N = 8
Output: 8×8 matrix showing knight's tour

Approach:
---------
1. Start from position (0, 0) and mark it as position 0
2. Try all 8 possible knight moves from current position
3. For each valid move (within board and unvisited):
   - Mark the cell with current position number
   - Recursively try to complete the tour from this new position
   - If recursion succeeds, solution found
   - If recursion fails, backtrack (unmark the cell) and try next move
4. A knight can move in 8 directions:
   (±2, ±1) and (±1, ±2) combinations

Time Complexity: O(8^(N²)) - 8 choices for each of N² positions (worst case)
Space Complexity: O(N²) - Board storage + O(N²) recursion depth

Flowchart:
----------
```mermaid
graph TD
    A[Start: pos=0 at 0,0] --> B{pos == N²?}
    B -->|Yes| C[All squares visited - Return True]
    B -->|No| D[Try all 8 knight moves]
    D --> E{Is new position valid?}
    E -->|No| F[Try next move]
    E -->|Yes| G{Is cell unvisited?}
    G -->|No| F
    G -->|Yes| H[Mark cell with pos number]
    H --> I[Recurse: solve new_pos, pos+1]
    I --> J{Solution found?}
    J -->|Yes| C
    J -->|No| K[Backtrack: Mark cell as -1]
    K --> F
    F -->|All moves tried| L[Return False]
```
"""


class Solution:

    def solve(self, i, j, pos, board):
        """
        Recursive backtracking function to find knight's tour

        Args:
            i (int): Current row position
            j (int): Current column position
            pos (int): Current position number (0 to N²-1)
            board (list): N×N board storing visit order

        Returns:
            bool: True if tour can be completed from here, False otherwise
        """
        # Base Case: All squares have been visited
        if pos == self.n ** 2:
            return True

        # Try all 8 possible knight moves
        for dx, dy in self.dir:
            # Calculate new position
            x = i + dx
            y = j + dy

            # Check if new position is valid:
            # 1. Within board boundaries
            # 2. Not yet visited (cell value is -1)
            if x >= 0 and x < self.n and y >= 0 and y < self.n and board[x][y] == -1:
                # Mark this cell with current position number
                board[x][y] = pos

                # Recursively try to complete tour from this position
                if self.solve(x, y, pos + 1, board):
                    return True  # Solution found

                # Backtracking: This move didn't lead to solution
                # Unmark the cell to try other moves
                board[x][y] = -1

        # No move from current position leads to solution
        return False

    def knightTour(self, n):
        """
        Main function to solve Knight's Tour problem

        Args:
            n (int): Size of the chessboard (n × n)
        """
        self.n = n

        # Create board initialized with -1 (unvisited)
        board = [[-1 for _ in range(n)] for _ in range(n)]

        # Knight starts at position (0, 0)
        board[0][0] = 0

        # All 8 possible knight moves (L-shaped moves)
        # 2 squares in one direction, 1 square perpendicular
        self.dir = [
            [-1, -2],  # Up 2, Left 1
            [1, -2],   # Down 2, Left 1
            [-2, -1],  # Up 1, Left 2
            [-2, 1],   # Up 1, Right 2
            [-1, 2],   # Up 2, Right 1
            [1, 2],    # Down 2, Right 1
            [2, -1],   # Down 1, Left 2
            [2, 1]     # Down 1, Right 2
        ]

        # Try to find a solution starting from (0, 0) with position 1
        if self.solve(0, 0, 1, board):
            # Print the board showing visit order
            print(f"Knight's Tour solution for {n}×{n} board:")
            for i in range(n):
                for j in range(n):
                    # Print each number with width 4 for alignment
                    print(f"{board[i][j]:4}", end=" ")
                print()
        else:
            print(f"No solution exists for {n}×{n} board")


# Example Usage and Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: 5×5 board
    print("Test Case 1: 5×5 Board")
    sol.knightTour(5)

    # Test Case 2: 8×8 board (standard chessboard)
    print("\n\nTest Case 2: 8×8 Board (Standard Chessboard)")
    print("Note: This may take a moment to compute...")
    sol.knightTour(8)

    # Test Case 3: Small boards (some may not have solutions)
    print("\n\nTest Case 3: 3×3 Board")
    sol.knightTour(3)

    print("\n\nTest Case 4: 6×6 Board")
    sol.knightTour(6)
