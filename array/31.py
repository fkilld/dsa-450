"""
PROBLEM: Three Way Partitioning
=================================
Given an array and a range [a, b], partition the array into three parts:
1. All elements less than 'a' come first
2. All elements in range [a, b] come next
3. All elements greater than 'b' come last

You don't need to maintain the relative order of elements within each partition.

Example:
    Input:  arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32], a = 10, b = 20
    Output: [1, 5, 4, 2, 3, 1, 14, 20, 20, 87, 98, 54, 32]
    Explanation:
        - Elements < 10: [1, 5, 4, 2, 3, 1]
        - Elements in [10, 20]: [14, 20, 20]
        - Elements > 20: [87, 98, 54, 32]

APPROACH: Dutch National Flag Algorithm (Modified for Range)
==============================================================
WHY THIS APPROACH?
- This is an extension of the famous Dutch National Flag problem by Dijkstra
- Instead of partitioning around a single pivot, we partition around a range [a, b]
- Uses three-way partitioning with three pointers: start, i, and end
- In-place partitioning: O(1) extra space
- Single pass: O(n) time complexity

CLASSICAL DNF: Partition around a single value (e.g., sort 0s, 1s, 2s)
THIS PROBLEM: Partition around a range [a, b]

HOW IT WORKS:
1. Use three pointers:
   - start: Position to place next element less than 'a' (grows from left)
   - i: Current element being examined (traversal pointer)
   - end: Position to place next element greater than 'b' (shrinks from right)

2. Three cases for arr[i]:
   - arr[i] < a: Swap with arr[start], increment both i and start
   - arr[i] > b: Swap with arr[end], decrement end only (don't increment i!)
   - a <= arr[i] <= b: Element is in correct region, increment i

3. WHY DON'T WE INCREMENT i WHEN SWAPPING WITH end?
   - When we swap arr[i] with arr[end], we bring an unknown element from the right
   - We don't know if this new element belongs to left, middle, or right partition
   - So we must examine it in the next iteration before moving forward
   - When we swap with start, we know arr[start] is either < a or in [a,b] (already examined)

FLOW EXAMPLE:
=============
Array: [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
Range: a = 10, b = 20
Goal: Partition into [<10] [10-20] [>20]

Initial state:
    start=0, i=0, end=12
    [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
     ^
     s,i                                         e

Step 1: i=0, arr[0]=1 < 10
    Swap arr[0] with arr[0] (same position)
    [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
     i=1, start=1, end=12

Step 2: i=1, arr[1]=14 in [10,20]
    Already in correct region, just move i
    [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
     s     i                                    e

Step 3: i=2, arr[2]=5 < 10
    Swap arr[2] with arr[1]=14
    [1, 5, 14, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
     s     i                                    e
    i=3, start=2

Step 4: i=3, arr[3]=20 in [10,20]
    Already correct, move i
    [1, 5, 14, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
     s        i                                 e

Step 5: i=4, arr[4]=4 < 10
    Swap arr[4] with arr[2]=14
    [1, 5, 4, 20, 14, 2, 54, 20, 87, 98, 3, 1, 32]
     s           i                              e
    i=5, start=3

Step 6: i=5, arr[5]=2 < 10
    Swap arr[5] with arr[3]=20
    [1, 5, 4, 2, 20, 14, 54, 20, 87, 98, 3, 1, 32]
     s              i                           e
    i=6, start=4

Step 7: i=6, arr[6]=54 > 20
    Swap arr[6] with arr[12]=32
    [1, 5, 4, 2, 20, 14, 32, 20, 87, 98, 3, 1, 54]
     s              i                        e
    i stays 6, end=11 (we need to examine 32 next!)

Step 8: i=6, arr[6]=32 > 20
    Swap arr[6] with arr[11]=1
    [1, 5, 4, 2, 20, 14, 1, 20, 87, 98, 3, 32, 54]
     s              i                     e
    i stays 6, end=10 (we need to examine 1 next!)

Step 9: i=6, arr[6]=1 < 10
    Swap arr[6] with arr[4]=20
    [1, 5, 4, 2, 1, 14, 20, 20, 87, 98, 3, 32, 54]
     s                 i                 e
    i=7, start=5

Step 10: i=7, arr[7]=20 in [10,20]
    Already correct, move i
    [1, 5, 4, 2, 1, 14, 20, 20, 87, 98, 3, 32, 54]
     s                      i            e

Step 11: i=8, arr[8]=87 > 20
    Swap arr[8] with arr[10]=3
    [1, 5, 4, 2, 1, 14, 20, 20, 3, 98, 87, 32, 54]
     s                      i         e
    i stays 8, end=9

Step 12: i=8, arr[8]=3 < 10
    Swap arr[8] with arr[5]=14
    [1, 5, 4, 2, 1, 3, 20, 20, 14, 98, 87, 32, 54]
     s                          i      e
    i=9, start=6

Step 13: i=9, arr[9]=98 > 20
    Swap arr[9] with arr[9] (same position)
    [1, 5, 4, 2, 1, 3, 20, 20, 14, 98, 87, 32, 54]
     s                          i   e
    i stays 9, end=8

Step 14: i=9 > end=8, STOP

Final: [1, 5, 4, 2, 1, 3, 20, 20, 14, 98, 87, 32, 54]
    Elements < 10: [1, 5, 4, 2, 1, 3] (indices 0-5)
    Elements in [10, 20]: [20, 20, 14] (indices 6-8)
    Elements > 20: [98, 87, 32, 54] (indices 9-12)

TIME COMPLEXITY:  O(n) - Single pass through array, each element examined at most twice
SPACE COMPLEXITY: O(1) - In-place partitioning using only three pointers
"""

class Solution:
	def threeWayPartition(self, arr, a, b):
		"""
		Partitions the array into three sections using Dutch National Flag algorithm.

		Args:
			arr: Input array to be partitioned
			a: Lower bound of the range
			b: Upper bound of the range

		Returns: None (array is modified in-place)
		"""
		n = len(arr)
		start = 0  # Pointer to track the position for elements less than 'a'
		end = n - 1  # Pointer to track the position for elements greater than 'b'
		i = 0  # Current element pointer for array traversal
		
		while i <= end:
			# Case 1: Current element is less than lower bound 'a'
			if arr[i] < a:
				# Swap current element with element at 'start' position
				arr[i], arr[start] = arr[start], arr[i]
				# Move both pointers forward
				i += 1
				start += 1
				
			# Case 2: Current element is greater than upper bound 'b'
			elif arr[i] > b:
				# Swap current element with element at 'end' position
				arr[i], arr[end] = arr[end], arr[i]
				# Only move 'end' pointer backward
				# We don't increment 'i' because we need to examine the swapped element
				end -= 1
				
			# Case 3: Current element is within the range [a, b]
			else:
				# Element is already in the correct position
				# Just move to the next element
				i += 1