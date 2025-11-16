"""
PROBLEM: Check if a Given Graph is a Tree
===========================================

Given an undirected graph with V vertices, determine if it forms a valid tree.

A graph is a tree if and only if:
1. It is connected (all vertices reachable from any vertex)
2. It has no cycles
3. It has exactly V-1 edges (for V vertices)

Example 1 (Is Tree):
    Input: V=5, edges=[(1,0), (0,2), (0,3), (3,4)]
    Graph:
        1---0---2
            |
            3
            |
            4
    Output: True (Connected, no cycles)

Example 2 (Not Tree - Has Cycle):
    Input: V=5, edges=[(1,0), (0,2), (2,1), (0,3), (3,4)]
    Graph:
        1---0---2
        |   |   |
        +---+   (cycle)
            |
            3---4
    Output: False (Has cycle 0-1-2-0)

APPROACH & REASONING:
====================
Use DFS to check for:
1. Cycles (using parent tracking)
2. Connectivity (all vertices visited)

WHY DFS?
- Can detect cycles during traversal
- Can check connectivity in single pass
- Parent tracking prevents false cycle detection

KEY INSIGHT:
- Tree properties: Connected + Acyclic
- DFS visits all connected vertices
- If any vertex unvisited → disconnected → not a tree
- If we see visited vertex (not parent) → cycle → not a tree

ALGORITHM STEPS:
1. Create adjacency list representation
2. Start DFS from vertex 0 with parent -1
3. For each vertex:
   - Mark as visited
   - For each neighbor:
     - If not visited: recurse
     - If visited and not parent: cycle detected
4. After DFS, check if all vertices visited

FLOWCHART:
    [DFS from 0] → [Check cycles] → [Check all visited] → [Return result]

TIME COMPLEXITY: O(V + E) - visit all vertices and edges
SPACE COMPLEXITY: O(V) - visited array + recursion

INTERVIEW TIPS:
- Explain tree properties clearly
- Discuss parent tracking for cycle detection
- Mention edge count property (V-1 edges)
- Compare with Union-Find approach
"""

from collections import defaultdict

class Graph:
    def __init__(self, V) -> None:
        """
        Initialize graph with V vertices.

        Args:
            V: Number of vertices
        """
        self.V = V
        self.graph = defaultdict(list)  # Adjacency list

    def addEdge(self, v, w):
        """
        Adds an undirected edge between v and w.

        Args:
            v: First vertex
            w: Second vertex
        """
        # Add edge v-w (undirected, so add both directions)
        self.graph[v].append(w)
        self.graph[w].append(v)

    def isCyclic(self, v, visited, parent):
        """
        Detects cycle using DFS with parent tracking.

        Args:
            v: Current vertex
            visited: Array tracking visited vertices
            parent: Parent vertex in DFS tree

        Returns:
            bool: True if cycle detected, False otherwise

        Time: O(V+E), Space: O(V)
        """
        # STEP 1: Mark current vertex as visited
        visited[v] = True

        # STEP 2: Visit all neighbors
        for i in self.graph[v]:
            # CASE 1: Neighbor not visited → recurse
            if visited[i] == False:
                # If subtree has cycle, propagate True upward
                if self.isCyclic(i, visited, v) == True:
                    return True

            # CASE 2: Neighbor visited and not parent → cycle found!
            # This means we found a back edge (edge to ancestor)
            elif i != parent:
                return True

        # STEP 3: No cycle found in this subtree
        return False

    def isTree(self):
        """
        Checks if graph is a valid tree.

        Returns:
            bool: True if tree, False otherwise

        Time: O(V+E), Space: O(V)
        """
        # STEP 1: Initialize all vertices as not visited
        visited = [False] * self.V

        # STEP 2: Check for cycles starting from vertex 0
        # Parent is -1 (no parent for root)
        if self.isCyclic(0, visited, -1):
            return False  # Has cycle → not a tree

        # STEP 3: Check connectivity - all vertices must be visited
        # If any vertex not visited → graph is disconnected → not a tree
        for i in range(self.V):
            if visited[i] == False:
                return False

        # STEP 4: Connected + No cycles = Tree!
        return True


# Driver Program
g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(0, 3)
g1.addEdge(3, 4)

if g1.isTree():
    print("It is a tree")
else:
    print("It is not a tree")

g2 = Graph(5)
g2.addEdge(1, 0)
g2.addEdge(0, 2)
g2.addEdge(2, 1)  # Creates cycle: 0-1-2-0
g2.addEdge(0, 3)
g2.addEdge(3, 4)

if g2.isTree():
    print("It is a tree")
else:
    print("It is not a tree")
