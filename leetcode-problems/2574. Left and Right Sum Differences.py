class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        running_sum = 0
        left_right = []
    
        for num in nums:
            total_sum -= num
            left_right.append(abs(total_sum - running_sum))
            running_sum += num
    
        return left_right