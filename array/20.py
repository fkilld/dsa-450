# Subarray with 0 sum 
# Given an array of positive and negative numbers. 
# Find if there is a subarray (of size at-least one) with 0 sum.

class Solution:
    """
    A class to solve array-based problems.
    """

    def subArrayExists(self, arr, n):
        """
        Check if there is a subarray with sum equal to 0.

        This function uses the prefix sum approach to find a subarray with sum 0.
        We keep track of prefix sums and check if we've seen the same sum before,
        which would indicate that the elements in between sum to zero.

        Args:
            arr (list): An array of integers (positive and negative)
            n (int): Size of the array (not used in the implementation)

        Returns:
            bool: True if there exists a subarray with sum = 0, False otherwise
        """
        # Flag to indicate if subarray with sum 0 exists
        f = 0
        
        # Dictionary to store prefix sums and their occurrence
        m = {}  
        
        # Variable to keep track of the running sum
        s = 0  
        
        # Iterate through each element in the array
        for i in range(len(arr)):
            # Add current element to running sum
            s += arr[i]
            
            # Check for any of the three conditions:
            # 1. If current prefix sum is 0, it means subarray from start to current index sums to 0
            # 2. If current prefix sum was seen before, it means subarray between previous occurrence and now sums to 0
            # 3. If current element itself is 0, it forms a subarray with sum 0
            if s == 0 or s in m or arr[i] == 0:
                # Set flag to indicate subarray found
                f = 1
                break
            else:
                # Store the current prefix sum in the dictionary
                m[s] = 1
        
        # Return True if a subarray with sum 0 was found, False otherwise
        return True if f == 1 else False
    
s = Solution()
arr = [4, 2, -3, 1, 6]  # Example array with a subarray summing to 0
n = len(arr)  # Length of the array
print(s.subArrayExists(arr, n))  # Expected output: True (subarray [4, 2, -3] sums to 0)
