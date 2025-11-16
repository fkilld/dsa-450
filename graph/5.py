"""
PROBLEM: Rat in a Maze

DESCRIPTION:
A rat is placed at position (0,0) in an n×n maze. The rat needs to reach
the destination at (n-1, n-1). The maze has some blocked cells (0) and
open cells (1). Find all possible paths from source to destination.

Movement: The rat can move in 4 directions: Up, Down, Left, Right
Path representation: U (Up), D (Down), L (Left), R (Right)

APPROACH (Backtracking with DFS):
1. Start from (0,0) with empty path string
2. At each cell, try all 4 directions: U, D, L, R
3. For each direction:
   - Check if move is valid (in bounds, not blocked, not visited)
   - Mark current cell as visited
   - Recursively explore that direction
   - If destination reached, add path to result
   - Backtrack: unmark cell (to allow other paths to use it)
4. Return all valid paths in sorted order

KEY TECHNIQUE - BACKTRACKING:
- Mark cell visited before exploring
- Unmark cell after exploring (allows reuse in other paths)
- This explores all possible paths

FLOWCHART:
┌─────────────────────┐
│ Start at (0,0)      │
│ path = ""           │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Is (i,j) valid?     │
│ - In bounds?        │
│ - Not blocked?      │
│ - Not visited?      │
└──────┬──────────────┘
       │
      NO│              YES
       │               │
       ▼               ▼
   ┌────────┐   ┌─────────────────────┐
   │ Return │   │ Reached (n-1,n-1)?  │
   └────────┘   └──────┬──────────────┘
                       │
                    NO │          YES
                       │           │
                       │           ▼
                       │    ┌──────────────┐
                       │    │ Add path to  │
                       │    │ result       │
                       │    │ Return       │
                       │    └──────────────┘
                       │
                       ▼
                ┌─────────────────────┐
                │ Mark (i,j) visited  │
                └──────┬──────────────┘
                       │
                       ▼
                ┌─────────────────────┐
                │ Try all 4 moves:    │
                │ dfs(i-1,j, path+'U')│
                │ dfs(i+1,j, path+'D')│
                │ dfs(i,j-1, path+'L')│
                │ dfs(i,j+1, path+'R')│
                └──────┬──────────────┘
                       │
                       ▼
                ┌─────────────────────┐
                │ Unmark (i,j)        │
                │ (BACKTRACK)         │
                └─────────────────────┘

EXAMPLE:
Maze:
1 0 0 0
1 1 0 1
0 1 0 0
1 1 1 1

Valid paths:
DDRDRR (Down, Down, Right, Down, Right, Right)
DRDDRR (Down, Right, Down, Down, Right, Right)

TIME COMPLEXITY: O(4^(n²))
- At each cell, we try 4 directions
- In worst case, we explore all cells
- Exponential due to backtracking

SPACE COMPLEXITY: O(n²)
- Visited matrix: O(n²)
- Recursion stack: O(n²) in worst case

INTERVIEW TIPS:
1. This is a classic backtracking problem
2. KEY: Mark visited before recursion, unmark after (backtrack)
3. Check boundary conditions first (avoid index errors)
4. Sort the result if lexicographic order is required
5. Handle edge cases: start/end is blocked
6. Can be solved with BFS too, but backtracking is more intuitive

VARIATIONS:
- 8-directional movement (include diagonals)
- Weighted maze (find minimum cost path)
- Multiple rats or destinations
"""

class Solution:
    def dfs(self, i, j, s):
        """
        DFS with backtracking to find all paths.

        Args:
            i: Current row position
            j: Current column position
            s: Path string so far (sequence of U/D/L/R moves)
        """
        # Base case 1: Check boundaries
        if i < 0 or j < 0 or i >= self.n or j >= self.n:
            return

        # Base case 2: Check if cell is blocked (0) or already visited
        if self.m[i][j] == 0 or self.vis[i][j] == True:
            return

        # Base case 3: Reached destination
        if i == self.n - 1 and j == self.n - 1:
            self.ans.append(s)
            return

        # Mark current cell as visited (part of current path)
        self.vis[i][j] = True

        # Explore all 4 directions (maintaining lexicographic order: D, L, R, U)
        self.dfs(i - 1, j, s + 'U')  # Move Up
        self.dfs(i + 1, j, s + 'D')  # Move Down
        self.dfs(i, j - 1, s + 'L')  # Move Left
        self.dfs(i, j + 1, s + 'R')  # Move Right

        # BACKTRACK: Unmark cell to allow it in other paths
        # This is crucial for finding all possible paths
        self.vis[i][j] = False

    def findPath(self, m, n):
        """
        Find all paths from (0,0) to (n-1,n-1) in the maze.

        Args:
            m: n×n maze matrix (1 = open, 0 = blocked)
            n: Size of the maze

        Returns:
            List of all valid paths in lexicographic order
        """
        # Initialize visited matrix (all False)
        self.vis = [[False for _ in range(n)] for _ in range(n)]

        # Store maze and size
        self.m = m
        self.n = n

        # Result list to store all valid paths
        self.ans = []

        # Edge case: source is blocked
        if self.m[0][0] == 0:
            return self.ans

        # Edge case: destination is blocked
        if self.m[n - 1][n - 1] == 0:
            return self.ans

        # Start DFS from (0,0) with empty path
        s = ""
        self.dfs(0, 0, s)

        # Sort paths in lexicographic order
        self.ans.sort()

        return self.ans
