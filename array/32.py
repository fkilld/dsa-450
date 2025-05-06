def minSwap(arr, n, k):
    """
    Find the minimum number of swaps required to bring all the numbers less than or equal to k together.
    
    Args:
        arr: List of positive integers
        n: Length of the array
        k: The given number
        
    Returns:
        Minimum number of swaps required
    """
    # Step 1: Count the number of elements less than or equal to k
    # This tells us the size of the contiguous subarray we're trying to form
    count = 0 
    for i in range(n):
        if arr[i] <= k:
            count += 1
    
    # Step 2: Count the number of elements greater than k in the first window of size 'count'
    # These are the elements that would need to be swapped out of this window
    bad = 0 
    for i in range(count):
        if arr[i] > k:
            bad += 1
    
    # Step 3: Initialize the minimum number of swaps required
    min_swaps = bad
    
    # Step 4: Slide the window of size 'count' through the array
    # We check each possible position to find where minimum swaps would be needed
    for i in range(1, n - count + 1):
        # Remove contribution of the element leaving the window
        if arr[i - 1] > k:
            bad -= 1
            
        # Add contribution of the element entering the window
        if arr[i + count - 1] > k:
            bad += 1
            
        # Update the minimum swaps count if current window has fewer "bad" elements
        min_swaps = min(min_swaps, bad)
    
    return min_swaps
