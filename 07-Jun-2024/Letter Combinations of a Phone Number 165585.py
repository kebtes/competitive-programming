# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        output = []

        def func(i, combinations=[]):
            if i == len(digits):
                output.append("".join(combinations[:]))
                return

            current_letters = letters[digits[i]]

            for j in range(len(current_letters)):
                combinations.append(current_letters[j])
                func(i + 1, combinations)
                combinations.pop()


        func(0)
        return output
            
        