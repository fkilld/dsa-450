"""
PROBLEM: Majority Element (Boyer-Moore Voting Algorithm)
Find the element that appears more than n/2 times in an array.

WHY THIS SOLUTION:
Naive approach: Use HashMap to count frequencies - O(n) time, O(n) space
Optimized approach: Boyer-Moore Voting Algorithm - O(n) time, O(1) space!

This is the FAMOUS Boyer-Moore Majority Vote Algorithm - a must-know for interviews!

KEY INSIGHT: Cancellation Property
If majority element exists (appears > n/2 times), it will "survive" a cancellation process where:
- Each occurrence of majority element "cancels out" one occurrence of any other element
- Since majority > n/2, it will remain after all cancellations

Think of it like a battle: majority vs all others. Majority will win because it's > 50%!

APPROACH:
1. PHASE 1: Find candidate (using voting/cancellation)
   - Track a candidate and its count
   - If current element == candidate: count++
   - If current element != candidate: count--
   - If count becomes 0: switch candidate

2. PHASE 2: Verify candidate (important!)
   - The algorithm guarantees: IF majority exists, candidate is correct
   - But it doesn't guarantee majority EXISTS
   - So we must verify by counting occurrences

TIME COMPLEXITY: O(n) - two passes
SPACE COMPLEXITY: O(1) - only variables

EXAMPLE: arr = [2, 2, 1, 1, 1, 2, 2]
Phase 1 (Finding candidate):
  i=0: candidate=2, count=1
  i=1: candidate=2, count=2
  i=2: candidate=2, count=1 (different element, count--)
  i=3: candidate=2, count=0
  i=4: count=0, switch to candidate=1, count=1
  i=5: candidate=1, count=0 (different element)
  i=6: count=0, switch to candidate=2, count=1

Phase 2 (Verification):
  Count occurrences of 2: appears 4 times out of 7
  4 > 7/2 → 2 is majority element ✓

WHY INTERVIEWER WILL ACCEPT:
- Classic algorithm (Boyer-Moore) that every strong candidate should know
- Optimizes space from O(n) to O(1)
- Shows deep understanding of the majority property
"""

arr = [int(x) for x in input("Enter the array : ").split()]
n = len(arr)

# PHASE 1: Find candidate using Boyer-Moore Voting
# The candidate is the element that "survives" the cancellation process
candidate = arr[0]  # Start with first element as candidate
count = 1

for i in range(1, n):
    if arr[i] == candidate:
        # Same element, increase support
        count += 1
    else:
        # Different element, reduce support (cancellation)
        count -= 1

    # If count reaches 0, switch candidate
    # This means previous elements "cancelled out"
    if count == 0:
        candidate = arr[i]
        count = 1

# PHASE 2: Verify if candidate is actually majority
# This step is CRUCIAL - the algorithm doesn't guarantee majority exists
verification_count = 0
for el in arr:
    if el == candidate:
        verification_count += 1

# Check if candidate appears more than n/2 times
if verification_count > n // 2:
    print(f"Majority Element: {candidate}")
    print(f"Appears {verification_count} times out of {n}")
else:
    print("Majority Element does not exist")
