"""
SHORTEST SAFE ROUTE IN A PATH WITH LANDMINES
=============================================

Problem Statement:
-----------------
Given a matrix where:
- 1 represents a safe cell
- 0 represents a landmine

Find the shortest safe route from any cell in the first column to any cell in
the last column. You can move in 4 directions (up, down, left, right).

Important: Cells adjacent (horizontally or vertically) to landmines are also unsafe.

Example:
--------
Input:
grid = [[1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1]]

Output: 14
Explanation: Shortest safe path length from first to last column is 14

Approach 1 - DFS with Backtracking:
------------------------------------
1. Mark all cells adjacent to landmines (0) as unsafe (-1)
2. For each safe cell in first column, try DFS
3. Try moving in all 4 directions from current cell
4. Mark cells as visited to avoid cycles
5. Track minimum distance to last column
6. Backtrack by unmarking cells for other paths

Time Complexity: O(4^(N*M)) - Exponential in worst case
Space Complexity: O(N*M) - Visited array + recursion stack

Approach 2 - BFS (Optimal):
----------------------------
1. Mark all cells adjacent to landmines as unsafe
2. Use BFS starting from all safe cells in first column
3. BFS guarantees shortest path in unweighted graph
4. Track distance to each cell
5. Return minimum distance to any cell in last column

Time Complexity: O(N*M) - Visit each cell at most once
Space Complexity: O(N*M) - Distance array + queue

Flowchart (DFS):
----------------
```mermaid
graph TD
    A[Mark unsafe cells] --> B[Try each row in first column]
    B --> C{Is cell safe?}
    C -->|No| D[Try next row]
    C -->|Yes| E[DFS from this cell]
    E --> F{Reached last column?}
    F -->|Yes| G[Update min distance]
    F -->|No| H[Mark visited]
    H --> I[Try 4 directions]
    I --> J{Valid and safe?}
    J -->|Yes| K[Recurse]
    K --> L[Backtrack: Unmark]
    L --> M{More directions?}
    J -->|No| M
    M -->|Yes| I
    M -->|No| N[Return]
    G --> N
    D --> B
```
"""

from collections import deque


# DFS APPROACH (Backtracking)
class DFS:

    def isSafe(self, x, y):
        """
        Check if position (x, y) is within grid bounds

        Args:
            x (int): Row position
            y (int): Column position

        Returns:
            bool: True if within bounds, False otherwise
        """
        if x >= 0 and x < self.n and y >= 0 and y < self.m:
            return True
        return False

    def markUnsafe(self, grid):
        """
        Mark cells adjacent to landmines as unsafe

        Args:
            grid (list): The grid with landmines (0) and safe cells (1)
        """
        # First pass: Mark adjacent cells of landmines as -1 (temporarily unsafe)
        for i in range(self.n):
            for j in range(self.m):
                # If current cell has a landmine
                if grid[i][j] == 0:
                    # Mark all 4 adjacent cells as unsafe
                    for dx, dy in self.dir:
                        if self.isSafe(i + dx, j + dy):
                            grid[i + dx][j + dy] = -1

        # Second pass: Convert -1 back to 0 (permanently unsafe)
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == -1:
                    grid[i][j] = 0

    def solve(self, row, col, dist, grid):
        """
        Recursive DFS to find shortest safe path

        Args:
            row (int): Current row
            col (int): Current column
            dist (int): Current distance traveled
            grid (list): The grid
        """
        # Base Case: Reached last column
        if col == self.m - 1:
            self.min = min(self.min, dist)
            return

        # Pruning: If current distance already exceeds minimum, no need to continue
        if dist >= self.min:
            return

        # Mark current cell as visited
        self.vis[row][col] = True

        # Try all 4 directions
        for dx, dy in self.dir:
            x = row + dx
            y = col + dy

            # Check if new position is valid, safe, and unvisited
            if self.isSafe(x, y):
                if grid[x][y] != 0 and not self.vis[x][y]:
                    # Recursively explore this path
                    self.solve(x, y, dist + 1, grid)

        # Backtracking: Unmark cell for other paths
        self.vis[row][col] = False

    def shortestPath(self, grid):
        """
        Main function to find shortest safe path using DFS

        Args:
            grid (list): Matrix with landmines and safe cells
        """
        self.n = len(grid)      # Number of rows
        self.m = len(grid[0])   # Number of columns

        # Initialize minimum distance to infinity
        self.min = float('inf')

        # Initialize visited array
        self.vis = [[False for _ in range(self.m)] for _ in range(self.n)]

        # Four possible directions: up, down, left, right
        self.dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # Mark cells adjacent to landmines as unsafe
        self.markUnsafe(grid)

        # Try starting from each safe cell in the first column
        for i in range(self.n):
            if grid[i][0] == 1:
                self.solve(i, 0, 0, grid)

        # Print result
        if self.min == float('inf'):
            print("No safe path exists")
        else:
            print(f"Shortest safe path (DFS): {self.min}")


# BFS APPROACH (Optimal - Guaranteed Shortest Path)
class BFS:

    def isSafe(self, x, y):
        """
        Check if position (x, y) is within grid bounds

        Args:
            x (int): Row position
            y (int): Column position

        Returns:
            bool: True if within bounds, False otherwise
        """
        if x >= 0 and x < self.n and y >= 0 and y < self.m:
            return True
        return False

    def markUnsafe(self, grid):
        """
        Mark cells adjacent to landmines as unsafe

        Args:
            grid (list): The grid with landmines (0) and safe cells (1)
        """
        # First pass: Mark adjacent cells of landmines as -1
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 0:
                    for dx, dy in self.dir:
                        if self.isSafe(i + dx, j + dy):
                            grid[i + dx][j + dy] = -1

        # Second pass: Convert -1 to 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == -1:
                    grid[i][j] = 0

    def shortestPath(self, grid):
        """
        Main function to find shortest safe path using BFS

        Args:
            grid (list): Matrix with landmines and safe cells

        Returns:
            int: Length of shortest safe path, or infinity if no path exists
        """
        self.n = len(grid)
        self.m = len(grid[0])

        # Four directions
        self.dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # Mark unsafe cells
        self.markUnsafe(grid)

        # Distance array: -1 means unvisited
        dist = [[-1 for _ in range(self.m)] for _ in range(self.n)]

        # Queue for BFS
        q = deque()

        # Add all safe cells from first column to queue
        for i in range(self.n):
            if grid[i][0] == 1:
                q.append([i, 0])
                dist[i][0] = 0

        # BFS traversal
        while q:
            i, j = q.popleft()
            d = dist[i][j]

            # Try all 4 directions
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x = i + dx
                y = j + dy

                # Check if new position is valid
                if x >= 0 and x < self.n and y >= 0 and y < self.m:
                    # If safe cell and not yet visited
                    if grid[x][y] == 1 and dist[x][y] == -1:
                        dist[x][y] = d + 1
                        q.append([x, y])

        # Find minimum distance in last column
        ans = float('inf')
        for i in range(self.n):
            if grid[i][self.m - 1] == 1 and dist[i][self.m - 1] != -1:
                ans = min(ans, dist[i][self.m - 1])

        # Print result
        if ans == float('inf'):
            print("No safe path exists")
        else:
            print(f"Shortest safe path (BFS): {ans}")

        return ans


# Example Usage and Test Cases
if __name__ == "__main__":
    # Test Case 1: Standard grid with landmines
    print("Test Case 1:")
    grid1 = [
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
    ]

    # DFS approach
    dfs = DFS()
    dfs.shortestPath([row[:] for row in grid1])  # Create copy

    # BFS approach
    bfs = BFS()
    bfs.shortestPath([row[:] for row in grid1])  # Create copy

    # Test Case 2: Simple grid
    print("\n\nTest Case 2:")
    grid2 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    dfs2 = DFS()
    dfs2.shortestPath([row[:] for row in grid2])

    bfs2 = BFS()
    bfs2.shortestPath([row[:] for row in grid2])

    # Test Case 3: No safe path
    print("\n\nTest Case 3:")
    grid3 = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]

    dfs3 = DFS()
    dfs3.shortestPath([row[:] for row in grid3])

    bfs3 = BFS()
    bfs3.shortestPath([row[:] for row in grid3])
