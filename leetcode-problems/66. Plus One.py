class Solution:
    def plusOne(self, digits):
        digits = digits[::-1]
        carry = 0
        i = 0

        while True:
            if carry == 0:
                if digits[i] + 1 + carry > 9:
                    carry = 1
                    digits[i] = 0
                    i += 1
                    continue

                else:
                    digits[i] = digits[i] + 1

            else:
                if i+1 > len(digits):
                    digits.append(1)

                elif digits[i] + carry > 9:
                    carry = 1
                    digits[i] = 0
                    i += 1
                    continue

                else:
                    digits[i] = digits[i] + 1

            break


        return digits[::-1]