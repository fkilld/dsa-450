# Common elements 
# Given three arrays sorted in increasing order. 
# Find the elements that are common in all three arrays.

class Solution:
    """
    Solution class for finding common elements in three arrays.
    This class implements methods to identify elements that appear in all three given arrays.
    The implementation uses dictionary-based frequency mapping to efficiently track occurrences.
    Methods:
    ---------
    mapping(arr, m): 
        Creates or updates a frequency map for elements in an array.
        Args:
            arr (list): Input array whose elements need to be counted
            m (dict): Dictionary to store the frequency mapping
        Returns:
            dict: Updated frequency map with counts of each element
    commonElements1(a, b, c, n1, n2, n3):
        Finds all common elements present in three arrays.
        The algorithm works by:
        1. Creating frequency maps for all three arrays
        2. Checking elements from first array for presence in all maps
        3. Adding common elements to result while avoiding duplicates
        Args:
            a (list): First input array
            b (list): Second input array
            c (list): Third input array
            n1 (int): Length of first array
            n2 (int): Length of second array
            n3 (int): Length of third array
        Returns:
            list: Sorted list of distinct elements common to all three arrays
        Time Complexity: O(n1 + n2 + n3) - Linear time as we iterate through each array once
        Space Complexity: O(n1 + n2 + n3) - Additional space for the three frequency maps
    """

    # used for mapping the elements
    def mapping(self, arr, m):
        for i in range(len(arr)):
            if arr[i] not in m:
                m[arr[i]] = 1
            else:
                m[arr[i]] += 1
        return m
    
    # Using a map
    # Time -> O(n1+n2+n3) Space -> O(n1 + n2 + n3)
    def commonElements1(self, a, b, c, n1, n2, n3):
        m1, m2, m3 = {}, {}, {} # map used to keep count of characters
        # mapping the elements in a,b and c respectively
        
        m1 = self.mapping(a, m1)
        m2 = self.mapping(b, m2)
        m3 = self.mapping(c, m3)
        
        res = []
        for i in range(n1):
            if a[i] in m1 and a[i] in m2 and a[i] in m3:
                res.append(a[i])
                m1.pop(a[i]) # removing the element from the amp
        
        return res
