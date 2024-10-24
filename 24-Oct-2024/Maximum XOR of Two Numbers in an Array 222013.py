# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = [None, None]  

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        curr = self.root
        
        for i in range(31, -1, -1):
            bit = (num >> i) & 1  

            if curr.children[bit] is None:
                curr.children[bit] = TrieNode()
        
            curr = curr.children[bit]

    def find_max_xor(self, num):
        curr = self.root
        max_xor = 0
        
        for i in range(31, -1, -1):
            bit = (num >> i) & 1  
            opposite_bit = 1 - bit

            if curr.children[opposite_bit] is not None:
                max_xor |= (1 << i)  
                curr = curr.children[opposite_bit]
            
            else:
                curr = curr.children[bit]
        
        return max_xor

class Solution:
    def findMaximumXOR(self, nums):
        trie = Trie()
        max_xor = 0
        
        for num in nums:
            trie.insert(num)
        
        for num in nums:
            max_xor = max(max_xor, trie.find_max_xor(num))
        
        return max_xor