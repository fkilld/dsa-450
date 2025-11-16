"""
Problem: Parenthesis Checker (Balanced Brackets)
-------------------------------------------------
Given a string containing only parentheses characters: '(', ')', '{', '}', '[', ']',
determine if the input string has valid balanced brackets.

Valid means:
- Every opening bracket has a corresponding closing bracket of the same type
- Brackets are closed in the correct order
- Every closing bracket matches the most recent unmatched opening bracket

APPROACH: Stack-Based Matching
-------------------------------
WHY THIS APPROACH?
- Stack is the natural data structure for matching pairs with LIFO order
- Opening brackets are pushed onto stack (to be matched later)
- When we see a closing bracket, we check if it matches the top of stack
- Stack automatically handles nested brackets due to LIFO property
- If stack is empty at the end, all brackets were properly matched
- Alternative approaches (counter-based) fail for cases like "([)]" which
  looks balanced but isn't properly nested

KEY INSIGHT:
- The most recent unmatched opening bracket must match the current closing bracket
- This is exactly what a stack provides - access to most recent element

ALGORITHM:
1. Initialize empty stack
2. Iterate through each character in string:
   a. If opening bracket ('(', '{', '['):
      - Push onto stack
   b. If closing bracket (')', '}', ']'):
      - If stack is empty: return False (no matching opening bracket)
      - Pop from stack and check if it matches current closing bracket
      - If mismatch: return False
3. After iteration, check if stack is empty:
   - Empty: all brackets matched, return True
   - Not empty: some opening brackets unmatched, return False

TIME COMPLEXITY: O(n) where n is the length of the string
- Single pass through the string
- Each push/pop operation is O(1)

SPACE COMPLEXITY: O(n)
- In worst case, all characters are opening brackets
- Stack would contain n elements

EDGE CASES:
- Empty string: returns True (no brackets to match)
- Only opening brackets: returns False (stack not empty)
- Only closing brackets: returns False (stack empty when checking)
- Mismatched types: e.g., "([)]" returns False
- Correct nesting: e.g., "([{}])" returns True

EXAMPLES:
1. Input: "{[()]}" -> Output: True
   - '{' pushed, '[' pushed, '(' pushed
   - ')' matches '(', ']' matches '[', '}' matches '{'
   - Stack empty at end

2. Input: "([)]" -> Output: False
   - '(' pushed, '[' pushed
   - ')' should match '(' but top is '[' -> False

3. Input: "(((" -> Output: False
   - All pushed, stack not empty at end
"""

class Solution:
    # Function to check if brackets are balanced or not
    def ispar(self,x):
        stack = []

        # Process each character in the string
        for char in x:
            # Case 1: Opening bracket - push onto stack for later matching
            if char in ['(', '{', '[']:
                stack.append(char)

            # Case 2: Closing bracket - must match top of stack
            else:
                # If stack is empty, no opening bracket to match this closing bracket
                if len(stack) == 0:
                    return False

                # Pop the most recent opening bracket
                curr = stack.pop()

                # Check if the popped opening bracket matches current closing bracket
                if curr == '(' and char != ')': return False  # '(' must match ')'
                if curr == '{' and char != '}': return False  # '{' must match '}'
                if curr == '[' and char != ']': return False  # '[' must match ']'

        # Final check: stack should be empty if all brackets are matched
        # If stack has elements, there are unmatched opening brackets
        return True if len(stack) == 0 else False