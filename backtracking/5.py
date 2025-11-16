"""
M-COLORING PROBLEM
==================

Problem Statement:
-----------------
Given an undirected graph and an integer M, determine if the graph can be
colored with at most M colors such that no two adjacent vertices have the
same color. This is the famous graph coloring problem.

Example:
--------
Input:
N = 4 (vertices numbered 0 to 3)
M = 3 (colors available: 1, 2, 3)
Edges: (0,1), (1,2), (2,3), (3,0), (0,2)

Graph representation:
  0 -- 1
  |\ / |
  | X  |
  |/ \ |
  3 -- 2

Output: True
Explanation: We can color it as: 0->1, 1->2, 2->3, 3->2

Approach:
---------
1. Try assigning colors from 1 to M to each vertex
2. Before assigning a color, check if it's safe:
   - Check all adjacent vertices
   - If any adjacent vertex has same color, not safe
3. If safe, assign color and move to next vertex
4. Recursively try to color remaining vertices
5. If coloring succeeds, return True
6. If not, backtrack (remove color) and try next color
7. If no color works, return False

Time Complexity: O(M^V) where V is number of vertices
Space Complexity: O(V) for color array and recursion stack

Flowchart:
----------
```mermaid
graph TD
    A[Start: node=0] --> B{node == V?}
    B -->|Yes| C[All nodes colored - Return True]
    B -->|No| D[Try colors 1 to M]
    D --> E{Is color valid?}
    E -->|No| F[Try next color]
    E -->|Yes| G[Assign color to node]
    G --> H[Recurse: color node+1]
    H --> I{Coloring successful?}
    I -->|Yes| C
    I -->|No| J[Backtrack: Remove color]
    J --> F
    F -->|All colors tried| K[Return False]
```
"""


def graphColoring(graph, V, m):
    """
    Main function to check if graph can be colored with m colors

    Args:
        graph (list): Adjacency matrix representation of graph
        V (int): Number of vertices
        m (int): Number of colors available

    Returns:
        bool: True if graph can be colored, False otherwise
    """
    # Array to store color assigned to each vertex
    # 0 means no color assigned yet
    color = [0] * V

    # Start coloring from vertex 0
    if solve(0, V, m, graph, color):
        return True

    return False


def solve(node, V, m, graph, color):
    """
    Recursive backtracking function to color the graph

    Args:
        node (int): Current node to color
        V (int): Total number of vertices
        m (int): Number of colors available
        graph (list): Adjacency matrix
        color (list): Array storing color of each node

    Returns:
        bool: True if coloring possible from this state
    """
    # Base Case: All nodes have been colored successfully
    if node == V:
        return True

    # Try assigning each color from 1 to m
    for c in range(1, m + 1):
        # Check if assigning color 'c' to current node is valid
        if isValid(node, c, V, graph, color):
            # Assign color c to current node
            color[node] = c

            # Recursively color remaining nodes
            if solve(node + 1, V, m, graph, color):
                return True  # Found valid coloring

            # Backtracking: Current color assignment didn't work
            # Remove color and try next color
            color[node] = 0

    # No color from 1 to m worked for this node
    return False


def isValid(node, c, V, graph, color):
    """
    Check if assigning color 'c' to 'node' is valid

    Args:
        node (int): Current node
        c (int): Color to assign
        V (int): Number of vertices
        graph (list): Adjacency matrix
        color (list): Current color assignment

    Returns:
        bool: True if assignment is valid, False otherwise
    """
    # Check all other vertices
    for i in range(V):
        # If there's an edge between node and i
        # AND vertex i already has color c
        # Then assigning c to node would violate constraint
        if graph[node][i] == 1 and color[i] == c:
            return False

    # No adjacent vertex has color c, so it's safe
    # BUG FIX: This should return True, not False!
    return True


# Example Usage and Test Cases
if __name__ == "__main__":

    # Test Case 1: Simple graph
    print("Test Case 1:")
    V1 = 4
    graph1 = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    m1 = 3
    if graphColoring(graph1, V1, m1):
        print(f"Graph can be colored with {m1} colors")
    else:
        print(f"Graph cannot be colored with {m1} colors")

    # Test Case 2: Complete graph K4 needs 4 colors
    print("\nTest Case 2:")
    V2 = 4
    graph2 = [
        [0, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 0]
    ]
    m2 = 3  # Complete graph K4 needs 4 colors
    if graphColoring(graph2, V2, m2):
        print(f"Graph can be colored with {m2} colors")
    else:
        print(f"Graph cannot be colored with {m2} colors")

    # Test Case 3: Bipartite graph needs only 2 colors
    print("\nTest Case 3:")
    V3 = 4
    graph3 = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    m3 = 2  # Bipartite needs only 2 colors
    if graphColoring(graph3, V3, m3):
        print(f"Graph can be colored with {m3} colors")
    else:
        print(f"Graph cannot be colored with {m3} colors")
