# Move all negative numbers to beginning and positive to end with constant extra space

# arr = [int(x) for x in input("Enter the array : ").split()]
arr = [1, -2, 3, -4, 5, -6, 7, -8, 9]

def move(arr):
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        # if left element is negative, move left pointer
        if arr[left] < 0:
            left += 1
        # if right element is positive, move right pointer
        elif arr[right] >= 0:
            right -= 1
        # if left is positive and right is negative, swap them
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
    return arr

print(move(arr))