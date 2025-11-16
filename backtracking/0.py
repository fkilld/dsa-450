"""
RAT IN A MAZE PROBLEM
=====================

Problem Statement:
-----------------
Given a square maze of size N x N, where each cell is either:
- 1: A valid path
- 0: A blocked cell

A rat starts from (0, 0) and needs to reach (N-1, N-1).
The rat can move in four directions: Down (D), Left (L), Right (R), Up (U).
Find all possible paths in lexicographical order.

Example:
--------
Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1},
         {1, 1, 0, 0},
         {0, 1, 1, 1}}

Output: DDRDRR DRDDRR
Explanation: The rat can reach the destination from (0,0) to (3,3)
using these two paths.

Approach:
---------
1. Use Backtracking to explore all possible paths
2. Start from (0, 0) and try all four directions in lexicographical order (D, L, R, U)
3. Mark cells as visited to avoid cycles in the current path
4. When destination (N-1, N-1) is reached, store the path
5. Backtrack by unmarking the cell for other potential paths

Time Complexity: O(4^(N*N)) - In worst case, we explore 4 directions for each cell
Space Complexity: O(N*N) - For visited array and recursion stack

Flowchart:
----------
```mermaid
graph TD
    A[Start at 0,0] --> B{Is position valid?}
    B -->|No| C[Return]
    B -->|Yes| D{Is cell = 0 or visited?}
    D -->|Yes| C
    D -->|No| E{Reached destination N-1,N-1?}
    E -->|Yes| F[Add path to result]
    F --> C
    E -->|No| G[Mark cell as visited]
    G --> H[Try Down: i+1,j]
    H --> I[Try Left: i,j-1]
    I --> J[Try Right: i,j+1]
    J --> K[Try Up: i-1,j]
    K --> L[Backtrack: Mark cell as unvisited]
    L --> C
```
"""

class Solution:

    def solve(self, i, j, path, m):
        """
        Recursive function to find all paths from current position to destination

        Args:
            i (int): Current row position
            j (int): Current column position
            path (str): Current path string (combination of D, L, R, U)
            m (list): The maze matrix
        """
        # Base Case 1: Check if current position is within the board boundaries
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            return

        # Base Case 2: Check if cell is blocked (0) or already visited
        if m[i][j] == 0 or self.vis[i][j]:
            return

        # Base Case 3: Check if we reached the destination
        if i == self.n - 1 and j == self.n - 1:
            self.res.append(path)
            return

        # Mark current cell as visited (part of current path)
        self.vis[i][j] = True

        # Explore all four directions in lexicographical order: D, L, R, U
        # Down: Move to (i+1, j)
        self.solve(i + 1, j, path + "D", m)

        # Left: Move to (i, j-1)
        self.solve(i, j - 1, path + "L", m)

        # Right: Move to (i, j+1)
        self.solve(i, j + 1, path + "R", m)

        # Up: Move to (i-1, j)
        self.solve(i - 1, j, path + "U", m)

        # Backtracking: Unmark the cell as it may be part of another path
        self.vis[i][j] = False


    def findPath(self, m, n):
        """
        Main function to find all paths from (0,0) to (n-1, n-1)

        Args:
            m (list): The maze matrix
            n (int): Size of the maze (n x n)

        Returns:
            list: All possible paths in lexicographical order
        """
        self.n = n  # Store the dimension of the maze

        # Initialize visited array to track cells in current path
        self.vis = [[False for _ in range(n)] for _ in range(n)]

        # Initialize result list to store all valid paths
        self.res = []

        # Start the backtracking from (0, 0) with empty path
        self.solve(0, 0, "", m)

        return self.res


# Example Usage and Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    maze1 = [[1, 0, 0, 0],
             [1, 1, 0, 1],
             [1, 1, 0, 0],
             [0, 1, 1, 1]]
    print("Test Case 1:")
    print("Paths:", sol.findPath(maze1, 4))

    # Test Case 2: Simple 2x2 maze
    maze2 = [[1, 1],
             [1, 1]]
    print("\nTest Case 2:")
    print("Paths:", sol.findPath(maze2, 2))