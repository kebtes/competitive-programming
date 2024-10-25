# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]

        curr.is_end = True

    def find_prefix(self, word):
        prefix = []
        curr = self.root

        for char in word:
            if char not in curr.children or curr.is_end:
                break

            prefix.append(char) 
            curr = curr.children[char]

        # print(prefix)
        return "".join(prefix)

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        quick_lookup = set(dictionary)

        for word in dictionary:
            trie.insert(word)

        output = []
        for word in sentence.split(" "):
            # trie.insert(word)
            prefix = trie.find_prefix(word)

            if prefix in quick_lookup:
                output.append(prefix)
            
            else:
                output.append(word)

        return " ".join(output)