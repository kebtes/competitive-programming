# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_notes = 0
        ten_notes = 0

        for bill in bills:
            if bill == 5:
                five_notes += 1
            elif bill == 10:
                if five_notes == 0:
                    return False
                
                ten_notes += 1
                five_notes -= 1
            
            else:
                if ten_notes >= 1 and five_notes >= 1:
                    ten_notes -= 1
                    five_notes -= 1
                elif five_notes >= 3:
                    five_notes -= 3
                else:
                    return False

        return True
                    
