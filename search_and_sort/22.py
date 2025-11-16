"""
PROBLEM: Allocate Minimum Number of Pages
Given N books with pages arr[i], allocate books to M students such that:
1. Each student gets at least one book
2. Books are allocated in contiguous manner
3. MINIMIZE the MAXIMUM pages allocated to any student

WHY THIS SOLUTION:
This is another BINARY SEARCH ON ANSWER problem!
We binary search on the maximum pages a student can get.

Naive: Try all possible allocations - O(M^N) - exponential!
Binary Search: O(N log(sum of pages))

KEY INSIGHT:
If we can allocate books such that no student gets more than X pages,
we can also allocate with max pages > X. This monotonic property enables binary search!

Search space: [max(arr), sum(arr)]
- Lower bound: At least max(arr) because one student must get the largest book
- Upper bound: sum(arr) when one student gets all books

APPROACH:
1. Binary search on maximum pages per student
2. For each mid value, check: "Can we allocate to M students with max pages = mid?"
   - Greedy: Allocate books sequentially to current student
   - When adding next book exceeds mid, assign to next student
   - If we need > M students, allocation is not possible
3. If possible with mid pages, try smaller (ub = mid - 1)
   If not possible, need more pages (lb = mid + 1)

TIME COMPLEXITY: O(N * log(sum))
- Binary search: log(sum of all pages) iterations
- Each check: O(N) to scan all books
- Total: O(N log(sum))

SPACE COMPLEXITY: O(1) - only using variables

EXAMPLE: books = [12, 34, 67, 90], M = 2
Total = 203, max = 90
Binary search on [90, 203]:
- mid=146: [12,34,67]=113, [90]=90 - works! Try smaller
- mid=118: [12,34,67]=113, [90]=90 - works!
- mid=104: [12,34]=46, [67]=67, [90]=90 - needs 3 students, doesn't work
- mid=111: [12,34,67]=113 exceeds, [12,34]=46, [67,90]=157 exceeds - doesn't work
Answer: 113

WHY INTERVIEWER WILL ACCEPT:
1. Recognizes binary search on answer pattern
2. Understanding of greedy allocation
3. Handles edge cases (book larger than mid)
4. Classic interview problem
"""

# Allocate minimum number of pages

n = int(input("Enter n : "))
arr = []
for i in range(n):
    arr.append(int(input("Enter book pages : ")))
m = int(input("Enter the number of students : "))

def solve(arr, n, mid, m):
    """
    Check if we can allocate books to m students
    such that no student gets more than 'mid' pages.

    Args:
        arr: Array of page counts
        n: Number of books
        mid: Maximum pages per student to try
        m: Number of students

    Returns:
        True if allocation possible, False otherwise
    """
    std = 1  # Current student number
    sum_pages = 0  # Pages allocated to current student

    for i in range(n):
        # If a single book has more pages than mid, impossible
        if arr[i] > mid:
            return False

        # If adding this book exceeds mid pages
        if sum_pages + arr[i] > mid:
            # Allocate to next student
            std += 1
            sum_pages = arr[i]
            # If we need more than m students, not possible
            if std > m:
                return False
        else:
            # Add book to current student
            sum_pages += arr[i]

    return True

def get_min_max(arr, m):
    """
    Find minimum of maximum pages allocated to any student.

    Args:
        arr: Array of page counts
        m: Number of students

    Returns:
        Minimum possible value of maximum pages
    """
    total_pages = sum(arr)

    # Binary search bounds
    lb = max(arr)  # At least one student must get the largest book
    ub = total_pages  # One student gets all books
    ans = ub

    while lb <= ub:
        mid = (lb + ub) // 2

        # Can we allocate with max pages = mid?
        if solve(arr, len(arr), mid, m):
            ans = mid  # This works, try smaller
            ub = mid - 1
        else:
            lb = mid + 1  # Need more pages

    return ans

result = get_min_max(arr, m)
print(f"Minimum of maximum pages: {result}")

