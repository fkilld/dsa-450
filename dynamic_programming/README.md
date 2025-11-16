# Dynamic Programming Solutions

## Table of Contents
- [What is Dynamic Programming?](#what-is-dynamic-programming)
- [When to Use Dynamic Programming](#when-to-use-dynamic-programming)
- [DP Approach Patterns](#dp-approach-patterns)
- [How to Solve DP Problems](#how-to-solve-dp-problems)
- [Problem Index](#problem-index)

## What is Dynamic Programming?

Dynamic Programming (DP) is an algorithmic paradigm that solves complex problems by breaking them down into simpler subproblems. It stores the results of subproblems to avoid redundant calculations, trading space for time efficiency.

### Key Characteristics:
1. **Optimal Substructure**: The optimal solution can be constructed from optimal solutions of its subproblems
2. **Overlapping Subproblems**: The same subproblems are solved multiple times
3. **Memoization/Tabulation**: Store results to avoid recomputation

## When to Use Dynamic Programming

Consider DP when you encounter:
- Problems asking for optimization (maximum/minimum)
- Problems asking for counting (number of ways)
- Problems with choices at each step
- Problems where brute force has overlapping subproblems

### DP vs Greedy vs Divide & Conquer:
- **Greedy**: Makes locally optimal choices (may not give global optimum)
- **Divide & Conquer**: Subproblems are independent
- **DP**: Subproblems overlap and depend on each other

## DP Approach Patterns

### 1. Top-Down (Memoization)
- Start with the original problem
- Recursively break it down
- Store results in a cache (usually a dictionary or array)
- Check cache before computing

```python
def solve(n, memo={}):
    if n in memo:
        return memo[n]
    # Base case
    if n <= 1:
        return n
    # Recursive case
    memo[n] = solve(n-1, memo) + solve(n-2, memo)
    return memo[n]
```

### 2. Bottom-Up (Tabulation)
- Start with the smallest subproblem
- Build up to the original problem
- Store results in a table (usually an array)
- No recursion overhead

```python
def solve(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

## How to Solve DP Problems

### Step-by-Step Framework:

#### 1. Identify if it's a DP Problem
- Does it ask for optimization?
- Are there overlapping subproblems?
- Can you make choices at each step?

#### 2. Define the State
- What parameters uniquely identify a subproblem?
- What information do you need to make a decision?

#### 3. Write the Recurrence Relation
- How does the current state relate to previous states?
- What are the choices at each state?

#### 4. Identify Base Cases
- What are the simplest subproblems?
- What happens at boundaries?

#### 5. Decide Implementation Approach
- Top-down (easier to write, has recursion overhead)
- Bottom-up (better performance, requires careful ordering)

#### 6. Optimize Space (if needed)
- Can you reduce dimensions?
- Do you only need previous results?

### Example: Fibonacci Number

**Problem**: Find the nth Fibonacci number

**1. Identify**: Has overlapping subproblems (fib(n) = fib(n-1) + fib(n-2))

**2. State**: `dp[i]` = ith Fibonacci number

**3. Recurrence**: `dp[i] = dp[i-1] + dp[i-2]`

**4. Base Case**: `dp[0] = 0, dp[1] = 1`

**5. Implementation**:
```python
# Bottom-up O(n) time, O(n) space
def fib(n):
    if n <= 1: return n
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Space optimized O(n) time, O(1) space
def fib_optimized(n):
    if n <= 1: return n
    prev, curr = 0, 1
    for i in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
```

## Common DP Patterns

### 1. Linear DP (1D)
- State depends on previous elements
- Examples: Climbing Stairs, House Robber, Maximum Subarray

### 2. Knapsack Pattern
- Include/exclude decisions
- Examples: 0/1 Knapsack, Subset Sum, Partition Equal Subset Sum

### 3. Unbounded Knapsack
- Can use items multiple times
- Examples: Coin Change, Rod Cutting

### 4. Longest Common Subsequence (LCS)
- Two sequences comparison
- Examples: LCS, Edit Distance, Shortest Common Supersequence

### 5. Palindrome Pattern
- Check/build palindromes
- Examples: Longest Palindromic Subsequence, Palindrome Partitioning

### 6. Grid/Matrix DP
- 2D grid traversal
- Examples: Unique Paths, Minimum Path Sum, Dungeon Game

### 7. Interval DP
- Process ranges/intervals
- Examples: Matrix Chain Multiplication, Burst Balloons

## Interview Tips

### 1. Always Clarify
- Ask about constraints (array size, value ranges)
- Confirm input/output format
- Check for edge cases

### 2. Start with Brute Force
- Explain the recursive solution first
- Identify overlapping subproblems
- Show how DP optimizes it

### 3. Explain Your Thought Process
- Walk through the state definition
- Explain the recurrence relation
- Trace through a small example

### 4. Analyze Complexity
- Time: Usually O(number of states × time per state)
- Space: Size of DP table (mention space optimization if possible)

### 5. Code Clean and Test
- Use meaningful variable names
- Add comments for complex logic
- Test with edge cases (empty input, single element, etc.)

## Problem Index

| #  | Problem | Pattern | Difficulty |
|----|---------|---------|------------|
| 0  | Coin Change | Unbounded Knapsack | Medium |
| 1  | 0-1 Knapsack | Knapsack | Medium |
| 2  | Binomial Coefficient | Math + DP | Medium |
| 3  | Permutation Coefficient | Math + DP | Medium |
| 10 | Assembly Line Scheduling | Linear DP | Medium |
| 20 | Longest Subsequence (diff=1) | LIS Variation | Medium |

## Resources

### Books:
- "Introduction to Algorithms" (CLRS) - Chapter on Dynamic Programming
- "Algorithm Design Manual" by Skiena

### Online:
- [GeeksforGeeks DP Tutorial](https://www.geeksforgeeks.org/dynamic-programming/)
- [LeetCode DP Patterns](https://leetcode.com/tag/dynamic-programming/)
- [Codeforces DP Tutorial](https://codeforces.com/blog/entry/43256)

### Practice Platforms:
- LeetCode (DP tag)
- Codeforces
- AtCoder (DP contests)
- HackerRank

---

**Note**: Each problem file contains:
- Problem description
- Approach explanation with reasoning
- Flowchart (using Mermaid diagrams)
- Detailed code with comments
- Time and space complexity analysis
