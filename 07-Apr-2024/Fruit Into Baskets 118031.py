# Problem: Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq_dict = {}
        max_length = float('-inf')
        l = 0
    
        for r in range(len(fruits)):
            freq_dict[fruits[r]] = freq_dict.get(fruits[r], 0) + 1
            
            while len(freq_dict) > 2:
                freq_dict[fruits[l]] -= 1
                
                if freq_dict[fruits[l]] == 0:
                    del freq_dict[fruits[l]] 
    
                l += 1
            
            max_length = max(max_length, r-l+1)
    
        return max_length
                     