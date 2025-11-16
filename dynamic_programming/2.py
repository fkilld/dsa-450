"""
BINOMIAL COEFFICIENT PROBLEM
=============================

Problem Statement:
-----------------
Calculate the binomial coefficient C(n, k) or "n choose k", which represents
the number of ways to choose k items from n items without regard to order.

Mathematical Definition:
    C(n, k) = n! / (k! * (n-k)!)

Example:
    Input: n = 5, k = 2
    Output: 10
    Explanation: Ways to choose 2 items from 5:
        {1,2}, {1,3}, {1,4}, {1,5}, {2,3}, {2,4}, {2,5}, {3,4}, {3,5}, {4,5}

APPROACH & REASONING:
====================

Why NOT just compute factorials?
--------------------------------
- For large n, factorial becomes huge (overflow issues)
- Computing three factorials is inefficient
- Intermediate results might not fit in standard data types

Pascal's Triangle Property:
--------------------------
The key insight is Pascal's Identity:
    C(n, k) = C(n-1, k-1) + C(n-1, k)

Intuition:
    When choosing k items from n items, consider the nth item:
    - Either we include it: then choose (k-1) from remaining (n-1) items
    - Or we exclude it: then choose k from remaining (n-1) items

This gives us OVERLAPPING SUBPROBLEMS → Perfect for DP!

Base Cases:
----------
- C(n, 0) = 1  (one way to choose 0 items: choose nothing)
- C(n, n) = 1  (one way to choose all items)
- C(n, k) = 0  if k > n (can't choose more items than available)

FLOWCHART (Space-Optimized Approach):
====================================

```mermaid
flowchart TD
    A[Start: n, k] --> B[Create dp array of size k+1]
    B --> C[Initialize dp0 = 1<br/>Base: C0,0 = 1]
    C --> D[Loop: for i from 1 to n]
    D --> E[Set j = mini, k]
    E --> F[Loop: while j > 0]
    F --> G[dpj += dpj-1]
    G --> H[j = j - 1]
    H --> I{j > 0?}
    I -->|Yes| F
    I -->|No| J{More rows i?}
    J -->|Yes| D
    J -->|No| K[Return dpk % 10^9+7]
    K --> L[End]
```

Pascal's Triangle Visualization:
================================

Row 0:           1
Row 1:         1   1
Row 2:       1   2   1
Row 3:     1   3   3   1
Row 4:   1   4   6   4   1
Row 5: 1   5  10  10   5   1

Each number = sum of two numbers directly above it
C(5,2) = 10 (row 5, position 2)

Three Approaches:
================

1. DIRECT FORMULA (Mathematical):
   C(n,k) = n×(n-1)×...×(n-k+1) / (1×2×...×k)
   Time: O(k), Space: O(1)
   Issue: Intermediate overflow for large values

2. 2D DP (Full Pascal's Triangle):
   Build entire triangle up to row n
   Time: O(n×k), Space: O(n×k)
   Clear but uses more space

3. 1D DP (Space Optimized):
   Only keep current row, build bottom-up
   Time: O(n×k), Space: O(k)
   BEST APPROACH for interviews

Complexity Analysis:
-------------------
Space-Optimized DP:
    Time: O(n × k) - build n rows, each with up to k updates
    Space: O(k) - single array of size k+1

Direct Formula:
    Time: O(k) - multiply k terms
    Space: O(1) - only variables

2D DP:
    Time: O(n × k)
    Space: O(n × k) - full Pascal's triangle
"""

class Solution:

    def nCr(self, n, k):
        """
        SPACE-OPTIMIZED DP APPROACH (1D Array)
        =====================================

        This is the RECOMMENDED approach for interviews because:
        - Optimal space complexity O(k)
        - Easy to implement
        - Handles large numbers with modulo
        - No overflow issues with factorials

        Args:
            n: Total number of items
            k: Number of items to choose

        Returns:
            C(n, k) modulo (10^9 + 7)

        Algorithm:
        ---------
        We build Pascal's triangle row by row, but only keep current row.
        Each element is sum of element directly above and above-left.

        DP State:
        --------
        dp[j] = C(current_row, j)

        For row i, we update:
            dp[j] = dp[j] + dp[j-1]
            (which is C(i-1,j) + C(i-1,j-1) = C(i,j))

        Why traverse j from right to left?
        ---------------------------------
        We need OLD values of dp[j-1] to compute NEW values of dp[j].
        If we go left to right, we'd overwrite dp[j-1] before using it.
        Going right to left preserves the values we need.

        Example trace for C(5, 2):
        -------------------------
        Initial: dp = [1, 0, 0]

        Row 1:   dp = [1, 1, 0]   (j from 1 to 1)
        Row 2:   dp = [1, 2, 1]   (j from 2 to 1)
        Row 3:   dp = [1, 3, 3]   (j from 2 to 1)
        Row 4:   dp = [1, 4, 6]   (j from 2 to 1)
        Row 5:   dp = [1, 5, 10]  (j from 2 to 1)

        Result: dp[2] = 10
        """

        # Edge case: can't choose more items than available
        if k > n:
            return 0

        # Optimization: C(n, k) = C(n, n-k), choose smaller
        if k > n - k:
            k = n - k

        # dp[j] will store C(current_row, j)
        # We only need values from 0 to k
        dp = [0 for i in range(k + 1)]

        # Base case: C(anything, 0) = 1
        # There's exactly one way to choose 0 items: choose nothing
        dp[0] = 1

        # Build Pascal's triangle row by row from 1 to n
        for i in range(1, n + 1):
            # For row i, we need to update positions 1 to min(i, k)
            # We can't have more positions than row number or k
            j = min(i, k)

            # Update from right to left to avoid overwriting needed values
            # This is crucial! Left to right would give wrong results
            while j > 0:
                # Pascal's identity: C(i,j) = C(i-1,j) + C(i-1,j-1)
                # dp[j] currently holds C(i-1, j)
                # dp[j-1] currently holds C(i-1, j-1)
                # We update dp[j] to C(i, j)
                dp[j] += dp[j - 1]

                # Apply modulo to prevent overflow
                # Standard practice for combinatorics problems
                dp[j] %= (10**9 + 7)

                j -= 1

        # dp[k] now contains C(n, k)
        return dp[k] % (10**9 + 7)


    def nCr_2d(self, n, k):
        """
        2D DP APPROACH (Full Pascal's Triangle)
        =======================================

        This approach builds the entire Pascal's triangle.
        Easier to understand but uses more space.

        DP State:
        --------
        dp[i][j] = C(i, j) = ways to choose j items from i items

        Recurrence:
        ----------
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

        Space: O(n × k)
        Time: O(n × k)
        """

        # Create 2D DP table
        dp = [[0 for j in range(k + 1)] for i in range(n + 1)]

        # Base case: C(i, 0) = 1 for all i
        for i in range(n + 1):
            dp[i][0] = 1

        # Fill the table using Pascal's identity
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                # C(i,j) = C(i-1,j-1) + C(i-1,j)
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % (10**9 + 7)

        return dp[n][k]


    def binomial_coefficient(self, n, k):
        """
        MATHEMATICAL FORMULA APPROACH
        ============================

        Direct computation using the formula:
        C(n,k) = n! / (k! × (n-k)!)
               = [n × (n-1) × ... × (n-k+1)] / [1 × 2 × ... × k]

        Optimization: C(n, k) = C(n, n-k)
        We choose the smaller of k and n-k to minimize computation.

        This is FASTEST but can overflow for large values.
        Only use when n and k are small enough.

        Time: O(k)
        Space: O(1)

        How it works:
        ------------
        Instead of computing full factorials (which overflow),
        we incrementally multiply and divide:

        res = 1
        res = res × n / 1       = n/1
        res = res × (n-1) / 2   = n(n-1)/2
        res = res × (n-2) / 3   = n(n-1)(n-2)/(1×2×3)
        ...

        This keeps intermediate values smaller and avoids overflow.
        """

        # Optimization: use smaller value
        # C(n, k) = C(n, n-k)
        if k > n - k:
            k = n - k

        res = 1

        # Calculate C(n, k) = n*(n-1)*...*(n-k+1) / (1*2*...*k)
        # Do multiplication and division together to avoid overflow
        for i in range(k):
            # Multiply by (n - i)
            res = res * (n - i)

            # Divide by (i + 1)
            # Integer division is safe here because C(n,k) is always integer
            res = res // (i + 1)

        return res


# ============================================================================
# TESTING & EXAMPLES
# ============================================================================

if __name__ == "__main__":
    sol = Solution()

    print("=" * 70)
    print("BINOMIAL COEFFICIENT - TEST CASES")
    print("=" * 70)

    # Test Case 1: Basic example
    print("\nTest 1: C(5, 2)")
    n1, k1 = 5, 2
    print(f"1D DP:      C({n1},{k1}) = {sol.nCr(n1, k1)}")
    print(f"2D DP:      C({n1},{k1}) = {sol.nCr_2d(n1, k1)}")
    print(f"Formula:    C({n1},{k1}) = {sol.binomial_coefficient(n1, k1)}")
    print(f"Expected: 10")

    # Test Case 2: Larger example
    print("\n" + "-" * 70)
    print("\nTest 2: C(10, 3)")
    n2, k2 = 10, 3
    print(f"1D DP:      C({n2},{k2}) = {sol.nCr(n2, k2)}")
    print(f"2D DP:      C({n2},{k2}) = {sol.nCr_2d(n2, k2)}")
    print(f"Formula:    C({n2},{k2}) = {sol.binomial_coefficient(n2, k2)}")
    print(f"Expected: 120")

    # Test Case 3: Edge case - choose 0
    print("\n" + "-" * 70)
    print("\nTest 3: C(5, 0)")
    n3, k3 = 5, 0
    print(f"1D DP:      C({n3},{k3}) = {sol.nCr(n3, k3)}")
    print(f"Expected: 1 (one way to choose nothing)")

    # Test Case 4: Edge case - choose all
    print("\n" + "-" * 70)
    print("\nTest 4: C(7, 7)")
    n4, k4 = 7, 7
    print(f"1D DP:      C({n4},{k4}) = {sol.nCr(n4, k4)}")
    print(f"Expected: 1 (one way to choose everything)")

    # Test Case 5: Symmetric property
    print("\n" + "-" * 70)
    print("\nTest 5: C(10, 3) = C(10, 7)")
    n5, k5a, k5b = 10, 3, 7
    result_a = sol.nCr(n5, k5a)
    result_b = sol.nCr(n5, k5b)
    print(f"C({n5},{k5a}) = {result_a}")
    print(f"C({n5},{k5b}) = {result_b}")
    print(f"Equal: {result_a == result_b}")

    # Test Case 6: Large numbers (with modulo)
    print("\n" + "-" * 70)
    print("\nTest 6: C(100, 50) mod 10^9+7")
    n6, k6 = 100, 50
    print(f"1D DP:      C({n6},{k6}) mod 10^9+7 = {sol.nCr(n6, k6)}")
    print("(Very large number, showing modulo result)")

    print("\n" + "=" * 70)


"""
INTERVIEW TALKING POINTS:
========================

1. PROBLEM RECOGNITION:
   "This is asking for binomial coefficient, which appears in:
   - Combinatorics problems
   - Probability calculations
   - Pascal's Triangle
   - Number of paths in grid (with restrictions)"

2. WHY NOT FACTORIALS?
   "Direct factorial computation has problems:
   - n! grows extremely fast (factorial of 20 already exceeds long)
   - Computing three factorials is wasteful
   - Division might lose precision with floating point
   DP approach avoids all these issues."

3. PASCAL'S TRIANGLE CONNECTION:
   "The recurrence C(n,k) = C(n-1,k-1) + C(n-1,k) comes from
   Pascal's Triangle. Each number is sum of two above it.
   This gives us overlapping subproblems → perfect for DP!"

4. APPROACH SELECTION:
   "I'll use 1D DP with O(k) space because:
   - Space efficient (vs O(n×k) for 2D)
   - Handles large numbers with modulo
   - Same time complexity as 2D
   - Standard approach for combinatorics problems"

5. WHY RIGHT TO LEFT?
   "When updating dp[j] = dp[j] + dp[j-1], we need the OLD value
   of dp[j-1]. If we go left to right, we overwrite dp[j-1] before
   using it for dp[j+1]. Right to left preserves needed values."

6. OPTIMIZATION TRICK:
   "Since C(n,k) = C(n,n-k), we can always use min(k, n-k).
   This cuts computation time in half when k > n/2."

7. APPLICATIONS:
   - Counting combinations and permutations
   - Grid path problems (unique paths)
   - Probability and statistics
   - Generating subsets
   - Pascal's Triangle problems

8. RELATED PROBLEMS:
   - Unique Paths in grid: C(m+n-2, m-1)
   - Catalan Numbers: Uses binomial coefficients
   - Probability calculations
   - Subset generation

EDGE CASES:
==========
- k = 0: Always returns 1
- k = n: Always returns 1
- k > n: Returns 0 (can't choose more than available)
- Large n: Use modulo to prevent overflow
- Negative inputs: Invalid (should handle gracefully)

COMMON MISTAKES:
===============
1. Not using modulo for large numbers
2. Going left to right in 1D DP (overwrites needed values)
3. Not optimizing k (should use min(k, n-k))
4. Off-by-one errors in loop bounds
5. Integer overflow with factorial approach
"""
