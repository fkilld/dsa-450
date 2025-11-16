"""
Count of Number of Given String in 2D Character Array

PROBLEM:
Given a 2D grid of characters and a target string, find the total number of occurrences
of the string in the grid. The string can be formed by moving in 4 directions (up, down,
left, right) from any starting position. Each cell can be used only once per path.

WHY THIS APPROACH:
We use DFS (Depth-First Search) with Backtracking because:
1. We need to explore all possible paths from each starting position
2. We must track which cells are already used in the current path (to avoid reuse)
3. Backtracking allows us to restore the grid state after exploring each path
4. DFS naturally explores one complete path before trying alternatives
5. This is more memory-efficient than BFS for this problem since we only care about
   counting valid paths, not finding shortest paths

ALGORITHM:
1. Try starting from each cell in the grid (nested loops)
2. For each starting position, call DFS solve() function:
   a. Check if current position is valid and matches current character in string
   b. Mark current cell as visited (set to 0) to prevent reuse in same path
   c. If we've matched all characters (idx == len(string)), found one occurrence
   d. Otherwise, recursively explore all 4 directions
   e. Backtrack: restore cell's original value for other paths to use
3. Sum up all valid paths found from all starting positions

TIME COMPLEXITY: O(m * n * 4^k) where:
- m, n are grid dimensions
- k is the length of target string
- For each cell, we explore up to 4^k paths in worst case

SPACE COMPLEXITY: O(k)
- Recursion stack depth equals string length k
- Grid is modified in-place (no extra space for visited tracking)

EDGE CASES:
1. String longer than total cells: Returns 0
2. String not present in grid: Returns 0
3. Single character string: Returns count of that character in grid
4. Multiple overlapping paths: All are counted separately

EXAMPLE:
Grid:
D D D G D D
B B D E B S
B S K E B K
D D D D D E
D D D D D E
D D D D D G

String: "GEEKS"
Output: 2 (can be found in 2 different paths)
"""

def solve(row, column, string, ch, idx):
    """
    DFS function to find occurrences of string starting from position (row, column)

    Args:
        row: Current row position in grid
        column: Current column position in grid
        string: Target string to find
        ch: 2D character grid
        idx: Current index in string being matched

    Returns:
        Count of valid paths from this position
    """
    found = 0  # Counter for valid paths found from this position

    # Validate: position is within bounds AND current character matches
    if row >= 0 and column >= 0 and row < len(ch) and column < len(ch[0]) and string[idx] == ch[row][column]:
        # Save current character for backtracking
        temp = string[idx]

        # Mark cell as visited by setting to 0 (prevents reuse in current path)
        ch[row][column] = 0

        # Move to next character in target string
        idx += 1

        # Base case: we've matched all characters in the string
        if idx == len(string):
            found = 1
        else:
            # Recursive case: explore all 4 directions and sum up valid paths
            found += solve(row + 1, column, string, ch, idx)  # Down
            found += solve(row - 1, column, string, ch, idx)  # Up
            found += solve(row, column + 1, string, ch, idx)  # Right
            found += solve(row, column - 1, string, ch, idx)  # Left

        # Backtrack: restore original character so other paths can use this cell
        ch[row][column] = temp

    return found

# ==================== Driver code ====================
# Example grid with characters
ch = [['D','D','D','G','D','D'],
     ['B','B','D','E','B','S'],
     ['B','S','K','E','B','K'],
     ['D','D','D','D','D','E'],
     ['D','D','D','D','D','E'],
     ['D','D','D','D','D','G']]

# Target string to find in the grid
string = 'GEEKS'
size = len(string)
matrix_size = len(ch)

# Try starting from every cell in the grid
ans = 0
for i in range(6):
    for j in range(6):
        # i, j => starting position in 2D grid
        # Last parameter (0) => start matching from first character of string
        ans += solve(i, j, string, ch, 0)

print(ans)  # Output: Total number of times string can be found