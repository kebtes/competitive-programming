# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False

        def func(f_num, s_num, rem):
            if len(rem) < max(len(f_num), len(s_num)):
                return False

            if (f_num[0] == "0" and len(f_num) != 1) or (s_num[0] == "0" and len(s_num) != 1):
                return False

            result = str(int(f_num) + int(s_num))
            
            if len(rem) < len(result):
                return False
            
            if result == rem[0: len(result)]:
                if len(rem) == len(result):
                    return True

                return func(s_num, result, rem[len(result):])

            return False
            
        for i in range(1, len(num)):
            for j in range(i+1, len(num)):
                f_num = num[:i]
                s_num = num[i:j]
                rem = num[j:]

                if func(f_num, s_num, rem): return True

        return False