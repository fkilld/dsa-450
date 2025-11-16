"""
PROBLEM: Longest Consecutive Subsequence
=========================================
Given an array of positive integers, find the length of the longest subsequence
such that elements in the subsequence are consecutive integers.

The consecutive numbers can be in any order in the original array.

Note: This is a SUBSEQUENCE problem, not subarray. Elements don't need to be
contiguous in the original array, but the resulting sequence must be consecutive.

Example:
    Input:  arr = [1, 9, 3, 10, 4, 20, 2]
    Output: 4
    Explanation: The longest consecutive subsequence is [1, 2, 3, 4]

    Input:  arr = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
    Output: 5
    Explanation: The longest consecutive subsequence is [32, 33, 34, 35, 36]

    Input:  arr = [1, 2, 3, 4, 5]
    Output: 5
    Explanation: The entire array is consecutive

    Input:  arr = [2, 0, 6, 1, 5, 3, 7]
    Output: 4
    Explanation: The longest consecutive subsequence is [0, 1, 2, 3]

APPROACH 1: Brute Force (Current Implementation)
=================================================
WHY THIS APPROACH?
- Simple and straightforward to understand
- No extra space needed (O(1) space)
- Works for small arrays
- Good for educational purposes to understand the problem
- Time Complexity: O(N³) - Very slow for large arrays
- Space Complexity: O(1) - No extra space

ALTERNATIVE APPROACHES:
1. Sorting: O(N log N) time, O(1) space
   - Sort array, then count consecutive elements in one pass
   - Simple but modifies input or needs copy

2. Hash Set (Optimal): O(N) time, O(N) space
   - Store all elements in hash set
   - For each element, check if it's the start of a sequence
   - Extend the sequence by checking next elements in set
   - Most efficient approach!

3. Union-Find: O(N α(N)) time, O(N) space
   - Complex but works for certain variations

HOW THE BRUTE FORCE APPROACH WORKS:
1. For each element in array (outer loop):
   - Treat it as the potential start of a consecutive sequence
2. For this starting value:
   - Try to find the next consecutive number (start + 1)
   - Then find start + 2, start + 3, etc.
   - Keep extending until no next number is found
3. Track the maximum length found across all starting points
4. Return the maximum length

DETAILED STEPS:
1. Initialize max_len = 1 (minimum length is 1)
2. For each index i from 0 to N-1:
   a. Set start_val = arr[i]
   b. Set current_len = 1 (the start element itself)
   c. While True:
      - Calculate next_val = start_val + current_len
      - Search entire array for next_val
      - If found: increment current_len
      - If not found: break
   d. Update max_len if current_len > max_len
3. Return max_len

FLOW EXAMPLE:
=============
Array: [1, 9, 3, 4, 2]
Goal: Find length of longest consecutive subsequence

Initial State:
    max_len = 1

Iteration 1: i=0, start_val=1
    current_len = 1

    Try next_val = 1 + 1 = 2
        Search array: Found at index 4 ✓
        current_len = 2

    Try next_val = 1 + 2 = 3
        Search array: Found at index 2 ✓
        current_len = 3

    Try next_val = 1 + 3 = 4
        Search array: Found at index 3 ✓
        current_len = 4

    Try next_val = 1 + 4 = 5
        Search array: Not found ✗
        Break

    max_len = max(1, 4) = 4

Iteration 2: i=1, start_val=9
    current_len = 1

    Try next_val = 9 + 1 = 10
        Search array: Not found ✗
        Break

    max_len = max(4, 1) = 4

Iteration 3: i=2, start_val=3
    current_len = 1

    Try next_val = 3 + 1 = 4
        Search array: Found at index 3 ✓
        current_len = 2

    Try next_val = 3 + 2 = 5
        Search array: Not found ✗
        Break

    max_len = max(4, 2) = 4

Iteration 4: i=3, start_val=4
    current_len = 1

    Try next_val = 4 + 1 = 5
        Search array: Not found ✗
        Break

    max_len = max(4, 1) = 4

Iteration 5: i=4, start_val=2
    current_len = 1

    Try next_val = 2 + 1 = 3
        Search array: Found at index 2 ✓
        current_len = 2

    Try next_val = 2 + 2 = 4
        Search array: Found at index 3 ✓
        current_len = 3

    Try next_val = 2 + 3 = 5
        Search array: Not found ✗
        Break

    max_len = max(4, 3) = 4

Final Answer: 4 (consecutive sequence: [1, 2, 3, 4])

FLOWCHART:
==========
    ┌────────────────────────────┐
    │  Start: longest(arr, N)    │
    └──────────────┬─────────────┘
                   │
                   ▼
    ┌────────────────────────────┐
    │ Initialize: max_len = 1    │
    └──────────────┬─────────────┘
                   │
                   ▼
    ┌────────────────────────────────┐
    │ For i from 0 to N-1            │
    │ (each element as start)        │
    └──────────────┬─────────────────┘
                   │
                   ▼
    ┌────────────────────────────────┐
    │ start_val = arr[i]             │
    │ current_len = 1                │
    └──────────────┬─────────────────┘
                   │
                   ▼
    ┌────────────────────────────────┐
    │ While True (extend sequence)   │
    └──────────────┬─────────────────┘
                   │
                   ▼
    ┌─────────────────────────────────┐
    │ next_val = start_val +          │
    │            current_len          │
    │ found = False                   │
    └──────────────┬──────────────────┘
                   │
                   ▼
    ┌─────────────────────────────────┐
    │ For j from 0 to N-1             │
    │ (search for next_val)           │
    └──────────────┬──────────────────┘
                   │
                   ▼
    ┌─────────────────────────────────┐
    │   Is arr[j] == next_val?        │
    └────┬──────────────────────┬─────┘
         │ Yes                  │ No
         │                      │
         ▼                      ▼
    ┌─────────┐           (Continue
    │found=True│            searching)
    │ break   │
    └────┬────┘
         │
         └──────────┬──────────┘
                    │
                    ▼
    ┌─────────────────────────────────┐
    │   Is found == True?             │
    └────┬──────────────────────┬─────┘
         │ Yes                  │ No
         │                      │
         ▼                      ▼
    ┌──────────────┐      ┌─────────┐
    │current_len++ │      │  break  │
    └──────┬───────┘      │ (exit   │
           │              │  while) │
           │              └────┬────┘
           │                   │
           └───────┐           │
                   │           │
                   └───┐   ┌───┘
                       │   │
                       ▼   ▼
    ┌─────────────────────────────────┐
    │ Update max_len:                 │
    │ max_len = max(max_len,          │
    │               current_len)      │
    └──────────────┬──────────────────┘
                   │
                   └──────┐
                          │
                          ▼
    ┌─────────────────────────────────┐
    │ All elements processed?         │
    └────┬──────────────────────┬─────┘
         │ No (continue loop)   │ Yes
         │                      │
         └──────────┐           ▼
                    │   ┌──────────────┐
                    │   │Return max_len│
                    │   └──────────────┘
                    │
                    └───► (back to outer loop)

WHY IS THIS APPROACH INEFFICIENT?
==================================
Time Complexity Analysis:
- Outer loop: N iterations (for each element)
- Middle loop: Can extend up to N times (for longest sequence)
- Inner loop: N iterations (searching for next value)
- Total: O(N) × O(N) × O(N) = O(N³)

Example: For array of size 1000
- Brute Force: 1,000,000,000 operations (1 billion!)
- Hash Set: 1,000 operations (1 thousand)
- Difference: 1,000,000x slower!

REDUNDANT WORK:
- We search for the same elements multiple times
- Example: Starting from 1, we search for 2, 3, 4
- Then starting from 2, we search for 3, 4 again (redundant!)
- Hash set eliminates this by O(1) lookups

OPTIMAL APPROACH (Hash Set - Not Implemented):
===============================================
```python
def longest_consecutive_optimal(arr, n):
    # Store all elements in a hash set
    num_set = set(arr)
    max_len = 0

    for num in num_set:
        # Only start counting if this is the beginning of a sequence
        # (i.e., num-1 is not in the set)
        if num - 1 not in num_set:
            current_num = num
            current_len = 1

            # Extend the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_len += 1

            max_len = max(max_len, current_len)

    return max_len
```

Time Complexity: O(N) - Each element visited at most twice
Space Complexity: O(N) - Hash set storage

TIME COMPLEXITY (BRUTE FORCE):
===============================
- Outer loop: O(N)
- For each element, we try to extend sequence: O(N) in worst case
- For each extension, we search entire array: O(N)
- Total: O(N³)
- Very inefficient for large arrays!

SPACE COMPLEXITY: O(1)
- Only using a few variables (max_len, current_len, start_val, etc.)
- No extra data structures

EDGE CASES:
===========
1. Single element: [5] → 1
2. All consecutive: [1, 2, 3, 4, 5] → 5
3. No consecutive pairs: [1, 3, 5, 7, 9] → 1
4. Duplicates: [1, 2, 2, 3] → 3 (duplicates don't extend sequence)
5. Reverse order: [5, 4, 3, 2, 1] → 5
6. Multiple sequences: [1, 2, 10, 11, 12] → 3
"""


class Solution:
    """
    Solution class for finding the longest consecutive subsequence.

    This implementation uses a brute force approach with O(N³) time complexity.
    For each element, it tries to extend a consecutive sequence by searching
    the entire array for the next consecutive number.

    For production code, consider using the hash set approach which achieves
    O(N) time complexity.
    """

    def longest(self, arr, N):
        """
        Finds the length of the longest subsequence of consecutive integers
        in the array using a brute-force approach.

        The algorithm treats each element as a potential start of a consecutive
        sequence and tries to extend it by searching for consecutive numbers
        in the array.

        Args:
            arr (list): Array of positive integers
            N (int): Length of the array

        Returns:
            int: Length of the longest consecutive subsequence

        Example:
            arr = [1, 9, 3, 10, 4, 20, 2], N = 7
            Returns: 4 (sequence: [1, 2, 3, 4])

        Time Complexity: O(N³)
            - Outer loop: O(N) - Try each element as start
            - Middle while loop: O(N) - Extend sequence up to N times
            - Inner for loop: O(N) - Search for next value
            - Total: O(N) × O(N) × O(N) = O(N³)

        Space Complexity: O(1)
            - Only uses a constant amount of extra space
            - No additional data structures
        """
        # Initialize the maximum run length found so far to 1
        # Minimum length is always 1 (single element itself)
        max_len = 1

        # Outer loop: Consider each element as the start of a sequence
        # We try every possible starting point to ensure we don't miss
        # the optimal sequence
        for i in range(N):
            # Current element is the candidate starting value
            start_val = arr[i]

            # Length of the current consecutive run
            # Initially 1 (just the starting element)
            current_len = 1

            # Attempt to extend the sequence one step at a time
            # We keep looking for start_val+1, start_val+2, etc.
            while True:
                # Calculate the next consecutive number we're looking for
                # Example: If start_val=5 and current_len=3,
                # we're looking for 5+3=8 (after finding 6, 7)
                next_val = start_val + current_len

                # Flag to track if we found next_val in the array
                found = False

                # Inner loop: Scan through the entire array to find next_val
                # This is the inefficient part - O(N) search for each extension
                for j in range(N):
                    if arr[j] == next_val:
                        # Found the next consecutive number!
                        found = True
                        break  # Stop scanning once found

                # Check if we successfully extended the sequence
                if found:
                    # We found the next consecutive number
                    # Increment length and continue looking for the next one
                    current_len += 1
                else:
                    # Cannot extend further - next consecutive number not in array
                    # Exit the while loop
                    break

            # After fully extending from this starting point,
            # update the global maximum if this sequence was longer
            if current_len > max_len:
                max_len = current_len

        # Return the length of the longest consecutive run discovered
        return max_len


# Test cases
if __name__ == "__main__":
    s = Solution()

    # Test 1: Basic example with consecutive subsequence
    arr1 = [1, 9, 3, 10, 4, 20, 2]
    n1 = len(arr1)
    print(f"Array: {arr1}")
    print(f"Longest consecutive length: {s.longest(arr1, n1)}")  # Expected: 4
    print(f"Explanation: Sequence [1, 2, 3, 4] has length 4\n")

    # Test 2: Longer consecutive sequence in middle
    arr2 = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
    n2 = len(arr2)
    print(f"Array: {arr2}")
    print(f"Longest consecutive length: {s.longest(arr2, n2)}")  # Expected: 5
    print(f"Explanation: Sequence [32, 33, 34, 35, 36] has length 5\n")

    # Test 3: Entire array is consecutive
    arr3 = [1, 2, 3, 4, 5]
    n3 = len(arr3)
    print(f"Array: {arr3}")
    print(f"Longest consecutive length: {s.longest(arr3, n3)}")  # Expected: 5
    print(f"Explanation: Entire array is consecutive\n")

    # Test 4: Consecutive sequence starting from 0
    arr4 = [2, 0, 6, 1, 5, 3, 7]
    n4 = len(arr4)
    print(f"Array: {arr4}")
    print(f"Longest consecutive length: {s.longest(arr4, n4)}")  # Expected: 4
    print(f"Explanation: Sequence [0, 1, 2, 3] has length 4\n")

    # Test 5: No consecutive pairs
    arr5 = [1, 3, 5, 7, 9]
    n5 = len(arr5)
    print(f"Array: {arr5}")
    print(f"Longest consecutive length: {s.longest(arr5, n5)}")  # Expected: 1
    print(f"Explanation: No consecutive pairs exist\n")

    # Test 6: Single element
    arr6 = [42]
    n6 = len(arr6)
    print(f"Array: {arr6}")
    print(f"Longest consecutive length: {s.longest(arr6, n6)}")  # Expected: 1

    # Test 7: Reverse order consecutive
    arr7 = [5, 4, 3, 2, 1]
    n7 = len(arr7)
    print(f"\nArray: {arr7}")
    print(f"Longest consecutive length: {s.longest(arr7, n7)}")  # Expected: 5
    print(f"Explanation: Sequence [1, 2, 3, 4, 5] exists in array (order doesn't matter)")

    # Test 8: Multiple sequences, find longest
    arr8 = [1, 2, 10, 11, 12, 13]
    n8 = len(arr8)
    print(f"\nArray: {arr8}")
    print(f"Longest consecutive length: {s.longest(arr8, n8)}")  # Expected: 4
    print(f"Explanation: Sequence [10, 11, 12, 13] has length 4 (longer than [1, 2])")
