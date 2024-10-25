# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = None

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

    def lcp(self):
        prefix = []

        curr = self.root
        while len(curr.children) == 1 and not curr.is_end:
            child = list(curr.children.keys())[0]
            prefix.append(child)

            curr = curr.children[child]

        return "".join(prefix)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()

        for word in strs:
            if not word: return ""
            trie.insert(word)
        
        return trie.lcp()
