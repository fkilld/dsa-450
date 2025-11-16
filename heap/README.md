# Heap / Priority Queue Problems

This folder contains solutions to common heap and priority queue problems, with detailed explanations, flowcharts, and interview tips.

## Table of Contents

1. [Heap Fundamentals](#heap-fundamentals)
2. [Problem List](#problem-list)
3. [Key Concepts](#key-concepts)
4. [Common Patterns](#common-patterns)
5. [Interview Tips](#interview-tips)

---

## Heap Fundamentals

### What is a Heap?

A **heap** is a specialized tree-based data structure that satisfies the heap property:
- **Max Heap**: Parent node ≥ all its children
- **Min Heap**: Parent node ≤ all its children

### Heap as Array

Heaps are typically implemented as arrays with these index relationships:
- For node at index `i`:
  - Left child: `2*i + 1`
  - Right child: `2*i + 2`
  - Parent: `(i-1) // 2`

### Key Operations

| Operation | Time Complexity | Description |
|-----------|----------------|-------------|
| Insert | O(log n) | Add element and bubble up |
| Extract Min/Max | O(log n) | Remove root and bubble down |
| Peek Min/Max | O(1) | View root element |
| Build Heap | O(n) | Convert array to heap |
| Heapify | O(log n) | Maintain heap property |

---

## Problem List

### Basic Heap Operations

| File | Problem | Difficulty | Key Concept |
|------|---------|-----------|-------------|
| `0.py` | **Build Max Heap** | Easy | Heapify from bottom-up |
| `1.py` | **Heap Sort** | Medium | Extract max repeatedly |
| `15.py` | **Convert Min to Max Heap** | Easy | Re-heapify with different property |

### K-th Element Problems

| File | Problem | Difficulty | Approach |
|------|---------|-----------|----------|
| `3.py` | **K Largest Elements** | Medium | Max heap - extract K times |
| `4.py` | **Kth Smallest Element** | Medium | Min heap or Max heap of size K |
| `7.py` | **Kth Largest Sum Subarray** | Hard | Min heap of size K with prefix sums |

### Merge Problems

| File | Problem | Difficulty | Strategy |
|------|---------|-----------|----------|
| `5.py` | **Merge K Sorted Arrays** | Medium | Min heap with (value, row, col) |
| `6.py` | **Merge Two Max Heaps** | Easy | Concatenate and heapify |
| `9.py` | **Merge K Sorted Linked Lists** | Hard | Min heap with list nodes |

### Range and Stream Problems

| File | Problem | Difficulty | Technique |
|------|---------|-----------|-----------|
| `10.py` | **Smallest Range in K Lists** | Hard | Min heap + tracking max |
| `11.py` | **Median in Stream** | Hard | Two heaps (max + min) |

### Greedy with Heap

| File | Problem | Difficulty | Pattern |
|------|---------|-----------|---------|
| `13.py` | **Minimum Cost of Ropes** | Medium | Always combine smallest |
| `17.py` | **Minimum Sum** | Medium | Distribute digits greedily |

### String Rearrangement

| File | Problem | Difficulty | Approach |
|------|---------|-----------|----------|
| `8.py` | **Reorganize String** | Medium | Max heap with frequency |
| `16.py` | **Rearrange Characters** | Medium | Two approaches provided |

### Tree Validation

| File | Problem | Difficulty | Method |
|------|---------|-----------|--------|
| `12.py` | **Is Binary Tree Heap** | Medium | Level order + heap property check |
| `14.py` | **Convert BST to Min Heap** | Medium | Inorder + Preorder traversal |

---

## Key Concepts

### 1. Heapify Operation

**Time Complexity**: O(log n)
**Purpose**: Restore heap property at a given node

```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

### 2. Build Heap

**Time Complexity**: O(n) - not O(n log n)!
**Insight**: Start from last non-leaf node, heapify upwards

```python
def buildHeap(arr):
    n = len(arr)
    # Start from last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
```

### 3. Python's heapq Module

Python provides a **min heap** by default:

```python
import heapq

# Create min heap
arr = [3, 1, 4, 1, 5]
heapq.heapify(arr)  # O(n)

# Push element
heapq.heappush(arr, 2)  # O(log n)

# Pop minimum
min_val = heapq.heappop(arr)  # O(log n)

# For MAX HEAP: negate values
max_heap = [-x for x in arr]
heapq.heapify(max_heap)
```

---

## Common Patterns

### Pattern 1: K-th Smallest/Largest

**Use Max Heap of size K for K-th smallest:**
```python
# Maintain K smallest elements in max heap
heap = [-x for x in arr[:k]]
heapq.heapify(heap)

for i in range(k, n):
    if arr[i] < -heap[0]:  # Found smaller element
        heapq.heappop(heap)
        heapq.heappush(heap, -arr[i])

kth_smallest = -heap[0]
```

### Pattern 2: Merge K Sorted Structures

**Use Min Heap with (value, source, index):**
```python
heap = []
for i in range(k):
    heapq.heappush(heap, (arr[i][0], i, 0))

while heap:
    val, row, col = heapq.heappop(heap)
    result.append(val)

    if col + 1 < len(arr[row]):
        heapq.heappush(heap, (arr[row][col+1], row, col+1))
```

### Pattern 3: Median in Stream

**Use Two Heaps (Max + Min):**
```python
max_heap = []  # Left half (smaller values)
min_heap = []  # Right half (larger values)

# max_heap size ≥ min_heap size
# max_heap size ≤ min_heap size + 1

def add_number(num):
    heapq.heappush(max_heap, -num)
    heapq.heappush(min_heap, -heapq.heappop(max_heap))

    if len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
```

### Pattern 4: Greedy with Heap

**Always process minimum/maximum first:**
```python
# Example: Minimum Cost of Ropes
heapq.heapify(ropes)
cost = 0

while len(ropes) > 1:
    first = heapq.heappop(ropes)
    second = heapq.heappop(ropes)
    cost += first + second
    heapq.heappush(ropes, first + second)
```

---

## Interview Tips

### Time Complexity Quick Reference

| Operation | Complexity | Note |
|-----------|-----------|------|
| Build heap | O(n) | Not O(n log n)! |
| Insert | O(log n) | Bubble up |
| Extract min/max | O(log n) | Bubble down |
| Peek | O(1) | Just return root |
| Search | O(n) | Heap not designed for search |

### Common Interview Questions

1. **"Why is build heap O(n) and not O(n log n)?"**
   - Most nodes are near leaves (short bubble-down distance)
   - Mathematical proof: Σ(height * nodes at height) = O(n)

2. **"When to use heap vs. sorting?"**
   - Heap: When you only need K elements (O(n log k))
   - Sort: When you need all elements sorted (O(n log n))

3. **"How to implement max heap in Python?"**
   - Negate values when inserting/extracting
   - Or use custom comparator (for objects)

4. **"Heap vs. Binary Search Tree?"**
   - Heap: Faster for min/max, O(1) peek
   - BST: Supports search, range queries
   - Heap: Simpler, cache-friendly (array-based)

### Problem-Solving Strategies

1. **Identify heap problems by keywords:**
   - "K largest/smallest"
   - "Median", "Running stream"
   - "Merge K sorted"
   - "Minimum/Maximum repeatedly"

2. **Choose heap type carefully:**
   - Min heap for K largest elements
   - Max heap for K smallest elements
   - Both for median in stream

3. **Consider alternatives:**
   - QuickSelect for K-th element: O(n) average
   - Counting sort for limited range
   - BST for dynamic sorted data

### Edge Cases to Consider

- Empty heap operations
- Single element heap
- All elements equal
- K > array size
- Negative numbers
- Duplicate elements

---

## Complexity Cheat Sheet

### Space-Time Tradeoffs

| Problem | Naive Approach | Heap Approach | Optimal |
|---------|---------------|---------------|---------|
| K-th smallest | Sort O(n log n) | Min heap O(n + k log n) | QuickSelect O(n) avg |
| Merge K arrays | Merge pairs O(NK log K) | Min heap O(NK log K) | Same |
| Running median | Sort each O(n² log n) | Two heaps O(n log n) | Same |

---

## Additional Resources

### Learning Path

1. Start with: `0.py`, `1.py` (Heap basics)
2. Practice: `3.py`, `4.py` (K-th elements)
3. Challenge: `11.py`, `10.py` (Two heaps, complex logic)

### Related Topics

- Priority Queues
- Heap applications (Dijkstra's algorithm, Huffman coding)
- Advanced: Fibonacci Heap, Binomial Heap
- External sorting (merge K files)

---

## Contributing

When adding new problems:
1. Include comprehensive docstring with approach and intuition
2. Add flowchart in comments
3. Provide example usage
4. Note time/space complexity
5. Include interview tips

---

**Happy Coding! 🚀**

*All solutions are optimized for interview settings with clear explanations and edge case handling.*
