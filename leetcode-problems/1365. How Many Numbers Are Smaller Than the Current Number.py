class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smp = sorted(nums)

        output = [0] * len(nums)

        for idx in range(len(nums)):
            output[idx] = smp.index(nums[idx])

        return output

        
        