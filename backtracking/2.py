"""
WORD BREAK II
=============

Problem Statement:
-----------------
Given a string s and a dictionary of words dict, add spaces in s to construct
sentences where each word is a valid dictionary word. Each dictionary word can
be used more than once. Return all such possible sentences.

Example:
--------
Input:
s = "catsanddog"
dict = ["cat", "cats", "and", "sand", "dog"]

Output: ["cats and dog", "cat sand dog"]

Explanation: We can break the string in these two ways using dictionary words.

Input:
s = "pineapplepenapple"
dict = ["apple", "pen", "applepen", "pine", "pineapple"]

Output: ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]

Approach:
---------
1. Use Backtracking to try all possible word combinations
2. Start from index 0 and try to match each dictionary word
3. If a word matches at current index, add it to current path
4. Recursively solve for remaining string
5. When we reach end of string (idx == len(s)), we found a valid sentence
6. Backtrack by removing word from path to explore other possibilities

Optimization: Can use memoization to avoid recomputing same subproblems

Time Complexity: O(2^n * n) - In worst case, exponential combinations
Space Complexity: O(n) - Recursion depth and path storage

Flowchart:
----------
```mermaid
graph TD
    A[Start: idx=0, path=[]] --> B{idx == len s ?}
    B -->|Yes| C[Add path.join with space to result]
    C --> D[Return]
    B -->|No| E[For each word in dictionary]
    E --> F{word matches at idx?}
    F -->|No| G[Try next word]
    G --> E
    F -->|Yes| H[Add word to path]
    H --> I[Recurse: idx + len word]
    I --> J[Backtrack: Remove word from path]
    J --> G
    G -->|All words tried| D
```
"""


class Solution:

    def solve(self, idx, path, dict, s):
        """
        Recursive backtracking function to find all word break combinations

        Args:
            idx (int): Current index in string s
            path (list): Current list of words forming valid sentence
            dict (list): Dictionary of valid words
            s (str): Input string to break
        """
        # Base Case: Reached end of string - found valid sentence
        if idx == self.m:
            # Join words with space and add to result
            self.res.append(" ".join(path))
            return

        # Try matching each word from dictionary at current index
        for word in dict:
            n = len(word)

            # Check if we have enough characters remaining
            if idx + n <= self.m:
                # Check if current substring matches the word
                if s[idx:idx + n] == word:
                    # Include this word in current path
                    path.append(word)

                    # Recursively solve for remaining string
                    self.solve(idx + n, path, dict, s)

                    # Backtracking: Remove word to try other possibilities
                    path.pop()


    def wordBreak(self, n, dict, s):
        """
        Main function to find all possible word break sentences

        Args:
            n (int): Size of dictionary (not used but part of signature)
            dict (list): List of valid dictionary words
            s (str): String to break into words

        Returns:
            list: All possible sentences using dictionary words
        """
        self.m = len(s)  # Length of input string

        # Initialize result list to store all valid sentences
        self.res = []

        # Start backtracking from index 0 with empty path
        self.solve(0, [], dict, s)

        return self.res


# Example Usage and Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    print("Test Case 1:")
    s1 = "catsanddog"
    dict1 = ["cat", "cats", "and", "sand", "dog"]
    result1 = sol.wordBreak(len(dict1), dict1, s1)
    print(f"Input: s = '{s1}'")
    print(f"Dictionary: {dict1}")
    print(f"Output: {result1}")

    # Test Case 2
    print("\nTest Case 2:")
    s2 = "pineapplepenapple"
    dict2 = ["apple", "pen", "applepen", "pine", "pineapple"]
    result2 = sol.wordBreak(len(dict2), dict2, s2)
    print(f"Input: s = '{s2}'")
    print(f"Dictionary: {dict2}")
    print(f"Output: {result2}")

    # Test Case 3: No solution
    print("\nTest Case 3:")
    s3 = "catsandog"
    dict3 = ["cats", "dog", "sand", "and", "cat"]
    result3 = sol.wordBreak(len(dict3), dict3, s3)
    print(f"Input: s = '{s3}'")
    print(f"Dictionary: {dict3}")
    print(f"Output: {result3}")
