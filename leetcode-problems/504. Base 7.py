class Solution:
    def convertToBase7(self, num: int) -> str:
        rem = 1
        result = ""
        negative = num < 0
        quotient = 1
        num = abs(num)
    
        while quotient != 0:
            rem = num%7
            quotient = num // 7
            num = quotient
            result += str(rem)
        
        if negative:
            return f"{result}-"[::-1]
        else:
            return result[::-1]
    