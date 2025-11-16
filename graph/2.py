"""
PROBLEM: Depth-First Search (DFS) Traversal of a Graph

DESCRIPTION:
Perform DFS traversal starting from vertex 0, exploring as far as possible
along each branch before backtracking (goes deep first, then wide).

APPROACH:
1. Use recursion (implicit stack) to explore vertices
2. Mark starting vertex as visited
3. Recursively visit all unvisited neighbors
4. Backtrack when no more unvisited neighbors exist
5. This creates a depth-first exploration pattern

KEY DIFFERENCE FROM BFS:
- BFS explores level by level (breadth-first)
- DFS explores branch by branch (depth-first)
- BFS uses Queue, DFS uses Stack (recursion = implicit stack)

FLOWCHART:
┌─────────────────────┐
│   Start DFS(0)      │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Mark vertex 'v'     │
│ as visited          │
│ Add to result       │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ For each neighbor   │
│ 'u' of 'v'          │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Is 'u' visited?     │
└──────┬──────────────┘
       │
    YES│              NO
       │               │
       │               ▼
       │       ┌─────────────────────┐
       │       │ Recursively call    │
       │       │ DFS(u)              │
       │       └──────┬──────────────┘
       │              │
       └──────────────┘
              │
              ▼
       ┌─────────────────────┐
       │ All neighbors done? │
       │ Backtrack           │
       └─────────────────────┘

RECURSION TREE EXAMPLE:
For graph: 0-1-2
          │
          3-4

      DFS(0)
      │
      ├─→ DFS(1)
      │   │
      │   └─→ DFS(2)
      │       (backtrack)
      │
      └─→ DFS(3)
          │
          └─→ DFS(4)
              (backtrack)

TIME COMPLEXITY: O(V + E)
- V: number of vertices (each visited once)
- E: number of edges (each explored once)

SPACE COMPLEXITY: O(V)
- Recursion stack depth can go up to V
- Visited array of size V

INTERVIEW TIPS:
1. DFS uses recursion (stack), BFS uses queue
2. DFS is simpler to code with recursion
3. Use DFS for: cycle detection, topological sort, path finding
4. Mark visited at the START of recursive call to prevent infinite loops

USE CASES:
- Detecting cycles in graphs
- Topological sorting
- Finding strongly connected components
- Maze solving
- Puzzle solving (Sudoku, N-Queens)
"""

class Solution:
    def solve(self, v):
        """
        Recursive helper function to perform DFS.

        Args:
            v: Current vertex being explored
        """
        # Add current vertex to result
        self.ans.append(v)

        # Mark current vertex as visited
        self.vis[v] = True

        # Explore all neighbors of current vertex
        for i in self.adj[v]:
            # If neighbor not visited, recursively explore it
            if not self.vis[i]:
                self.solve(i)  # Recursive call (goes deep)

    def dfsOfGraph(self, V, adj):
        """
        Perform DFS traversal of graph starting from vertex 0.

        Args:
            V: Number of vertices in graph
            adj: Adjacency list representation of graph

        Returns:
            List of vertices in DFS traversal order
        """
        # Result list to store DFS traversal
        self.ans = []

        # Track visited vertices to avoid cycles
        self.vis = [False] * (V)

        # Store adjacency list for access in helper function
        self.adj = adj

        # Start DFS from vertex 0
        self.solve(0)

        return self.ans
