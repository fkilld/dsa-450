"""
Boyer Moore Algorithm for Pattern Searching

PROBLEM:
Given a text and a pattern, find all occurrences of the pattern in the text.
Boyer-Moore is one of the most efficient string searching algorithms in practice.

WHY THIS APPROACH:
Boyer-Moore algorithm is preferred because:
1. It's faster than naive pattern matching, especially for longer patterns
2. It skips sections of the text, rather than checking every position
3. It uses two heuristics to skip unnecessary comparisons:
   - Bad Character Heuristic: Skip based on mismatched character
   - Good Suffix Heuristic: Skip based on matched suffix
4. Best case: O(n/m) where n is text length, m is pattern length
5. Works particularly well on natural language text with large alphabets

ALGORITHM OVERVIEW:
Two main components to implement:

1. Bad Character Heuristic:
   - Preprocess pattern to store last occurrence of each character
   - When mismatch occurs, shift pattern so that:
     * Bad character in text aligns with its last occurrence in pattern, OR
     * Pattern moves past the bad character if it's not in pattern

2. Good Suffix Heuristic:
   - Preprocess pattern to find suffixes that appear elsewhere in pattern
   - When mismatch occurs after matching a suffix:
     * Shift pattern to align matching suffix with its previous occurrence, OR
     * Shift to align longest prefix that matches a suffix, OR
     * Shift pattern completely past the matched portion

3. Main Search:
   - Compare pattern with text from right to left
   - On mismatch, use maximum shift suggested by both heuristics
   - Continue until pattern reaches end of text

TIME COMPLEXITY:
- Preprocessing: O(m + σ) where σ is alphabet size
- Best case: O(n/m) - can skip large portions of text
- Worst case: O(n*m) - rare, occurs with patterns like "aaa...a" in text "aaa...a"
- Average case: O(n) - much faster than naive approach

SPACE COMPLEXITY: O(m + σ)
- Bad character table: O(σ)
- Good suffix table: O(m)

EDGE CASES:
1. Pattern longer than text: No matches
2. Empty pattern: Match at every position (or handle as error)
3. Single character pattern: Degenerates to simple search
4. Pattern not in text: Returns empty list

TODO: IMPLEMENTATION NEEDED
The following functions need to be implemented:

1. badCharacterTable(pattern):
   - Create a dictionary mapping each character to its rightmost position in pattern
   - Characters not in pattern will use default value -1

2. goodSuffixTable(pattern):
   - Create an array of shift values for each position
   - For each suffix, find where it occurs earlier in pattern
   - Handle cases where suffix doesn't reoccur

3. boyerMooreSearch(text, pattern):
   - Preprocess pattern using above two functions
   - Align pattern with beginning of text
   - Compare from right to left
   - On mismatch, calculate shifts from both heuristics
   - Use maximum shift and continue
   - On complete match, record position and shift by good suffix value

EXAMPLE IMPLEMENTATION STRUCTURE:

def badCharacterTable(pattern):
    # Returns dict: char -> rightmost position in pattern
    pass

def goodSuffixTable(pattern):
    # Returns list of shift values for each position
    pass

def boyerMooreSearch(text, pattern):
    # Main search function
    # Returns list of starting positions where pattern is found
    pass

EXAMPLE:
Text: "ABAAABCD"
Pattern: "ABC"
Output: [4] (pattern found starting at index 4)

REFERENCE:
- Original paper: Boyer & Moore (1977)
- More efficient than KMP for large alphabets
- Used in GNU grep and many text editors
"""

# TODO: Implement the Boyer-Moore algorithm here
# Follow the structure outlined in the docstring above
