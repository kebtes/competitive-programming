class Solution:
    def reverse(self, x: int) -> int:
        
        reversed = 0
        isNegative = x < 1
        num = abs(x)

        while num != 0:

            remainder = num % 10
            reversed = (reversed * 10) + remainder
            num //= 10

        if isNegative:
            reversed = (reversed)*-1

        if reversed < -2**31 or reversed > 2**31 - 1:
            return 0

        else:
            return reversed

