"""
PROBLEM: Evaluation of Postfix Expression
==========================================

Given a postfix expression, evaluate it and return the result.

Postfix notation (also called Reverse Polish Notation - RPN):
- Operators come after operands
- No need for parentheses
- Easy to evaluate using a stack

Examples:
- "23+"  → 2+3 = 5
- "23*5+" → (2*3)+5 = 11
- "231*+9-" → 2+(3*1)-9 = -4

Conversion from Infix to Postfix:
- Infix: (2 + 3) * 5
- Postfix: 2 3 + 5 *

APPROACH & REASONING:
====================
We use a Stack-based approach because:
1. Operands are pushed onto stack
2. When operator is encountered, pop two operands, compute, and push result
3. Stack naturally handles the order of operations
4. Final result is the only element left in stack

Algorithm:
1. Scan postfix expression left to right
2. If operand (number): push to stack
3. If operator (+, -, *, /):
   - Pop two operands (b, then a)
   - Compute: a operator b
   - Push result back to stack
4. Return final value from stack

Why Stack?
- Last two values pushed are first to be used (LIFO)
- Handles nested operations naturally
- Simple single-pass solution

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
   Done    More            │
     │       │             │
     │       ▼             │
     │  ┌──────────────┐   │
     │  │Is operator?  │   │
     │  │(+,-,*,/)     │   │
     │  └──┬────────┬──┘   │
     │     │        │      │
     │    No       Yes     │
     │     │        │      │
     │     ▼        ▼      │
     │ ┌────────┐ ┌──────────────┐
     │ │Convert │ │ b = pop()    │
     │ │to int  │ │ a = pop()    │
     │ │ Push   │ │              │
     │ │to stack│ │ result =     │
     │ └───┬────┘ │ a operator b │
     │     │      │              │
     │     │      │ push(result) │
     │     │      └──────┬───────┘
     │     │             │
     │     └─────────────┘
     │           │
     ▼           │
┌──────────────┐ │
│ Pop and     │◄┘
│ return top  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│     END      │
└──────────────┘

Example Trace for "231*+":
Step 1: '2' → Push 2 → Stack: [2]
Step 2: '3' → Push 3 → Stack: [2, 3]
Step 3: '1' → Push 1 → Stack: [2, 3, 1]
Step 4: '*' → Pop 1, pop 3 → 3*1=3 → Push 3 → Stack: [2, 3]
Step 5: '+' → Pop 3, pop 2 → 2+3=5 → Push 5 → Stack: [5]
Result: 5

Note on Operator Order:
When we pop b then a:
- For subtraction: a - b (not b - a)
- For division: a / b (not b / a)
This is important! First popped is second operand.

TIME COMPLEXITY:
===============
- O(n) where n is the length of the expression
- We scan the expression once
- Each push/pop is O(1)

SPACE COMPLEXITY:
================
- O(n) for the stack
- In worst case, all operands are pushed before any operator
"""

class Solution:
    def evaluatePostfix(self, S):
        """
        Evaluate a postfix expression and return the result.

        Args:
            S: String representing postfix expression
               Contains single-digit numbers and operators (+, -, *, /)

        Returns:
            Integer result of the evaluation
        """
        # Stack to store operands and intermediate results
        stack = []

        # Process each character in the postfix expression
        for char in S:
            # Check if current character is an operator
            if char in ['*', '/', '+', '-']:
                # Pop the second operand (last pushed)
                b = stack.pop()
                # Pop the first operand (second last pushed)
                a = stack.pop()

                # Perform the operation based on the operator
                # Important: Order matters for - and /
                if char == '*':
                    stack.append(a * b)
                elif char == '/':
                    # Integer division (rounds down)
                    stack.append(a // b)
                elif char == '+':
                    stack.append(a + b)
                else:  # char == '-'
                    stack.append(a - b)

            else:
                # It's an operand (number)
                # Convert character to integer and push to stack
                stack.append(int(char))

        # The final result is the only element left in the stack
        return stack.pop()


# EXAMPLE USAGE AND TEST CASES
if __name__ == "__main__":
    solution = Solution()

    # Test cases: (expression, expected_result)
    test_cases = [
        ("23+", 5),           # 2 + 3
        ("23*", 6),           # 2 * 3
        ("23*5+", 11),        # (2 * 3) + 5
        ("231*+9-", -4),      # (2 + (3 * 1)) - 9 = 5 - 9
        ("52/", 2),           # 5 / 2 (integer division)
        ("82-", 6),           # 8 - 2
        ("123*+", 7),         # 1 + (2 * 3)
        ("12+3*", 9),         # (1 + 2) * 3
    ]

    print("Testing Postfix Expression Evaluation:")
    for expression, expected in test_cases:
        result = solution.evaluatePostfix(expression)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{expression}' → {result} (expected: {expected})")

    # Example with detailed trace
    print("\n--- Detailed Trace Example ---")
    expr = "231*+"
    print(f"Expression: {expr}")
    print("Step-by-step evaluation:")
    print("1. '2' → push(2) → stack: [2]")
    print("2. '3' → push(3) → stack: [2, 3]")
    print("3. '1' → push(1) → stack: [2, 3, 1]")
    print("4. '*' → pop(1), pop(3), 3*1=3, push(3) → stack: [2, 3]")
    print("5. '+' → pop(3), pop(2), 2+3=5, push(5) → stack: [5]")
    print(f"Result: {solution.evaluatePostfix(expr)}")
