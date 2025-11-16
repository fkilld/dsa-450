"""
PROBLEM: Factorial of Large Numbers
====================================
Given a positive integer N, find the factorial of N.
The factorial of a number is the product of all positive integers less than or equal to N.

Note: Since the factorial can be very large (e.g., 100! has 158 digits),
return the result as a list of digits.

Example:
    Input:  N = 5
    Output: [1, 2, 0]
    Explanation: 5! = 5 × 4 × 3 × 2 × 1 = 120

    Input:  N = 10
    Output: [3, 6, 2, 8, 8, 0, 0]
    Explanation: 10! = 3,628,800

    Input:  N = 100
    Output: [9, 3, 3, 2, 6, 2, 1, 5, 4, 4, 3, 9, 4, 4, 1, 5, 2, 6, 8, 1, 6, 9, 9, 2, 3, 8, 8, 5, 6, 2, 6, 6, 7, 0, 0, 4, 9, 0, 7, 1, 5, 9, 6, 8, 2, 6, 4, 3, 8, 1, 6, 2, 1, 4, 6, 8, 5, 9, 2, 9, 6, 3, 8, 9, 5, 2, 1, 7, 5, 9, 9, 9, 9, 3, 2, 2, 9, 9, 1, 5, 6, 0, 8, 9, 4, 1, 4, 6, 3, 9, 7, 6, 1, 5, 6, 5, 1, 8, 2, 8, 6, 2, 5, 3, 6, 9, 7, 9, 2, 0, 8, 2, 7, 2, 2, 3, 7, 5, 8, 2, 5, 1, 1, 8, 5, 2, 1, 0, 9, 1, 6, 8, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Explanation: 100! has 158 digits

APPROACH: Array-Based Multiplication (Digit-by-Digit)
======================================================
WHY THIS APPROACH?
- Standard integer types (int, long) cannot handle very large factorials
- 20! = 2,432,902,008,176,640,000 (already 19 digits)
- 100! has 158 digits - far beyond standard integer limits
- We store each digit in an array and perform multiplication manually
- This mimics how we multiply large numbers by hand in school
- Time Complexity: O(N²) where N is the input number
- Space Complexity: O(D) where D is the number of digits in result

ALTERNATIVE APPROACHES:
1. Using BigInteger/arbitrary precision libraries: Easier but less educational
2. String-based multiplication: Similar concept but slower
3. Recursion with memoization: Still faces overflow issues

HOW IT WORKS:
1. Initialize result array with value 1 (since 0! = 1 and 1! = 1)
2. For each number from 2 to N:
   - Multiply the entire result array by this number
   - Handle carry propagation digit by digit
   - Extend array size when needed for new digits
3. Reverse the result array (stored in reverse for easier manipulation)
4. Return the list of digits

MULTIPLICATION PROCESS:
When multiplying a multi-digit number by a single digit:
- Start from the least significant digit (rightmost)
- Multiply each digit and add carry from previous digit
- Store the units digit and propagate the carry
- Continue until all digits are processed and no carry remains

FLOW EXAMPLE:
=============
Calculate 5! = 5 × 4 × 3 × 2 × 1 = 120

Initial State:
    res = [1], res_size = 1
    This represents: 1

Step 1: Multiply by 2 (calculating 2!)
    multiply(2, res, 1)
    i=0: prod = 1*2 + 0 = 2
         res[0] = 2 % 10 = 2
         carry = 2 // 10 = 0
    res = [2], res_size = 1
    This represents: 2

Step 2: Multiply by 3 (calculating 3!)
    multiply(3, res, 1)
    i=0: prod = 2*3 + 0 = 6
         res[0] = 6 % 10 = 6
         carry = 6 // 10 = 0
    res = [6], res_size = 1
    This represents: 6

Step 3: Multiply by 4 (calculating 4!)
    multiply(4, res, 1)
    i=0: prod = 6*4 + 0 = 24
         res[0] = 24 % 10 = 4
         carry = 24 // 10 = 2
    Process carry:
         res[1] = 2 % 10 = 2
         carry = 2 // 10 = 0
         res_size = 2
    res = [4, 2], res_size = 2
    This represents: 24 (digits in reverse)

Step 4: Multiply by 5 (calculating 5!)
    multiply(5, res, 2)
    i=0: prod = 4*5 + 0 = 20
         res[0] = 20 % 10 = 0
         carry = 20 // 10 = 2
    i=1: prod = 2*5 + 2 = 12
         res[1] = 12 % 10 = 2
         carry = 12 // 10 = 1
    Process carry:
         res[2] = 1 % 10 = 1
         carry = 1 // 10 = 0
         res_size = 3
    res = [0, 2, 1], res_size = 3
    This represents: 120 (digits in reverse)

Final: Reverse the array
    ans = [1, 2, 0]
    Output: 120

DETAILED MULTIPLICATION EXAMPLE (23 × 4 = 92):
===============================================
Initial: res = [3, 2] (represents 23 in reverse), multiply by 4

i=0: Process digit 3
     prod = 3 × 4 + 0 = 12
     res[0] = 12 % 10 = 2
     carry = 12 // 10 = 1

i=1: Process digit 2
     prod = 2 × 4 + 1 = 9
     res[1] = 9 % 10 = 9
     carry = 9 // 10 = 0

Result: res = [2, 9] (represents 92 in reverse)

FLOWCHART:
==========
    ┌──────────────────────────┐
    │  Start: factorial(N)     │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │ Initialize:              │
    │ res = [0] * 3000         │
    │ res[0] = 1               │
    │ res_size = 1             │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │ For x from 2 to N        │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────────┐
    │ Call multiply(x, res,        │
    │              res_size)       │
    └────────────┬─────────────────┘
                 │
                 ▼
    ┌─────────────────────────────────────┐
    │      MULTIPLY FUNCTION               │
    │                                      │
    │  Initialize: carry = 0, i = 0       │
    └────────────┬────────────────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │  while i < res_size?     │
    └────┬───────────────┬─────┘
         │ No            │ Yes
         │               ▼
         │    ┌────────────────────────┐
         │    │ prod = res[i]*x + carry│
         │    │ res[i] = prod % 10     │
         │    │ carry = prod // 10     │
         │    │ i++                    │
         │    └────────────┬───────────┘
         │                 │
         │                 └──────┐
         │                        │
         ▼                        ▼
    ┌──────────────────────────┐
    │  while carry > 0?        │
    └────┬───────────────┬─────┘
         │ No            │ Yes
         │               ▼
         │    ┌────────────────────────┐
         │    │ res[res_size] =        │
         │    │      carry % 10        │
         │    │ carry = carry // 10    │
         │    │ res_size++             │
         │    └────────────┬───────────┘
         │                 │
         │                 └──────┐
         │                        │
         ▼                        ▼
    ┌──────────────────────────┐
    │ Return res_size          │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │ All multiplications done │
    │ Reverse res array        │
    │ Return as list           │
    └──────────────────────────┘

WHY STORE DIGITS IN REVERSE ORDER?
===================================
When we multiply by hand, we start from the rightmost digit (units place).
Storing in reverse order allows us to:
1. Easily access the least significant digit at index 0
2. Append new digits at the end when carry creates more digits
3. Avoid shifting all elements when the number of digits increases

Example: 123 is stored as [3, 2, 1]
- res[0] = 3 (units place)
- res[1] = 2 (tens place)
- res[2] = 1 (hundreds place)

TIME COMPLEXITY:
================
- Outer loop runs N-1 times (from 2 to N)
- For each iteration, multiply() processes all digits
- Average number of digits in k! ≈ k*log₁₀(k)
- Total: O(N²*log(N)) approximately
- Simplified: O(N²) for practical purposes

SPACE COMPLEXITY:
=================
- O(D) where D is the number of digits in N!
- For N = 100, we need 158 digits
- Array size of 3000 is sufficient for N up to ~1000

EDGE CASES:
===========
1. N = 0: 0! = 1 → [1]
2. N = 1: 1! = 1 → [1]
3. N = 2: 2! = 2 → [2]
4. Large N (e.g., 1000): Array must be large enough
"""


class Solution:
    """
    A class that provides methods to calculate factorials of large numbers.

    The standard integer data types cannot handle very large factorials due to overflow.
    This class implements array-based arithmetic to compute factorials that can have
    hundreds or thousands of digits.
    """

    def multiply(self, x, res, res_size):
        """
        Multiply the current factorial result stored in res[] with a number x.

        This function performs digit-by-digit multiplication similar to how we
        multiply large numbers by hand. The result array stores digits in reverse
        order (least significant digit first) for easier manipulation.

        Args:
            x (int): The number to multiply with the current result
            res (list): Array storing the current factorial digits (in reverse order)
            res_size (int): Number of digits in the current result

        Returns:
            int: Updated size of the result after multiplication

        Example:
            If res = [4, 2] (representing 24) and x = 5
            After multiply: res = [0, 2, 1] (representing 120)
            Returns: 3 (new size)

        Time Complexity: O(res_size) - Process each existing digit once
        Space Complexity: O(1) - Only uses a few variables for carry
        """
        carry = 0  # Initialize carry for the multiplication
        i = 0

        # Process each digit of the current result
        while i < res_size:
            # Multiply current digit with x and add previous carry
            # Example: If res[i]=4, x=5, carry=0 → prod=20
            prod = res[i] * x + carry

            # Store only the units digit of the product
            # Example: prod=20 → res[i]=0
            res[i] = prod % 10

            # Calculate carry for the next digit position
            # Example: prod=20 → carry=2
            carry = prod // 10

            i += 1

        # Handle any remaining carry by adding new digits to the result
        # This extends the number when multiplication produces more digits
        # Example: 99 × 2 = 198 (2 digits become 3 digits)
        while carry:
            # Store the units digit of carry
            res[res_size] = carry % 10

            # Update carry for next position (if carry >= 10)
            carry = carry // 10

            # Increment size as we've added a new digit
            res_size += 1

        return res_size  # Return the updated size of the result

    def factorial(self, n):
        """
        Calculate the factorial of n (n!).

        The factorial is calculated using array-based arithmetic to handle
        very large numbers. Each digit is stored in an array, and multiplication
        is performed digit by digit with carry propagation.

        Args:
            n (int): The number for which factorial is to be calculated (n >= 0)

        Returns:
            list: List of digits representing the factorial value (in correct order)

        Example:
            factorial(5) returns [1, 2, 0] representing 120
            factorial(10) returns [3, 6, 2, 8, 8, 0, 0] representing 3,628,800

        Time Complexity: O(N²) - For each number from 2 to N, we multiply all digits
        Space Complexity: O(D) - Where D is the number of digits in result
        """
        # Create an array to store digits
        # Size 3000 is large enough for factorials up to ~1000
        # (1000! has about 2568 digits)
        res = [0] * 3000

        # Initialize result with 1 (since 0! = 1 and 1! = 1)
        res[0] = 1

        # Initial size of result is 1 digit
        res_size = 1

        # Calculate factorial by iterative multiplication
        # Multiply 1 × 2 × 3 × 4 × ... × n
        x = 2
        while x <= n:
            # Multiply current result with x
            # Example: If res represents 6 and x=4, res becomes 24
            res_size = self.multiply(x, res, res_size)

            # Move to next number
            x += 1

        # Initialize the final answer list
        ans = []

        # Convert the reversed digit array to a properly ordered list
        # res is stored as [0, 2, 1] for 120
        # We reverse it to get [1, 2, 0]
        for i in range(res_size - 1, -1, -1):
            ans.append(res[i])

        return ans  # Return the factorial as a list of digits


# Test cases
if __name__ == "__main__":
    s = Solution()

    # Test 1: Small factorial
    n1 = 5
    result1 = s.factorial(n1)
    print(f"Factorial of {n1}: {result1}")  # Expected: [1, 2, 0] (120)
    print(f"Value: {''.join(map(str, result1))}")

    # Test 2: Moderate factorial
    n2 = 10
    result2 = s.factorial(n2)
    print(f"\nFactorial of {n2}: {result2}")  # Expected: [3, 6, 2, 8, 8, 0, 0]
    print(f"Value: {''.join(map(str, result2))}")

    # Test 3: Edge case - 0!
    n3 = 0
    result3 = s.factorial(n3)
    print(f"\nFactorial of {n3}: {result3}")  # Expected: [1]
    print(f"Value: {''.join(map(str, result3))}")

    # Test 4: Large factorial
    n4 = 20
    result4 = s.factorial(n4)
    print(f"\nFactorial of {n4}: {result4}")
    print(f"Value: {''.join(map(str, result4))}")
    print(f"Number of digits: {len(result4)}")

    # Test 5: Very large factorial
    n5 = 100
    result5 = s.factorial(n5)
    print(f"\nFactorial of {n5}:")
    print(f"Number of digits: {len(result5)}")
    print(f"First 10 digits: {''.join(map(str, result5[:10]))}")
    print(f"Last 10 digits: {''.join(map(str, result5[-10:]))}")
