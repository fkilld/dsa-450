# Kadane's Algorithm: An efficient algorithm to find the maximum sum of a contiguous subarray in a one-dimensional array
# Given an array arr of N integers. Find the contiguous sub-array with maximum sum

class Solution:
    # Method that implements Kadane's algorithm to find maximum subarray sum
    def max_subarray_sum(self, arr):
        # Initialize max_int to negative infinity to handle arrays with all negative numbers
        max_int = float('-inf')  # Using float('-inf') as it's smaller than any possible sum we might encounter
        
        # Initialize max_till_here to track the maximum sum ending at current position
        max_till_here = 0  # Start with 0 since empty subarrays are allowed with sum 0
        
        # Loop through each element in the array to calculate running sums
        for i in range(len(arr)):
            # Add current element to the running sum to extend current subarray
            max_till_here += arr[i]
            
            # If current running sum is greater than our global maximum, update the global maximum
            if max_till_here > max_int:
                max_int = max_till_here  # This represents the best subarray sum found so far
            
            # Key insight of Kadane's algorithm: if sum becomes negative, discard the current subarray
            # A negative sum will only reduce future subarrays' sums, so better to start fresh
            if max_till_here < 0:
                max_till_here = 0  # Reset to 0 to start a new potential subarray from next element
        
        # Return the maximum subarray sum found throughout the entire array traversal
        return max_int
s = Solution()
arr = [-2, -3, 4, -1, -2, 1, 5, -3]  # Example array with both positive and negative numbers
print(s.max_subarray_sum(arr))  # Expected output: 7 (subarray [4, -1, -2, 1, 5] has the maximum sum of 7)