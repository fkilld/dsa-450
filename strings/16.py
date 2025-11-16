"""
Problem: Word Break (Dictionary Segmentation)
----------------------------------------------
Given a string and a dictionary of words, determine if the string can be
segmented into a space-separated sequence of one or more dictionary words.

Note: The same word in the dictionary may be reused multiple times.

APPROACH: Greedy Dictionary Matching (Simple Iterative)
--------------------------------------------------------
WHY THIS APPROACH?
- This is a simplified greedy approach that repeatedly tries to match dictionary
  words from the beginning of the remaining string
- For certain inputs where words appear in a convenient order, this works quickly
- Key idea: Try each dictionary word, if it matches the prefix, remove it and restart
- IMPORTANT: This approach is NOT optimal for all cases! It can fail on inputs
  where we need to try different word combinations (e.g., "aaab" with dict=["a", "aa", "aaa", "aaaa", "b"])
- A proper DP solution would be more robust, but this greedy approach is simpler
  and works for many practical cases

WHY GREEDY CAN FAIL:
- Example: string="aaab", dict=["a", "aa", "aaa", "aaaa", "b"]
- Greedy might pick "a" three times, leaving "ab" which can't be formed
- Correct: pick "aaa" once, then "b"
- This approach restarts from beginning each time, which can help in some cases

WHEN THIS WORKS WELL:
- When dictionary words don't have overlapping prefixes
- When there's a natural greedy choice at each step
- For testing/prototyping before implementing full DP solution

ALGORITHM:
1. Initialize index i = 0 to track position in dictionary
2. While i < len(dictionary):
   a. Get current dictionary word length l
   b. Extract substring from string of length l
   c. If substring matches dictionary word:
      - Remove this prefix from string
      - Reset i = 0 (restart dictionary search from beginning)
   d. Else:
      - Move to next dictionary word (i++)
3. After trying all words:
   - If string is empty: successfully segmented, return 1
   - If string is not empty: segmentation failed, return 0

TIME COMPLEXITY: O(n * m * k) where:
- n = length of string
- m = number of words in dictionary
- k = average length of dictionary words
- In worst case, we restart from beginning many times

SPACE COMPLEXITY: O(n)
- String slicing creates new strings (in Python)
- Could be O(1) with index tracking instead of slicing

EDGE CASES:
- Empty string: returns 1 (can be formed by 0 words)
- Empty dictionary: returns 0 if string non-empty
- String not in dictionary: returns 0
- Dictionary has string as single word: returns 1
- Repeated words: works if same word can be reused

EXAMPLE 1:
Input: string = "ilike", dictionary = ["i", "like", "sam", "sung", "samsung"]
- Match "i" (len=1), string becomes "like"
- Restart, match "like" (len=4), string becomes ""
- String empty -> return 1

EXAMPLE 2:
Input: string = "ilikesamsung", dictionary = ["i", "like", "sam", "sung", "samsung"]
- Match "i", string = "likesamsung"
- Match "like", string = "samsung"
- Match "samsung", string = ""
- Return 1

NOTE: For production code, consider using Dynamic Programming approach for
guaranteed correctness on all inputs.
"""

# Greedy approach without DP
def wordBreak(string, dictionary):
    i = 0  # Index to track current position in dictionary

    # Greedy matching: try each dictionary word against string prefix
    while i < len(dictionary):
        l = len(dictionary[i])  # Length of current dictionary word

        # Extract substring from beginning of string with same length as current word
        s = string[:l]

        # Check if prefix matches current dictionary word
        if s == dictionary[i]:
            # Match found! Remove this prefix from string
            # This represents "using" this word in our segmentation
            string = string[l:]

            # Restart search from beginning of dictionary
            # This allows us to reuse words and find new matches in updated string
            i = 0
        else:
            # No match, try next word in dictionary
            i += 1

    # Final check: if string is completely consumed, segmentation successful
    if len(string) == 0:
        return 1  # Success: all of string matched dictionary words
    else:
        return 0  # Failure: some part of string couldn't be matched

