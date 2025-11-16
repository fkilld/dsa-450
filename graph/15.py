"""
PROBLEM: Number of Islands (Connected Components)

DESCRIPTION:
Given an m×n 2D grid of '1's (land) and '0's (water), count the number
of islands. An island is surrounded by water and is formed by connecting
adjacent lands horizontally, vertically, or diagonally.

KEY INSIGHT:
This is a "connected components" problem. Each island is a connected
component of '1's. We use DFS/BFS to mark all cells of one island, then
count how many times we start a new DFS.

APPROACH (DFS):
1. Iterate through all cells in the grid
2. When we find an unvisited land cell ('1'):
   - Increment island count
   - Start DFS to mark all connected land cells as visited
   - DFS explores all 8 directions (horizontal, vertical, diagonal)
3. Return total island count

WHY DFS?
- We need to explore entire connected component
- DFS naturally traverses all reachable cells
- Could also use BFS (same time complexity)

FLOWCHART:
┌─────────────────────┐
│ Start               │
│ count = 0           │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ For each cell       │
│ (row, col)          │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Is cell:            │
│ - Not visited?      │
│ - Land ('1')?       │
└──────┬──────────────┘
       │
      NO│              YES
       │               │
       │               ▼
       │       ┌─────────────────────┐
       │       │ count++             │
       │       │ DFS(row, col)       │
       │       └──────┬──────────────┘
       │              │
       └──────────────┘
              │
              ▼
       ┌─────────────────────┐
       │ All cells done?     │
       └──────┬──────────────┘
              │
             YES
              │
              ▼
       ┌─────────────────────┐
       │ Return count        │
       └─────────────────────┘

DFS PROCEDURE:
┌─────────────────────┐
│ DFS(row, col)       │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Mark (row,col)      │
│ as visited          │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ For all 8 neighbors │
│ (i, j)              │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Is (i,j):           │
│ - In bounds?        │
│ - Not visited?      │
│ - Land ('1')?       │
└──────┬──────────────┘
       │
      NO│              YES
       │               │
       │               ▼
       │       ┌─────────────────────┐
       │       │ DFS(i, j)           │
       │       │ (Recursive)         │
       │       └─────────────────────┘
       │              │
       └──────────────┘

8-DIRECTIONAL MOVEMENT:
(-1,-1) (-1,0) (-1,1)    NW  N  NE
( 0,-1) (curr) ( 0,1)     W  *  E
( 1,-1) ( 1,0) ( 1,1)    SW  S  SE

EXAMPLE:
Grid:
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1

Islands = 3:
- Island 1: top-left (connected 1's)
- Island 2: middle (single 1)
- Island 3: bottom-right (connected 1's)

Step-by-step:
1. Start at (0,0): land & unvisited → count=1, DFS marks all connected
2. Continue scanning... (0,1) already visited
3. Find (2,2): land & unvisited → count=2, DFS marks it
4. Find (3,3): land & unvisited → count=3, DFS marks (3,3) and (3,4)
5. All cells scanned → return 3

TIME COMPLEXITY: O(M × N)
- M: number of rows
- N: number of columns
- Visit each cell at most once

SPACE COMPLEXITY: O(M × N)
- Visited array: O(M × N)
- Recursion stack: O(M × N) in worst case (all land)

INTERVIEW TIPS:
1. This is a classic "flood fill" / "connected components" problem
2. Can use DFS or BFS (both work equally well)
3. Mark visited to avoid infinite loops
4. Count increments only when starting new DFS (new island)
5. Remember to check all 8 directions (or 4 if problem specifies)
6. Edge cases: all water (return 0), all land (return 1)

VARIATIONS:
- 4-directional instead of 8-directional
- Count size of largest island
- Union-Find approach (more complex but elegant)
"""

class Solution:
    def dfs(self, row, col):
        """
        DFS to mark all connected land cells as visited.

        Args:
            row: Current row position
            col: Current column position
        """
        # Mark current cell as visited
        self.visited[row][col] = True

        # 8-directional movement arrays
        # Represents: NW, N, NE, W, E, SW, S, SE
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]

        # Explore all 8 neighbors
        for k in range(8):
            x = row + rowNbr[k]
            y = col + colNbr[k]

            # Check if neighbor is valid
            if x >= 0 and x < self.rows and y >= 0 and y < self.columns:
                # If unvisited land, recursively explore
                if not self.visited[x][y] and self.grid[x][y] == '1':
                    self.dfs(x, y)

    def numIslands(self, grid):
        """
        Count number of islands in the grid.

        Args:
            grid: m×n grid of '1's (land) and '0's (water)

        Returns:
            Number of islands (connected components of land)
        """
        # Store grid and dimensions
        self.grid = grid
        self.rows, self.columns = len(grid), len(grid[0])

        # Initialize visited matrix
        # IMPORTANT: Correct way to create 2D array (avoid aliasing)
        self.visited = [[False for _ in range(self.columns)] for _ in range(self.rows)]

        # Count of islands (connected components)
        count = 0

        # Scan entire grid
        for row in range(self.rows):
            for col in range(self.columns):
                # Found unvisited land → new island!
                if not self.visited[row][col] and self.grid[row][col] == '1':
                    # Start DFS to mark entire island
                    self.dfs(row, col)

                    # Increment island count
                    count += 1

        return count