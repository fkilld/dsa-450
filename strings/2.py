"""
Problem: Find Duplicate Characters in a String
-----------------------------------------------
Given a string, find all characters that appear more than once and their frequencies.

APPROACH: Hash Map (Dictionary) for Frequency Counting
------------------------------------------------------
WHY THIS APPROACH?
- Hash map provides O(1) lookup and insertion time
- Single pass through string is sufficient (O(n) time)
- Automatically handles all characters without pre-allocation
- Easy to count and retrieve frequencies
- Most intuitive and efficient solution for frequency problems

ALTERNATIVE APPROACHES (and why we DON'T use them):
1. Nested loops (O(n²)) - Too slow for large strings
2. Sorting first (O(n log n)) - Slower than hash map, modifies order
3. Array of size 256 (O(1) but wastes space for small character sets)

ALGORITHM:
1. Create empty dictionary to store character frequencies
2. Iterate through each character in string
   - If character not in dictionary → initialize count to 1
   - If character already exists → increment its count
3. Iterate through dictionary
   - Print only characters with count > 1 (duplicates)

TIME COMPLEXITY: O(n) where n = length of string
- First loop: O(n) to count all characters
- Second loop: O(k) where k = unique characters (k ≤ n)
- Total: O(n + k) ≈ O(n)

SPACE COMPLEXITY: O(k) where k = number of unique characters
- Dictionary stores at most k unique characters
- In worst case (all unique): O(n)

EDGE CASES:
- No duplicates: nothing printed
- All same character: prints "char : n"
- Empty string: nothing printed
- Special characters and spaces: counted normally

EXAMPLES:
Input: "hello"
Output: l : 2

Input: "programming"
Output: g : 2
        r : 2
        m : 2
"""

string = input("Enter the string : ")

def duplicates(string):
    # Dictionary to store character frequencies
    # Key: character, Value: count of occurrences
    count = {}
    n = len(string)

    # First pass: Count frequency of each character
    for i in range(n):
        if string[i] not in count:
            # First occurrence of this character
            count[string[i]] = 1
        else:
            # Character seen before, increment count
            count[string[i]] += 1

    # Second pass: Print only duplicates (count > 1)
    for i in count:
        if count[i] > 1:
            # This character appears more than once
            print(i + " : " + str(count[i]))

duplicates(string)