# Rearrange array in alternating positive & negative items with O(1) extra space

def arrange(arr, n):
    """
    Rearranges array elements so that positive and negative elements appear alternately.
    
    Args:
        arr (list): The input array containing positive and negative elements
        n (int): Length of the array
    
    Returns:
        None: Modifies the array in-place
    """
    # First phase: Segregate negative elements to the left and positive to the right
    i = 0  # Pointer starting from the beginning of the array
    j = n - 1  # Pointer starting from the end of the array

    while i <= j:
        if arr[i] < 0 and arr[j] > 0:
            # If element at i is negative and element at j is positive, swap them
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif arr[i] > 0 and arr[j] < 0:
            # If element at i is positive and element at j is negative, both are in wrong positions
            # but swapping would not help, so just move both pointers
            i += 1
            j -= 1
        elif arr[i] > 0:
            # If element at i is positive, it's in wrong position, move forward
            i += 1
        elif arr[j] < 0:
            # If element at j is negative, it's in wrong position, move backward
            j -= 1
    
    print(*arr)  # Print the array after segregation phase
    
    # Second phase: Rearrange to alternate positive and negative elements
    if i == 0 or i == n:
        # If either all elements are negative (i == 0) or all are positive (i == n)
        # No further rearrangement needed
        print(*arr)
    else:
        # 'i' points to the first positive element after segregation
        k = 0  # Start placing positive elements at even indices (0, 2, 4...)
        while k < n and i < n:
            # Swap the positive element at position 'i' with element at position 'k'
            arr[k], arr[i] = arr[i], arr[k]
            k += 2  # Move to next even index
            i += 1  # Move to next positive element
        
        print(*arr)  # Print the final rearranged array

# Get user input
# n = int(input("Enter the length of array : "))
# arr = list(map(int, input('Enter the array : ').split()))
n = 9
arr = [1, -2, 3, -4, 5, -6, 7, -8, 9]
# Example array for testing
# Call the function
arrange(arr, n)
# Expected output: Rearranged array with alternating positive and negative elements
# Example output: 1 -2 3 -4 5 -6 7 -8 9
print(arr)  # Final output of the rearranged array