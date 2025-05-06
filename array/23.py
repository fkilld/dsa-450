class Solution:
    def longest(self, arr, N):
        """
        Finds the length of the longest subsequence of consecutive integers
        in the array 'arr' of size N using a brute-force approach.

        Approach:
        1. Treat each element arr[i] as a potential start of a consecutive run.
        2. For each start value, attempt to extend the run by checking for
           the presence of the next integer (start + current_length) by scanning
           the entire array.
        3. Continue extending until the next integer is not found.
        4. Track the maximum run length encountered.

        Time Complexity: O(N^3) in the worst case (two nested loops plus an inner scan).
        Space Complexity: O(1), aside from the input array.
        """

        # Initialize the maximum run length found so far to 1
        max_len = 1

        # Outer loop: consider each element as the start of a sequence
        for i in range(N):
            start_val = arr[i]         # candidate starting value
            # length of the current run (at least the start itself)
            current_len = 1

            # Attempt to extend the sequence one step at a time
            while True:
                next_val = start_val + current_len
                found = False

                # Scan through the array to see if next_val exists
                for j in range(N):
                    if arr[j] == next_val:
                        found = True     # we've extended the run by one
                        break            # stop scanning once found

                # If next_val was found, increase current length and try the next
                if found:
                    current_len += 1
                else:
                    # cannot extend further; exit the while loop
                    break

            # Update the global maximum if this run was longer
            if current_len > max_len:
                max_len = current_len

        # Return the length of the longest consecutive run discovered
        return max_len

s = Solution()
print(s.longest([1, 2, 3, 4, 5], 5))  # Output: 5 (1, 2, 3, 4, 5)
print(s.longest([1, 9, 3, 4, 2, 6], 6))  # Output: 4 (1, 2, 3, 4)