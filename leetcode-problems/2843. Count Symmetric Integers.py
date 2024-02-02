class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for i in range(low, high+1):
            digit = str(i)
            length = len(digit)

            if len(digit)%2 == 0:
                lh = digit[:length//2]
                rh = digit[length//2:]

                ls = sum(map(int, lh))
                rs = sum(map(int, rh))

                if ls == rs: count +=1

        return count