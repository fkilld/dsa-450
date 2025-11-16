"""
PROBLEM: Word Ladder (Shortest Transformation Sequence)

DESCRIPTION:
Given a beginWord, an endWord, and a dictionary wordList, find the length
of the shortest transformation sequence from beginWord to endWord.

Rules:
1. Only one letter can be changed at a time
2. Each transformed word must exist in wordList
3. beginWord is not in wordList (but can be used as starting point)

Example:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

Transformation: hit → hot → dot → dog → cog (length = 5)

APPROACH (BFS - Breadth First Search):
Why BFS? We want the SHORTEST path, and BFS finds shortest path in
unweighted graphs (each transformation has cost 1).

1. Convert wordList to set for O(1) lookup
2. Use BFS with queue starting from beginWord
3. For each word:
   - Try changing each position to all 26 letters
   - If new word exists in wordList:
     * Remove it from wordList (mark as visited)
     * Add to queue with incremented length
   - If new word is endWord, return length
4. If queue empties without finding endWord, return 0

KEY INSIGHT:
- This is essentially finding shortest path in an implicit graph
- Each word is a node
- Two words are connected if they differ by one letter
- We don't build the graph explicitly; we generate neighbors on-the-fly

FLOWCHART:
┌─────────────────────┐
│ Start               │
│ Queue: [beginWord,1]│
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Queue empty?        │
└──────┬──────────────┘
       │
      NO│              YES
       │               │
       ▼               ▼
┌─────────────────────┐  ┌──────────────┐
│ Dequeue (word, len) │  │ Return 0     │
└──────┬──────────────┘  │ (no path)    │
       │                 └──────────────┘
       ▼
┌─────────────────────┐
│ word == endWord?    │
└──────┬──────────────┘
       │
      NO│              YES
       │               │
       ▼               ▼
┌─────────────────────┐  ┌──────────────┐
│ For each position i │  │ Return len   │
│ in word             │  └──────────────┘
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ For each letter     │
│ 'a' to 'z'          │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Create new_word by  │
│ replacing char at i │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ new_word in         │
│ wordList?           │
└──────┬──────────────┘
       │
      NO│              YES
       │               │
       │               ▼
       │       ┌─────────────────────┐
       │       │ Remove from wordList│
       │       │ Enqueue [new_word,  │
       │       │         len+1]      │
       │       └──────┬──────────────┘
       │              │
       └──────────────┘
              │
              ▼
       (Loop back to dequeue)

EXAMPLE TRACE:
beginWord = "hit", endWord = "cog"
wordList = {"hot","dot","dog","lot","log","cog"}

Queue: [("hit", 1)]
Process "hit": try all variations → find "hot"
Queue: [("hot", 2)]
Process "hot": try all variations → find "dot", "lot"
Queue: [("dot", 3), ("lot", 3)]
Process "dot": try all variations → find "dog"
Queue: [("lot", 3), ("dog", 4)]
Process "lot": try all variations → find "log"
Queue: [("dog", 4), ("log", 4)]
Process "dog": try all variations → find "cog"
Return 5

TIME COMPLEXITY: O(M² × N)
- M: length of each word
- N: number of words in wordList
- For each word, we try M positions × 26 letters = O(M × 26)
- Creating new word takes O(M)
- Total: O(M² × N)

SPACE COMPLEXITY: O(M × N)
- Queue can hold up to N words
- Each word is of length M
- WordList set: O(M × N)

INTERVIEW TIPS:
1. Use BFS for shortest path in unweighted graphs
2. Convert to set for O(1) lookup (critical optimization)
3. Remove word from set when visited (prevents revisiting)
4. Generate neighbors on-the-fly (don't pre-build graph)
5. Edge case: endWord not in wordList → return 0
6. This is a classic "implicit graph" problem
"""

from collections import deque

class Solution:
    def wordLadder(self, beginWord, endWord, wordList):
        """
        Find shortest transformation sequence from beginWord to endWord.

        Args:
            beginWord: Starting word
            endWord: Target word
            wordList: List of valid intermediate words

        Returns:
            Length of shortest transformation sequence, or 0 if impossible
        """
        # Convert to set for O(1) lookup instead of O(n)
        wordList = set(wordList)

        # Length of words (all words have same length)
        wordLen = len(beginWord)

        # BFS queue: stores [word, transformation_length]
        q = deque([[beginWord, 1]])

        # BFS traversal
        while q:
            # Dequeue current word and its transformation length
            word, length = q.popleft()

            # Base case: reached target word
            if word == endWord:
                return length

            # Try changing each character position
            for i in range(wordLen):
                # Try all 26 lowercase letters
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    # Create new word by replacing character at position i
                    new_word = word[:i] + c + word[i + 1:]

                    # If new word exists in dictionary
                    if new_word in wordList:
                        # Remove to mark as visited (prevent cycles)
                        wordList.remove(new_word)

                        # Add to queue with incremented length
                        q.append([new_word, length + 1])

        # No transformation sequence found
        return 0