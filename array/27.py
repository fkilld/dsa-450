class Solution:
    # Function to find if there exists a triplet in the array A[] which sums up to X.
    def find3Numbers(self, arr, n, X):
        # Step 1: Sort the array to enable the two-pointer approach
        arr.sort()
        
        # Step 2: Iterate through the array for the first element of triplet
        # We only need to go up to n-3 as we need at least 2 more elements after i
        for i in range(n - 2):
            # Step 3: Initialize two pointers for the remaining elements
            j = i + 1      # Left pointer (starts right after current element)
            k = n - 1      # Right pointer (starts at the end of array)
            
            # Step 4: Use the two-pointer technique to find the other two elements
            while j < k:
                current_sum = arr[i] + arr[j] + arr[k]
                
                # If we found the target sum, return True immediately
                if current_sum == X:
                    return True
                
                # If current sum is less than target X, move left pointer right to increase sum
                elif current_sum < X:
                    j += 1
                
                # If current sum is greater than target X, move right pointer left to decrease sum
                else:  # current_sum > X
                    k -= 1
        
        # Step 5: If we've checked all possible triplets and found none, return False
        return False