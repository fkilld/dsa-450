"""
Recursively Print All Sentences from List of Word Lists

PROBLEM DESCRIPTION:
Given a 2D array where each row contains a list of words, print all possible sentences
that can be formed by picking exactly one word from each row.

Example:
Input:
[
  ["you", "we", ""],
  ["have", "are", ""],
  ["sleep", "eat", "drink"]
]

Output:
you have sleep
you have eat
you have drink
you are sleep
you are eat
you are drink
we have sleep
we have eat
we have drink
we are sleep
we are eat
we are drink

This is essentially computing the Cartesian Product of word sets.

WHY THIS APPROACH (Recursive Cartesian Product):
We use RECURSION because:
1. Problem has recursive structure: sentence = word_from_row_0 + sentence_from_remaining_rows
2. Number of rows is variable, making iteration complex
3. Recursion naturally handles:
   - Branching: each word in a row creates a new branch
   - Backtracking: after exploring one word, try next word
   - Variable depth: number of rows determines recursion depth
4. Base case (last row reached) naturally terminates recursion
5. This is a classic backtracking problem structure

ALTERNATIVE APPROACHES (Not Used):
1. Iterative with nested loops: Would need dynamic number of loops (not feasible)
2. Iterative with stack: Possible but more complex to implement
3. Product function (itertools.product): Could work but problem asks for recursive solution

ALGORITHM:
Step 1: Helper Function - print_recur(arr, m, n, output)
   Parameters:
   - arr: 2D array of words
   - m: current row index
   - n: current column index (word chosen from current row)
   - output: array storing current sentence being built

   Base Case (m == row - 1): Reached last row
     - Add arr[m][n] to output
     - Print the complete sentence (output array)
     - Return

   Recursive Case (m < row - 1):
     - Add arr[m][n] to output (current word)
     - For each word in next row (m + 1):
       - If word is not empty:
         - Recursively call print_recur for next row
     - This explores all combinations

Step 2: Main Function - print_all(arr)
   - Initialize output array with 'row' empty strings
   - For each word in first row:
     - If word is not empty:
       - Start recursion with that word

EDGE CASES:
1. Empty array -> no output
2. Single row -> each word is a sentence
3. Empty strings in rows -> skip them (only use non-empty words)
4. All words in a row are empty -> no sentences possible from that path
5. Rows with different number of words -> handle with empty string padding

TIME COMPLEXITY: O(n^m)
- n = average number of words per row
- m = number of rows
- Each word in each row branches to n possibilities in next row
- Total sentences = n^m (Cartesian product)
- Printing each sentence: O(m) words
- Overall: O(m * n^m)

SPACE COMPLEXITY: O(m)
- Recursion depth: O(m) for m rows
- Output array: O(m) to store current sentence
- Overall: O(m)
- Note: If storing all sentences, would be O(m * n^m)

EXAMPLE WALKTHROUGH:
Input:
arr = [
  ["you", "we", ""],
  ["have", "are", ""],
  ["sleep", "eat", "drink"]
]

Execution tree:
Start with row 0:
  Choose "you":
    Row 1, choose "have":
      Row 2, choose "sleep": PRINT "you have sleep"
      Row 2, choose "eat": PRINT "you have eat"
      Row 2, choose "drink": PRINT "you have drink"
    Row 1, choose "are":
      Row 2, choose "sleep": PRINT "you are sleep"
      Row 2, choose "eat": PRINT "you are eat"
      Row 2, choose "drink": PRINT "you are drink"
  Choose "we":
    Row 1, choose "have":
      Row 2, choose "sleep": PRINT "we have sleep"
      ... (similar pattern)

Total sentences: 2 * 2 * 3 = 12 sentences
(2 choices in row 0, 2 in row 1, 3 in row 2)
"""

# Recursively print all sentences that can be formed from list of word lists

def print_recur(arr, m, n, output):
    """
    Recursive helper to build and print sentences.

    Args:
        arr: 2D array of words
        m: Current row index
        n: Current column index (word to use from current row)
        output: Array storing the sentence being built
    """
    # Step 1: Add current word to the sentence at position m
    output[m] = arr[m][n]

    # Step 2: Base case - reached the last row
    if m == row - 1:
        # We have selected one word from each row, print the complete sentence
        for i in range(column):
            print(output[i], end=" ")
        print()  # Newline after sentence
        return

    # Step 3: Recursive case - explore all words in the next row
    # Try each word in the next row (m + 1)
    for i in range(column):
        # Skip empty strings (only use actual words)
        if arr[m + 1][i] != "":
            # Recursively build sentences with this word from next row
            print_recur(arr, m + 1, i, output)


def print_all(arr):
    """
    Main function to print all possible sentences.

    Args:
        arr: 2D array where each row contains words
    """
    # Initialize output array to store one word from each row
    output = [""] * row

    # Start recursion by trying each word in the first row
    for i in range(column):
        # Skip empty strings in first row
        if arr[0][i] != "":
            # Start building sentences with this word as first word
            print_recur(arr, 0, i, output)

# Example usage:
arr = [
    ["you", "we", ""],
    ["have", "are", ""],
    ["sleep", "eat", "drink"]
]

# Global variables for array dimensions
row = len(arr)  # Number of rows (number of word groups)
column = len(arr[0])  # Number of columns (max words per group)

# Generate and print all possible sentences
print_all(arr)