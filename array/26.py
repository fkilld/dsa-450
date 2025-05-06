# Array Subset of another array problem solution
# Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m
# Task: Check if a2[] is a subset of a1[] or not

def isSubset(a1, a2, n, m):
    """
    Function to check if array a2 is a subset of array a1
    
    Args:
        a1: First array of size n
        a2: Second array of size m
        n: Size of array a1
        m: Size of array a2
        
    Returns:
        "Yes" if a2 is a subset of a1, "No" otherwise
    """
    # Create a hash map to store elements of a1
    # Using a dictionary for O(1) lookup time
    hash_map = {}
    
    # Populate the dictionary with elements from a1
    # Each element becomes a key with value 1
    for i in range(n):
        hash_map[a1[i]] = 1
    
    # Counter to track how many elements of a2 are found in a1
    found_count = 0
    
    # Check each element of a2
    for i in range(m):
        # If current element exists in our hash_map, increment the counter
        if a2[i] in hash_map:
            found_count += 1
    
    # If all elements of a2 are found in a1, then a2 is a subset
    # This is true when found_count equals m (size of a2)
    return "Yes" if found_count == m else "No"