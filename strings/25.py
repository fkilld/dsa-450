"""
Roman Number to Integer Conversion

PROBLEM:
Given a string representing a Roman numeral, convert it to an integer.
Roman numerals use these symbols: I=1, V=5, X=10, L=50, C=100, D=500, M=1000
Special cases use subtraction: IV=4, IX=9, XL=40, XC=90, CD=400, CM=900

WHY THIS APPROACH:
We use Single Pass with Subtraction Logic because:
1. Roman numerals follow a specific rule: smaller value before larger means subtract
2. We can determine if we should add or subtract by comparing consecutive values
3. Single pass is efficient - we only need to look at each character once
4. We handle the "2*prev" subtraction to correct for already-added values
5. This is simpler and more elegant than checking for specific patterns like "IV", "IX", etc.

ALGORITHM:
1. Create a mapping of Roman symbols to their integer values
2. Initialize result with the value of first character
3. For each remaining character (left to right):
   a. If current value > previous value:
      - This is a subtraction case (e.g., IV, IX, XL)
      - Add current value but subtract 2*previous value
      - Why 2*prev? Because we already added prev once, so we need to:
        * Remove that addition: -prev
        * Apply the subtraction: -prev
        * Total: -2*prev, then add current
   b. Otherwise:
      - Simple addition case
      - Just add current value to result
   c. Update previous value to current
4. Return final result

TIME COMPLEXITY: O(n) where n is length of Roman numeral string
- Single pass through the string
- Constant time operations for each character

SPACE COMPLEXITY: O(1)
- Fixed size dictionary (7 entries)
- Only a few variables regardless of input size

EDGE CASES:
1. Single character: Returns that character's value (e.g., "V" -> 5)
2. All same characters: Returns sum (e.g., "III" -> 3)
3. Multiple subtractions: Handles correctly (e.g., "MCMXCIV" -> 1994)
4. Largest value: "MMMCMXCIX" -> 3999

EXAMPLES:
Input: "III"     -> Output: 3 (1 + 1 + 1)
Input: "IV"      -> Output: 4 (5 - 1)
Input: "IX"      -> Output: 9 (10 - 1)
Input: "LVIII"   -> Output: 58 (50 + 5 + 1 + 1 + 1)
Input: "MCMXCIV" -> Output: 1994 (1000 + 900 + 90 + 4)
"""

def romanToDecimal(string):
    """
    Convert Roman numeral string to integer using single-pass subtraction logic

    Args:
        string: Roman numeral string (e.g., "XIV", "MCMXC")

    Returns:
        Integer value of the Roman numeral
    """
    # Map Roman symbols to their integer values
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Initialize with first character's value
    num = values[string[0]]
    prev = values[string[0]]

    # Process remaining characters from left to right
    for i in range(1, len(string)):
        # Subtraction case: smaller value before larger (e.g., IV, IX, CM)
        if values[string[i]] > prev:
            # Subtract 2*prev because:
            # 1. We already added prev to num (need to remove it: -prev)
            # 2. We need to subtract prev from current value (another -prev)
            # Then add current value: current - 2*prev
            num += values[string[i]] - (2*prev)
        else:
            # Normal case: just add current value
            num += values[string[i]]

        # Update previous value for next iteration
        prev = values[string[i]]

    return num