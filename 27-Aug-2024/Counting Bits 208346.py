# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        nums = [i for i in range(0, n+1)]
        output = [bin(i).count('1') for i in nums]
        return output