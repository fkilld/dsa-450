# Problem: Find the smallest subarray with sum greater than a given value x
# Time Complexity: O(n) where n is the length of the array
# Space Complexity: O(1) as we only use a constant amount of extra space

class Solution:
    def sb(self, arr, n, x):
        # Initialize min_len to n+1 which is greater than any possible subarray length
        # This helps identify if no solution exists
        min_len = n + 1
        
        # Running sum of the current window
        curr_sum = 0

        # Two-pointer technique (sliding window)
        i = 0  # Start index of the current window
        j = 0  # End index of the current window

        while j < n:
            # Phase 1: Expand the window by adding elements from the right
            # until sum exceeds x or we reach the end of array
            while curr_sum <= x and j < n:
                curr_sum += arr[j]  # Add current element to window sum
                j += 1              # Move right pointer forward
            
            # Phase 2: Shrink the window from the left and update minimum length
            # while maintaining the sum > x condition
            while curr_sum > x and i < j:
                # Current window size is j-i, if smaller than min_len, update it
                min_len = min(min_len, j - i)
                
                # Remove leftmost element from sum
                curr_sum -= arr[i]
                i += 1  # Move left pointer forward
        
        # If min_len is still n+1, it means no subarray found with sum > x
        return min_len if min_len <= n else 0

# Solution Walkthrough:
# 1. We use a sliding window approach with two pointers i and j
# 2. Expand the window by adding elements until the sum exceeds x
# 3. Once sum > x, we have a valid window, so update min_len if needed
# 4. Then try to shrink the window from the left to find smaller valid windows
# 5. Repeat until we process the entire array
# 6. Return the minimum window size or 0 if no solution exists