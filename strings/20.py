"""
Problem: Count Minimum Reversals to Balance Brackets
----------------------------------------------------
Given a string of only '{' and '}' brackets, find minimum number of reversals
needed to make the expression balanced. A reversal means changing '{' to '}' or vice versa.

Example: "}{" → 2 reversals needed (reverse both to get "{}")
Example: "{{" → 1 reversal needed (reverse one to get "{}")
Example: "}}{{" → 2 reversals needed

APPROACH: Greedy Matching with Unmatched Count
----------------------------------------------
WHY THIS APPROACH?
- We use greedy matching because:
  * We should match brackets whenever possible (reduces reversals needed)
  * Only unmatched brackets need to be considered for reversal
  * One pass through string is sufficient - O(n) time

- Key insight: After removing all matched pairs, we're left with:
  * Some unmatched opening brackets: {{{{
  * Some unmatched closing brackets: }}}}
  * Pattern is ALWAYS: }}}}{{{{ (all closes before all opens)

- Why this pattern? Because any close that comes AFTER an open can be matched!

MATHEMATICAL FORMULA:
After greedy matching, we have:
- 'm' unmatched opening brackets: {{{{
- 'n' unmatched closing brackets: }}}}

Minimum reversals = ⌈m/2⌉ + ⌈n/2⌉

WHY?
- For 'm' opens ({{{{): Need to reverse ⌈m/2⌉ to closes
  Example: {{{{ → }{} → need to reverse 2 brackets
- For 'n' closes (}}}}): Need to reverse ⌈n/2⌉ to opens
  Example: }}}} → {}{ → need to reverse 2 brackets

ALGORITHM:
1. Check if length is odd → return -1 (impossible to balance)
2. Initialize counters: open_bracket = 0, close_bracket = 0
3. Scan through string:
   a. If '{' found → increment open_bracket (potential to match)
   b. If '}' found:
      - If open_bracket > 0: Match it (decrement open_bracket)
      - Else: No open bracket available, increment close_bracket (unmatched)
4. After scan:
   - open_bracket = count of unmatched open brackets
   - close_bracket = count of unmatched close brackets
5. Return ⌈open_bracket/2⌉ + ⌈close_bracket/2⌉

TIME COMPLEXITY: O(n)
- Single pass through string
- Each character processed once

SPACE COMPLEXITY: O(1)
- Only using two counter variables
- No stack or additional data structures needed

WHY NOT USE A STACK?
- Stack would work but uses O(n) space
- We only need to COUNT unmatched brackets, not track positions
- Counter-based approach is more space-efficient

EDGE CASES:
- Odd length: return -1 (impossible)
- Empty string: return 0
- Already balanced: return 0
- All opens "{{{{": return n/2
- All closes "}}}}": return n/2

EXAMPLE TRACE: s = "}}{{" (length=4)
i=0: '}'→ open_bracket=0, so close_bracket=1
i=1: '}'→ open_bracket=0, so close_bracket=2
i=2: '{'→ open_bracket=1
i=3: '{'→ open_bracket=2

Final: open_bracket=2, close_bracket=2
Reversals = ⌈2/2⌉ + ⌈2/2⌉ = 1 + 1 = 2

Result after 2 reversals: "}{{{" → "{{{}" or "}}{}" → "{}{}"

EXAMPLE TRACE 2: s = "}}{{{" (length=5)
Result: -1 (odd length, impossible)

EXAMPLE TRACE 3: s = "{{{{" (length=4)
i=0-3: All '{', open_bracket=4
Reversals = ⌈4/2⌉ + ⌈0/2⌉ = 2 + 0 = 2
After reversals: "{{{{" → "}{}{" (need to reverse 2 brackets)
"""

import math

def countRev(s):
    """
    Count minimum reversals needed to balance bracket expression.

    Args:
        s: String containing only '{' and '}' brackets

    Returns:
        Minimum number of reversals needed, or -1 if impossible
    """

    n = len(s)

    # EDGE CASE: Odd length cannot be balanced
    # Every bracket needs a pair, so even length is required
    if n % 2 != 0:
        return -1

    # Counters for unmatched brackets after greedy matching
    open_bracket = 0    # Count of unmatched '{' brackets
    close_bracket = 0   # Count of unmatched '}' brackets

    # GREEDY MATCHING: Match closing brackets with opening brackets whenever possible
    for i in range(n):
        if s[i] == '{':
            # Found an opening bracket - potential for matching
            open_bracket += 1

        else:  # s[i] == '}'
            # Found a closing bracket - try to match it

            if open_bracket != 0:
                # MATCH FOUND: We have an unmatched open bracket available
                # This closing bracket matches with a previous opening bracket
                open_bracket -= 1  # One less unmatched open bracket

            else:
                # NO MATCH: No unmatched open bracket available
                # This closing bracket cannot be matched (it came too early)
                close_bracket += 1  # One more unmatched close bracket

    # After greedy matching, we're left with:
    # - open_bracket unmatched '{' brackets
    # - close_bracket unmatched '}' brackets
    #
    # Pattern will be: }}}}...{{{{{ (all closes before all opens)
    #
    # To balance:
    # - Need to reverse ⌈open_bracket/2⌉ opening brackets to closing
    # - Need to reverse ⌈close_bracket/2⌉ closing brackets to opening
    #
    # Example: {{{{ → }{} (reverse 2 out of 4)
    # Example: }}}} → {}{ (reverse 2 out of 4)

    return math.ceil(open_bracket / 2) + math.ceil(close_bracket / 2)