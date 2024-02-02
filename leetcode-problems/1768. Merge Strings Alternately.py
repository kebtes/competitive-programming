class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        length = min(len(word1), len(word2))
        
        for i in range(length):
            output.append(word1[i])
            output.append(word2[i])
            
        if word1[length:] == "":
            output.extend(word2[length:])        
        
        if word2[length:] == "":
            output.extend(word1[length:])
            
        return "".join(output)
