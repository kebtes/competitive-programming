class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        t = nums[0]
        for num in nums:
            if abs(num) == abs(t):
                t = max(t,num)
            elif abs(num) < abs(t):
                t= num
        return t
          
        
            