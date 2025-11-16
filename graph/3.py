"""
PROBLEM: Detect Cycle in a Directed Graph using DFS

DESCRIPTION:
Determine if a directed graph contains a cycle. A cycle exists if you can
start at a vertex and follow directed edges to return to that same vertex.

KEY INSIGHT:
In a directed graph, we need to track two things:
1. Visited nodes (overall)
2. Nodes in current recursion path (recursion stack)

A cycle exists if we encounter a node that is:
- Already visited AND
- Currently in the recursion stack (being processed)

APPROACH:
1. Use DFS with two arrays:
   - vis[]: tracks all visited nodes
   - order[]: tracks nodes in current DFS path (recursion stack)
2. For each unvisited node, start DFS
3. During DFS:
   - Mark node as visited and in current path
   - Recursively visit all neighbors
   - If neighbor is in current path → cycle found
   - After exploring all neighbors, remove from path (backtrack)

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
│ findCycle(v):       │
│ - Mark v visited    │
│ - Add v to path     │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ For each neighbor u │
│ of v                │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Is u visited?       │
└──────┬──────────────┘
       │
      NO│              YES
       │               │
       ▼               ▼
┌─────────────────────┐  ┌─────────────────────┐
│ Recurse on u        │  │ Is u in current     │
│                     │  │ path (order)?       │
└──────┬──────────────┘  └──────┬──────────────┘
       │                        │
       │ Found cycle?       YES │          NO
       │                        │           │
       ▼                        ▼           │
   ┌────────┐           ┌────────────┐     │
   │Return  │           │CYCLE FOUND!│     │
   │True    │           │Return True │     │
   └────────┘           └────────────┘     │
                                           │
       ┌────────────────────────────────────┘
       │
       ▼
┌─────────────────────┐
│ Remove v from path  │
│ (backtrack)         │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Return False        │
└─────────────────────┘

EXAMPLE:
Graph with cycle: 0 → 1 → 2 → 0

DFS(0): vis[0]=T, order[0]=T
  → DFS(1): vis[1]=T, order[1]=T
    → DFS(2): vis[2]=T, order[2]=T
      → Check 0: vis[0]=T AND order[0]=T → CYCLE!

Graph without cycle: 0 → 1 → 2

DFS(0): vis[0]=T, order[0]=T
  → DFS(1): vis[1]=T, order[1]=T
    → DFS(2): vis[2]=T, order[2]=T
      → No more neighbors
    order[2]=F (backtrack)
  order[1]=F (backtrack)
order[0]=F (backtrack)
No cycle found

TIME COMPLEXITY: O(V + E)
- Visit each vertex once
- Explore each edge once

SPACE COMPLEXITY: O(V)
- Two arrays of size V
- Recursion stack up to V depth

INTERVIEW TIPS:
1. Directed graph cycle detection needs recursion stack tracking
2. Undirected graph cycle detection only needs parent tracking
3. The 'order' array is the KEY difference for directed graphs
4. After processing all neighbors, set order[v] = False (backtrack)
5. This algorithm is used in detecting deadlocks and finding topological order
"""

class Solution:
    def findCycle(self, v):
        """
        DFS helper to detect cycle starting from vertex v.

        Args:
            v: Current vertex being explored

        Returns:
            True if cycle detected, False otherwise
        """
        # Mark current vertex as visited
        self.vis[v] = True

        # Add current vertex to recursion stack
        self.order[v] = True

        # Explore all neighbors of current vertex
        for i in self.adj[v]:
            # If neighbor not visited, recursively check for cycle
            if not self.vis[i]:
                conf = self.findCycle(i)
                if conf == True:
                    return True

            # If neighbor is in current recursion path → cycle detected!
            # This means we've reached a node we're currently processing
            elif self.order[i]:
                return True

        # Remove current vertex from recursion stack (backtrack)
        # Important: This allows the node to be part of other paths
        self.order[v] = False

        return False

    def isCyclicDFS(self, V, adj):
        """
        Check if directed graph contains a cycle using DFS.

        Args:
            V: Number of vertices
            adj: Adjacency list of directed graph

        Returns:
            True if cycle exists, False otherwise
        """
        # Track all visited vertices
        self.vis = [False] * (V + 1)

        # Track vertices in current DFS recursion path
        self.order = [False] * (V + 1)

        # Store adjacency list
        self.adj = adj

        # Check for cycle starting from each unvisited vertex
        # (graph may have multiple components)
        for i in range(V):
            if self.vis[i] == False:
                if self.findCycle(i) == True:
                    return True

        return False
