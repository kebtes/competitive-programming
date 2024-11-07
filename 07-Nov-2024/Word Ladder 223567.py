# Problem: Word Ladder - https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)

        if endWord not in wordList:
            return 0
            
        queue = deque([(beginWord, 1)])
        seen = set()

        while queue:
            word, level = queue.popleft()

            for idx in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:idx] + char + word[idx + 1:]

                    if new_word == endWord:
                        return level + 1

                    if new_word not in seen and new_word in wordList:
                        seen.add(new_word)
                        queue.append((new_word, level + 1))

        return 0