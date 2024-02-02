from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    
        symbols = "!?',;."
   
        for symbol in symbols:
            paragraph = paragraph.replace(symbol, " ")
        
        paragraph_list = paragraph.lower().split()
        
        count_dict = Counter(paragraph_list)
        
        max_count = 0
        most_common_words = []

        for word, count in count_dict.items():
            if word not in banned and count > max_count:
                max_count = count
                most_common_words = [word]
            elif word not in banned and count == max_count:
                most_common_words.append(word)
        return most_common_words[0] 
