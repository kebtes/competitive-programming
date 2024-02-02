class Solution:
    def pivotInteger(self, n: int) -> int:
        left_sum = 0
        right_sum = sum(range(2, n+1))
        
        for i in range(1,n+1):
            if left_sum == right_sum:
                return i
            
            left_sum += i
            right_sum -= i+1   
    
        return -1