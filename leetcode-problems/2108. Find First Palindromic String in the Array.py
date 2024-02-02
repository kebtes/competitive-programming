class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        ans=""

        for item in words:
            x=item[::-1]
            if(item==x):
                return item
        return ans