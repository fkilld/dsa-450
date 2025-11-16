"""
PROBLEM: Graph Representation - Adjacency List and Adjacency Matrix

DESCRIPTION:
Implement two common ways to represent a graph:
1. Adjacency List - Space efficient for sparse graphs
2. Adjacency Matrix - Space efficient for dense graphs, faster edge lookup

APPROACH:
1. Adjacency List:
   - Create an array of lists where index represents vertex
   - Each list contains neighbors of that vertex
   - For undirected graph, add edge in both directions

2. Adjacency Matrix:
   - Create a 2D matrix of size V x V
   - matrix[i][j] = 1 if there's an edge between i and j
   - For undirected graph, matrix is symmetric

FLOWCHART (Adjacency List):
┌─────────────────────┐
│   Start             │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Initialize array    │
│ of empty lists      │
│ graph[v+1]          │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ For each edge (x,y) │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Add y to graph[x]   │
│ Add x to graph[y]   │
│ (undirected)        │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Print adjacency     │
│ list for each vertex│
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│   End               │
└─────────────────────┘

TIME COMPLEXITY:
- Adjacency List: O(V + E) space, O(V) to traverse neighbors
- Adjacency Matrix: O(V²) space, O(1) to check edge existence

SPACE COMPLEXITY:
- Adjacency List: O(V + E)
- Adjacency Matrix: O(V²)

INTERVIEW TIPS:
1. Use adjacency list for sparse graphs (E << V²)
2. Use adjacency matrix for dense graphs or when you need O(1) edge lookup
3. Weighted graphs can store weights instead of 1s
"""

from collections import defaultdict

def adjacent_list(v, e):
    """
    Create adjacency list representation of graph.

    Args:
        v: Number of vertices
        e: Number of edges

    Returns:
        Prints adjacency list for each vertex
    """
    # Initialize empty list for each vertex (1-indexed)
    graph = [[] for i in range(v + 1)]

    # Read edges and build adjacency list
    for _ in range(e):
        x, y = [int(x) for x in input("x, y: ").split()]

        # Add edge in both directions (undirected graph)
        graph[x].append(y)
        graph[y].append(x)

    # Display the adjacency list
    for i in range(1, v + 1):
        print(f"{i} -->", *graph[i])

def adjacent_matrix(v, e):
    """
    Create adjacency matrix representation of graph.

    Args:
        v: Number of vertices
        e: Number of edges

    Returns:
        Prints adjacency matrix for graph
    """
    # Initialize V x V matrix with zeros
    graph = [[0 for _ in range(v + 1)] for _ in range(v + 1)]

    # Read edges and mark connections
    for i in range(e):
        x, y = [int(x) for x in input("x, y: ").split()]

        # Mark edge in both directions (undirected graph)
        graph[x][y] = 1
        graph[y][x] = 1

    # Display the adjacency matrix
    for i in range(1, v + 1):
        print(f"{i} ==>", *graph[i])

# Main execution
v, e = [int(x) for x in input("Enter the vertices, edge: ").split()]

# Demonstrate adjacency list representation
print("\nAdjacency List Representation:")
adjacent_list(v, e)

# Demonstrate adjacency matrix representation
print("\nAdjacency Matrix Representation:")
adjacent_matrix(v, e)