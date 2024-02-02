class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
    
        for word in magazine:
            magazine_dict[word] = magazine_dict.get(word, 0) + 1

        for word in ransomNote:
            if word not in magazine_dict or magazine_dict[word] == 0:
                return False
            magazine_dict[word] -= 1

        return True
