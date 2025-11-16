"""
PROBLEM: Kth Smallest Number Again (HackerEarth)
Given N ranges [A, B], and Q queries asking for kth smallest number
considering all numbers in the union of all ranges.

WHY THIS SOLUTION:
Naive approach: Generate all numbers from all ranges - O(N * max_range) space!
We use INTERVAL MERGING to avoid generating actual numbers:
1. Merge overlapping ranges
2. For each query, walk through merged ranges counting elements

KEY INSIGHT:
After merging overlapping ranges, we have disjoint sorted ranges.
To find kth element:
- Walk through ranges in order
- Subtract each range's size from k
- When k becomes <= current range size, answer is in this range

APPROACH:
1. Sort ranges by start point
2. Merge overlapping ranges:
   - If ranges[i-1].end >= ranges[i].start, they overlap
   - Merge by extending end to max(ranges[i-1].end, ranges[i].end)
3. For each query k:
   - Iterate through merged ranges
   - If range size >= k, answer = range.start + k - 1
   - Else, subtract range size from k and continue

TIME COMPLEXITY:
- Sorting ranges: O(N log N)
- Merging: O(N)
- Each query: O(N) in worst case
- Total: O(N log N + Q*N)

SPACE COMPLEXITY: O(N) - for storing ranges

EXAMPLE: Ranges = [[1,4], [3,7], [10,15]]
After sorting: [[1,4], [3,7], [10,15]]
After merging: [[1,7], [10,15]]
- Range [1,7] has 7 elements: 1,2,3,4,5,6,7
- Range [10,15] has 6 elements: 10,11,12,13,14,15

Query k=5: In range [1,7], answer = 1+5-1 = 5
Query k=10: Range [1,7] has 7 elements, so k'=10-7=3
           In range [10,15], answer = 10+3-1 = 12

WHY INTERVIEWER WILL ACCEPT:
1. Shows interval merging technique
2. Space optimization by not generating all numbers
3. Understanding of range arithmetic
4. Handles overlapping intervals correctly
"""

# Kth smallest number again (Important Question)
# HackerEarth

n, q = input().split()
n = int(n)
q = int(q)

ranges = []

# Read N ranges
for i in range(n):
    a, b = input("Enter A, B: ").split()
    ranges.append([int(a), int(b)])

# Sort ranges by start point
ranges.sort()

# Merge overlapping ranges
idx = 0
for i in range(1, len(ranges)):
    # Check if current range overlaps with previous
    if ranges[idx][1] >= ranges[i][0]:
        # Merge: extend the end point
        ranges[idx][1] = max(ranges[idx][1], ranges[i][1])
    else:
        # No overlap, move to next position
        idx += 1
        ranges[idx] = ranges[i]

# Now ranges[0..idx] contains all merged ranges

# Process Q queries
for i in range(q):
    k = int(input("Enter k: "))
    ans = -1

    # Walk through merged ranges to find kth element
    for j in range(idx + 1):
        range_size = ranges[j][1] - ranges[j][0] + 1

        if range_size >= k:
            # kth element is in this range
            ans = ranges[j][0] + k - 1
            break
        else:
            # Skip this entire range
            k -= range_size

    if ans != -1:
        print(f"The {i+1}th query answer: {ans}")
    else:
        print(f"The {i+1}th query: k is out of range")
