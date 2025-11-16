"""
PROBLEM: Find Maximum and Minimum Using Minimum Comparisons
Find both max and min elements of an array using the MINIMUM number of comparisons.

WHY THIS SOLUTION:
Naive approach: 2(n-1) comparisons
- Find max: n-1 comparisons
- Find min: n-1 comparisons
- Total: 2n-2 comparisons

Optimized approach (this solution): ~3n/2 comparisons
- Process elements in PAIRS
- Compare pair elements with each other (1 comparison)
- Compare smaller with min (1 comparison)
- Compare larger with max (1 comparison)
- Total: 3 comparisons per 2 elements = 3n/2

This is the OPTIMAL solution - you cannot do better than 3n/2 comparisons!

APPROACH:
1. Initialize min and max:
   - If even length: compare first two elements
   - If odd length: first element is both min and max initially
2. Process remaining elements in pairs:
   - Compare the two elements in pair (determine which is larger)
   - Compare larger one with current max
   - Compare smaller one with current min
3. This way, we do 3 comparisons for every 2 elements

TIME COMPLEXITY: O(n) with ~3n/2 comparisons (optimal)
SPACE COMPLEXITY: O(1)

EXAMPLE: arr = [3, 1, 4, 1, 5, 9, 2, 6]
Length = 8 (even)
Initial: max=4, min=1 (from comparing arr[0]=3 and arr[1]=1)
Process pairs:
- (4,1): max stays 4, min stays 1
- (5,9): max=9, min stays 1
- (2,6): max stays 9, min stays 1
Result: max=9, min=1

WHY INTERVIEWER WILL ACCEPT:
- Demonstrates knowledge of comparison-optimal algorithms
- Reduces comparisons from 2n to 3n/2
- Shows understanding of pair-wise processing technique
"""

arr = [int(x) for x in input("Enter the array : ").split()]

min_val, max_val, i = 0, 0, 0

# Initialize min and max based on whether array has odd or even number of elements
if len(arr) % 2 == 0:
    # Even number of elements: compare first two elements
    if arr[0] >= arr[1]:
        max_val = arr[0]
        min_val = arr[1]
    else:
        max_val = arr[1]
        min_val = arr[0]
    i = 2  # Start processing from index 2
else:
    # Odd number of elements: first element is both min and max initially
    max_val = arr[0]
    min_val = arr[0]
    i = 1  # Start processing from index 1

# Process remaining elements in PAIRS
# This is the key optimization: process two elements at a time
while i < len(arr) - 1:
    # Compare the two elements in the pair first
    if arr[i] > arr[i + 1]:
        # arr[i] is larger, arr[i+1] is smaller
        # Compare larger with max
        if arr[i] > max_val:
            max_val = arr[i]
        # Compare smaller with min
        if arr[i + 1] < min_val:
            min_val = arr[i + 1]
    else:
        # arr[i+1] is larger, arr[i] is smaller
        # Compare smaller with min
        if arr[i] < min_val:
            min_val = arr[i]
        # Compare larger with max
        if arr[i + 1] > max_val:
            max_val = arr[i + 1]

    # Move to next pair
    i += 2

print(f"Maximum: {max_val}")
print(f"Minimum: {min_val}")
