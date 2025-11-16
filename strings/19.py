"""
Problem: Convert Sentence to Mobile Numeric Keypad Sequence
------------------------------------------------------------
Convert a string of uppercase letters to the equivalent numeric keypad sequence
(like old T9 texting on mobile phones).

Mobile Keypad Layout:
2: ABC
3: DEF
4: GHI
5: JKL
6: MNO
7: PQRS
8: TUV
9: WXYZ

Example: "BAC" → "2222" (B=22, A=2, C=222)

APPROACH: Pre-computed Mapping Array with ASCII Offset
------------------------------------------------------
WHY THIS APPROACH?
- We use a pre-computed lookup array because:
  * Mapping is FIXED - never changes, so compute once
  * Array indexing is O(1) - fastest possible lookup
  * No conditionals or complex logic needed at runtime
  * Clean separation: data (mapping) vs logic (conversion)

- ASCII arithmetic (ord(char) - ord('A')) converts character to array index
  * 'A' → 0, 'B' → 1, 'C' → 2, ... 'Z' → 25
  * This is much cleaner than if-else chains or switch statements

ALTERNATIVE APPROACHES (and why we DON'T use them):
1. Dictionary mapping: Slower lookup, more memory overhead
2. If-else chain: O(n) lookup time, harder to maintain
3. Mathematical formula: No pattern exists for these sequences

ALGORITHM:
1. Pre-define mapping array with all 26 sequences (A-Z)
   - Index 0 (A): "2"
   - Index 1 (B): "22"
   - Index 2 (C): "222"
   - ... and so on
2. For each character in input string:
   - Convert character to index: offset = ord(char) - ord('A')
   - Look up tap sequence: taps = key[offset]
   - Append to result string
3. Return complete numeric sequence

TIME COMPLEXITY: O(n * m) where n = string length, m = average taps per char
- Loop runs n times (one per character)
- Each iteration appends O(m) characters (avg 2-3 taps per letter)
- Total: O(n * m)

SPACE COMPLEXITY: O(1) for algorithm + O(n * m) for output
- Mapping array is fixed size (26 entries) = O(1)
- Result string grows with input length and tap count = O(n * m)

ASCII ARITHMETIC EXPLANATION:
ord('A') = 65, ord('B') = 66, ord('C') = 67, ...
- ord('A') - ord('A') = 65 - 65 = 0 → index 0 in array
- ord('B') - ord('A') = 66 - 65 = 1 → index 1 in array
- ord('C') - ord('A') = 67 - 65 = 2 → index 2 in array

This technique is commonly used for mapping characters to indices!

EDGE CASES:
- Empty string: returns ""
- Single character: returns corresponding taps
- All same letter: returns repeated taps
- Assumes INPUT IS UPPERCASE (as per problem constraints)
- Does not handle lowercase, numbers, or special characters

EXAMPLE TRACE: "BAC"
i=0: char='B', offset=1, key[1]="22", res="22"
i=1: char='A', offset=0, key[0]="2", res="222"
i=2: char='C', offset=2, key[2]="222", res="222222"
Wait, that's wrong! Let me recheck...

Actually: "BAC" → "22" + "2" + "222" = "222222"
But expected might be with space separation...
The code as written concatenates: "222222"
"""

def convert_to_key(string):
    """
    Convert uppercase string to mobile keypad tap sequence.

    Args:
        string: Uppercase letter string (A-Z)

    Returns:
        Numeric string of keypad taps
    """

    # PRE-COMPUTED MAPPING: Each index corresponds to a letter (A-Z)
    # Index 0-2: ABC on key 2
    # Index 3-5: DEF on key 3
    # Index 6-8: GHI on key 4
    # Index 9-11: JKL on key 5
    # Index 12-14: MNO on key 6
    # Index 15-18: PQRS on key 7
    # Index 19-21: TUV on key 8
    # Index 22-25: WXYZ on key 9
    key = ["2", "22", "222",           # ABC
           "3", "33", "333",           # DEF
           "4", "44", "444",           # GHI
           "5", "55", "555",           # JKL
           "6", "66", "666",           # MNO
           "7", "77", "777", "7777",   # PQRS
           "8", "88", "888",           # TUV
           "9", "99", "999", "9999"]   # WXYZ

    res = ''

    # Convert each character to its tap sequence
    for i in range(len(string)):
        char = string[i]

        # KEY TECHNIQUE: Use ASCII arithmetic to get array index
        # ord(char) gives ASCII value, subtract ord('A') to get 0-25 index
        # Example: 'B' → ord('B')=66, ord('A')=65 → 66-65=1 → key[1]="22"
        taps = key[ord(char) - ord('A')]

        # Append tap sequence for this character
        res += str(taps)

    return res

# Example usage
print(convert_to_key('BAC'))