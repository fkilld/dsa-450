"""
PROBLEM: Detect Cycle in an Undirected Graph using DFS

DESCRIPTION:
Determine if an undirected graph contains a cycle. A cycle exists if there's
a path from a vertex back to itself without using the same edge twice.

KEY INSIGHT:
In an undirected graph, we only need to track:
1. Visited nodes
2. Parent of current node (to avoid false positives)

A cycle exists if we encounter a visited node that is NOT the parent
of the current node (because edges are bidirectional).

DIFFERENCE FROM DIRECTED GRAPH:
- Directed: Need recursion stack tracking (order array)
- Undirected: Only need parent tracking
- Undirected edges go both ways, so we must ignore the edge we came from

APPROACH:
1. Use DFS with parent tracking
2. For each unvisited node, start DFS with parent = -1
3. During DFS:
   - Mark node as visited
   - For each neighbor:
     * If unvisited, recursively check with current node as parent
     * If visited AND not parent → cycle found
     * If visited AND is parent → ignore (came from this edge)

FLOWCHART:
┌─────────────────────┐
│   Start             │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ For each vertex v   │
│ (not visited)       │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ isCyclePresent(v,-1)│
│ Mark v visited      │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ For each neighbor i │
│ of v                │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Is i visited?       │
└──────┬──────────────┘
       │
      NO│              YES
       │               │
       ▼               ▼
┌─────────────────────┐  ┌─────────────────────┐
│ Recurse:            │  │ Is i the parent?    │
│ isCyclePresent(i,v) │  │                     │
└──────┬──────────────┘  └──────┬──────────────┘
       │                        │
       │ Found cycle?       NO  │          YES
       │                        │           │
       ▼                        ▼           ▼
   ┌────────┐           ┌────────────┐  ┌─────────┐
   │Return  │           │CYCLE FOUND!│  │ Ignore  │
   │True    │           │Return True │  │(came    │
   └────────┘           └────────────┘  │from     │
                                        │parent)  │
                                        └─────────┘

EXAMPLE 1 - Cycle Present:
Graph: 0 - 1 - 2
       |       |
       +-------+

DFS(0, -1): vis[0]=T
  → DFS(1, 0): vis[1]=T
    → DFS(2, 1): vis[2]=T
      → Check 0: vis[0]=T AND parent≠0 → CYCLE!

EXAMPLE 2 - No Cycle:
Graph: 0 - 1 - 2

DFS(0, -1): vis[0]=T
  → DFS(1, 0): vis[1]=T
    → DFS(2, 1): vis[2]=T
      → No more unvisited neighbors
    ← Backtrack
  ← Backtrack
No cycle found

EXAMPLE 3 - Why Parent Matters:
Graph: 0 - 1

DFS(0, -1): vis[0]=T
  → DFS(1, 0): vis[1]=T
    → Check 0: vis[0]=T BUT parent=0 → Ignore (same edge)

TIME COMPLEXITY: O(V + E)
- Visit each vertex once
- Check each edge once

SPACE COMPLEXITY: O(V)
- Visited array of size V
- Recursion stack up to V depth

INTERVIEW TIPS:
1. Key difference: undirected uses parent, directed uses recursion stack
2. Parent check prevents false positives from bidirectional edges
3. Initialize parent as -1 when starting DFS
4. Always check if visited neighbor is NOT parent before declaring cycle
5. This is simpler than directed graph cycle detection
"""

class Solution:
    def isCyclePresent(self, v, parent):
        """
        DFS helper to detect cycle in undirected graph.

        Args:
            v: Current vertex being explored
            parent: Vertex from which we reached v (-1 if starting vertex)

        Returns:
            True if cycle detected, False otherwise
        """
        # Mark current vertex as visited
        self.vis[v] = True

        # Explore all neighbors of current vertex
        for i in self.adj[v]:
            # If neighbor not visited, recursively explore
            if not self.vis[i]:
                # Set current vertex as parent for the recursive call
                if self.isCyclePresent(i, v) == True:
                    return True

            # If neighbor is visited AND not the parent → cycle detected!
            # (We've found a back edge to an already visited node)
            elif parent != i:
                return True

        return False

    def isCycle(self, V, adj):
        """
        Check if undirected graph contains a cycle.

        Args:
            V: Number of vertices
            adj: Adjacency list of undirected graph

        Returns:
            True if cycle exists, False otherwise
        """
        # Track visited vertices
        self.vis = [False] * V

        # Store adjacency list
        self.adj = adj

        # Check each component (graph may be disconnected)
        for i in range(V):
            if not self.vis[i]:
                # Start DFS with parent = -1 (no parent for starting node)
                if self.isCyclePresent(i, -1) == True:
                    return True

        return False
		