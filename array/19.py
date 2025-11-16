"""
PROBLEM: Rearrange Array in Alternating Positive & Negative Items
====================================================================
Given an array of positive and negative numbers, arrange them in an alternating
fashion such that every positive number is followed by a negative number and
vice-versa. The order of appearance should be maintained.

Note: If there are more positive numbers, they appear at the end of the array.
If there are more negative numbers, they appear at the end of the array.

Example:
    Input:  arr = [1, 2, 3, -4, -1, 4]
    Output: [-4, 1, -1, 2, 3, 4] or [1, -4, 2, -1, 3, 4]
    Explanation: Positive and negative numbers alternate

    Input:  arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
    Output: [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]
    Explanation: Negative at even index (0,2,4...), positive at odd (1,3,5...)

    Input:  arr = [1, -2, 3, -4, 5, -6, 7, -8, 9]
    Output: [-2, 1, -4, 3, -6, 5, -8, 7, 9]

APPROACH: Two-Phase Segregation and Rearrangement
===================================================
WHY THIS APPROACH?
- Attempts to achieve O(n) time complexity
- Works with O(1) extra space (in-place)
- Handles unequal counts of positive and negative numbers
- Two distinct phases: segregate, then rearrange

ALTERNATIVE APPROACHES:
1. Using Extra Space: O(n) time, O(n) space
   - Create separate lists for positive and negative numbers
   - Merge them alternately
   - Simpler but uses O(n) extra space

2. Rotation-based: O(n²) time, O(1) space
   - For each position, find appropriate element and rotate
   - Very inefficient for large arrays

3. Modified QuickSort Partition: O(n) time, O(1) space
   - Similar to Dutch National Flag algorithm
   - More efficient segregation

HOW IT WORKS (Two-Phase Approach):
Phase 1: Partial Segregation
   - Use two pointers: i (from left) and j (from right)
   - Try to move negatives towards left and positives towards right
   - When arr[i] < 0 and arr[j] > 0: swap them
   - When both are on wrong sides: move both pointers inward
   - Track where first positive element starts (index i)

Phase 2: Alternate Rearrangement
   - If all elements are same sign (i==0 or i==n), no rearrangement needed
   - Otherwise, starting from index 0 (even positions)
   - Swap elements to place positives and negatives alternately
   - Use index k for even positions (0,2,4,...)
   - Use index i for positive elements section
   - Increment k by 2 (to next even position)
   - Increment i by 1 (to next positive element)

FLOW EXAMPLE:
=============
Array: [1, -2, 3, -4, 5, -6, 7, -8, 9]
Goal: Rearrange to alternate positive and negative

PHASE 1: PARTIAL SEGREGATION
-----------------------------
Initial State:
    i=0, j=8
    [1, -2, 3, -4, 5, -6, 7, -8, 9]
     ↑                          ↑
     i                          j

Step 1: arr[0]=1 (positive), arr[8]=9 (positive)
        Both positive → move i forward
        i=1, j=8

Step 2: arr[1]=-2 (negative), arr[8]=9 (positive)
        Negative left, positive right → swap
        [1, 9, 3, -4, 5, -6, 7, -8, -2]
        i=2, j=7

Step 3: arr[2]=3 (positive), arr[7]=-8 (negative)
        Both wrong positions → move both inward
        i=3, j=6

Step 4: arr[3]=-4 (negative), arr[6]=7 (positive)
        Negative left, positive right → swap
        [1, 9, 3, 7, 5, -6, -4, -8, -2]
        i=4, j=5

Step 5: arr[4]=5 (positive), arr[5]=-6 (negative)
        Both wrong positions → move both inward
        i=5, j=4

Loop ends (i > j)

After Phase 1:
    [1, 9, 3, 7, 5, -6, -4, -8, -2]
     <-positives-> <--negatives-->
                   ↑
                   i=5 (where negatives start)

PHASE 2: ALTERNATE REARRANGEMENT
---------------------------------
Since i != 0 and i != n, proceed with rearrangement
k = 0 (start at even index)
i = 5 (first negative element after segregation)

Goal: Place negatives at even indices (0,2,4,...) by swapping with positives

Step 1: k=0, i=5
        Swap arr[0] and arr[5]
        [-6, 9, 3, 7, 5, 1, -4, -8, -2]
        k=2, i=6

Step 2: k=2, i=6
        Swap arr[2] and arr[6]
        [-6, 9, -4, 7, 5, 1, 3, -8, -2]
        k=4, i=7

Step 3: k=4, i=7
        Swap arr[4] and arr[7]
        [-6, 9, -4, 7, -8, 1, 3, 5, -2]
        k=6, i=8

Step 4: k=6, i=8
        Swap arr[6] and arr[8]
        [-6, 9, -4, 7, -8, 1, -2, 5, 3]
        k=8, i=9

Loop ends (k >= n or i >= n)

Final Result:
    [-6, 9, -4, 7, -8, 1, -2, 5, 3]
    Alternating pattern: negative, positive, negative, positive...

FLOWCHART:
==========
    ┌──────────────────────────┐
    │  Start: arrange(arr, n)  │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │ PHASE 1: SEGREGATION     │
    │ Initialize: i=0, j=n-1   │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │    while i <= j?         │
    └──┬──────────────────┬────┘
       │ No               │ Yes
       │                  ▼
       │    ┌───────────────────────────┐
       │    │  Check arr[i] and arr[j]  │
       │    └─┬─────────┬───────┬───────┘
       │      │         │       │
       │   Case 1    Case 2  Case 3
       │      │         │       │
       │      ▼         ▼       ▼
       │  ┌────────┐ ┌────┐ ┌──────┐
       │  │arr[i]<0│ │Both│ │arr[i]│
       │  │arr[j]>0│ │opp │ │>0    │
       │  │        │ │site│ │only  │
       │  └───┬────┘ └─┬──┘ └──┬───┘
       │      │        │       │
       │      ▼        ▼       ▼
       │  ┌────────┐ ┌────┐ ┌────┐
       │  │ Swap   │ │i++ │ │i++ │
       │  │arr[i]  │ │j-- │ │    │
       │  │arr[j]  │ │    │ │    │
       │  └───┬────┘ └─┬──┘ └──┬─┘
       │      │        │       │
       │      ▼        ▼       ▼
       │  ┌────────┐ ┌─────────┐
       │  │  i++   │ │Case 4:  │
       │  │  j--   │ │arr[j]<0 │
       │  └───┬────┘ │  j--    │
       │      │      └────┬────┘
       │      └───────────┘
       │              │
       │              └──────────┐
       │                         │
       ▼                         ▼
    ┌──────────────────────────────┐
    │ PHASE 2: REARRANGEMENT       │
    │ Check: i==0 or i==n?         │
    └──┬───────────────────────┬───┘
       │ Yes (all same sign)   │ No
       │                       │
       │                       ▼
       │         ┌──────────────────────┐
       │         │ Initialize: k=0      │
       │         │ (even index pointer) │
       │         └──────────┬───────────┘
       │                    │
       │                    ▼
       │         ┌──────────────────────┐
       │         │  while k<n AND i<n?  │
       │         └──┬────────────────┬──┘
       │            │ No             │ Yes
       │            │                │
       │            │                ▼
       │            │     ┌────────────────┐
       │            │     │ Swap arr[k]    │
       │            │     │ with arr[i]    │
       │            │     └───────┬────────┘
       │            │             │
       │            │             ▼
       │            │     ┌────────────────┐
       │            │     │ k += 2 (skip   │
       │            │     │ to next even)  │
       │            │     │ i += 1         │
       │            │     └───────┬────────┘
       │            │             │
       │            │             └────┐
       │            │                  │
       ▼            ▼                  ▼
    ┌──────────────────────────────────┐
    │  Print final rearranged array    │
    └──────────────────────────────────┘

TIME COMPLEXITY:
- Phase 1 (Segregation): O(n) - Single pass with two pointers
- Phase 2 (Rearrangement): O(n) - At most n/2 swaps
- Total: O(n)

SPACE COMPLEXITY: O(1)
- Only using a constant amount of extra space for pointers
- All operations are done in-place

LIMITATIONS AND EDGE CASES:
============================
1. If all elements are positive (i == n):
   - No rearrangement needed, array stays as is

2. If all elements are negative (i == 0):
   - No rearrangement needed, array stays as is

3. Unequal positive/negative counts:
   - Extra elements appear at the end of array
   - Alternation continues as long as both types available

4. Zero values:
   - Treated as positive (since arr[i] > 0 is false, arr[i] < 0 is also false)
   - May need special handling depending on requirements
"""

def arrange(arr, n):
    """
    Rearranges array elements so that positive and negative elements appear alternately.

    The function works in two phases:
    1. Segregation: Partially separate negative and positive numbers
    2. Rearrangement: Swap elements to create alternating pattern

    Args:
        arr (list): The input array containing positive and negative elements
        n (int): Length of the array

    Returns:
        None: Modifies the array in-place and prints intermediate results

    Time Complexity: O(n) - Two passes through the array
    Space Complexity: O(1) - In-place modification

    Example:
        >>> arr = [1, -2, 3, -4, 5, -6, 7, -8, 9]
        >>> arrange(arr, 9)
        # Output will show alternating positive and negative numbers
    """
    # PHASE 1: SEGREGATION
    # ====================
    # Pointer starting from the beginning of the array
    # Will scan forward looking for elements to swap
    i = 0

    # Pointer starting from the end of the array
    # Will scan backward looking for elements to swap
    j = n - 1

    # Continue until pointers meet or cross
    while i <= j:
        # Case 1: arr[i] is negative and arr[j] is positive
        # This means they are both in good positions relative to each other
        # Swap them to bring negative to left and positive to right
        if arr[i] < 0 and arr[j] > 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1  # Move to next element from left
            j -= 1  # Move to next element from right

        # Case 2: arr[i] is positive and arr[j] is negative
        # Both are in wrong positions relative to each other
        # Swapping won't help, so move both pointers inward
        elif arr[i] > 0 and arr[j] < 0:
            i += 1
            j -= 1

        # Case 3: arr[i] is positive
        # Element at i is on the wrong side, move forward to find negative
        elif arr[i] > 0:
            i += 1

        # Case 4: arr[j] is negative
        # Element at j is on the wrong side, move backward to find positive
        elif arr[j] < 0:
            j -= 1

    # Print intermediate result after segregation
    # At this point, i points to where positive numbers start
    print("After segregation:", *arr)

    # PHASE 2: REARRANGEMENT
    # ======================
    # Check if all elements are of the same sign
    if i == 0 or i == n:
        # If i == 0: all elements are positive (no negatives found)
        # If i == n: all elements are negative (no positives found)
        # In both cases, no alternation is possible
        print("All elements same sign:", *arr)
    else:
        # We have both positive and negative elements
        # Now arrange them in alternating fashion

        # k: pointer for even indices (0, 2, 4, 6, ...)
        # We'll place negative numbers at even indices
        k = 0

        # i: already points to the start of positive numbers section
        # We'll swap positive numbers to odd indices

        # Continue until we run out of either negatives or reach end of array
        while k < n and i < n:
            # Swap element at position k (even index) with element at position i
            # This places a positive element at an even index
            # and moves a negative element towards odd positions
            arr[k], arr[i] = arr[i], arr[k]

            # Move k to next even index (skip odd index)
            k += 2

            # Move to next element in the positive section
            i += 1

        # Print final rearranged array
        print("After rearrangement:", *arr)


# Test cases
if __name__ == "__main__":
    # Test 1: Equal number of positive and negative elements
    print("Test 1: Equal positive and negative")
    print("=" * 50)
    n1 = 9
    arr1 = [1, -2, 3, -4, 5, -6, 7, -8, 9]
    print(f"Original array: {arr1}")
    arrange(arr1, n1)
    print(f"Final array: {arr1}")
    print()

    # Test 2: More positive than negative
    print("Test 2: More positive than negative")
    print("=" * 50)
    n2 = 7
    arr2 = [1, 2, 3, -4, -1, 4, 5]
    print(f"Original array: {arr2}")
    arrange(arr2, n2)
    print(f"Final array: {arr2}")
    print()

    # Test 3: More negative than positive
    print("Test 3: More negative than positive")
    print("=" * 50)
    n3 = 7
    arr3 = [-1, -2, -3, -4, -5, 1, 2]
    print(f"Original array: {arr3}")
    arrange(arr3, n3)
    print(f"Final array: {arr3}")
    print()

    # Test 4: All positive
    print("Test 4: All positive elements")
    print("=" * 50)
    n4 = 5
    arr4 = [1, 2, 3, 4, 5]
    print(f"Original array: {arr4}")
    arrange(arr4, n4)
    print(f"Final array: {arr4}")
    print()

    # Test 5: All negative
    print("Test 5: All negative elements")
    print("=" * 50)
    n5 = 5
    arr5 = [-1, -2, -3, -4, -5]
    print(f"Original array: {arr5}")
    arrange(arr5, n5)
    print(f"Final array: {arr5}")
