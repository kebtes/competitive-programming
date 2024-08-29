# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        previous_bit = n & 1

        while n > 0:
            n >>= 1
            current_bit = n & 1

            if current_bit == previous_bit:
                return False

            previous_bit = current_bit

        return True
        