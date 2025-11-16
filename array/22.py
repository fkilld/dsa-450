"""
PROBLEM: Maximum Product Subarray
==================================
Given an array that contains N integers (may be positive, negative or zero),
find the product of the maximum product subarray.

A subarray is a contiguous part of an array.

Example:
    Input:  arr = [6, -3, -10, 0, 2]
    Output: 180
    Explanation: The subarray [6, -3, -10] gives maximum product = 180

    Input:  arr = [2, 3, 4, 5, -1, 0]
    Output: 120
    Explanation: The subarray [2, 3, 4, 5] gives maximum product = 120

    Input:  arr = [-1, -3, -10, 0, 60]
    Output: 60
    Explanation: The subarray [60] gives maximum product = 60

    Input:  arr = [2, 3, -2, 4]
    Output: 6
    Explanation: The subarray [2, 3] gives maximum product = 6

APPROACH: Dynamic Programming with Min/Max Tracking
====================================================
WHY THIS APPROACH?
- Similar to Kadane's algorithm but tracks BOTH maximum and minimum products
- Key insight: A negative number can flip signs when multiplied
  * Maximum product can become minimum when multiplied by negative
  * Minimum product can become maximum when multiplied by negative
- Need to track minimum because: min × negative = potentially large positive
- Single pass solution: O(n) time complexity
- Constant space: O(1) space complexity

ALTERNATIVE APPROACHES:
1. Brute Force: Check all subarrays - O(n²) time, O(1) space
2. Divide and Conquer: Split at zeros - O(n log n) time
3. Handle positive/negative/zero separately - Complex logic

WHY TRACK BOTH MAX AND MIN?
============================
Consider array: [2, 3, -2, 4]

Without tracking min:
- At index 2 (-2): max = max(2*3*(-2), -2) = max(-12, -2) = -2
- At index 3 (4): max = max(-2*4, 4) = max(-8, 4) = 4
- We miss the product 2*3 = 6!

With tracking both max and min:
- At index 2 (-2):
  * max = max(6*(-2), -2) = -2
  * min = min(6*(-2), -2) = -12  (tracking this!)
- At index 3 (4):
  * max = max(-2*4, -12*4, 4) = max(-8, -48, 4) = 4
  * Wait, we need to reconsider...

Actually, when we swap before multiplication, we correctly handle it!

HOW IT WORKS:
1. Initialize three variables with the first element:
   - ma (max_ending_here): Maximum product ending at current position
   - mi (min_ending_here): Minimum product ending at current position
   - prod (global_max): Overall maximum product found so far

2. For each element from index 1 to n-1:
   a. If current element is negative, swap ma and mi
      (because multiplying by negative flips the values)
   b. Update ma = max(ma * arr[i], arr[i])
      (either extend previous subarray or start new from current)
   c. Update mi = min(mi * arr[i], arr[i])
      (track minimum for future negative multiplications)
   d. Update prod = max(prod, ma)
      (update global maximum if needed)

3. Return prod

FLOW EXAMPLE:
=============
Array: [2, 3, -2, 4]
Goal: Find maximum product subarray

Initial State:
    ma = arr[0] = 2  (max product ending at index 0)
    mi = arr[0] = 2  (min product ending at index 0)
    prod = arr[0] = 2  (global maximum)

Step 1: i=1, arr[1]=3 (positive number)
    arr[1] >= 0, so no swap
    ma = max(ma * arr[1], arr[1]) = max(2*3, 3) = max(6, 3) = 6
    mi = min(mi * arr[1], arr[1]) = min(2*3, 3) = min(6, 3) = 3
    prod = max(prod, ma) = max(2, 6) = 6
    State: ma=6, mi=3, prod=6

Step 2: i=2, arr[2]=-2 (negative number)
    arr[2] < 0, SWAP ma and mi
    After swap: ma=3, mi=6
    ma = max(ma * arr[2], arr[2]) = max(3*(-2), -2) = max(-6, -2) = -2
    mi = min(mi * arr[2], arr[2]) = min(6*(-2), -2) = min(-12, -2) = -12
    prod = max(prod, ma) = max(6, -2) = 6
    State: ma=-2, mi=-12, prod=6

Step 3: i=3, arr[3]=4 (positive number)
    arr[3] >= 0, so no swap
    ma = max(ma * arr[3], arr[3]) = max(-2*4, 4) = max(-8, 4) = 4
    mi = min(mi * arr[3], arr[3]) = min(-12*4, 4) = min(-48, 4) = -48
    prod = max(prod, ma) = max(6, 4) = 6
    State: ma=4, mi=-48, prod=6

Final Answer: 6

WHY THE ANSWER IS 6:
The subarray [2, 3] gives product 6, which is the maximum.
Even though we have -2*4 = -8 or even 2*3*(-2)*4 = -48,
the algorithm correctly maintains the maximum product of 6.

DETAILED EXAMPLE WITH NEGATIVE NUMBERS:
========================================
Array: [6, -3, -10, 0, 2]

Initial: ma=6, mi=6, prod=6

i=1, arr[1]=-3 (negative):
    Swap: ma=6, mi=6 (no change since they're equal)
    ma = max(6*(-3), -3) = max(-18, -3) = -3
    mi = min(6*(-3), -3) = min(-18, -3) = -18
    prod = max(6, -3) = 6
    State: ma=-3, mi=-18, prod=6

i=2, arr[2]=-10 (negative):
    Swap: ma=-18, mi=-3
    ma = max(-18*(-10), -10) = max(180, -10) = 180  ← Key moment!
    mi = min(-3*(-10), -10) = min(30, -10) = -10
    prod = max(6, 180) = 180
    State: ma=180, mi=-10, prod=180

i=3, arr[3]=0 (zero):
    No swap (0 is not negative)
    ma = max(180*0, 0) = max(0, 0) = 0
    mi = min(-10*0, 0) = min(0, 0) = 0
    prod = max(180, 0) = 180
    State: ma=0, mi=0, prod=180

i=4, arr[4]=2 (positive):
    No swap
    ma = max(0*2, 2) = max(0, 2) = 2
    mi = min(0*2, 2) = min(0, 2) = 0
    prod = max(180, 2) = 180
    State: ma=2, mi=0, prod=180

Final Answer: 180 (from subarray [6, -3, -10])

FLOWCHART:
==========
    ┌──────────────────────────────┐
    │ Start: max_product(arr, n)   │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │ Initialize with arr[0]:      │
    │ ma = arr[0]  (max so far)    │
    │ mi = arr[0]  (min so far)    │
    │ prod = arr[0] (global max)   │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │ For i from 1 to n-1          │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │   Is arr[i] < 0?             │
    │   (negative number)          │
    └────┬───────────────────┬─────┘
         │ Yes               │ No
         │                   │
         ▼                   │
    ┌─────────────┐          │
    │ Swap ma,mi  │          │
    └──────┬──────┘          │
           │                 │
           └─────────┬───────┘
                     │
                     ▼
    ┌──────────────────────────────────┐
    │ Update maximum ending here:      │
    │ ma = max(ma * arr[i], arr[i])    │
    │                                  │
    │ Explanation:                     │
    │ - ma * arr[i]: extend subarray   │
    │ - arr[i]: start new subarray     │
    └────────────────┬─────────────────┘
                     │
                     ▼
    ┌──────────────────────────────────┐
    │ Update minimum ending here:      │
    │ mi = min(mi * arr[i], arr[i])    │
    │                                  │
    │ Why? Negative × negative might   │
    │ give maximum in future steps     │
    └────────────────┬─────────────────┘
                     │
                     ▼
    ┌──────────────────────────────────┐
    │ Update global maximum:           │
    │ prod = max(prod, ma)             │
    └────────────────┬─────────────────┘
                     │
                     └─────┐
                           │
                           ▼
    ┌──────────────────────────────────┐
    │ All elements processed?          │
    └────┬────────────────────────┬────┘
         │ No (continue loop)     │ Yes
         │                        │
         └───────────┐            ▼
                     │    ┌─────────────┐
                     │    │ Return prod │
                     │    └─────────────┘
                     │
                     └────► (back to loop)

KEY INSIGHT - WHY SWAP WHEN NEGATIVE?
======================================
When we multiply by a negative number:
1. The current maximum becomes the new minimum (positive × negative = negative)
2. The current minimum becomes the new maximum (negative × negative = positive)

Example:
    Before: ma=6, mi=-18
    Multiply by -10:
    - 6 × (-10) = -60  (previous max becomes negative)
    - (-18) × (-10) = 180  (previous min becomes LARGE positive!)

By swapping before multiplication, we ensure:
    After swap: ma=-18, mi=6
    ma = max(-18 × (-10), -10) = max(180, -10) = 180 ✓

HANDLING SPECIAL CASES:
=======================
1. Zero in array:
   - Resets both ma and mi to 0
   - Effectively starts a new potential subarray
   - Example: [2, 3, 0, 4, 5] → max(6, 20) = 20

2. All negative numbers:
   - The maximum will be the largest single negative number
   - Example: [-2, -3, -4] → max product = -2

3. Single element:
   - Returns that element
   - Example: [5] → 5, [-3] → -3

TIME COMPLEXITY:  O(n) - Single pass through array
SPACE COMPLEXITY: O(1) - Only using three variables (ma, mi, prod)

COMPARISON WITH KADANE'S ALGORITHM:
===================================
Kadane's Algorithm (Maximum Sum Subarray):
- Tracks only maximum sum ending at current position
- Simple: max = max(max + arr[i], arr[i])

Maximum Product Subarray:
- Must track BOTH max and min products
- More complex due to negative number handling
- Swapping mechanism is the key difference
"""


class Solution:
    """
    Solution class for finding the maximum product subarray.

    This implements a dynamic programming approach similar to Kadane's algorithm,
    but adapted for products instead of sums. The key difference is tracking both
    maximum and minimum products because multiplying by a negative number can
    convert a minimum into a maximum.
    """

    def max_sum_subarr(self, arr, n):
        """
        Find the maximum product of any contiguous subarray.

        This function uses dynamic programming to track both the maximum and
        minimum products ending at each position. When encountering a negative
        number, it swaps max and min since negative × negative can produce
        a large positive number.

        Parameters:
            arr (list): The input array containing integers (positive, negative, or zero)
            n (int): The length of the input array

        Returns:
            int: The maximum product of any subarray

        Example:
            arr = [2, 3, -2, 4] → returns 6 (subarray [2, 3])
            arr = [6, -3, -10, 0, 2] → returns 180 (subarray [6, -3, -10])

        Time Complexity: O(n) - Single pass through array
        Space Complexity: O(1) - Only using constant extra space
        """
        # Initialize all three variables with first element
        # ma: Maximum product ending at current index
        # mi: Minimum product ending at current index (important for negative numbers!)
        # prod: Overall maximum product found so far (our answer)
        ma = arr[0]
        mi = arr[0]
        prod = arr[0]

        # Iterate through array starting from second element
        for i in range(1, n):
            # If current element is negative, swap max and min
            # WHY? Because multiplying by negative flips the sign:
            # - A large positive × negative = large negative (becomes our new min)
            # - A large negative × negative = large positive (becomes our new max!)
            if arr[i] < 0:
                # Swap maximum and minimum values
                # This prepares us for the multiplication with negative number
                ma, mi = mi, ma

            # Update maximum product ending at current position
            # Two choices:
            # 1. Extend previous subarray: ma * arr[i]
            # 2. Start new subarray from current element: arr[i]
            # We take the maximum of these two options
            ma = max(ma * arr[i], arr[i])

            # Update minimum product ending at current position
            # Why track minimum?
            # - If we encounter another negative number later, this minimum
            #   can become maximum (negative × negative = positive)
            # - Example: min=-18, next element=-10 → -18*(-10)=180 (large positive!)
            mi = min(mi * arr[i], arr[i])

            # Update overall maximum product if current maximum is larger
            # This ensures we remember the best product seen so far
            if ma > prod:
                prod = ma

        # Return the maximum product subarray result
        return prod


# Test cases
if __name__ == "__main__":
    s = Solution()

    # Test 1: Array with negative numbers giving maximum product
    arr1 = [6, -3, -10, 0, 2]
    n1 = len(arr1)
    print(f"Array: {arr1}")
    print(f"Maximum product: {s.max_sum_subarr(arr1, n1)}")  # Expected: 180
    print(f"Explanation: Subarray [6, -3, -10] = 6*(-3)*(-10) = 180\n")

    # Test 2: Array with positive numbers and ending negative
    arr2 = [2, 3, -2, 4]
    n2 = len(arr2)
    print(f"Array: {arr2}")
    print(f"Maximum product: {s.max_sum_subarr(arr2, n2)}")  # Expected: 6
    print(f"Explanation: Subarray [2, 3] = 2*3 = 6\n")

    # Test 3: Array with all negative numbers
    arr3 = [-2, -3, -4]
    n3 = len(arr3)
    print(f"Array: {arr3}")
    print(f"Maximum product: {s.max_sum_subarr(arr3, n3)}")  # Expected: 24
    print(f"Explanation: Subarray [-2, -3, -4] = -2*(-3)*(-4) = -24 or [-3, -4] = 12 or all three if even count\n")

    # Test 4: Array with zero
    arr4 = [2, 3, 0, 4, 5]
    n4 = len(arr4)
    print(f"Array: {arr4}")
    print(f"Maximum product: {s.max_sum_subarr(arr4, n4)}")  # Expected: 20
    print(f"Explanation: Subarray [4, 5] = 4*5 = 20\n")

    # Test 5: Single element positive
    arr5 = [8]
    n5 = len(arr5)
    print(f"Array: {arr5}")
    print(f"Maximum product: {s.max_sum_subarr(arr5, n5)}")  # Expected: 8

    # Test 6: Single element negative
    arr6 = [-3]
    n6 = len(arr6)
    print(f"\nArray: {arr6}")
    print(f"Maximum product: {s.max_sum_subarr(arr6, n6)}")  # Expected: -3

    # Test 7: All positive numbers
    arr7 = [2, 3, 4, 5]
    n7 = len(arr7)
    print(f"\nArray: {arr7}")
    print(f"Maximum product: {s.max_sum_subarr(arr7, n7)}")  # Expected: 120
    print(f"Explanation: Subarray [2, 3, 4, 5] = 2*3*4*5 = 120")
