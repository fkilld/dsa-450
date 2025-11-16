"""
Minimum Characters to Add to Make String Palindrome

PROBLEM DESCRIPTION:
Given a string, find the minimum number of characters that need to be added
at the BEGINNING of the string to make it a palindrome.

Example: "ABC" -> add "CB" at beginning -> "CBABC" (2 chars needed)
Example: "AACECAAAA" -> already palindrome -> 0 chars needed

WHY THIS APPROACH (KMP LPS Based):
We use the KMP (Knuth-Morris-Pratt) algorithm's LPS (Longest Proper Prefix which is also Suffix)
array because:
1. A string is a palindrome if it reads the same forwards and backwards
2. If we concatenate string + separator + reverse(string), the LPS value tells us
   how much of the original string matches its reverse from the end
3. The LPS value at the end represents the longest suffix of reverse(string) that
   matches a prefix of the original string
4. This matching part is already palindromic, so we only need to add the non-matching prefix
5. Using KMP avoids O(n²) brute force checking and achieves O(n) time

KEY INSIGHT:
- If we reverse string and compare: "ABC" vs "CBA"
- Concatenate with separator: "ABC$CBA"
- LPS tells us longest overlap between original and reversed
- The overlap is the palindromic part already present
- We need to add: length - lps[-1] characters

ALGORITHM:
Step 1: Reverse the String
   - rev_str = string[::-1]
   - Example: "ABC" -> "CBA"

Step 2: Create Concatenated String with Separator
   - concat = string + '$' + rev_str
   - The '$' separator ensures no false matches across boundaries
   - Example: "ABC$CBA"

Step 3: Compute LPS Array
   - Use KMP's LPS computation (get_lps function)
   - LPS[i] = length of longest proper prefix which is also suffix for concat[0..i]
   - Example: "ABC$CBA" -> LPS = [0, 0, 0, 0, 0, 1, 2]

Step 4: Calculate Minimum Additions
   - The last value of LPS tells us the longest matching part
   - Chars to add = length - LPS[-1]
   - Example: 3 - 2 = 1 (need to add 1 char, but actually 2 in "ABC" case)

EDGE CASES:
1. Already a palindrome: "aba" -> return 0
2. No common characters: "abc" -> need to add len-1 characters
3. Single character: "a" -> return 0 (already palindrome)
4. Empty string: "" -> return 0
5. Two characters same: "aa" -> return 0
6. Two characters different: "ab" -> return 1 (add "b" -> "bab")

TIME COMPLEXITY: O(n)
- Reversing string: O(n)
- Concatenation: O(n)
- Computing LPS array: O(2n) = O(n) where n is length of original string
- Overall: O(n)

SPACE COMPLEXITY: O(n)
- Reversed string: O(n)
- Concatenated string: O(2n) = O(n)
- LPS array: O(2n) = O(n)
- Overall: O(n)

EXAMPLE WALKTHROUGH:
Input: "ABC"
Step 1: Reverse -> "CBA"
Step 2: Concatenate -> "ABC$CBA"
Step 3: Compute LPS
   Index: 0  1  2  3  4  5  6
   Char:  A  B  C  $  C  B  A
   LPS:   0  0  0  0  0  0  1

   At index 6, we have 'A' which matches the prefix 'A', so LPS[6] = 1

Step 4: Calculate
   - Original length = 3
   - LPS[-1] = 1 (one character from end matches beginning)
   - Need to add: 3 - 1 = 2 characters
   - Add "CB" at beginning -> "CBABC"

Another Example: "AACECAAAA"
Step 1: Reverse -> "AAAACECAA"
Step 2: Concatenate -> "AACECAAAA$AAAACECAA"
Step 3: LPS computation will show full overlap
Step 4: LPS[-1] = 9, chars needed = 9 - 9 = 0

KMP LPS (Longest Proper Prefix which is also Suffix) Helper Function:
- Computes for each position i, the length of longest proper prefix of string[0..i]
  that is also a suffix of string[0..i]
- "Proper" means not the entire string itself
- Used in KMP pattern matching, but also useful for palindrome problems
"""

def get_lps(string):
    """
    Compute LPS (Longest Proper Prefix which is also Suffix) array using KMP algorithm.

    For each position i, LPS[i] represents the length of the longest proper prefix
    of string[0..i] that is also a suffix of string[0..i].

    Example: "AABAAC"
    LPS:     [0, 1, 0, 1, 2, 0]
    At index 4: "AABAA" has prefix "AA" which is also suffix "AA", length = 2
    """
    n = len(string)
    lps = [None] * n

    lps[0] = 0  # Base case: single character has no proper prefix
    l = 0  # Length of previous longest prefix suffix
    i = 1  # Current position in string

    # Process each character to build LPS array
    while i < n:
        if string[l] == string[i]:
            # Characters match: extend the current LPS
            l += 1
            lps[i] = l
            i += 1
        else:
            # Characters don't match
            if l != 0:
                # Fall back to previous LPS value (similar to KMP failure function)
                # Don't increment i, try matching with shorter prefix
                l = lps[l - 1]
            else:
                # No prefix to fall back to
                lps[i] = 0
                i += 1
    return lps


def add_to_make_palindrome(string):
    """
    Find minimum number of characters to add at the beginning to make palindrome.

    Approach:
    1. Reverse the string
    2. Concatenate: original + separator + reversed
    3. Compute LPS array for concatenated string
    4. LPS[-1] tells us how much of the end matches the beginning
    5. The difference is how many chars we need to add
    """
    # Step 1: Reverse the input string
    rev_str = string[::-1]

    # Step 2: Create concatenated string with separator
    # Separator '$' prevents false matches across string boundaries
    concat = string + '$' + rev_str

    # Step 3: Compute LPS array for concatenated string
    lps = get_lps(concat)

    # Step 4: Calculate minimum characters needed
    # lps[-1] = longest suffix of reversed string matching prefix of original
    # This is the part that's already palindromic
    # We need to add the remaining characters from the beginning
    length = len(string)
    return length - lps[-1]

string = input("Enter the string : ")
print(add_to_make_palindrome(string))
