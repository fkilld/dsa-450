# Sort an array of 0s, 1s and 2s 

class Solution:
    """
    Sort an array containing only 0s, 1s, and 2s using the Dutch National Flag algorithm.
    This algorithm sorts the array in a single pass with O(n) time complexity
    without using any sorting algorithm. It uses three pointers (low, mid, high) to
    partition the array into three sections: 0s, 1s, and 2s.
    Parameters:
        arr (list): The array to be sorted containing only 0s, 1s, and 2s
        n (int): Length of the array
    Returns:
        list: The sorted array with 0s followed by 1s followed by 2s
    Time Complexity: O(n)
    Space Complexity: O(1)
    This is a solution for the Dutch National Flag problem, originally proposed by
    Edsger W. Dijkstra.
    """
    def sort012(self, arr, n):
        low = 0
        high = n - 1
        mid = 0

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[high], arr[mid] = arr[mid], arr[high]
                high -= 1
        return arr

s1 = Solution()
arr = [0, 1, 2, 0, 1, 2, 0, 1, 2]
n = len(arr)
print(s1.sort012(arr, n))