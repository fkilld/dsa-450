# Union of two arrays

# Problem:
# Find the union of two arrays - count the number of distinct elements that appear in either array or both.
# For example, union of [1, 2, 3] and [2, 3, 4] is 4 (distinct elements: 1, 2, 3, 4)

# Solution approach:
# We use a dictionary (hash map) to track which elements we've seen before.
# This gives us O(n+m) time complexity and O(n+m) space complexity in the worst case.

class Solution:
    def union(self, a, n, b, m):
        # a is the first array, n is its length
        # b is the second array, m is its length
        
        # Dictionary to track elements we've already counted
        # Key: the element, Value: 1 (marking that we've seen it)
        occur = {}
        
        # Counter for the total number of unique elements found
        count = 0

        # First, process all elements from array 'a'
        for i in range(n):
            # Check if this element has been seen before
            if a[i] not in occur:
                # If not seen before, mark it as seen in our dictionary
                occur[a[i]] = 1
                # Increment our unique elements counter
                count += 1
                
        # Now, process all elements from array 'b'
        for i in range(m):
            # Check if this element has been seen before (either in array 'a' or earlier in 'b')
            if b[i] not in occur:
                # If not seen before, mark it as seen in our dictionary
                occur[b[i]] = 1
                # Increment our unique elements counter
                count += 1
                
        # Return the total count of unique elements (the union size)
        return count
    
# Create an instance of the Solution class
s = Solution()

# Test arrays
a = [1, 2, 3, 4, 5, 6]  # First array with 6 elements
b = [6, 7, 8, 9, 10, 11]  # Second array with 6 elements (note: 6 appears in both)

# Get the lengths of both arrays
n = len(a)  # Length of first array = 6
m = len(b)  # Length of second array = 6

# Call the union function and print the result
# Expected output: 11 (elements 1,2,3,4,5,6,7,8,9,10,11)
print(s.union(a, n, b, m))  # 11
