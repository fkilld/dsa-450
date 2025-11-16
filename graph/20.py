"""
PROBLEM: Bellman-Ford Algorithm (Shortest Path + Negative Cycle Detection)

DESCRIPTION:
Find shortest paths from a source vertex to all other vertices in a weighted
directed graph. Unlike Dijkstra's algorithm, Bellman-Ford can handle negative
edge weights and detect negative cycles.

WHEN TO USE BELLMAN-FORD vs DIJKSTRA:
- Bellman-Ford: Handles negative weights, slower O(V×E)
- Dijkstra: Only positive weights, faster O((V+E)log V)
- If negative weights exist, MUST use Bellman-Ford

NEGATIVE CYCLE:
A cycle whose total edge weight is negative. If such a cycle exists and is
reachable from source, there's no shortest path (can keep reducing cost).

APPROACH:
1. Initialize distances: dist[source] = 0, others = infinity
2. Relax all edges (V-1) times:
   - For each edge (u,v,w): if dist[u] + w < dist[v], update dist[v]
   - Why (V-1) times? Longest simple path has at most V-1 edges
3. Check for negative cycles:
   - Try relaxing all edges one more time
   - If any distance decreases → negative cycle exists

KEY INSIGHT - Why (V-1) iterations?
- After i iterations, we've found shortest paths with at most i edges
- Maximum edges in a simple path = V-1 (visit each vertex once)
- So V-1 iterations guarantee finding all shortest paths

FLOWCHART:
┌─────────────────────┐
│ Initialize          │
│ dist[0] = 0         │
│ dist[i] = ∞ (i≠0)   │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Repeat (V-1) times  │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ For each edge       │
│ (u, v, w)           │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Can we relax edge?  │
│ dist[u]+w < dist[v]?│
└──────┬──────────────┘
       │
      NO│              YES
       │               │
       │               ▼
       │       ┌─────────────────────┐
       │       │ dist[v] = dist[u]+w │
       │       │ (Relaxation)        │
       │       └─────────────────────┘
       │              │
       └──────────────┘
              │
              ▼
┌─────────────────────┐
│ Try relaxing all    │
│ edges one more time │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Any edge relaxed?   │
└──────┬──────────────┘
       │
      NO│              YES
       │               │
       ▼               ▼
┌─────────────┐  ┌──────────────────┐
│ No negative │  │ NEGATIVE CYCLE!  │
│ cycle       │  │ Return 1         │
│ Return 0    │  └──────────────────┘
└─────────────┘

EXAMPLE WITHOUT NEGATIVE CYCLE:
Edges: [(0,1,4), (1,2,3), (0,2,5)]
Vertices: 0, 1, 2

Initial: dist = [0, ∞, ∞]

Iteration 1:
- Edge (0,1,4): dist[1] = 0+4 = 4    → [0, 4, ∞]
- Edge (1,2,3): dist[2] = 4+3 = 7    → [0, 4, 7]
- Edge (0,2,5): dist[2] = min(7,5) = 5 → [0, 4, 5]

Iteration 2:
- No changes (already optimal)

Check negative cycle: No edge can be relaxed → No cycle

EXAMPLE WITH NEGATIVE CYCLE:
Edges: [(0,1,1), (1,2,-3), (2,0,1)]

Forms cycle: 0→1→2→0 with total weight = 1+(-3)+1 = -1 (negative!)

After V-1 iterations, trying to relax again will succeed → Negative cycle!

TIME COMPLEXITY: O(V × E)
- V-1 iterations
- Each iteration checks all E edges

SPACE COMPLEXITY: O(V)
- Distance array of size V

INTERVIEW TIPS:
1. Bellman-Ford is for graphs with negative weights
2. Dijkstra is faster but fails with negative weights
3. The V-1 iterations guarantee finding shortest paths
4. Extra iteration detects negative cycles
5. If negative cycle exists from source, shortest path is undefined
6. Used in routing protocols (e.g., RIP - Routing Information Protocol)

EDGE CASES:
- Disconnected graph: some distances remain infinity
- Negative cycle: report it (no shortest path exists)
- Single vertex: distance to itself is 0
"""

class Solution:
    def isNegativeWeightCycle(self, n, edges):
        """
        Detect negative weight cycle using Bellman-Ford algorithm.

        Args:
            n: Number of vertices (0 to n-1)
            edges: List of [u, v, w] where edge from u→v has weight w

        Returns:
            1 if negative cycle exists, 0 otherwise
        """
        # Initialize distances: 0 for source, infinity for others
        dist = [float('inf')] * n
        dist[0] = 0  # Source vertex is 0

        # Phase 1: Relax all edges (V-1) times
        # This finds shortest paths with at most (V-1) edges
        for _ in range(n - 1):
            # Try to relax each edge
            for edge in edges:
                u, v, w = edge

                # Relax edge (u, v) if possible
                # Check dist[u] != inf to avoid overflow issues
                if dist[u] != float('inf') and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w

        # Phase 2: Detect negative cycle
        # If we can still relax any edge, a negative cycle exists
        for edge in edges:
            u, v, w = edge

            # If we can still improve distance, negative cycle exists
            if dist[u] != float('inf') and dist[v] > dist[u] + w:
                return 1  # Negative cycle detected

        return 0  # No negative cycle