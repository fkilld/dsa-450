"""
PROBLEM: Construct Binary Tree from String with Bracket Representation
========================================================================

Given a string representation of a binary tree with bracket notation,
construct the actual binary tree.

Format: root(left_subtree)(right_subtree)
- Numbers are single digits (0-9)
- Each subtree is enclosed in parentheses
- Empty subtree is represented by ()

Example 1:
    Input: "4(2(3)(1))(6(5))"

    Tree Structure:
           4
         /   \
        2     6
       / \   /
      3   1 5

    Output: Preorder = 4 2 3 1 6 5

Example 2:
    Input: "1(2)(3)"

    Tree Structure:
           1
         /   \
        2     3

    Output: Preorder = 1 2 3

APPROACH & REASONING:
====================
Parse the string recursively using bracket matching.

WHY THIS APPROACH?
- String format mirrors tree structure (parent before children)
- Brackets define subtree boundaries
- Recursive structure matches tree structure

KEY INSIGHT:
- Find matching closing bracket for each opening bracket
- First '(' after root encloses left subtree
- Second '(' after left subtree encloses right subtree
- Use stack to match brackets

ALGORITHM STEPS:
1. Extract root value from first character
2. Find first '(' - marks start of left subtree
3. Find matching ')' for left subtree
4. Recursively build left subtree from substring
5. Recursively build right subtree from remaining substring
6. Return constructed node

FLOWCHART:
         START
           |
           v
    <start > end?>----YES----> [Return None]
           |
          NO
           |
           v
    [Create node with string[start]]
           |
           v
    [Find matching bracket for left subtree]
           |
           v
    <index found?>----YES----> [Build left subtree recursively]
           |                          |
          NO                          |
           |<------------------------
           v
    [Build right subtree if exists]
           |
           v
    [Return node]

TIME COMPLEXITY: O(N²) where N is string length
    - findIdx is O(N) for each character
    - Called recursively for each node
    - Total: O(N²) in worst case

SPACE COMPLEXITY: O(N)
    - Recursion depth equals tree height
    - Stack for bracket matching

INTERVIEW TIPS:
- Explain bracket matching using stack
- Discuss how to handle empty subtrees
- Mention optimization to O(N) with preprocessing
- Compare with other tree construction methods
- Common follow-up: Construct from other formats (level-order, etc.)
"""

class Node:
    def __init__(self, data) -> None:
        """
        Node structure for binary tree.

        Args:
            data: Integer value stored in node
        """
        self.data = data
        self.left = self.right = None


class Solution_1:
    """O(n²) solution using bracket matching"""

    def findIdx(self, string, start, end):
        """
        Finds the closing bracket that matches opening bracket at start.

        Uses stack to track nested brackets.

        Args:
            string: Input string with bracket notation
            start: Index of opening bracket
            end: End of search range

        Returns:
            int: Index of matching closing bracket, -1 if not found

        Time Complexity: O(N) - scan substring once
        """
        # EDGE CASE: Invalid range
        if start > end:
            return -1

        # STEP 1: Initialize stack for bracket matching
        stack = []

        # STEP 2: Scan from start to end
        for i in range(start, end + 1):
            # STEP 3: If opening bracket, push to stack
            if string[i] == '(':
                stack.append(string[i])

            # STEP 4: If closing bracket
            elif string[i] == ")":
                # Pop the matching opening bracket
                stack.pop()

                # STEP 5: If stack is empty, we found the matching bracket
                # This closing bracket matches the first opening bracket
                if len(stack) == 0:
                    del stack  # Clean up
                    return i

        # STEP 6: No matching bracket found
        del stack
        return -1

    def buildTreeFromString(self, string, start, end):
        """
        Recursively builds binary tree from string representation.

        Args:
            string: Input string with bracket notation
            start: Start index of current subtree
            end: End index of current subtree

        Returns:
            Node: Root of constructed subtree

        Time Complexity: O(N²) - findIdx called for each node
        """
        # BASE CASE: Invalid range
        if start > end:
            return

        # STEP 1: Create node with first character (root of this subtree)
        # Convert character digit to integer
        curr = Node(ord(string[start]) - ord('0'))

        # STEP 2: Initialize index to track left subtree position
        index = -1

        # STEP 3: Check if left subtree exists
        # Left subtree starts at start+1 if there's an opening bracket
        if start + 1 <= end and string[start + 1] == '(':
            # Find the matching closing bracket for left subtree
            index = self.findIdx(string, start + 1, end)

        # STEP 4: If left subtree exists, build it recursively
        if index != -1:
            # Build left subtree: skip outer brackets (start+2 to index-1)
            curr.left = self.buildTreeFromString(string, start + 2, index - 1)

            # Build right subtree: starts after left subtree's closing bracket
            # Skip the opening bracket (index+2) and ending bracket (end-1)
            curr.right = self.buildTreeFromString(string, index + 2, end - 1)

        # STEP 5: Return constructed node
        return curr

    def preorder(self, root):
        """
        Prints preorder traversal (for verification).

        Args:
            root: Root of binary tree
        """
        if root is None:
            return

        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)


# O(n) solution placeholder
class Solution_2:
    """
    O(N) solution can be implemented using:
    - Single pass with index tracking
    - Avoid repeated bracket matching
    - Use iterative approach with stack
    """
    pass


# Driver code
s = Solution_1()
string = "4(2(3)(1))(6(5))"

# Build tree from string
root = s.buildTreeFromString(string, 0, len(string) - 1)

# Print preorder traversal
# Expected output: 4 2 3 1 6 5
s.preorder(root)
