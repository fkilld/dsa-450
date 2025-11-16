"""
Problem: Print All Subsequences of a String
--------------------------------------------
Given a string, generate all possible subsequences (subsets of characters in order).

APPROACH: Recursive Backtracking (Include/Exclude Pattern)
----------------------------------------------------------
WHY THIS APPROACH?
- We use recursion because subsequences have a natural recursive structure
- For EVERY character, we have 2 choices: include it OR exclude it
- This creates a binary decision tree → recursion is perfect for this
- Backtracking explores ALL possible combinations systematically
- No iterative solution is simpler or more intuitive

KEY INSIGHT: Include/Exclude Recursion
For any string, a subsequence is formed by either:
1. INCLUDING the first character + subsequences of remaining string
2. EXCLUDING the first character + subsequences of remaining string

Example: "abc"
- Include 'a': 'a' + subsequences of "bc" → "a", "ab", "ac", "abc"
- Exclude 'a': "" + subsequences of "bc" → "", "b", "c", "bc"

RECURSION TREE (for "abc"):
                    ""
                  /    \
            "a"           ""
           /   \         /   \
       "ab"   "a"     "b"    ""
       / \    / \     / \    / \
    "abc" "ab" "ac" "a" "bc" "b" "c" ""

BASE CASE:
When string becomes empty → we've made all decisions → add current subsequence to result

TIME COMPLEXITY: O(2^n)
- For each of n characters, we make 2 recursive calls
- Total subsequences generated = 2^n
- Each subsequence creation involves string slicing O(n)
- Total: O(n * 2^n)

SPACE COMPLEXITY: O(n * 2^n)
- Recursion depth: O(n) call stack
- Result storage: 2^n subsequences, average length n/2
- Total: O(n * 2^n) for storing all results

WHY GLOBAL VARIABLE?
- Using global `res` list to collect results from all recursive branches
- Alternative: return lists and merge (more memory overhead, same time)
- For clean code, consider passing `res` as parameter instead of global

EDGE CASES:
- Empty string: returns [""] (one empty subsequence)
- Single character "a": returns ["", "a"]
- All unique characters: 2^n distinct subsequences
- Duplicates in string: will generate duplicate subsequences

EXAMPLE TRACE: "ab"
Call 1: subsequence("ab", "")
  ├─ Include 'a': Call 2: subsequence("b", "a")
  │   ├─ Include 'b': Call 3: subsequence("", "ab") → add "ab"
  │   └─ Exclude 'b': Call 4: subsequence("", "a") → add "a"
  └─ Exclude 'a': Call 5: subsequence("b", "")
      ├─ Include 'b': Call 6: subsequence("", "b") → add "b"
      └─ Exclude 'b': Call 7: subsequence("", "") → add ""
Result: ["ab", "a", "b", ""]
"""

# Global list to store all subsequences
res = []

def subsequence(string, ans):
    """
    Generate all subsequences using include/exclude recursion.

    Args:
        string: Remaining string to process
        ans: Current subsequence being built
    """
    # BASE CASE: No more characters to process
    if len(string) == 0:
        # We've made all include/exclude decisions
        # Add the built subsequence to results
        # Note: You can also print directly here instead of collecting
        global res
        res.append(ans)
        return

    # RECURSIVE CASE: Process first character of remaining string

    # CHOICE 1: INCLUDE the current (first) character
    # Add string[0] to answer and recurse on rest
    subsequence(string[1:], ans + string[0])

    # CHOICE 2: EXCLUDE the current (first) character
    # Don't add string[0], just recurse on rest
    subsequence(string[1:], ans)

string = input("Enter the string : ")
subsequence(string, "")
print(res)

