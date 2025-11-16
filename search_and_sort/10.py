"""
PROBLEM: Four Sum (4Sum)
Find all unique quadruplets [a, b, c, d] in array that sum to a target value k.

WHY THIS SOLUTION:
This is a classic extension of the 2Sum and 3Sum problems!

Naive approach: 4 nested loops - O(n⁴)
Better approach: HashMap with 3 loops - O(n³) space expensive
Best approach (this): Sort + 2 loops + Two Pointers - O(n³) time, O(1) space!

KEY INSIGHT: Reduce to 2Sum
We reduce 4Sum → 3Sum → 2Sum:
- Fix first element (i loop)
- Fix second element (j loop)
- Use TWO POINTERS for remaining two elements (k reduction from O(n²) to O(n))

The sorted array allows two-pointer technique for the inner part!

APPROACH:
1. Sort array first
2. Outer loop i: first element (0 to n-3)
3. Inner loop j: second element (i+1 to n-2)
4. Two pointers (left, right): find pairs that sum to (k - arr[i] - arr[j])
5. Skip duplicates to avoid duplicate quadruplets

TIME COMPLEXITY: O(n³)
  - Sorting: O(n log n)
  - i loop: O(n)
  - j loop: O(n)
  - Two pointers: O(n)
  - Total: O(n) * O(n) * O(n) = O(n³)

SPACE COMPLEXITY: O(1) - excluding output array

EXAMPLE: arr = [10, 2, 3, 4, 5, 7, 8], k = 23
After sorting: [2, 3, 4, 5, 7, 8, 10]

i=0 (2), j=1 (3): need 23-2-3=18 from remaining
  left=2 (4), right=6 (10): 4+10=14 < 18 → left++
  left=3 (5), right=6 (10): 5+10=15 < 18 → left++
  left=4 (7), right=6 (10): 7+10=17 < 18 → left++
  left=5 (8), right=6 (10): 8+10=18 = 18 → Found [2,3,8,10]!

WHY INTERVIEWER WILL ACCEPT:
- Classic LeetCode medium problem
- Shows understanding of problem reduction (4Sum → 2Sum)
- Optimal O(n³) solution (can't do better for 4Sum)
- Proper handling of duplicates
"""

# Input (commented for testing)
# l, k = [int(x) for x in input("Enter n,k : ").split()]
# arr = [int(x) for x in input("Enter the array : ").split()]

# Test case
l, k = 7, 23
arr = [10, 2, 3, 4, 5, 7, 8]

def get_quad(arr, k):
    """
    Find all unique quadruplets that sum to k.

    Uses sorting + two loops + two pointers to reduce from O(n⁴) to O(n³).

    Args:
        arr: Input array
        k: Target sum

    Returns:
        List of quadruplets
    """
    n = len(arr)

    # Edge case: need at least 4 elements
    if n < 4:
        return []

    res = []
    arr.sort()  # Sort to enable two-pointer technique

    # Fix first element
    for i in range(n - 3):
        # Skip duplicates for first element
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        # Fix second element
        for j in range(i + 1, n - 2):
            # Skip duplicates for second element
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            # Use two pointers for remaining two elements
            left = j + 1
            right = n - 1

            # Calculate what the remaining two elements should sum to
            sum_i_j = arr[i] + arr[j]
            remain = k - sum_i_j

            # Two pointer search
            while left < right:
                two_sum = arr[left] + arr[right]

                if two_sum == remain:
                    # Found a quadruplet!
                    res.append([arr[i], arr[j], arr[left], arr[right]])

                    # Move both pointers
                    left += 1
                    right -= 1

                    # Skip duplicates for third element
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1

                    # Skip duplicates for fourth element
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1

                elif two_sum < remain:
                    # Sum too small, need larger value
                    left += 1
                else:
                    # Sum too large, need smaller value
                    right -= 1

    return res

print(f"Array: {arr}")
print(f"Target sum: {k}")

result = get_quad(arr, k)

if result:
    print(f"\nQuadruplets found: {len(result)}")
    for quad in result:
        print(f"  {quad} → sum = {sum(quad)}")
else:
    print("No quadruplets found")
