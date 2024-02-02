class Solution:
    def selfDividingNumbers(self,left, right):
        lst = []
        for i in range(left, right + 1):
            isDiv = True

            if "0" in str(i):
                continue

            for char in str(i):
                if i%int(char) != 0:
                    isDiv = False
                    break

            if isDiv:
                lst.append(i)

        return lst
