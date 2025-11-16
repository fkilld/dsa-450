"""
Problem: Split the Binary String into Substrings with Equal Number of 0s and 1s
--------------------------------------------------------------------------------
Given a binary string, find the maximum count of substrings it can be split into
such that each substring has equal number of 0s and 1s.

APPROACH: Single Pass Counter (Greedy)
---------------------------------------
WHY THIS APPROACH?
- We use a greedy single-pass approach that splits the string whenever we find
  equal counts of 0s and 1s up to the current position
- This works because if we have equal 0s and 1s up to position i, we can make
  a valid split there and start fresh from position i+1
- No need for complex DP or backtracking - greedy gives optimal result
- Key insight: Any time we achieve balance (count0 == count1), we should split
  immediately to maximize the number of substrings

ALGORITHM:
1. Initialize counters for 0s, 1s, and valid substrings
2. Traverse the string character by character
3. Increment count0 or count1 based on current character
4. Whenever count0 == count1, we found a valid substring - increment result
5. The counters continue accumulating (don't reset) which naturally handles
   subsequent substrings
6. Return the total count of valid substrings

TIME COMPLEXITY: O(n) where n is the length of the string
- Single pass through the string

SPACE COMPLEXITY: O(1)
- Only using constant extra space for counters

EDGE CASES:
- Empty string: returns 0
- String with all 0s or all 1s: returns 0 (no valid split possible)
- String with odd length: may have valid substrings but won't use all characters
- Single "01" or "10": returns 1

EXAMPLE:
Input: "0100110101"
- At index 1: count0=1, count1=1 -> valid substring "01" (count=1)
- At index 5: count0=3, count1=3 -> valid substring "001101" (count=2)
- At index 7: count0=4, count1=4 -> valid substring "01" (count=3)
- At index 9: count0=5, count1=5 -> valid substring "01" (count=4)
Output: 4
"""

def maxSubstr(string):
    count0 = 0 # counts the number of '0's till that index 
    count1 = 0 # counts the number of '1's till that index
    count = 0 # counts the number of substrings which have the same number 0s and 1s

    for i in range(len(string)):
        if string[i] == '0':
            count0 += 1
        else:
            count1 += 1
        
        # checking if number of 1s and 0s are equal till here
        if count1 == count0:
            count += 1
    
    return count if count > 0 else 0

string = input("Enter the binary string: ")
print(maxSubstr(string))