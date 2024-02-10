class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        mistake = False
    
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if mistake:
                    return False
                
                if i > 0 and nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i + 1]
    
                mistake = True
        
        return True