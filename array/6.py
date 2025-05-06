# Cyclically rotate an array by one 
# Given an array, rotate the array by one position in clock-wise direction.

def rotate(arr, n):
    # This function rotates an array of size n by one position clockwise
    # Parameters: arr (the input array), n (size of the array)
    
    last = arr[n-1] # Store the last element of the array in variable 'last' because it will be moved to the front
    
    for i in range(n-2, -1, -1): # Loop from second-last element (n-2) to first element (0) in reverse order
                                 # We use reverse order to avoid overwriting elements before they're moved
                                 # The -1 step makes the loop decrement i in each iteration
        
        arr[i + 1] = arr[i] # Move each element one position forward (to the right)
                            # This overwrites the next position with current element
                            # This creates space at index 0 for the last element
    
    arr[0] = last # Place the stored last element at the first position (index 0)
                  # This completes the cyclic rotation by one position clockwise
    
    return arr # Return the rotated array back to the caller

rotated_array = rotate([1, 2, 3, 4, 5], 5) # Call the function with an example array and its size
print(rotated_array) # Print the rotated array to verify the result