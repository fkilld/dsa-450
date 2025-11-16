# BST Problems - Solutions Summary

## Documented Files (with Flowcharts & Detailed Explanations)

### ✅ Completed (0-6):
- **0.py** - Search & Insertion: O(h) time, uses BST property for efficient operations
- **1.py** - Deletion: Three cases (leaf, one child, two children with inorder successor)
- **2.py** - Min/Max: Leftmost for min, rightmost for max - O(h) time
- **3.py** - Inorder Pred/Succ: Find predecessor (max in left) and successor (min in right)
- **4.py** - Validate BST: Range-based validation (recommended) vs inorder approach
- **5.py** - Populate Next Pointers: Use inorder traversal to link successors
- **6.py** - LCA in BST: Split point where paths to two nodes diverge

### 📝 Remaining Files (8-21):

#### Tree Conversions:
- **8.py** - Binary Tree → BST: Collect inorder, sort, reassign values
- **9.py** - BST → Balanced BST: Inorder + binary search tree construction
- **10.py** - Merge 2 BSTs: Merge sorted inorder arrays, build balanced BST

#### Kth Element:
- **11.py** - Kth Largest: Reverse inorder (Right-Root-Left), count k nodes
- **12.py** - Kth Smallest: Normal inorder (Left-Root-Right), count k nodes

#### Advanced Queries:
- **13.py** - Count Pairs (sum=X): Inorder first tree, search in second for complement
- **14.py** - Median: Find middle element(s) in inorder traversal
- **15.py** - Count in Range: Use BST property to prune search space

#### Special Problems:
- **16.py** - Replace with Least Greater: Build BST from right, track successor
- **19.py** - Dead End: Check if any leaf node has no space for children
- **20.py** - **[VERY IMPORTANT]** Largest BST Subtree: Return [isBST, size, min, max]
- **21.py** - Flatten to List: Inorder traversal with pointer manipulation

## Key Techniques:

1. **Inorder Traversal** (most common): Gives sorted sequence
2. **Range Validation**: For BST validation
3. **BST Property**: Left < Root < Right for efficient search
4. **Reverse Inorder**: For reverse sorted operations
5. **Recursion with Info**: Return multiple values for subtree problems

## Complexity Patterns:

- **Time**: Most operations are O(h) where h = height
  - Balanced BST: O(log n)
  - Skewed BST: O(n)
- **Space**: O(h) for recursion stack

## Interview Strategy:

1. Draw the tree structure
2. Walk through example manually
3. Identify BST property usage
4. Consider edge cases (empty, single node, skewed)
5. Discuss time/space complexity
6. Code iterative when possible (better space complexity)
