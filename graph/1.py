"""
PROBLEM: Breadth-First Search (BFS) Traversal of a Graph

DESCRIPTION:
Perform BFS traversal starting from vertex 0, visiting all reachable vertices
level by level (exploring all neighbors before moving to the next level).

APPROACH:
1. Use a queue to track vertices to visit (FIFO - First In First Out)
2. Mark starting vertex as visited and enqueue it
3. While queue is not empty:
   - Dequeue a vertex and add to result
   - For each unvisited neighbor, mark as visited and enqueue
4. This ensures level-by-level traversal

FLOWCHART:
┌─────────────────────┐
│   Start             │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Initialize:         │
│ - Queue with node 0 │
│ - Visited array     │
│ - Result list       │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Mark node 0 visited │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Queue empty?        │
└──────┬──────────────┘
       │
    NO │              YES
       │               │
       ▼               ▼
┌─────────────────────┐  ┌──────────────┐
│ Dequeue vertex 'u'  │  │ Return result│
│ Add to result       │  └──────────────┘
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ For each neighbor   │
│ 'v' of 'u'          │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Is 'v' visited?     │
└──────┬──────────────┘
       │
    YES│              NO
       │               │
       │               ▼
       │       ┌─────────────────────┐
       │       │ Mark 'v' visited    │
       │       │ Enqueue 'v'         │
       │       └──────┬──────────────┘
       │              │
       └──────────────┘
              │
              ▼
       (Loop back to check queue)

TIME COMPLEXITY: O(V + E)
- V: number of vertices (each visited once)
- E: number of edges (each checked once)

SPACE COMPLEXITY: O(V)
- Queue can hold at most V vertices
- Visited array of size V

INTERVIEW TIPS:
1. BFS uses Queue (FIFO), DFS uses Stack (LIFO)
2. BFS finds shortest path in unweighted graphs
3. BFS is useful for level-order traversal
4. Remember to mark vertex visited BEFORE adding to queue (prevents duplicates)

USE CASES:
- Finding shortest path in unweighted graph
- Level order traversal
- Finding connected components
- Web crawlers
- Social network analysis (friends at distance k)
"""

from collections import deque

class Solution:
    def bfsOfGraph(self, V, adj):
        """
        Perform BFS traversal of graph starting from vertex 0.

        Args:
            V: Number of vertices in graph
            adj: Adjacency list representation of graph

        Returns:
            List of vertices in BFS traversal order
        """
        # Result list to store BFS traversal
        ans = []

        # Queue for BFS - starts with vertex 0
        vertices = deque([0])

        # Track visited vertices to avoid cycles
        visited = [False] * (V + 1)
        visited[0] = True  # Mark starting vertex as visited

        # Process vertices level by level
        while len(vertices) != 0:
            # Dequeue the front vertex
            temp = vertices.popleft()

            # Add current vertex to result
            ans.append(temp)

            # Explore all neighbors of current vertex
            for i in adj[temp]:
                # If neighbor not visited, mark and enqueue
                if visited[i] == False:
                    vertices.append(i)
                    visited[i] = True  # Mark visited when enqueuing

        return ans


