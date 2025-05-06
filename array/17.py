# Count pairs with given sum 
# Given an array of N integers, and an integer K,
# find the number of pairs of elements in the array whose sum is equal to K.

class Solution:
    """
    Count the number of pairs in an array that sum to a given value.
    This class provides a solution to find the count of pairs of elements in an array
    that sum up to a specified value k. The implementation uses a hash map (dictionary)
    to track the frequency of each element, allowing for O(n) time complexity.
    Example:
        arr = [1, 5, 7, 1]
        n = 4
        k = 6
        Solution().getPairsCount(arr, n, k) returns 2 (pairs: (1,5) and (5,1))
    Attributes:
        None
    Methods:
        getPairsCount(arr, n, k): Counts pairs in array that sum to k
    """
    """
            Count the number of pairs in the array that sum up to k.
            Algorithm:
            1. Create a frequency map for all elements in the array
            2. For each element arr[i], check if (k - arr[i]) exists in the map
            3. Add the frequency of (k - arr[i]) to the count
            4. Adjust count if arr[i] equals (k - arr[i]) to avoid counting the element with itself
            5. Return count/2 since each pair is counted twice
            Args:
                arr (list): The input array of integers
                n (int): Size of the array
                k (int): Target sum value
            Returns:
                int: Number of pairs in the array that sum to k
            Time Complexity: O(n) - The array is traversed twice
            Space Complexity: O(n) - In worst case, all elements are unique
            """
    def getPairsCount(self, arr, n, k):
        m = {}
        count = 0
        # counting the occurence of each element
        for i in range(n):
            if arr[i] not in m: # if the element occurs for the first time
                m[arr[i]] = 1
            else: # if it is recurring
                m[arr[i]] += 1
        
        # counting pairs
        for i in range(n):
            x = k - arr[i]
            if x in m: # if the element exists in the map
                count += m[x] # since the current element would be paired with every ouccurence of x

                if x == arr[i]: # if x and arr[i] are same then it is the same pair
                    count -= 1

        return count // 2


s = Solution()
arr = [1, 5, 7, 1] # Example array
n = len(arr) # Length of the array
k = 6 # Target sum
print(s.getPairsCount(arr, n, k)) # Expected output: 2 (pairs: (1,5) and (5,1))
# The output will be 2, as there are two pairs (1,5) and (5,1) that sum to 6.
