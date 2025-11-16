# Binary Search Tree (BST) - Complete Problem Set

This folder contains comprehensive solutions to common BST problems with detailed explanations, flowcharts, and examples.

## Problem List

### Basic Operations
- **0.py** - Search and Insertion in BST
- **1.py** - Deletion of a node in BST  
- **2.py** - Find minimum and maximum values in BST

### Traversal & Successor/Predecessor
- **3.py** - Find inorder successor and predecessor
- **5.py** - Populate inorder successor for all nodes

### Validation
- **4.py** - Check if a tree is valid BST

### Lowest Common Ancestor
- **6.py** - Find LCA of two nodes in BST

### Tree Conversions
- **8.py** - Convert Binary Tree to BST
- **9.py** - Convert BST to Balanced BST
- **10.py** - Merge two balanced BSTs

### Kth Element Problems
- **11.py** - Find Kth largest element in BST
- **12.py** - Find Kth smallest element in BST

### Advanced Problems
- **13.py** - Count pairs from two BSTs whose sum equals X
- **14.py** - Find median of BST
- **15.py** - Count BST nodes in a given range
- **16.py** - Replace every element with least greater on right

### Special BST Problems
- **19.py** - Check if BST contains a dead end
- **20.py** - Find largest BST in a binary tree [VERY IMPORTANT]
- **21.py** - Flatten BST to sorted linked list

## Key Concepts

### BST Properties
1. Left subtree contains only nodes with keys < node's key
2. Right subtree contains only nodes with keys > node's key
3. Both subtrees must also be BSTs
4. Inorder traversal gives sorted sequence

### Time Complexities
- Search/Insert/Delete: O(h) where h = height
  - Balanced BST: O(log n)
  - Skewed BST: O(n)
- Traversals: O(n)

### Common Patterns
1. **Range-based validation** - For BST validation
2. **Inorder traversal** - For sorted operations
3. **Binary search** - For search operations
4. **Recursion with bounds** - For most BST problems

## Interview Tips
1. Always clarify if duplicates are allowed
2. Ask about tree balance (affects time complexity)
3. Consider both recursive and iterative approaches
4. Draw examples to verify logic
5. Test edge cases: empty tree, single node, skewed tree
