"""
Recursively Remove All Adjacent Duplicates

PROBLEM DESCRIPTION:
Given a string, recursively remove all adjacent duplicate characters.
After removing, if new adjacent duplicates are formed, remove them too.
Continue until no more adjacent duplicates remain.

Example: "azxxzy" -> "azzy" -> "ay"
Example: "mississippi" -> "m" (i->ss->pp all removed)
Example: "aabbcc" -> "" (all chars removed)

WHY THIS APPROACH (Recursive String Reduction):
We use RECURSION because:
1. After removing one set of duplicates, NEW duplicates may form
   - "abccba" -> remove "cc" -> "abba" -> remove "bb" -> "aa" -> remove "aa" -> ""
2. Recursion naturally handles this cascading removal
3. Each recursive call processes one "layer" of duplicates
4. The problem itself is recursive in nature: solve for smaller string, combine results
5. We need to check if removal causes new duplicates at boundaries

WHY NOT ITERATIVE:
- Stack-based iterative solution possible but more complex
- Need to track what was just removed to check boundaries
- Recursion makes boundary checking natural (compare first char with result[0])

ALGORITHM (remove_recur function):
Step 1: Base Cases
   - If string length is 0 or 1, no duplicates possible, return as-is

Step 2: Check for Adjacent Duplicates at Start
   - If string[0] == string[1]:
     a) Remember this character (last_word)
     b) Skip all consecutive occurrences of this character
     c) Recursively process remaining string
     d) Return result (duplicates removed, don't add back)

Step 3: Process Rest of String
   - Recursively call on string[1:] (ignore first character for now)
   - Get result rem_str

Step 4: Check Boundary with Recursive Result
   - If rem_str[0] == string[0]:
     - New duplicate formed at boundary
     - Remove first char from rem_str (don't add string[0])
   - If len(rem_str) == 0 and last_word == string[0]:
     - Previous removal left a duplicate
     - Return empty (don't add string[0])
   - Otherwise:
     - No boundary duplicate, safe to add string[0]

Step 5: Return Result
   - Return string[0] + rem_str

EDGE CASES:
1. Empty string -> return ""
2. Single character -> return that character
3. No duplicates -> return original string
4. All same characters -> return "" or single char (depending on count)
5. Alternating duplicates "aabbcc" -> ""
6. Nested duplicates "abccba" -> ""

TIME COMPLEXITY: O(n²) in worst case
- In worst case, each recursive call processes n-1 characters
- We may have O(n) recursive calls (each removing one layer)
- Total: O(n²)
- Example worst case: "aabbccdd..." -> multiple passes needed

SPACE COMPLEXITY: O(n)
- Recursion depth: O(n) in worst case
- String slicing creates new strings: O(n)
- Overall: O(n)

EXAMPLE WALKTHROUGH:
Input: "abccba"

Call 1: remove_recur("abccba", 0)
  - string[0]='a', string[1]='b' (not equal)
  - Recurse on "bccba"

Call 2: remove_recur("bccba", 0)
  - string[0]='b', string[1]='c' (not equal)
  - Recurse on "ccba"

Call 3: remove_recur("ccba", 0)
  - string[0]='c', string[1]='c' (EQUAL!)
  - Skip all 'c': left with "ba"
  - Recurse on "ba", last_word='c'

Call 4: remove_recur("ba", ord('c'))
  - string[0]='b', string[1]='a' (not equal)
  - Recurse on "a"

Call 5: remove_recur("a", ord('c'))
  - Length 1, return "a"

Unwind:
Call 4: rem_str="a", string[0]='b', no match, return ['b'] + "a" = "ba"
Call 3: rem_str="ba", string[0]='c', no match but we removed 'c', return "ba"
Call 2: rem_str="ba", string[0]='b', MATCH! Remove 'b', return "a"
Call 1: rem_str="a", string[0]='a', MATCH! Remove 'a', return ""

Output: ""
"""

# Recursively remove all adjacent duplicates
# question => https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

def remove_recur(string, last_word):
    """
    Recursively remove adjacent duplicates from a string.

    Args:
        string: List of characters to process
        last_word: ASCII value of last removed character (to detect boundary duplicates)

    Returns:
        List of characters with all adjacent duplicates removed
    """
    # Base case: string with 0 or 1 characters has no adjacent duplicates
    if len(string) == 0 or len(string) == 1:
        return string

    # Case 1: Found adjacent duplicates at the start
    if string[0] == string[1]:
        # Remember which character we're removing
        last_word = ord(string[0])

        # Skip ALL consecutive occurrences of this duplicate character
        # Example: "aaab" -> skip to "b"
        while len(string) > 1 and string[0] == string[1]:
            string = string[1:]
        string = string[1:]  # Remove the last occurrence too

        # Recursively process the remaining string
        return remove_recur(string, last_word)

    # Case 2: No duplicate at start, process rest of string first
    # Recursively process string[1:], keeping first character aside
    rem_str = remove_recur(string[1:], last_word)

    # Case 3: Check if removal created a boundary duplicate
    # After processing rest, check if first char now matches result's first char
    if len(rem_str) != 0 and rem_str[0] == string[0]:
        last_word = ord(string[0])
        # Boundary duplicate formed! Remove first char from result
        # Example: "abc" where "bc" -> "c", if first char 'a' == 'c' after processing
        return rem_str[1:]

    # Case 4: Check if current char matches the last removed char
    # This handles cascading removals
    if len(rem_str) == 0 and last_word == ord(string[0]):
        # The remaining string is empty and current char was just removed
        # Don't add current char back
        return rem_str

    # Case 5: Safe to add first character back
    # No duplicates formed, combine first char with processed rest
    return [string[0]] + rem_str


def remove_duplicate(string):
    """
    Main function to remove all adjacent duplicates from a string.

    Args:
        string: Input string

    Returns:
        String with all adjacent duplicates recursively removed
    """
    last_word = 0  # Initially, no character has been removed
    string = list(string)  # Convert to list for easier manipulation
    ans = remove_recur(string, last_word)  # Recursively remove duplicates
    return ''.join(ans)  # Convert list back to string
    

