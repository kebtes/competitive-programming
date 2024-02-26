class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones = sum(nums)
        zeros = 0

        max_sum = 0
        output = []

        for idx in range(len(nums) + 1):
            sum_ = zeros + ones
            
            if sum_ > max_sum:
                max_sum = sum_
                output = [idx]
            elif sum_ == max_sum:
                output.append(idx)

            if idx == len(nums):
                break

            if nums[idx] == 0:
                zeros += 1
            elif nums[idx] == 1:
                ones -= 1

        return output
