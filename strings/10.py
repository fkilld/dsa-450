"""
Problem: Generate All Permutations of a String
----------------------------------------------
Given a string, generate all possible permutations (rearrangements) of its characters.

APPROACH: Recursive Backtracking with Character Selection
---------------------------------------------------------
WHY THIS APPROACH?
- We use recursion because permutations have recursive structure
- At each step, we can choose ANY remaining character to add next
- This creates an n-ary decision tree → recursion handles this naturally
- Backtracking explores all possible orderings systematically
- More intuitive than iterative generation algorithms

KEY INSIGHT: Fix-and-Permute Recursion
To generate permutations:
1. Pick ANY character from the string
2. FIX it in current position
3. Recursively permute the REMAINING characters
4. Try ALL possible characters in current position

Example: "abc"
- Fix 'a' → permute "bc" → "abc", "acb"
- Fix 'b' → permute "ac" → "bac", "bca"
- Fix 'c' → permute "ab" → "cab", "cba"

RECURSION TREE (for "abc"):
                    ""
           /         |         \
        "a"         "b"        "c"
       /   \       /   \      /   \
    "ab"  "ac"  "ba"  "bc"  "ca"  "cb"
     |     |     |     |     |     |
   "abc" "acb" "bac" "bca" "cab" "cba"

BASE CASE:
When string becomes empty → we've placed all characters → add permutation to result

ALGORITHM:
1. If string is empty → add current answer to results (base case)
2. For each position i in the string:
   a. Extract character at position i
   b. Create new string with that character removed (left + right parts)
   c. Recursively permute the remaining string
   d. Add current character to the answer being built

TIME COMPLEXITY: O(n! * n)
- Number of permutations: n! (factorial)
- Generating each permutation: O(n) for string operations
- Total: O(n! * n)

SPACE COMPLEXITY: O(n! * n)
- Recursion depth: O(n) call stack
- Result storage: n! permutations, each of length n
- Total: O(n! * n) for storing all results

STRING SLICING TECHNIQUE:
To remove character at index i:
  rest = string[0:i] + string[i+1:]

Example: string="abc", i=1 (remove 'b')
  left = string[0:1] = "a"
  right = string[2:] = "c"
  rest = "a" + "c" = "ac"

WHY GLOBAL VARIABLE?
- Collects results from all recursive branches
- Alternative: return and merge lists (more overhead)

EDGE CASES:
- Empty string: returns [""] (one empty permutation)
- Single character "a": returns ["a"]
- Duplicates: will generate duplicate permutations (e.g., "aab" → "aab", "aab", "aba", "aba", "baa", "baa")
  For unique permutations with duplicates, need different approach

EXAMPLE TRACE: "ab"
Call 1: permute("ab", "")
  ├─ i=0, ch='a', rest="b"
  │   └─ Call 2: permute("b", "a")
  │       └─ i=0, ch='b', rest=""
  │           └─ Call 3: permute("", "ab") → add "ab"
  └─ i=1, ch='b', rest="a"
      └─ Call 4: permute("a", "b")
          └─ i=0, ch='a', rest=""
              └─ Call 5: permute("", "ba") → add "ba"
Result: ["ab", "ba"]
"""

# Global list to store all permutations
res = []

def permute(string, ans):
    """
    Generate all permutations using fix-and-permute recursion.

    Args:
        string: Remaining characters to permute
        ans: Current permutation being built
    """
    # BASE CASE: No more characters to arrange
    if len(string) == 0:
        # We've placed all characters - permutation complete
        global res
        res.append(ans)
        return

    # RECURSIVE CASE: Try each character in current position
    # Loop through all positions in remaining string
    for i in range(len(string)):
        # Pick character at position i for current position
        ch = string[i]

        # Build remaining string by removing selected character
        # Combine left part (before i) and right part (after i)
        left_substr = string[0:i]       # Characters before index i
        right_substr = string[i + 1:]   # Characters after index i
        rest = left_substr + right_substr  # String without character i

        # Recursively permute remaining characters
        # Add chosen character to answer being built
        permute(rest, ans + ch)

string = input("Enter the string : ")
permute(string, "")
print(res)

