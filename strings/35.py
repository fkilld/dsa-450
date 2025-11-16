"""
Print Anagrams Together

PROBLEM DESCRIPTION:
Given an array of strings, group all anagrams together and return them.
Anagrams are words that contain the same characters in different orders.

Example: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

WHY THIS APPROACH (Sorted Key Grouping):
We use SORTED STRING as a key in a hash map because:
1. Anagrams have the SAME characters, just in different order
2. When we sort the characters of anagrams, they produce the SAME sorted string
   - "eat" -> sorted: "aet"
   - "tea" -> sorted: "aet"
   - "ate" -> sorted: "aet"
3. By using sorted string as a hash map key, all anagrams automatically group together
4. Hash map provides O(1) average lookup and insertion
5. This avoids O(n²) comparison of every word with every other word

ALTERNATIVE APPROACHES (Not Used):
1. Character Count Array: Count frequency of each character (26 letters)
   - Similar time complexity but more complex to implement
   - Would need to convert count array to tuple for hashing
2. Prime Number Product: Assign each letter a prime, multiply them
   - Risk of integer overflow for long strings
   - Not as intuitive as sorted string approach

ALGORITHM:
Step 1: Create Hash Map
   - Use defaultdict(list) to automatically create empty list for new keys
   - Key: sorted string, Value: list of original words

Step 2: Process Each Word
   - For each word in the input array:
     a) Sort its characters to create a key
     b) Use sorted string as key to group with other anagrams
     c) Append original word to the list for this key

Step 3: Extract Groups
   - Iterate through hash map values
   - Each value is a list of anagrams
   - Collect all lists into result array

Step 4: Return Result
   - Return array of anagram groups

EDGE CASES:
1. Empty array -> return []
2. Single word -> return [[word]]
3. No anagrams -> each word in its own group
4. All words are anagrams -> single group with all words
5. Duplicate words -> both appear in same group (they're anagrams of each other)

TIME COMPLEXITY: O(n * k * log k)
- n = number of words
- k = average length of each word
- For each word: sorting takes O(k log k)
- Hash map operations (insert, lookup): O(1) average
- Total: O(n * k * log k)

SPACE COMPLEXITY: O(n * k)
- Hash map stores all n words
- Each sorted key takes O(k) space
- Overall: O(n * k)

EXAMPLE WALKTHROUGH:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]

Processing:
1. "eat" -> sort -> "aet" -> keys["aet"] = ["eat"]
2. "tea" -> sort -> "aet" -> keys["aet"] = ["eat", "tea"]
3. "tan" -> sort -> "ant" -> keys["ant"] = ["tan"]
4. "ate" -> sort -> "aet" -> keys["aet"] = ["eat", "tea", "ate"]
5. "nat" -> sort -> "ant" -> keys["ant"] = ["tan", "nat"]
6. "bat" -> sort -> "abt" -> keys["abt"] = ["bat"]

Final Hash Map:
{
  "aet": ["eat", "tea", "ate"],
  "ant": ["tan", "nat"],
  "abt": ["bat"]
}

Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""

# Print Anagrams Together

from collections import defaultdict

def Anagrams(words, n):
    """
    Group anagrams together using sorted string as hash key.

    Args:
        words: List of strings to group
        n: Number of words (not used, but kept for interface compatibility)

    Returns:
        List of lists, where each inner list contains anagrams
    """
    # Step 1: Create hash map with default value as empty list
    # defaultdict automatically creates empty list for new keys
    keys = defaultdict(list)

    # Step 2: Process each word and group by sorted characters
    for word in words:
        temp = word

        # Sort the characters in the word
        # All anagrams will produce the same sorted string
        # Example: "eat", "tea", "ate" all become "aet" when sorted
        temp = ''.join(sorted(temp))

        # Use sorted string as key and append original word to its group
        keys[temp].append(word)

    # Step 3: Extract all anagram groups from hash map
    ans = []  # Result array to store grouped anagrams
    for key in keys:
        ans.append(keys[key])  # Each value is a list of anagrams

    return ans
