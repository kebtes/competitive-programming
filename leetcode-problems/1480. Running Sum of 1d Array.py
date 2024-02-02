class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []
        curr_sum = 0

        for num in nums:
            curr_sum += num
            prefix.append(curr_sum)

        return prefix