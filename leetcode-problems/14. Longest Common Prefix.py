class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        minimum, maximum = min(strs), max(strs)
    
        for i in range(len(minimum)):
            if minimum[i] == maximum[i]:
                prefix += minimum[i]
            else:
                break
        return prefix