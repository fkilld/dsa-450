"""
PROBLEM: Minimum Swaps to Sort
Given an array of n distinct elements, find the minimum number of swaps
required to sort the array in strictly increasing order.

WHY THIS SOLUTION:
Naive approach: Try different swap combinations - exponential complexity!
We use CYCLE DETECTION in graphs to solve optimally.

KEY INSIGHT:
Think of this as a graph problem:
- Each position i points to where arr[i] should go in sorted array
- This creates CYCLES in the graph
- For a cycle of length k, we need (k-1) swaps to sort it
- Total swaps = sum of (cycle_length - 1) for all cycles

Example: arr = [4, 3, 2, 1]
After pairing with indices: [(4,0), (3,1), (2,2), (1,3)]
After sorting by value: [(1,3), (2,2), (3,1), (4,0)]
Graph: 0→3→0 (cycle), 1→1 (no cycle), 2→2 (no cycle)
Wait, let me recalculate:
Position 0 should have 1 (currently at index 3)
Position 1 should have 2 (currently at index 2)
Position 2 should have 3 (currently at index 1)
Position 3 should have 4 (currently at index 0)
Graph: 0→3→0, 1→2→1 forms cycles
Swaps needed: (2-1) + (2-1) = 2

APPROACH:
1. Create pairs: (value, original_index)
2. Sort by value
3. For each unvisited position:
   - Follow the cycle: current position → where it should go → ...
   - Count cycle length
   - Add (cycle_length - 1) to answer
4. Return total swaps

TIME COMPLEXITY: O(n log n)
- Creating pairs: O(n)
- Sorting: O(n log n)
- Cycle detection: O(n) - each element visited once
- Total: O(n log n)

SPACE COMPLEXITY: O(n) - for pairs array and visited dictionary

EXAMPLE: arr = [1, 5, 4, 3, 2]
Pairs: [(1,0), (5,1), (4,2), (3,3), (2,4)]
Sorted: [(1,0), (2,4), (3,3), (4,2), (5,1)]
Position 0: already correct (1 is at index 0)
Position 1: should have value 2 (from index 4) → 1→4→1 (cycle of 2)
  Swaps: 2-1 = 1
Position 2: should have value 3 (from index 3) → 2→3→2 (cycle of 2)
  Swaps: 2-1 = 1
Total swaps: 2

WHY INTERVIEWER WILL ACCEPT:
1. Shows graph thinking for array problems
2. Optimal O(n log n) solution
3. Understanding of permutation cycles
4. Creative problem-solving approach
"""

# Input
# arr = [int(x) for x in input("Enter the array : ").split()]
arr = [1, 5, 4, 3, 2]

def min_swap(arr):
	"""
	Find minimum swaps to sort array using cycle detection.

	Args:
		arr: Array of distinct integers

	Returns:
		Minimum number of swaps needed
	"""
	v = []  # Store (value, original_index) pairs
	n = len(arr)

	# Create pairs of (value, original_index)
	for i in range(n):
		v.append([arr[i], i])

	vis = {k: False for k in range(n)}  # Track visited positions
	ans = 0

	# Sort by value to know where each element should go
	v.sort()

	for i in range(n):
		# Skip if already visited or already in correct position
		if vis[i] or v[i][1] == i:
			continue

		# Find cycle length
		cycle = 0
		j = i

		# Follow the cycle until we return to start
		while not vis[j]:
			vis[j] = True
			j = v[j][1]  # Next position in cycle
			cycle += 1

		# For a cycle of length k, we need (k-1) swaps
		if cycle > 0:
			ans += (cycle - 1)

	return ans

print(min_swap(arr))


