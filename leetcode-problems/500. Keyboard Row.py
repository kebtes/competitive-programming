class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ouput = []

        row1 = list("qwertyuiop")
        row2 = list("asdfghjkl")
        row3 = list("zxcvbnm")
    
        for word in words:
            flag = 0
            temp = word
            word = word.lower()
    
            if word[0] in row1:
                res_row = row1
            elif word[0] in row2:
                res_row = row2
            else:
                res_row = row3
    
            for i in range(0, len(word)):
                if word[i] not in res_row:
                    flag = 1
                    break
            
            if flag == 0:
                ouput.append(temp)
        
        return ouput