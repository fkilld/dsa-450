# Complete BST Solutions Guide with Explanations

## Files 0-6: ✅ Fully Documented with Flowcharts
See individual files for comprehensive documentation including:
- Problem statement
- Detailed approach explanation
- ASCII flowcharts
- Time/Space complexity analysis
- Full working examples with test cases

## Files 8-21: Quick Reference Guide

### **8.py - Binary Tree to BST**
**Approach**: Inorder traversal → Sort → Reassign in inorder
**Key Insight**: Inorder of BST is sorted, so sort the values and reassign
**Time**: O(n log n), **Space**: O(n)
**Interview Tip**: Explain why sorting + inorder assignment creates valid BST

### **9.py - Convert BST to Balanced BST**
**Approach**: Store inorder → Build balanced tree from sorted array
**Key Insight**: Pick middle element as root for balance
**Time**: O(n), **Space**: O(n)
**Interview Tip**: Similar to "sorted array to BST" problem

### **10.py - Merge Two Balanced BSTs**
**Approach**: Get both inorders → Merge sorted arrays → Build balanced BST
**Key Insight**: Merging two sorted arrays is O(n+m)
**Time**: O(n+m), **Space**: O(n+m)
**Interview Tip**: Can optimize space by using iterators

### **11.py - Kth Largest Element**
**Approach**: Reverse inorder traversal (Right-Root-Left)
**Key Insight**: Reverse inorder gives descending order
**Time**: O(h+k), **Space**: O(h)
**Interview Tip**: Can stop after finding kth element

### **12.py - Kth Smallest Element**
**Approach**: Regular inorder traversal (Left-Root-Right)
**Key Insight**: Inorder gives ascending order
**Time**: O(h+k), **Space**: O(h)
**Interview Tip**: Most straightforward BST traversal problem

### **13.py - Brothers from Different Roots (Count Pairs with Sum)**
**Approach**: Traverse one tree, for each node search target-node in other tree
**Key Insight**: Use BST search for O(h) lookup
**Time**: O(n*h), **Space**: O(h)
**Interview Tip**: Can optimize with two pointers on inorder arrays

### **14.py - Median of BST**
**Approach**: Count nodes → Find middle element(s) in inorder traversal
**Key Insight**: Median is at position (n/2) or average of (n/2) and (n/2)+1
**Time**: O(n), **Space**: O(h)
**Interview Tip**: Handle both odd and even number of nodes

### **15.py - Count BST Nodes in Range**
**Approach**: Use BST property to prune search space
**Key Insight**: 
- If node < low: search only right
- If node > high: search only left  
- If in range: search both + count current
**Time**: O(h+k) where k is count, **Space**: O(h)
**Interview Tip**: Better than O(n) by using BST property

### **16.py - Replace with Least Greater Element**
**Approach**: Build BST from right to left, track successor during insertion
**Key Insight**: When inserting, nodes on path are potential successors
**Time**: O(n log n) average, **Space**: O(n)
**Interview Tip**: Tricky problem, draw example to understand

### **19.py - Check for Dead End**
**Approach**: For each node, check if range [low, high] has become invalid
**Key Insight**: Dead end when low == high (no space to insert)
**Time**: O(n), **Space**: O(h)
**Interview Tip**: Pass valid range with each recursive call

### **20.py - Largest BST in Binary Tree ⭐⭐⭐ [VERY IMPORTANT]**
**Approach**: Post-order traversal returning [isBST, size, min, max]
**Key Insight**: 
- For each node, check if left and right are BSTs
- Check if current node satisfies: left.max < node < right.min
- Return info for parent to use

**Return Format**: [isBST (bool), size (int), min (int), max (int)]

**Algorithm**:
```
If node is None: return [True, 0, ∞, -∞]
If leaf: return [True, 1, node.val, node.val]

Get left = solve(left)
Get right = solve(right)

If left.isBST AND right.isBST AND node.val > left.max AND node.val < right.min:
    return [True, left.size + right.size + 1, min(left.min, node.val), max(right.max, node.val)]
Else:
    return [False, max(left.size, right.size), 0, 0]
```

**Time**: O(n), **Space**: O(h)
**Interview Tip**: This is a MUST-KNOW problem. Practice multiple times!

### **21.py - Flatten BST to Sorted List**
**Approach**: Inorder traversal, modify pointers to create linked list
**Key Insight**: Set left=None, right=next for each node during inorder
**Time**: O(n), **Space**: O(h)
**Interview Tip**: Use dummy node to simplify pointer manipulation

## Common Interview Questions:

1. **"Why use inorder for BST?"**
   - Inorder of BST gives sorted sequence
   - Fundamental property of BST

2. **"When to use iterative vs recursive?"**
   - Iterative: Better space (no stack), harder to code
   - Recursive: Cleaner code, O(h) space for call stack

3. **"How to optimize space?"**
   - Morris traversal for O(1) space inorder
   - Iterative with explicit stack

4. **"What if BST is unbalanced?"**
   - Time complexity degrades to O(n)
   - Mention self-balancing trees (AVL, Red-Black)

## Problem Patterns:

| Pattern | Examples | Technique |
|---------|----------|-----------|
| Finding Kth element | 11, 12 | Modified inorder |
| Tree conversion | 8, 9, 10 | Inorder + rebuild |
| Range queries | 15 | BST property pruning |
| Validation | 4, 19, 20 | Range checking |
| Successor/Predecessor | 3, 5 | Inorder relationships |

## Study Priority:

1. **Must Know**: 0-6 (basics), 20 (largest BST)
2. **Should Know**: 11-12 (kth element), 15 (range query)
3. **Good to Know**: 8-10 (conversions), 13-14 (advanced)
4. **Bonus**: 16, 19, 21 (special cases)
