"""
Problem: Check if String is Valid Shuffle of Two Strings
---------------------------------------------------------
Given two strings str1 and str2, check if a result string is a valid shuffle of both.
A valid shuffle maintains the relative order of characters from each string.

Example: str1="abc", str2="def", result="adbecf" → Valid (order preserved)
         str1="abc", str2="def", result="fedcba" → Invalid (order changed)

APPROACH: Three Pointer Linear Scan
------------------------------------
WHY THIS APPROACH?
- We use three pointers because we need to track position in THREE strings simultaneously
- Linear time O(n+m) is optimal - can't solve without examining each character
- Greedy matching works because we must maintain relative order
- Single pass is sufficient - no backtracking needed
- Space efficient - only 3 integer pointers needed

KEY INSIGHT:
A valid shuffle means characters from str1 and str2 appear in result in the
SAME RELATIVE ORDER as they appear in original strings.

ALGORITHM:
1. Check length constraint: len(result) must equal len(str1) + len(str2)
2. Initialize three pointers: i (str1), j (str2), k (result)
3. For each character in result:
   - Try to match with str1[i] first (if available)
   - Otherwise try to match with str2[j] (if available)
   - If neither matches → invalid shuffle
   - Move matched pointer forward
4. Verify all characters from both strings were used

TIME COMPLEXITY: O(n + m) where n=len(str1), m=len(str2)
- Single pass through result string (length n+m)
- Each character checked once

SPACE COMPLEXITY: O(1)
- Only using 3 pointer variables and 3 length variables
- No additional data structures needed

EDGE CASES:
- Empty str1 or str2: result must equal the other string
- Both empty: result must be empty
- Result length mismatch: return False immediately
- Result contains extra characters: detected in while loop
- Incomplete shuffle (not all chars used): detected in final check

WHY THIS WORKS:
Since we maintain order, a greedy left-to-right scan is sufficient.
If str1[i] matches res[k], we MUST use it (can't skip and use later).

EXAMPLES:
str1="abc", str2="def", res="adbecf"
- a matches str1[0] → i=1
- d matches str2[0] → j=1
- b matches str1[1] → i=2
- e matches str2[1] → j=2
- c matches str1[2] → i=3
- f matches str2[2] → j=3
- All pointers at end → Valid!
"""

def shuffled(str1, str2, res):
    # Initialize three pointers for three strings
    i = j = k = 0
    l1 = len(str1)  # Length of the first substring
    l2 = len(str2)  # Length of the second substring
    lr = len(res)   # Length of the result string

    # Length validation: result must contain exactly all characters from both strings
    if l1 + l2 < lr:
        return False  # Result has extra characters

    # Scan through result string character by character
    while k < lr:
        # Try to match current result character with str1
        if i < l1 and str1[i] == res[k]:
            i += 1  # Match found in str1, advance str1 pointer
        # If not matched with str1, try str2
        elif j < l2 and str2[j] == res[k]:
            j += 1  # Match found in str2, advance str2 pointer
        else:
            # Current character doesn't match either string
            # OR the relative order has been violated
            return False

        # Move to next character in result
        k += 1

    # Verify that we've used ALL characters from both substrings
    # If any characters remain unused, it's not a valid shuffle
    if i < l1 or j < l2:
        return False  # Some characters from str1 or str2 were not used
    else:
        return True   # Perfect shuffle - all chars used in correct order

# Input handling
str1, str2 = [str(x) for x in input("Enter s1 and s2 : ").split()]
string = input("Enter the string : ")

if shuffled(str1, str2, string):
    print("Yes")
else:
    print("No")