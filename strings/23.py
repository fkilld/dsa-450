"""
Find the String in Grid (Word Search in 8 Directions)

PROBLEM:
Given a 2D grid of characters and a word, find all starting positions where the word
appears in the grid. The word can be formed by moving in any of the 8 directions
(horizontal, vertical, and diagonal) from a starting position. Unlike the previous
problem, each direction is followed consistently (no zigzag paths).

WHY THIS APPROACH:
We use Directional Linear Search because:
1. The word must be in a straight line (not zigzag), so we check each direction separately
2. Once we pick a direction, we continue in that direction only (simpler than DFS)
3. We don't need backtracking since cells can be reused (different constraint than problem 22)
4. This is more efficient than DFS when the pattern must be linear
5. Checking 8 directions independently is clearer and easier to debug

ALGORITHM:
1. For each cell (row, column) in the grid:
   a. Check if first character matches word[0]
   b. If not, skip to next cell
2. If first character matches, try all 8 directions:
   a. For each direction (x, y):
      - Start from (row + x, column + y)
      - Check if remaining characters match in this direction
      - If any character doesn't match or goes out of bounds, try next direction
   b. If all characters match in any direction, record this position
3. Return list of all starting positions where word was found

TIME COMPLEXITY: O(m * n * 8 * k) = O(m * n * k) where:
- m, n are grid dimensions
- k is word length
- We check 8 directions, which is constant

SPACE COMPLEXITY: O(1)
- Only storing direction vectors and result list
- No recursion or extra data structures for tracking

EDGE CASES:
1. Word longer than grid dimensions: Returns empty list
2. Word not found: Returns empty list
3. Single character word: Returns all positions with that character
4. Word appears in multiple directions from same cell: Returns cell only once

EXAMPLE:
Grid:
A B C D
E F G H
I J K L

Word: "ABC"
Output: [[0, 0]] (found horizontally starting at position [0,0])
"""

class Solution:
	def find(self, grid, row, column, word):
		"""
		Check if word exists starting from position (row, column) in any of 8 directions

		Args:
			grid: 2D character array
			row: Starting row position
			column: Starting column position
			word: Target word to find

		Returns:
			True if word found in any direction, False otherwise
		"""
		# Early exit: if first character doesn't match, no need to check directions
		if grid[row][column] != word[0]:
			return False

		# Try all 8 directions from this starting position
		for x, y in self.dir:
			# Initialize position for current direction
			# (rd, cd) will move in direction (x, y)
			rd, cd = row + x, column + y
			flag = True  # Assume word can be found in this direction

			# Check remaining characters (first char already matched)
			for k in range(1, len(word)):
				# Validate: position in bounds AND character matches
				if 0 <= rd < self.R and 0 <= cd < self.C and word[k] == grid[rd][cd]:
					# Continue moving in the same direction
					rd += x
					cd += y
				else:
					# Mismatch or out of bounds - try next direction
					flag = False
					break

			# If all characters matched in this direction, word is found
			if flag:
				return True

		# Word not found in any of the 8 directions
		return False
			

	def searchWord(self, grid, word):
		"""
		Main function to find all starting positions where word appears in grid

		Args:
			grid: 2D character array
			word: Target word to search

		Returns:
			List of [row, column] positions where word starts
		"""
		self.R = len(grid)      # Total number of rows
		self.C = len(grid[0])   # Total number of columns

		# Define all 8 possible directions: [row_delta, column_delta]
		# Up, Down, Down-Right, Down-Left, Up-Left, Up-Right, Right, Left
		self.dir = [[-1, 0], [1, 0], [1, 1], [1, -1],
					[-1, -1], [-1, 1], [0, 1], [0, -1]]

		res = []  # Store all starting positions where word is found

		# Check every cell as a potential starting position
		for row in range(self.R):
			for column in range(self.C):
				# If word is found starting from this position, add to result
				if self.find(grid, row, column, word):
					res.append([row, column])

		return res