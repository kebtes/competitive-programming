class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft = 0
        sumRight = sum(nums[1:])

        for i in range(len(nums)-1):
            if sumLeft == sumRight:
                return i

            sumLeft += nums[i]
            sumRight -= nums[i+1]
        
        if sumLeft == 0:
            return len(nums) - 1
        
        return -1