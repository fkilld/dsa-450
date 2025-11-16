"""
PALINDROME PARTITIONING
=======================

Problem Statement:
-----------------
Given a string s, partition s such that every substring of the partition is a
palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example:
--------
Input: s = "aab"
Output: [["a","a","b"], ["aa","b"]]

Input: s = "racecar"
Output: [["r","a","c","e","c","a","r"], ["r","a","cec","a","r"],
         ["r","aceca","r"], ["racecar"]]

Input: s = "a"
Output: [["a"]]

Approach:
---------
1. Use Backtracking to explore all possible partitions
2. Start from index 0 and try to partition at every possible position
3. For each partition point, check if substring is a palindrome
4. If it's a palindrome, add it to current path and recurse for remaining string
5. When we reach end of string (idx == len(s)), we found a valid partition
6. Backtrack by removing last substring to explore other partitions

Time Complexity: O(N * 2^N) - We have 2^N possible partitions, and palindrome
                 check takes O(N) time
Space Complexity: O(N) - Recursion stack depth + path storage

Flowchart:
----------
```mermaid
graph TD
    A[Start: idx=0, path=[]] --> B{idx == len s ?}
    B -->|Yes| C[Found valid partition - Add to result]
    C --> D[Return]
    B -->|No| E[Try each position i from idx to n]
    E --> F{Is s[idx:i+1] palindrome?}
    F -->|No| G[Try next position]
    G --> E
    F -->|Yes| H[Add substring to path]
    H --> I[Recurse: solve idx=i+1]
    I --> J[Backtrack: Remove substring from path]
    J --> G
    G -->|All positions tried| D
```
"""


class Solution:

    def isPalindrome(self, s, i, j):
        """
        Check if substring s[i:j+1] is a palindrome

        Args:
            s (str): Input string
            i (int): Starting index
            j (int): Ending index

        Returns:
            bool: True if substring is palindrome, False otherwise
        """
        # Use two pointers to check from both ends
        while i <= j:
            # If characters don't match, not a palindrome
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def solve(self, idx, path, s):
        """
        Recursive backtracking function to find all palindrome partitions

        Args:
            idx (int): Current index in string
            path (list): Current partition path (list of palindrome substrings)
            s (str): Input string
        """
        # Base Case: Reached end of string - found valid partition
        if idx == self.n:
            # Add copy of current path to result
            self.res.append(path[:])
            return

        # Try partitioning at each possible position from idx to end
        for i in range(idx, self.n):
            # Check if current substring s[idx:i+1] is a palindrome
            if self.isPalindrome(s, idx, i):
                # Extract the palindrome substring
                new_str = s[idx:i + 1]

                # Include this palindrome in current path
                path.append(new_str)

                # Recursively partition the remaining string
                self.solve(i + 1, path, s)

                # Backtracking: Remove substring to try other partitions
                path.pop()

    def partition(self, s):
        """
        Main function to find all palindrome partitions

        Args:
            s (str): Input string to partition

        Returns:
            list: List of all possible palindrome partitions
        """
        self.n = len(s)  # Length of input string

        # Initialize result list to store all valid partitions
        self.res = []

        # Start backtracking from index 0 with empty path
        self.solve(0, [], s)

        return self.res


# Example Usage and Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Simple case with double letters
    print("Test Case 1:")
    s1 = "aab"
    result1 = sol.partition(s1)
    print(f"Input: s = '{s1}'")
    print(f"Output: {result1}")
    print(f"Explanation: 'aab' can be partitioned as ['a','a','b'] or ['aa','b']")

    # Test Case 2: Palindrome string
    print("\nTest Case 2:")
    s2 = "racecar"
    result2 = sol.partition(s2)
    print(f"Input: s = '{s2}'")
    print(f"Output: {result2}")
    print(f"Total partitions: {len(result2)}")

    # Test Case 3: Single character
    print("\nTest Case 3:")
    s3 = "a"
    result3 = sol.partition(s3)
    print(f"Input: s = '{s3}'")
    print(f"Output: {result3}")

    # Test Case 4: All different characters
    print("\nTest Case 4:")
    s4 = "abc"
    result4 = sol.partition(s4)
    print(f"Input: s = '{s4}'")
    print(f"Output: {result4}")
    print(f"Explanation: Only one way - each character separately")
