# Maximum Product Subarray
# Given an array Arr that contains N integers (may be positive, negative or zero). 
# Find the product of the maximum product subarray

class Solution:
	def max_sum_subarr(self, arr, n):
		"""
		Function to find the maximum product subarray.
		
		Parameters:
		arr (list): The input array containing integers
		n (int): The length of the input array
		
		Returns:
		int: The maximum product of any subarray
		
		Algorithm:
		- We keep track of both maximum and minimum products ending at current position
		- We need minimum product because multiplying a negative number with a negative
		  can give a large positive number
		
		Time Complexity: O(n) - single pass through array
		Space Complexity: O(1) - constant space used
		"""
		# Initialize all three variables with first element
		ma = arr[0]  # Maximum product ending at current index
		mi = arr[0]  # Minimum product ending at current index (could be negative)
		prod = arr[0]  # Overall maximum product found so far
		
		# Iterate through array starting from second element
		for i in range(1, n):
			# If current element is negative, swap max and min
			# This handles sign change when multiplying by negative number
			if arr[i] < 0:
				# When multiplying by negative:
				# - A large positive becomes large negative
				# - A small negative becomes large positive
				ma, mi = mi, ma  # Swap max and min values
			
			# Update maximum product ending at current position
			# Either extend previous subarray or start new one from current element
			ma = max(ma * arr[i], arr[i])
			
			# Update minimum product ending at current position
			# We track minimum because it might become maximum when multiplied by future negative
			mi = min(mi * arr[i], arr[i])
			
			# Update overall maximum product if needed
			if ma > prod:
				prod = ma
				
		# Return maximum product subarray result
		return prod

s = Solution()
arr = [2, 3, -2, 4]  # Example array with both positive and negative numbers
n = len(arr)  # Length of the array
print(s.max_sum_subarr(arr, n))  # Expected output: 6 (subarray [2, 3] has the maximum product of 6)
# arr = [-2, 0, -1]  # Example array with negative numbers and zero