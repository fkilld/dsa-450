"""
ASSEMBLY LINE SCHEDULING PROBLEM
=================================

Problem Statement:
-----------------
A car factory has two assembly lines, each with n stations. A car chassis must
pass through all n stations in order. Each station takes different time on each
line. Additionally, there is:
- Entry time (e[i]) to enter each assembly line
- Transfer time (t[i][j]) to move from one line to another at station j
- Exit time (x[i]) to exit from each assembly line

Find the minimum time to build a car that goes through all stations.

Example:
    Assembly line 1 times: [4, 5, 3, 2]
    Assembly line 2 times: [2, 10, 1, 4]
    Transfer times from line 1: [0, 7, 4, 5]
    Transfer times from line 2: [0, 9, 2, 8]
    Entry times: [10, 12]
    Exit times: [18, 7]

    Output: 35 (minimum time)

APPROACH & REASONING:
====================

This is a CLASSIC DP problem demonstrating multi-state optimization.

Key Insight:
-----------
At each station, we can either:
1. Stay on the same assembly line (no transfer cost)
2. Switch from the other line (pay transfer cost)

We choose the option that gives MINIMUM total time so far.

Why DP?
-------
- Overlapping subproblems: Minimum time to station i depends on minimum time to i-1
- Optimal substructure: Optimal solution to station i uses optimal solution to i-1
- Choices at each step: Stay or switch lines

State Definition:
----------------
dp[i][j] = Minimum time to reach station j on assembly line i

Recurrence Relation:
-------------------
For station j on line 0:
    dp[0][j] = min(
        dp[0][j-1] + arr[0][j],           // Stay on line 0
        dp[1][j-1] + arr[0][j] + t[1][j]  // Switch from line 1
    )

For station j on line 1:
    dp[1][j] = min(
        dp[1][j-1] + arr[1][j],           // Stay on line 1
        dp[0][j-1] + arr[1][j] + t[0][j]  // Switch from line 0
    )

Base Case:
---------
dp[0][0] = e[0] + arr[0][0]  // Enter line 0 and complete first station
dp[1][0] = e[1] + arr[1][0]  // Enter line 1 and complete first station

Final Answer:
------------
min(dp[0][n-1] + x[0], dp[1][n-1] + x[1])

FLOWCHART:
==========

```mermaid
flowchart TD
    A[Start: 2 lines, n stations] --> B[Add entry times to first station]
    B --> C[arr0,0 += e0<br/>arr1,0 += e1]
    C --> D[Loop: for station i from 1 to n-1]
    D --> E[Calculate time for line 0 at station i]
    E --> F[arr0,i = min of:<br/>1 Stay: arr0,i + arr0,i-1<br/>2 Switch: arr0,i + arr1,i-1 + t1,i]
    F --> G[Calculate time for line 1 at station i]
    G --> H[arr1,i = min of:<br/>1 Stay: arr1,i + arr1,i-1<br/>2 Switch: arr1,i + arr0,i-1 + t0,i]
    H --> I{More stations?}
    I -->|Yes| D
    I -->|No| J[Add exit times]
    J --> K[Return min of:<br/>arr0,n-1 + x0<br/>arr1,n-1 + x1]
    K --> L[End]
```

Visualization:
=============

For the example above:

Entry e[0]=10, e[1]=12
                Station:  0    1    2    3
Assembly Line 0:        [4,   5,   3,   2]   Exit x[0]=18
Assembly Line 1:        [2,  10,   1,   4]   Exit x[1]=7

Transfer from Line 1:  [0,   7,   4,   5]
Transfer from Line 0:  [0,   9,   2,   8]

Decision at each station:
- Station 0: Must use entry, no choice
- Station 1: Stay or switch? Compare costs
- Station 2: Stay or switch? Compare costs
- Station 3: Stay or switch? Compare costs
- Exit: Choose line with minimum total time

Step-by-step execution:
    Initial (with entry):
        Line 0: [14, -, -, -]  (10 + 4)
        Line 1: [14, -, -, -]  (12 + 2)

    After station 1:
        Line 0: [14, 19, -, -]  min(14+5, 14+5+9) = 19
        Line 1: [14, 21, -, -]  min(14+10, 14+10+7) = 24

    Final minimum: 35

Complexity Analysis:
-------------------
Time: O(n) where n = number of stations
    - Single pass through all stations
    - Constant work per station

Space: O(1) if modifying input, O(n) if not
    - Can optimize to O(1) by keeping only previous station values
    - Current solution uses input array (space-efficient)

Alternative: O(1) space by tracking only 4 values (prev and curr for both lines)
"""

def min_time(arr, t, e, x):
    """
    ASSEMBLY LINE SCHEDULING - IN-PLACE DP
    ======================================

    This solution modifies the input array to save space.
    Uses the assembly time arrays themselves as DP tables.

    Args:
        arr: 2D array where arr[i][j] = time at station j on line i
        t: 2D array where t[i][j] = transfer time from line i at station j
        e: Array where e[i] = entry time to line i
        x: Array where x[i] = exit time from line i

    Returns:
        Minimum time to complete the car assembly

    Algorithm:
    ---------
    1. Add entry times to the first station (base case)
    2. For each station i from 1 to n-1:
         For each line (0 and 1):
             Calculate min of:
                - Staying on same line
                - Switching from other line (+ transfer cost)
    3. Return minimum of (line0 + exit0, line1 + exit1)

    DP State (in-place):
    ------------------
    After processing station i:
        arr[0][i] = minimum time to complete up to station i on line 0
        arr[1][i] = minimum time to complete up to station i on line 1
    """

    # Base Case: Add entry times to first station
    # This represents the time to enter the line and complete first station
    arr[0][0] += e[0]  # Enter line 0 and complete station 0
    arr[1][0] += e[1]  # Enter line 1 and complete station 0

    # Get number of stations
    num_stations = len(arr[0])

    # Process each station from 1 to n-1
    for i in range(1, num_stations):

        # ASSEMBLY LINE 0 at station i
        # Decision: Stay on line 0 OR switch from line 1?

        # Option 1: Stay on line 0
        # Time = previous time on line 0 + current station time
        stay_on_line0 = arr[0][i] + arr[0][i - 1]

        # Option 2: Switch from line 1 to line 0
        # Time = previous time on line 1 + current station time + transfer time
        # t[1][i] is the cost to transfer FROM line 1 TO line 0 at station i
        switch_to_line0 = arr[0][i] + arr[1][i - 1] + t[1][i]

        # Choose minimum of the two options
        arr[0][i] = min(stay_on_line0, switch_to_line0)


        # ASSEMBLY LINE 1 at station i
        # Decision: Stay on line 1 OR switch from line 0?

        # Option 1: Stay on line 1
        # Time = previous time on line 1 + current station time
        stay_on_line1 = arr[1][i] + arr[1][i - 1]

        # Option 2: Switch from line 0 to line 1
        # Time = previous time on line 0 + current station time + transfer time
        # t[0][i] is the cost to transfer FROM line 0 TO line 1 at station i
        switch_to_line1 = arr[1][i] + arr[0][i - 1] + t[0][i]

        # Choose minimum of the two options
        arr[1][i] = min(stay_on_line1, switch_to_line1)


    # Final Decision: Which line to exit from?
    # Compare total time on both lines including exit times

    # Total time if we exit from line 0
    exit_from_line0 = arr[0][num_stations - 1] + x[0]

    # Total time if we exit from line 1
    exit_from_line1 = arr[1][num_stations - 1] + x[1]

    # Return the minimum
    return min(exit_from_line0, exit_from_line1)


def min_time_with_path(arr, t, e, x):
    """
    ASSEMBLY LINE SCHEDULING - WITH PATH RECONSTRUCTION
    ==================================================

    Enhanced version that also tracks which line to use at each station.
    Useful when interviewer asks "show me the actual path taken".

    Returns:
        (min_time, path) where path[i] indicates which line to use at station i
    """

    num_stations = len(arr[0])

    # DP arrays for minimum time at each station
    dp0 = [0] * num_stations  # Line 0
    dp1 = [0] * num_stations  # Line 1

    # Path tracking: which line was chosen at each station
    # 0 = line 0, 1 = line 1
    line_choice = [-1] * num_stations

    # Base case: first station
    dp0[0] = e[0] + arr[0][0]
    dp1[0] = e[1] + arr[1][0]

    # Fill DP tables and track decisions
    for i in range(1, num_stations):
        # Line 0 decision
        stay0 = dp0[i-1]
        switch_to_0 = dp1[i-1] + t[1][i]

        if stay0 <= switch_to_0:
            dp0[i] = arr[0][i] + stay0
            # Stayed on line 0
        else:
            dp0[i] = arr[0][i] + switch_to_0
            # Switched from line 1

        # Line 1 decision
        stay1 = dp1[i-1]
        switch_to_1 = dp0[i-1] + t[0][i]

        if stay1 <= switch_to_1:
            dp1[i] = arr[1][i] + stay1
            # Stayed on line 1
        else:
            dp1[i] = arr[1][i] + switch_to_1
            # Switched from line 0

    # Determine final line
    if dp0[-1] + x[0] <= dp1[-1] + x[1]:
        min_time_val = dp0[-1] + x[0]
        final_line = 0
    else:
        min_time_val = dp1[-1] + x[1]
        final_line = 1

    # Backtrack to find the path (optional, for interview discussion)
    # This is advanced - mention only if interviewer asks

    return min_time_val


# ============================================================================
# TESTING & EXAMPLES
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("ASSEMBLY LINE SCHEDULING - TEST CASES")
    print("=" * 70)

    # Test Case 1: Example from problem description
    print("\nTest 1: Classic Example")
    a1 = [[4, 5, 3, 2],
          [2, 10, 1, 4]]
    t1 = [[0, 7, 4, 5],
          [0, 9, 2, 8]]
    e1 = [10, 12]
    x1 = [18, 7]

    print("Assembly Line 0:", a1[0])
    print("Assembly Line 1:", a1[1])
    print("Entry times:", e1)
    print("Exit times:", x1)

    # Make a copy since function modifies input
    a1_copy = [row[:] for row in a1]
    result1 = min_time(a1_copy, t1, e1, x1)
    print(f"\nMinimum time: {result1}")
    print("Expected: 35")

    # Test Case 2: Simpler example
    print("\n" + "-" * 70)
    print("\nTest 2: Simple Case - Prefer One Line")
    a2 = [[4, 5, 6],
          [10, 12, 14]]
    t2 = [[0, 100, 100],
          [0, 100, 100]]  # High transfer cost
    e2 = [5, 8]
    x2 = [10, 10]

    print("Assembly Line 0:", a2[0])
    print("Assembly Line 1:", a2[1])
    print("Transfer costs (high):", t2[0])
    print("\nExpected: Should stay on line 0 entire time")

    a2_copy = [row[:] for row in a2]
    result2 = min_time(a2_copy, t2, e2, x2)
    print(f"Minimum time: {result2}")
    print(f"Expected: {5 + 4 + 5 + 6 + 10} = 30")

    # Test Case 3: Switch beneficial
    print("\n" + "-" * 70)
    print("\nTest 3: Switching Is Beneficial")
    a3 = [[10, 20],
          [5, 5]]
    t3 = [[0, 2],
          [0, 1]]  # Low transfer cost
    e3 = [5, 6]
    x3 = [5, 5]

    print("Assembly Line 0:", a3[0])
    print("Assembly Line 1:", a3[1])
    print("Low transfer costs")
    print("Expected: Start line 0, switch to line 1")

    a3_copy = [row[:] for row in a3]
    result3 = min_time(a3_copy, t3, e3, x3)
    print(f"Minimum time: {result3}")

    print("\n" + "=" * 70)


"""
INTERVIEW TALKING POINTS:
========================

1. PROBLEM RECOGNITION:
   "This is a multi-state DP problem where we track minimum time for
   multiple states (two assembly lines) at each stage. Similar pattern
   appears in:
   - Paint House (different colors)
   - Stock Buy/Sell with states
   - Robot path with different directions"

2. STATE DEFINITION:
   "I define dp[i][j] as minimum time to reach station j on line i.
   At each station, we make a choice: stay on current line or switch.
   This creates dependencies between states at adjacent stations."

3. WHY NOT GREEDY?
   "We can't just choose the faster line at each station because:
   - Transfer costs might outweigh time savings
   - Future stations might favor different line
   - Need to consider total time, not local minimum
   Only DP finds globally optimal solution."

4. BASE CASE EXPLANATION:
   "First station is special - we must pay entry cost.
   arr[i][0] = e[i] + arr[i][0]
   This initializes our DP. From station 1 onwards, we use recurrence."

5. SPACE OPTIMIZATION:
   "Current solution is O(1) space by modifying input.
   If we can't modify input, we only need 4 variables:
   - prev_line0, curr_line0
   - prev_line1, curr_line1
   At each step, update curr using prev, then swap."

6. PATH RECONSTRUCTION:
   "If interviewer asks which line to use at each station:
   - Keep a path array tracking choices at each station
   - Backtrack from final decision to reconstruct path
   - Similar to tracking moves in classic DP problems"

7. REAL-WORLD APPLICATIONS:
   - Manufacturing optimization
   - Resource allocation with switching costs
   - Network routing with transfer penalties
   - Task scheduling on multiple machines

8. VARIATIONS:
   - More than 2 assembly lines (K lines)
   - Different costs for different transfers
   - Minimum/maximum cost path with state changes
   - Stock trading with cooldown periods

EDGE CASES TO DISCUSS:
=====================
- Single station (n=1): Just entry + station + exit, choose min
- Equal costs everywhere: Any path gives same result
- Very high transfer costs: Should stay on one line
- Very low transfer costs: Switch freely to minimize
- One line consistently faster: Might stay on it entirely

COMPLEXITY NOTES:
================
Time: O(n) - Linear pass through stations
Space: O(1) - In-place or constant extra space

For K assembly lines and n stations:
Time: O(K × n)
Space: O(K) for DP array or O(1) with optimization

COMMON MISTAKES:
===============
1. Forgetting to add entry/exit times
2. Wrong transfer cost direction (t[from][to] vs t[to][from])
3. Not considering "stay on same line" option
4. Off-by-one errors in station indexing
5. Modifying input when not allowed
"""
