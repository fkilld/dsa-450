"""
Problem: Check if One String is Rotation of Another
----------------------------------------------------
Given two strings str1 and str2, check if str2 is a rotation of str1.
Example: "waterbottle" is a rotation of "erbottlewat"

APPROACH: Concatenation Trick
-----------------------------
WHY THIS APPROACH?
- Brilliant mathematical insight: If str2 is a rotation of str1, then str2
  MUST be a substring of str1+str1
- Only requires O(n) time complexity
- Simple and elegant - just 2 operations (concatenation + substring search)
- No complex rotation logic needed

INTUITION:
If str1 = "waterbottle" and we rotate at index 5:
  str2 = "erbottlewat"

When we concatenate str1 with itself:
  str1 + str1 = "waterbottlewaterbottle"
                      ^^^^^^^^^^^
  Notice str2 appears as a substring! This works for ANY rotation point.

ALTERNATIVE APPROACHES (and why we DON'T use them):
1. Generate all rotations (O(n²)) - Too slow, requires lots of string operations
2. Character-by-character rotation checking (O(n²)) - Complex logic
3. KMP pattern matching (O(n)) - Correct but overkill for this problem

ALGORITHM:
1. Check if lengths are equal (different lengths can't be rotations)
2. Concatenate str1 with itself → temp = str1 + str1
3. Check if str2 exists as substring in temp
4. If yes → str2 is a rotation of str1
   If no → str2 is NOT a rotation

TIME COMPLEXITY: O(n) where n = length of strings
- Length check: O(1)
- Concatenation: O(n)
- Substring search (.count()): O(n) in Python (uses efficient algorithm)
- Total: O(n)

SPACE COMPLEXITY: O(n)
- temp string requires 2n characters ≈ O(n) space

EDGE CASES:
- Different lengths → return False immediately
- Empty strings → return True (empty is rotation of empty)
- Same strings → return True (rotation at position 0)
- Single character → return True if characters match

EXAMPLES:
str1 = "waterbottle", str2 = "erbottlewat" → True
str1 = "hello", str2 = "lohel" → True
str1 = "hello", str2 = "world" → False
str1 = "abc", str2 = "bca" → True
"""

def areRotated(str1, str2):
    # Different lengths means cannot be rotations
    if len(str1) != len(str2):
        return False

    # The key insight: If str2 is a rotation of str1,
    # then str2 will be a substring of str1+str1
    # Example: str1="abc", rotations are "abc", "bca", "cab"
    # str1+str1 = "abcabc" contains all rotations as substrings
    temp = str1 + str1

    # Check if str2 exists in the concatenated string
    if temp.count(str2) > 0:
        return True
    else:
        return False


str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

if areRotated(str1, str2):
    print("Rotated")
else:
    print("Not Rotated")