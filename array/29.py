def findMinDiff(self, arr, N, M):
    # Edge case 1: If there are no students or no chocolate packets
    if M == 0 or N == 0:
        return 0
        
    # Sort the array to make it easier to find minimum difference
    # After sorting, packets with similar number of chocolates are adjacent
    arr.sort()
    
    # Edge case 2: If number of students is more than available packets
    # Cannot distribute packets to all students
    if N < M:
        return -1
            
    # Initialize minimum difference with largest possible value
    min_diff = float('inf')
    
    # Iterate through all possible consecutive segments of length M
    # We need to check N-M+1 segments to cover all possible distributions
    # Each segment represents one possible way to distribute chocolates
    for i in range(N - M + 1):
        # Calculate difference between maximum and minimum chocolates 
        # in current distribution (arr[i] to arr[i+M-1])
        current_diff = arr[i + M - 1] - arr[i]
        
        # Update minimum difference if current difference is smaller
        min_diff = min(min_diff, current_diff)
    
    return min_diff