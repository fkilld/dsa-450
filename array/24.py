class Solution:
    def majorityElement(self, nums):
        """
        Problem:
          Given an integer array nums of size n, find all elements that appear
          more than ⌊n/3⌋ times.

        Constraints:
          • There can be at most two such elements.
          • Expected time complexity: O(n).
          • Expected space complexity: O(1) (excluding output list).

        Approach (Extended Boyer–Moore Voting for k = 3):
          1. We maintain up to two candidate values (num1, num2) and their counts (c1, c2).
          2. First pass:
             • If the current element matches one of the candidates, increment its count.
             • Else if a candidate’s count is zero, replace that candidate with the current element and set its count to 1.
             • Otherwise, decrement both counts (this “cancels out” one occurrence of each candidate).
          3. Second pass:
             • Reset counts and re-count the actual occurrences of num1 and num2.
          4. Collect those candidates whose final counts exceed ⌊n/3⌋.

        Time Complexity: O(n) - two linear passes.
        Space Complexity: O(1) - only a fixed number of extra variables.
        """

        n = len(nums)
        # Initialize two potential majority candidates and their counts
        num1, num2 = 0, 0   # placeholders for the two candidates
        c1, c2 = 0, 0     # their respective occurrence counters

        # First pass: find up to two candidates
        for x in nums:
            if x == num1:
                # x matches the first candidate
                c1 += 1
            elif x == num2:
                # x matches the second candidate
                c2 += 1
            elif c1 == 0:
                # no current first candidate; adopt x as num1
                num1, c1 = x, 1
            elif c2 == 0:
                # no current second candidate; adopt x as num2
                num2, c2 = x, 1
            else:
                # x matches neither candidate and both counters > 0:
                # decrement both counters (cancel out one occurrence of each)
                c1 -= 1
                c2 -= 1

        # Second pass: verify actual counts of the two candidates
        c1, c2 = 0, 0
        for x in nums:
            if x == num1:
                c1 += 1
            elif x == num2:
                c2 += 1

        # Collect valid majority elements (> ⌊n/3⌋ occurrences)
        result = []
        if c1 > n // 3:
            result.append(num1)
        if c2 > n // 3:
            result.append(num2)

        return result

s = Solution()
print(s.majorityElement([3, 2, 3]))  # Output: [3]
print(s.majorityElement([1]))  # Output: [1]

