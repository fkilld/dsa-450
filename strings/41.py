"""
Isomorphic Strings

PROBLEM DESCRIPTION:
Two strings are isomorphic if the characters in one string can be replaced to get
the other string, while preserving the order of characters. No two characters may
map to the same character, but a character may map to itself.

Example: "egg" and "add" are isomorphic
- e -> a
- g -> d
Mapping: e->a, g->d (consistent throughout)

Example: "foo" and "bar" are NOT isomorphic
- f -> b
- o -> a (first 'o')
- o -> r (second 'o')
CONFLICT: 'o' cannot map to both 'a' and 'r'

Example: "paper" and "title" are isomorphic
- p -> t
- a -> i
- p -> t (consistent!)
- e -> l
- r -> e

WHY THIS APPROACH (Bidirectional Mapping):
We use TWO hash maps (bidirectional mapping) because:
1. We need to ensure ONE-TO-ONE mapping between characters
2. Single map is insufficient:
   - Example: "ab" vs "aa"
   - Map1: a->a, b->a (CONFLICT if we check)
   - Without Map2, we might miss that 'a' is already mapped TO by 'a'
3. TWO maps prevent:
   - Multiple characters in s1 mapping to same character in s2
   - One character in s1 mapping to multiple characters in s2
4. Bidirectional checking ensures bijection (one-to-one correspondence)

WHY NOT ALTERNATIVES:
1. Single hash map: Can't detect "aa" vs "ab" (both 'a's map to different chars)
2. Character frequency: "aab" and "xxy" have same pattern but need mapping validation
3. Set of pairs: Less efficient, harder to check conflicts

ALGORITHM:
Step 1: Length Validation
   - If len(s1) != len(s2), cannot be isomorphic, return 0 (False)

Step 2: Initialize Two Hash Maps
   - m1: maps characters from s1 to s2
   - m2: maps characters from s2 to s1
   - Use defaultdict(str) to return empty string for unmapped keys

Step 3: Iterate Through Both Strings Simultaneously
   For each position i:

   Case A: Both characters unmapped (m1[s1[i]] == "" and m2[s2[i]] == "")
     - Create new mapping:
       - m1[s1[i]] = s2[i]
       - m2[s2[i]] = s1[i]

   Case B: One or both characters already mapped
     - Check if mapping is consistent:
       - If m1[s1[i]] != s2[i], mapping conflict, return 0
       - Bidirectional check ensures m2 consistency too

Step 4: Return Success
   - If we processed all characters without conflict, return 1 (True)

EDGE CASES:
1. Both strings empty -> True (isomorphic)
2. Different lengths -> False
3. Same string -> True (identity mapping)
4. "ab" vs "aa" -> False (conflict: can't map both a->a and b->a)
5. "aa" vs "ab" -> False (conflict: can't map a->a and a->b)
6. Single character -> True

TIME COMPLEXITY: O(n)
- n = length of strings
- Single pass through both strings: O(n)
- Hash map operations (insert, lookup): O(1)
- Overall: O(n)

SPACE COMPLEXITY: O(k)
- k = number of distinct characters in the strings
- Two hash maps store at most k mappings each
- In worst case (all unique chars), k = n
- Overall: O(k) = O(n)

EXAMPLE WALKTHROUGH:
Input: s1 = "egg", s2 = "add"

Step 1: Length check: both length 3 ✓

Step 2: Initialize: m1 = {}, m2 = {}

Step 3: Process each character:

i=0: s1[0]='e', s2[0]='a'
  - m1['e'] == "", m2['a'] == "" -> create mapping
  - m1 = {'e': 'a'}, m2 = {'a': 'e'}

i=1: s1[1]='g', s2[1]='d'
  - m1['g'] == "", m2['d'] == "" -> create mapping
  - m1 = {'e': 'a', 'g': 'd'}, m2 = {'a': 'e', 'd': 'g'}

i=2: s1[2]='g', s2[2]='d'
  - m1['g'] == 'd' (not empty)
  - Check: m1['g'] == s2[2]? -> 'd' == 'd' ✓
  - Mappings consistent, continue

Step 4: All characters processed successfully
Output: 1 (True, strings are isomorphic)

COUNTER-EXAMPLE:
Input: s1 = "foo", s2 = "bar"

i=0: 'f'->'b', mappings: m1={'f':'b'}, m2={'b':'f'}
i=1: 'o'->'a', mappings: m1={'f':'b','o':'a'}, m2={'b':'f','a':'o'}
i=2: 'o'->'r'
  - m1['o'] = 'a' (from i=1)
  - Check: 'a' != 'r' -> CONFLICT!
Output: 0 (False, not isomorphic)
"""

# Isomorphic Strings

from collections import defaultdict

class Solution:
    def areIsomorphic(self, s1, s2):
        """
        Check if two strings are isomorphic.

        Args:
            s1: First string
            s2: Second string

        Returns:
            1 if strings are isomorphic, 0 otherwise
        """
        n = len(s1)
        m = len(s2)

        # Step 1: Length validation
        # Strings of different lengths cannot be isomorphic
        if n != m:
            return 0

        # Step 2: Create bidirectional mapping
        m1 = defaultdict(str)  # Maps each char in s1 to corresponding char in s2
        m2 = defaultdict(str)  # Maps each char in s2 to corresponding char in s1

        # Step 3: Process each character pair
        for i in range(n):
            # Case A: Neither character has been mapped yet
            if m1[s1[i]] == "" and m2[s2[i]] == "":
                # Create new bidirectional mapping
                m1[s1[i]] = s2[i]  # s1[i] maps to s2[i]
                m2[s2[i]] = s1[i]  # s2[i] maps back to s1[i]

            # Case B: At least one character already mapped
            # Check if the mapping is consistent
            elif m1[s1[i]] != s2[i]:
                # Conflict detected:
                # s1[i] is already mapped to a different character
                # OR s2[i] is already mapped from a different character
                # (the second condition is implicitly checked by the first)
                return 0

        # Step 4: All characters processed without conflict
        return 1

