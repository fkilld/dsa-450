"""
PROBLEM: ANARC05B - The Double HeLiX (SPOJ)
Two strictly increasing integer sequences are given. Common integers are intersection points.
You can start at the beginning of either sequence and walk forward. At each intersection,
you can choose to switch sequences or continue. Find the maximum sum path.
Link: https://www.spoj.com/problems/ANARC05B/

WHY THIS SOLUTION:
This is a TWO POINTER + GREEDY problem.

Naive: Try all possible paths - O(2^k) where k is number of intersections!
Two Pointer: O(n + m) - single pass through both arrays

KEY INSIGHT:
Between two intersection points, we MUST take the path with higher sum.
At each intersection, we:
1. Compare sums accumulated on both paths since last intersection
2. Take the maximum sum path
3. Add the intersection point value
4. Reset both path sums

APPROACH:
1. Use two pointers (i for a1, j for a2)
2. Maintain running sums s1 and s2 for each path
3. While both pointers valid:
   - If a1[i] < a2[j]: Add to s1, increment i
   - If a2[j] < a1[i]: Add to s2, increment j
   - If equal (intersection):
     - Add max(s1, s2) + intersection_value to total
     - Reset s1 and s2
     - Increment both pointers
4. Process remaining elements in either array
5. Add max(s1, s2) to handle the last segment

TIME COMPLEXITY: O(n + m) - single pass through both arrays
SPACE COMPLEXITY: O(1) - only using pointers and sums

EXAMPLE: a1 = [3,5,7,9,20,25], a2 = [1,4,7,11,14,25]
Intersection points: 7, 25
Path 1: 3+5 = 8, then 7 (intersection)
Path 2: 1+4 = 5, then 7 (intersection)
Take max(8, 5) + 7 = 15

Between 7 and 25:
Path 1: 9+20 = 29
Path 2: 11+14 = 25
Take max(29, 25) + 25 = 54

Total: 15 + 54 = 69

WHY INTERVIEWER WILL ACCEPT:
1. Two pointer technique mastery
2. Greedy choice correctness proof
3. Handles sorted array merging
4. Optimal O(n+m) solution
"""

# ANARC05B - The Double HeLiX
# Link: https://www.spoj.com/problems/ANARC05B/

a1 = [int(x) for x in input("Enter 1st arr: ").split()]
a2 = [int(x) for x in input("Enter 2nd arr: ").split()]

def max_sum(a1, a2):
    """
    Find maximum sum path through two sorted arrays with intersection points.

    Args:
        a1: First sorted array
        a2: Second sorted array

    Returns:
        Maximum sum achievable
    """
    n = len(a1)
    m = len(a2)
    s1, s2 = 0, 0  # Running sums for each path
    i, j = 0, 0    # Pointers for each array
    total = 0      # Total maximum sum

    # Traverse both arrays simultaneously
    while i < n and j < m:
        if a1[i] < a2[j]:
            # Element only in a1, add to s1 path
            s1 += a1[i]
            i += 1
        elif a2[j] < a1[i]:
            # Element only in a2, add to s2 path
            s2 += a2[j]
            j += 1
        else:
            # Intersection point found!
            # Choose the path with maximum sum up to this point
            total += max(s1, s2) + a1[i]
            i += 1
            j += 1
            s1, s2 = 0, 0  # Reset path sums for next segment

    # Process remaining elements in a1
    while i < n:
        s1 += a1[i]
        i += 1

    # Process remaining elements in a2
    while j < m:
        s2 += a2[j]
        j += 1

    # Add the maximum of the last segment
    total += max(s1, s2)

    return total

# Note: The original code uses a1[1::] and a2[1::] suggesting the first element
# might be the array size in the input format
result = max_sum(a1, a2)
print(f"Maximum sum path: {result}")
    