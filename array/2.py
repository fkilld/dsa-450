def kth_smallest(arr, k):
    """
    Find the kth smallest element in an array using QuickSelect.
    
    Args:
        arr: List of integers
        k: Position of the element to find (1-based index)
    
    Returns:
        The kth smallest element or -1 if not found
    
    Time Complexity: Average O(n), worst case O(n²)
    Space Complexity: O(1)
    """
    if not arr or k <= 0 or k > len(arr):
        return -1
    
    def partition(arr, left, right):
        pivot = arr[right]
        i = left - 1
        
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return i + 1
    
    def quick_select(arr, left, right, k_index):
        if left == right:
            return arr[left]
        
        pivot_index = partition(arr, left, right)
        
        if pivot_index == k_index:
            return arr[pivot_index]
        elif k_index < pivot_index:
            return quick_select(arr, left, pivot_index - 1, k_index)
        else:
            return quick_select(arr, pivot_index + 1, right, k_index)
    
    # Convert to 0-based index
    return quick_select(arr, 0, len(arr) - 1, k - 1)
