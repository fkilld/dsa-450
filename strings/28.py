"""
Second Most Repeated String in a Sequence

PROBLEM:
Given an array of strings, find the string that appears with the second highest frequency.
If multiple strings have the same second-highest frequency, return the first one encountered.

WHY THIS APPROACH:
We use Frequency Counting with Two-Max Tracking because:
1. We need frequency information, so counting is essential (HashMap/Dictionary)
2. We only need the top 2 frequencies, not a full sort
3. Tracking two max values (max_1, max_2) is more efficient than sorting all frequencies
4. Single pass to count + single pass to find maximums = O(n) time
5. This avoids the O(n log n) cost of sorting the frequency map

ALTERNATIVE APPROACHES NOT USED:
- Sorting: Would be O(n log n), slower than needed
- Heap: Overkill when we only need top 2 values
- Counter + most_common(2): Cleaner but same complexity, less educational

ALGORITHM:
1. Count Frequencies:
   - Create a dictionary to count occurrences of each string
   - Iterate through array and increment count for each string

2. Find Top 2 Frequencies:
   - Initialize max_1 (highest) and max_2 (second highest) to -1
   - For each string in the array:
     * If count > max_1: update max_2 = max_1, then max_1 = count
     * Else if count > max_2 and count != max_1: update max_2 = count

3. Find String with Second Highest Frequency:
   - Iterate through array again
   - Return first string whose count equals max_2

TIME COMPLEXITY: O(n) where n is the length of array
- O(n) to build frequency map
- O(n) to find max_1 and max_2
- O(n) to find the string with second max frequency
- Total: O(3n) = O(n)

SPACE COMPLEXITY: O(k) where k is number of unique strings
- Dictionary to store frequencies of unique strings
- In worst case (all unique), k = n, so O(n)

EDGE CASES:
1. Only one unique string: No second most frequent (return None or handle as error)
2. All strings have same frequency: max_2 will be -1 (no second highest)
3. Two strings with different frequencies: Second one is the answer
4. Multiple strings with second-highest frequency: Returns first occurrence in array

EXAMPLES:
Input: ["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"]
Frequencies: {"aaa": 3, "bbb": 2, "ccc": 1}
Output: "bbb" (frequency 2 is second highest)

Input: ["geek", "for", "geek", "for", "geek"]
Frequencies: {"geek": 3, "for": 2}
Output: "for" (frequency 2 is second highest)

Input: ["apple", "banana", "apple", "cherry", "banana", "apple"]
Frequencies: {"apple": 3, "banana": 2, "cherry": 1}
Output: "banana"
"""

class Solution:
    def secFrequent(self, arr, n):
        """
        Find the string with second highest frequency in array

        Args:
            arr: Array of strings
            n: Length of array (not used, can get from len(arr))

        Returns:
            String with second highest frequency
        """
        # Step 1: Build frequency map
        count = {}
        for i in range(len(arr)):
            if arr[i] not in count:
                count[arr[i]] = 1
            else:
                count[arr[i]] += 1

        # Step 2: Find the top 2 frequencies using two-max tracking
        max_1 = -1  # Stores the highest frequency
        max_2 = -1  # Stores the second highest frequency

        for string in arr:
            if count[string] > max_1:
                # Found new maximum: shift max_1 to max_2, update max_1
                max_2 = max_1
                max_1 = count[string]
            elif count[string] > max_2 and count[string] != max_1:
                # Found new second maximum (must be different from max_1)
                max_2 = count[string]

        # Step 3: Find and return first string with second highest frequency
        for string in arr:
            if count[string] == max_2:
                return string