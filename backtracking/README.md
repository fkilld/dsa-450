# Backtracking Problems - Complete Guide

## Table of Contents
- [Introduction to Backtracking](#introduction-to-backtracking)
- [Problem List](#problem-list)
- [Key Concepts](#key-concepts)
- [Interview Tips](#interview-tips)
- [Time Complexities](#time-complexities)

---

## Introduction to Backtracking

**Backtracking** is an algorithmic technique that considers searching through all possible configurations to find a solution. It builds candidates incrementally and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly lead to a valid solution.

### Core Principles:
1. **Choice**: At each step, make a choice from available options
2. **Constraint**: Check if the choice satisfies constraints
3. **Goal**: Check if we've reached the goal/solution
4. **Backtrack**: If current path doesn't work, undo the choice and try another

### General Template:
```python
def backtrack(state):
    if is_goal(state):
        save_solution(state)
        return

    for choice in available_choices(state):
        if is_valid(choice, state):
            make_choice(choice, state)
            backtrack(state)
            undo_choice(choice, state)  # Backtrack
```

---

## Problem List

### 1. Combinatorial Problems

| File | Problem | Difficulty | Key Concepts |
|------|---------|-----------|--------------|
| `0.py` | **Rat in a Maze** | Medium | Grid traversal, Path finding |
| `6.py` | **Palindrome Partitioning** | Medium | String partitioning, Palindrome check |
| `13.py` | **String Permutations** | Medium | Swapping, All permutations |

### 2. Constraint Satisfaction Problems (CSP)

| File | Problem | Difficulty | Key Concepts |
|------|---------|-----------|--------------|
| `1.py` | **N-Queens** | Hard | Diagonal tracking, Column placement |
| `4.py` | **Sudoku Solver** | Hard | Row/Column/Box constraints |
| `5.py` | **M-Coloring** | Medium | Graph coloring, Adjacency check |

### 3. Subset and Partition Problems

| File | Problem | Difficulty | Key Concepts |
|------|---------|-----------|--------------|
| `2.py` | **Word Break II** | Hard | String matching, Dictionary |
| `7.py` | **Equal Subset Sum** | Medium | Subset sum, DP optimization |
| `9.py` | **Tug of War** | Medium | Min difference, Equal partitions |
| `11.py` | **Combination Sum II** | Medium | Avoiding duplicates, Target sum |
| `17.py` | **K Subset Partition** | Hard | K-way partition, Equal sums |

### 4. Path and Tour Problems

| File | Problem | Difficulty | Key Concepts |
|------|---------|-----------|--------------|
| `8.py` | **Knight's Tour** | Hard | Chess moves, Hamiltonian path |
| `10.py` | **Safe Route with Landmines** | Medium | BFS/DFS, Unsafe cells |
| `14.py` | **Path > K Length** | Medium | Weighted graph, Path length |
| `16.py` | **All Paths in Matrix** | Medium | 2D grid, Path enumeration |

### 5. Optimization Problems

| File | Problem | Difficulty | Key Concepts |
|------|---------|-----------|--------------|
| `12.py` | **Largest Number K Swaps** | Medium | Greedy + Backtracking, Optimization |

---

## Key Concepts

### 1. State Space Tree
Every backtracking problem can be visualized as a state space tree where:
- **Nodes** represent partial solutions
- **Edges** represent choices/decisions
- **Leaves** represent complete solutions or dead ends

### 2. Pruning
Eliminate branches that cannot lead to a solution:
```python
if not is_valid(current_choice):
    continue  # Prune this branch
```

### 3. Choice vs Decision
- **Choice**: What options are available?
- **Constraint**: What makes a choice valid?
- **Goal**: When do we have a complete solution?

### 4. Common Patterns

#### Pattern 1: Generate All Solutions (N-Queens, Rat in Maze)
```python
def solve(state):
    if is_complete(state):
        result.append(copy(state))
        return

    for choice in choices:
        if is_valid(choice):
            make_choice(choice)
            solve(state)
            undo_choice(choice)
```

#### Pattern 2: Find One Solution (Sudoku, Graph Coloring)
```python
def solve(state):
    if is_complete(state):
        return True

    for choice in choices:
        if is_valid(choice):
            make_choice(choice)
            if solve(state):
                return True
            undo_choice(choice)

    return False
```

#### Pattern 3: Optimization (Largest Number in K Swaps)
```python
def solve(state):
    if is_complete(state):
        global_max = max(global_max, current_value)
        return

    for choice in choices:
        if is_promising(choice):
            make_choice(choice)
            solve(state)
            undo_choice(choice)
```

---

## Interview Tips

### 1. Problem Identification
**How to recognize a backtracking problem:**
- ✅ Need to explore all/multiple possible solutions
- ✅ Problem has constraints that must be satisfied
- ✅ Can make incremental choices
- ✅ Able to detect invalid states early
- ✅ Involves permutations, combinations, or subsets

### 2. Interview Approach
```
Step 1: Clarify the problem
  - What are the constraints?
  - Do we need all solutions or just one?
  - What's the expected output format?

Step 2: Identify the choices
  - What decisions do we make at each step?
  - What's the order of making choices?

Step 3: Define base cases
  - When have we found a complete solution?
  - When should we stop exploring?

Step 4: Implement validation
  - How do we check if a choice is valid?
  - What constraints must be satisfied?

Step 5: Code the backtracking
  - Make choice
  - Recurse
  - Undo choice (backtrack)

Step 6: Optimize if needed
  - Add memoization
  - Prune invalid branches early
  - Use better data structures
```

### 3. Common Pitfalls
```python
# ❌ Forgetting to backtrack
state.append(choice)
solve(state)
# Missing: state.pop()

# ✅ Correct backtracking
state.append(choice)
solve(state)
state.pop()  # Always undo

# ❌ Modifying shared state without copying
result.append(current_path)  # current_path changes later!

# ✅ Proper copying
result.append(current_path[:])  # or deepcopy()

# ❌ Not checking validity before recursion
make_choice()
solve()

# ✅ Check before making choice
if is_valid():
    make_choice()
    solve()
    undo_choice()
```

### 4. Explaining Your Solution
Use the "3-C Framework":
1. **Choices**: "At each step, I can choose to..."
2. **Constraints**: "A choice is valid only if..."
3. **Complete**: "I know I have a solution when..."

Example:
> "In N-Queens, at each **column**, I **choose** to place a queen in any row. A placement is **valid** if no other queen attacks it (checked via row and diagonal arrays). The solution is **complete** when all N queens are placed."

---

## Time Complexities

| Problem | Time Complexity | Space Complexity | Notes |
|---------|----------------|------------------|-------|
| Rat in Maze | O(4^(N²)) | O(N²) | 4 directions, N×N grid |
| N-Queens | O(N!) | O(N²) | N positions for first queen, N-1 for second... |
| Word Break II | O(2^N * N) | O(N) | Exponential combinations |
| Sudoku Solver | O(9^(N²)) | O(N²) | 9 choices per empty cell |
| M-Coloring | O(M^V) | O(V) | M colors, V vertices |
| Palindrome Partition | O(N * 2^N) | O(N) | 2^N partitions, N palindrome check |
| Equal Subset Sum | O(N * Sum) | O(N * Sum) | DP optimization |
| Knight's Tour | O(8^(N²)) | O(N²) | 8 moves per position |
| Tug of War | O(2^N) | O(N) | Include/exclude each element |
| Landmines Path | O(N * M * 4^(N*M)) | O(N * M) | DFS worst case |
| Combination Sum | O(2^N) | O(N) | Include/exclude decisions |
| K Swaps | O(N^K) | O(N) | N choices, K levels deep |
| Permutations | O(N! * N) | O(N) | N! permutations, N to generate each |
| Path > K Length | O(V!) | O(V) | All paths exploration |
| All Matrix Paths | O(2^(M+N)) | O(M+N) | Right/down decisions |
| K Subset Partition | O(k * 2^N) | O(N) | K subsets, 2^N combinations |

---

## Problem-Solving Checklist

Before coding any backtracking problem:

- [ ] Identify what choices you make at each step
- [ ] Define what makes a choice valid (constraints)
- [ ] Determine the base case (goal state)
- [ ] Decide if you need all solutions or just one
- [ ] Plan how to represent state (array, set, etc.)
- [ ] Consider what to backtrack (undo operations)
- [ ] Think about optimization (pruning, memoization)
- [ ] Write test cases including edge cases

---

## Running the Solutions

Each file is self-contained with test cases. To run any solution:

```bash
# Run individual problem
python3 backtracking/0.py

# Run all problems (from parent directory)
for file in backtracking/*.py; do
    echo "Running $file..."
    python3 "$file"
    echo "---"
done
```

---

## Study Plan

### Week 1: Fundamentals
1. Day 1-2: Rat in Maze (0.py) - Basic grid backtracking
2. Day 3-4: Permutations (13.py) - Swapping technique
3. Day 5-7: N-Queens (1.py) - Constraint satisfaction

### Week 2: Intermediate
1. Day 1-2: Palindrome Partition (6.py) - String problems
2. Day 3-4: Combination Sum (11.py) - Subset problems
3. Day 5-7: Sudoku (4.py) - Complex constraints

### Week 3: Advanced
1. Day 1-2: Knight's Tour (8.py) - Hard path problems
2. Day 3-4: K Subset Partition (17.py) - Multi-way partition
3. Day 5-7: Review and practice variations

---

## Additional Resources

### Practice Platforms
- LeetCode: Filter by "Backtracking" tag
- GeeksforGeeks: Backtracking category
- HackerRank: Recursion and Backtracking

### Related Topics
- Dynamic Programming (optimization of backtracking)
- Branch and Bound (optimization problems)
- Constraint Satisfaction Problems
- Graph Theory (for path/tour problems)

---

## Contributing

If you find any bugs or have suggestions for improvements:
1. Test the solution thoroughly
2. Document the issue clearly
3. Provide example test cases
4. Suggest the fix with explanation

---

**Good luck with your interview preparation! Remember: Practice makes perfect, but understanding makes it permanent.** 🚀
