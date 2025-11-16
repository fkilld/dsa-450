# Stacks and Queues - DSA 450

A comprehensive collection of Stack and Queue problems with detailed solutions, explanations, flowcharts, and complexity analysis.

## Table of Contents

- [Overview](#overview)
- [Data Structure Implementations](#data-structure-implementations)
- [Stack Problems](#stack-problems)
- [Queue Problems](#queue-problems)
- [Advanced Problems](#advanced-problems)
- [Problem Index](#problem-index)

## Overview

This folder contains 33+ problems covering fundamental and advanced concepts of Stacks and Queues. Each solution includes:

- ✅ **Problem Statement**: Clear description of the problem
- ✅ **Approach & Reasoning**: Why we use this approach
- ✅ **Flowchart**: Visual representation of the algorithm
- ✅ **Detailed Comments**: Line-by-line explanation
- ✅ **Time & Space Complexity**: Big-O analysis
- ✅ **Test Cases**: Example usage and edge cases

## Key Concepts

### Stack (LIFO - Last In First Out)
- Operations: push, pop, peek, isEmpty
- Applications: Expression evaluation, bracket matching, undo operations
- Time Complexity: O(1) for all operations

### Queue (FIFO - First In First Out)
- Operations: enqueue, dequeue, front, rear
- Applications: BFS, scheduling, resource sharing
- Time Complexity: O(1) for all operations

## Data Structure Implementations

| File | Problem | Difficulty | Time | Space |
|------|---------|------------|------|-------|
| [0.py](0.py) | **Stack Implementation** | Basic | O(1) | O(n) |
| [1.py](1.py) | **Circular Queue Implementation** | Basic | O(1) | O(n) |
| [2.py](2.py) | **Two Stacks in One Array** | Medium | O(1) | O(1) |
| [3.py](3.py) | **Stack with Middle Element Operations** | Medium | O(1) | O(n) |
| [24.py](24.py) | **Circular Queue** | Medium | O(1) | O(n) |

## Stack Problems

### Basic Stack Applications

| File | Problem | Approach | Time | Space |
|------|---------|----------|------|-------|
| [5.py](5.py) | **Balanced Parentheses** | Stack for matching pairs | O(n) | O(n) |
| [6.py](6.py) | **Reverse String using Stack** | Push all chars, then pop | O(n) | O(n) |
| [7.py](7.py) | **Special Stack (GetMin)** | Auxiliary stack for min | O(1) | O(n) |
| [11.py](11.py) | **Evaluate Postfix Expression** | Stack for operands | O(n) | O(n) |
| [12.py](12.py) | **Insert at Bottom of Stack** | Recursion | O(n) | O(n) |
| [13.py](13.py) | **Reverse Stack using Recursion** | Recursion + Insert at bottom | O(n²) | O(n) |
| [14.py](14.py) | **Sort Stack using Recursion** | Recursion + Sorted insert | O(n²) | O(n) |

### Advanced Stack Problems

| File | Problem | Approach | Time | Space |
|------|---------|----------|------|-------|
| [8.py](8.py) | **Next Greater Element** | Monotonic stack | O(n) | O(n) |
| [37.py](37.py) | **Next Smaller Element** | Monotonic stack | O(n) | O(n) |
| [15.py](15.py) | **Merge Overlapping Intervals** | Sort + Stack | O(n log n) | O(n) |
| [16.py](16.py) | **Max Rectangular Area in Histogram** | Stack for heights | O(n) | O(n) |
| [17.py](17.py) | **Longest Valid Parentheses** | Stack for indices | O(n) | O(n) |
| [18.py](18.py) | **Redundant Brackets** | Stack + operator check | O(n) | O(n) |
| [9.py](9.py) | **Celebrity Problem** | Stack elimination | O(n) | O(n) |

### Conversion Problems

| File | Problem | Approach | Time | Space |
|------|---------|----------|------|-------|
| [19.py](19.py) | **Stack using Queue** | Two queues | O(n) push | O(n) |
| [22.py](22.py) | **Queue using Stack** | Two stacks | O(1) amortized | O(n) |
| [21.py](21.py) | **Stack Permutations** | Simulation | O(n) | O(n) |

## Queue Problems

### Basic Queue Applications

| File | Problem | Approach | Time | Space |
|------|---------|----------|------|-------|
| [26.py](26.py) | **Reverse Queue using Recursion** | Recursion | O(n) | O(n) |
| [27.py](27.py) | **Reverse First K Elements** | Stack + Queue | O(n) | O(k) |
| [28.py](28.py) | **Interleave Queue Halves** | Auxiliary queue | O(n) | O(n) |
| [36.py](36.py) | **First Non-Repeating Character (Stream)** | Queue + HashMap | O(n) | O(26) |

### Advanced Queue Problems

| File | Problem | Approach | Time | Space |
|------|---------|----------|------|-------|
| [29.py](29.py) | **Circular Tour (Petrol Pumps)** | Queue simulation | O(n) | O(1) |
| [30.py](30.py) | **Rotten Oranges (BFS)** | Multi-source BFS | O(n×m) | O(n×m) |
| [31.py](31.py) | **Distance to Nearest 1** | Multi-source BFS | O(n×m) | O(n×m) |
| [25.py](25.py) | **LRU Cache** | OrderedDict / DLL+HashMap | O(1) | O(capacity) |

### Sliding Window with Deque

| File | Problem | Approach | Time | Space |
|------|---------|----------|------|-------|
| [32.py](32.py) | **First Negative in Window K** | Deque | O(n) | O(k) |
| [34.py](34.py) | **Sum of Min+Max in All Subarrays K** | Two deques | O(n) | O(k) |
| [35.py](35.py) | **Min Sum of Squares after K Removals** | Priority Queue | O(n log n) | O(n) |

## Problem Index

### By Difficulty

**Easy (10)**
- Stack Implementation (0.py)
- Queue Implementation (1.py)
- Balanced Parentheses (5.py)
- Reverse String (6.py)
- Postfix Evaluation (11.py)
- Insert at Bottom (12.py)
- Reverse Queue (26.py)
- First Negative in Window (32.py)
- Next Greater Element (8.py)
- Next Smaller Element (37.py)

**Medium (18)**
- Two Stacks in Array (2.py)
- Stack with Middle Operations (3.py)
- Special Stack (7.py)
- Reverse Stack (13.py)
- Sort Stack (14.py)
- Merge Intervals (15.py)
- Longest Valid Parentheses (17.py)
- Redundant Brackets (18.py)
- Stack using Queue (19.py)
- Queue using Stack (22.py)
- Stack Permutations (21.py)
- Circular Queue (24.py)
- Reverse First K (27.py)
- Interleave Queue (28.py)
- Circular Tour (29.py)
- First Non-Repeating (36.py)
- Sum Min+Max Subarrays (34.py)
- Min Sum Squares (35.py)

**Hard (5)**
- Max Rectangular Area (16.py)
- Celebrity Problem (9.py)
- Rotten Oranges (30.py)
- Distance to Nearest 1 (31.py)
- LRU Cache (25.py)

### By Pattern

**Monotonic Stack**
- Next Greater Element (8.py)
- Next Smaller Element (37.py)
- Max Rectangular Area (16.py)
- Merge Intervals (15.py)

**Recursion with Stack**
- Reverse Stack (13.py)
- Sort Stack (14.py)
- Insert at Bottom (12.py)
- Reverse Queue (26.py)

**BFS with Queue**
- Rotten Oranges (30.py)
- Distance to Nearest 1 (31.py)

**Sliding Window with Deque**
- First Negative in Window (32.py)
- Sum of Min+Max (34.py)

**Design Problems**
- Two Stacks in Array (2.py)
- Stack with Middle Operations (3.py)
- Special Stack (7.py)
- LRU Cache (25.py)
- Stack using Queue (19.py)
- Queue using Stack (22.py)

## Interview Tips

### When to Use Stack:
1. **Matching pairs**: Balanced parentheses, valid HTML tags
2. **Next/Previous Greater/Smaller**: Use monotonic stack
3. **Recursion simulation**: DFS, expression evaluation
4. **Undo operations**: Browser history, text editor
5. **Expression parsing**: Infix to postfix, evaluation

### When to Use Queue:
1. **Order preservation**: FIFO scheduling, printer queue
2. **BFS traversal**: Level order, shortest path
3. **Sliding window**: First negative, maximum in window
4. **Stream processing**: First non-repeating character
5. **Resource sharing**: CPU scheduling, IO buffers

### Common Patterns:
1. **Two Stack/Queue trick**: Reverse, implement one using other
2. **Monotonic Stack**: NGE, NSE, histogram problems
3. **Auxiliary data structure**: GetMin in O(1)
4. **Multi-source BFS**: Rotten oranges, distance problems
5. **Deque for sliding window**: Min/max in all subarrays

## Complexity Cheat Sheet

| Operation | Stack | Queue | Deque |
|-----------|-------|-------|-------|
| Insert | O(1) | O(1) | O(1) |
| Delete | O(1) | O(1) | O(1) |
| Peek/Front | O(1) | O(1) | O(1) |
| Search | O(n) | O(n) | O(n) |
| Space | O(n) | O(n) | O(n) |

## How to Use This Repository

1. **Start with basics**: Begin with files 0.py, 1.py to understand implementations
2. **Practice by pattern**: Group similar problems (NGE, BFS, etc.)
3. **Understand flowcharts**: Visual representation helps in interviews
4. **Analyze complexity**: Every solution has time/space analysis
5. **Try variations**: Modify problems to practice different scenarios

## Contributing

Each solution follows this structure:
```python
"""
PROBLEM: [Clear problem statement]
APPROACH & REASONING: [Why this approach?]
FLOWCHART: [Visual algorithm representation]
TIME COMPLEXITY: [Big-O analysis]
SPACE COMPLEXITY: [Memory usage]
"""
# Detailed comments in code
# Example usage and test cases
```

## Resources

- [GeeksforGeeks - Stack](https://www.geeksforgeeks.org/stack-data-structure/)
- [GeeksforGeeks - Queue](https://www.geeksforgeeks.org/queue-data-structure/)
- [LeetCode Stack Problems](https://leetcode.com/tag/stack/)
- [LeetCode Queue Problems](https://leetcode.com/tag/queue/)

---

**Happy Coding! 🚀**

*All solutions are optimized for interview settings with clear explanations and proper complexity analysis.*
