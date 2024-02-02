class Solution:
    def sequentialDigits(self, low, high):
        s = "123456789"
        output = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for i in range(len(s) - length + 1):
                num = int(s[i:i+length])

                if num > high:
                    break
                elif low <= num:
                    output.append(num)

        return output