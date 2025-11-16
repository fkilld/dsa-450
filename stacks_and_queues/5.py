"""
PROBLEM: Check for Balanced Parentheses
=======================================

Given an expression string containing only brackets of types: (, ), {, }, [, ]
determine if the brackets are balanced.

An expression is balanced if:
1. Every opening bracket has a corresponding closing bracket
2. Brackets are closed in the correct order
3. No closing bracket appears before its corresponding opening bracket

Examples:
- "{()}[]" → True (balanced)
- "[{()}]" → True (balanced)
- "({[}])" → False ('}' closes before '[')
- "(()" → False (missing closing bracket)
- "())" → False (extra closing bracket)

APPROACH & REASONING:
====================
We use a Stack-based approach because:
1. Stack's LIFO property naturally matches bracket nesting
2. The most recent opening bracket should match the current closing bracket
3. O(n) time complexity with single pass through the string
4. Simple and elegant solution

Algorithm Steps:
1. Traverse each character in the expression
2. If it's an opening bracket: push to stack
3. If it's a closing bracket:
   - Check if stack is empty (unmatched closing bracket)
   - Pop from stack and verify it matches the closing bracket
4. After traversal, stack should be empty (all brackets matched)

Why Stack?
- Last opened bracket must be first closed (LIFO)
- Stack maintains the order of unmatched opening brackets
- Easy to check matching pairs

FLOWCHART:
=========

┌─────────────────┐
│     START       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Initialize      │
│ empty stack     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ For each char   │◄───────┐
│ in expression   │        │
└────┬───────┬────┘        │
     │       │             │
   Done   More chars       │
     │       │             │
     │       ▼             │
     │  ┌──────────────┐   │
     │  │Is opening    │   │
     │  │bracket?      │   │
     │  └──┬────────┬──┘   │
     │     │        │      │
     │    Yes       No     │
     │     │        │      │
     │     ▼        ▼      │
     │ ┌────────┐ ┌──────────────┐
     │ │ Push   │ │Is closing    │
     │ │to stack│ │bracket?      │
     │ └───┬────┘ └──┬────────┬──┘
     │     │         │        │
     │     └─────────┘       Yes
     │           │            │
     │           │            ▼
     │           │      ┌──────────────┐
     │           │      │ Stack empty? │
     │           │      └──┬────────┬──┘
     │           │         │        │
     │           │        Yes       No
     │           │         │        │
     │           │         ▼        ▼
     │           │    ┌────────┐ ┌──────────┐
     │           │    │Return  │ │Pop stack │
     │           │    │ False  │ │Check if  │
     │           │    └────────┘ │matches   │
     │           │               └──┬───┬───┘
     │           │                  │   │
     │           │              Match Mismatch
     │           │                  │   │
     │           │                  │   ▼
     │           │                  │ ┌────────┐
     │           │                  │ │Return  │
     │           │                  │ │ False  │
     │           │                  │ └────────┘
     │           └──────────────────┘
     │                    │
     ▼                    │
┌──────────────┐         │
│ Stack empty? │◄────────┘
└──┬────────┬──┘
   │        │
  Yes       No
   │        │
   ▼        ▼
┌────────┐ ┌────────┐
│Return  │ │Return  │
│ True   │ │ False  │
└────────┘ └────────┘

Example Trace for "{()}":
Step 1: '{' → Push '{' → Stack: ['{']
Step 2: '(' → Push '(' → Stack: ['{', '(']
Step 3: ')' → Pop '(' → Match! → Stack: ['{']
Step 4: '}' → Pop '{' → Match! → Stack: []
Result: Stack empty → True (balanced)

Example Trace for "({[}])":
Step 1: '(' → Push '(' → Stack: ['(']
Step 2: '{' → Push '{' → Stack: ['(', '{']
Step 3: '[' → Push '[' → Stack: ['(', '{', '[']
Step 4: '}' → Pop '[' → Mismatch! → Return False

TIME COMPLEXITY:
===============
- O(n) where n is the length of the expression
- We traverse the string once
- Each push/pop operation is O(1)

SPACE COMPLEXITY:
================
- O(n) in the worst case
- When all brackets are opening brackets: "(((("
- Stack will contain all n characters
"""

class Solution:
    def ispar(self, x):
        """
        Check if the given expression has balanced parentheses.

        Args:
            x: String containing only bracket characters

        Returns:
            True if brackets are balanced, False otherwise
        """
        # Initialize an empty stack to track opening brackets
        stack = []

        # Iterate through each character in the expression
        for char in x:
            # If it's an opening bracket, push to stack
            if char in ['[', '{', '(']:
                stack.append(char)
            else:
                # It's a closing bracket
                # First check if stack is empty (unmatched closing bracket)
                if len(stack) == 0:
                    return False

                # Pop the most recent opening bracket
                top = stack.pop()

                # Check if the popped opening bracket matches the closing bracket
                # '(' should match ')', '{' should match '}', '[' should match ']'
                if top == '(' and char != ')':
                    return False
                elif top == '{' and char != '}':
                    return False
                elif top == '[' and char != ']':
                    return False

        # After processing all characters, stack should be empty
        # If stack is not empty, some opening brackets were not closed
        return len(stack) == 0


# EXAMPLE USAGE AND TEST CASES
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ("{()}[]", True),           # Balanced
        ("[()]{}{[()()]()}", True), # Complex balanced
        ("[(])", False),            # Wrong order
        ("(((", False),             # Missing closing
        ("())", False),             # Extra closing
        ("", True),                 # Empty string
        ("{[()]}", True),           # Nested balanced
        ("({[}])", False),          # Mismatched nesting
    ]

    print("Testing Balanced Parentheses:")
    for expression, expected in test_cases:
        result = solution.ispar(expression)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{expression}' → {result} (expected: {expected})")
