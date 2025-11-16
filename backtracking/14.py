"""
FIND IF THERE IS A PATH OF MORE THAN K LENGTH FROM A SOURCE
============================================================

Problem Statement:
-----------------
Given a weighted undirected graph with V vertices and E edges, and a source
vertex 'src'. Find if there is a path of length more than K from the source
vertex.

A path's length is the sum of weights of all edges in the path.

Example:
--------
Input:
Vertices = 9
Edges: (0,1,4), (0,7,8), (1,2,8), (1,7,11), (2,3,7), (2,8,2), (2,5,4),
       (3,4,9), (3,5,14), (4,5,10), (5,6,2), (6,7,1), (6,8,6), (7,8,7)
Source = 0, K = 60

Output: True
Explanation: One path from 0 of length > 60 exists

Approach:
---------
1. Use Backtracking/DFS to explore all possible paths from source
2. Maintain a path array to track visited nodes (avoid cycles)
3. For each unvisited adjacent node:
   - Mark it as visited (add to path)
   - Recursively explore with updated weight sum
   - If path weight exceeds K, return True
   - Backtrack by marking node as unvisited
4. Return True if any path exceeds K, False otherwise

Key Insight: Need to explore all paths, not just shortest path,
so backtracking is essential.

Time Complexity: O(V!) - In worst case, explore all possible paths
Space Complexity: O(V) - Path array + recursion depth

Flowchart:
----------
```mermaid
graph TD
    A[Start: node=src, k] --> B{k <= 0?}
    B -->|Yes| C[Return True]
    B -->|No| D[For each adjacent node v, w]
    D --> E{Is v not in path?}
    E -->|No| F[Try next adjacent]
    E -->|Yes| G[Mark v as visited]
    G --> H[Recurse: node=v, k=k-w]
    H --> I{Found path > k?}
    I -->|Yes| C
    I -->|No| J[Backtrack: Unmark v]
    J --> F
    F -->|All adjacent tried| K[Return False]
```
"""


class Solution:
    def __init__(self, v):
        """
        Initialize graph with V vertices

        Args:
            v (int): Number of vertices
        """
        self.v = v  # Number of vertices
        # Adjacency list: adj[u] contains list of [v, weight] pairs
        self.adj = [[] for _ in range(v)]

    def addEdge(self, u, v, w):
        """
        Add an undirected weighted edge to the graph

        Args:
            u (int): First vertex
            v (int): Second vertex
            w (int): Weight of edge
        """
        # Since graph is undirected, add edge in both directions
        self.adj[u].append([v, w])
        self.adj[v].append([u, w])

    def pathMoreThanK(self, src, k):
        """
        Check if there exists a path of length more than k from source

        Args:
            src (int): Source vertex
            k (int): Minimum path length required

        Returns:
            bool: True if path of length > k exists, False otherwise
        """
        # Path array to track visited nodes in current path
        # This prevents cycles
        self.path = [False] * self.v

        # Mark source as visited
        self.path[src] = True

        # Start DFS from source
        return self.solve(src, k)

    def solve(self, node, k):
        """
        Recursive backtracking function to find path of length > k

        Args:
            node (int): Current node
            k (int): Remaining length needed

        Returns:
            bool: True if path of length > k found, False otherwise
        """
        # Base Case: If k becomes <= 0, we found a path of required length
        if k <= 0:
            return True

        # Explore all adjacent nodes
        for v, w in self.adj[node]:
            # If adjacent node 'v' is not in current path
            if not self.path[v]:
                # Mark node 'v' as visited
                self.path[v] = True

                # Recursively check if we can find path from v
                # with remaining length k - w
                # BUG FIX: Added return statement to properly propagate result
                if self.solve(v, k - w):
                    return True

                # Backtracking: Unmark node 'v' for other paths
                self.path[v] = False

        # No path of required length found from this node
        return False


# Example Usage and Test Cases
if __name__ == "__main__":
    # Test Case 1: Graph with path > k
    print("Test Case 1:")
    graph1 = Solution(9)

    # Add edges (vertex1, vertex2, weight)
    graph1.addEdge(0, 1, 4)
    graph1.addEdge(0, 7, 8)
    graph1.addEdge(1, 2, 8)
    graph1.addEdge(1, 7, 11)
    graph1.addEdge(2, 3, 7)
    graph1.addEdge(2, 8, 2)
    graph1.addEdge(2, 5, 4)
    graph1.addEdge(3, 4, 9)
    graph1.addEdge(3, 5, 14)
    graph1.addEdge(4, 5, 10)
    graph1.addEdge(5, 6, 2)
    graph1.addEdge(6, 7, 1)
    graph1.addEdge(6, 8, 6)
    graph1.addEdge(7, 8, 7)

    src1 = 0
    k1 = 60
    result1 = graph1.pathMoreThanK(src1, k1)
    print(f"Source: {src1}, K: {k1}")
    print(f"Path of length > {k1} exists: {result1}")

    # Test Case 2: Smaller k value
    print("\n\nTest Case 2:")
    src2 = 0
    k2 = 20
    result2 = graph1.pathMoreThanK(src2, k2)
    print(f"Source: {src2}, K: {k2}")
    print(f"Path of length > {k2} exists: {result2}")

    # Test Case 3: Simple linear graph
    print("\n\nTest Case 3:")
    graph3 = Solution(4)
    graph3.addEdge(0, 1, 5)
    graph3.addEdge(1, 2, 6)
    graph3.addEdge(2, 3, 7)

    src3 = 0
    k3 = 15
    result3 = graph3.pathMoreThanK(src3, k3)
    print(f"Linear graph: 0-1-2-3 with weights 5,6,7")
    print(f"Source: {src3}, K: {k3}")
    print(f"Path of length > {k3} exists: {result3}")
    print(f"Explanation: Path 0->1->2->3 has length 5+6+7=18 > 15")

    # Test Case 4: Graph with cycle
    print("\n\nTest Case 4:")
    graph4 = Solution(4)
    graph4.addEdge(0, 1, 3)
    graph4.addEdge(1, 2, 4)
    graph4.addEdge(2, 3, 5)
    graph4.addEdge(3, 0, 2)  # Creates cycle

    src4 = 0
    k4 = 10
    result4 = graph4.pathMoreThanK(src4, k4)
    print(f"Graph with cycle")
    print(f"Source: {src4}, K: {k4}")
    print(f"Path of length > {k4} exists: {result4}")

    # Test Case 5: No path exists
    print("\n\nTest Case 5:")
    graph5 = Solution(3)
    graph5.addEdge(0, 1, 2)
    graph5.addEdge(1, 2, 3)

    src5 = 0
    k5 = 100
    result5 = graph5.pathMoreThanK(src5, k5)
    print(f"Simple graph with total path length = 5")
    print(f"Source: {src5}, K: {k5}")
    print(f"Path of length > {k5} exists: {result5}")
    print("Explanation: Maximum possible path length is 5, cannot exceed 100")
