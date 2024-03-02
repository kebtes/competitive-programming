class Solution:
    def smallestNumber(self, num: int) -> int:
        is_negative = num < 0
        output = None

        if len(str(num)) == 1:
            return num

        if is_negative:
            num = str(num).replace("-","")
            num = "".join(sorted(num, reverse=True))
            num = int(num) * -1
            output = num 
        else:
            z_count = str(num).count('0')
            num = sorted(str(num))
            num = "".join(num).replace("0","")
            zeroes = "0"*z_count
            num = f"{num[0]}{zeroes}{num[1:]}"
            output = int(num)

        return output


        