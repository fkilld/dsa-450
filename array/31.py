class Solution:
	def threeWayPartition(self, arr, a, b):
		"""
		Partitions the array into three sections:
		- Elements less than 'a'
		- Elements between 'a' and 'b' (inclusive)
		- Elements greater than 'b'
		
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