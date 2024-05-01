# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def invert(self, s):
        if s in self.inverted_cache:
            return self.inverted_cache[s]
        
        inverted_s = "".join(['1' if c == '0' else '0' for c in s])
        self.inverted_cache[s] = inverted_s
        return inverted_s
    
    def reverse(self, s):
        if s in self.reversed_cache:
            return self.reversed_cache[s]
        
        reversed_s = s[::-1]
        self.reversed_cache[s] = reversed_s
        return reversed_s

    def findKthBit(self, n: int, k: int) -> str:
        bs = ["0"] * (n + 1)
        
        self.inverted_cache = {}
        self.reversed_cache = {}

        for i in range(1, n+1):
            bs[i] = bs[i-1] + "1" + self.reverse(self.invert(bs[i-1]))

        return bs[n-1][k-1]
