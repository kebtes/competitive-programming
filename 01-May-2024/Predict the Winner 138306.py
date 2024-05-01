# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def func(self, nums, left, right, turn, memo):
        if left > right:
            return 0
        
        if (left, right, turn) not in memo:
            if turn == 0:
                op_1 = self.func(nums, left+1, right, 1-turn, memo) + nums[left]
                op_2 = self.func(nums, left, right-1, 1-turn, memo) + nums[right]

                memo[(left, right, turn)]  = max(op_1, op_2)

            else:
                op_1 = self.func(nums, left+1, right, 1-turn, memo) - nums[left]
                op_2 = self.func(nums, left, right-1, 1-turn, memo) - nums[right]

                memo[(left, right, turn)] = min(op_1, op_2)

        return memo[(left, right, turn)]

    def predictTheWinner(self, nums: List[int]) -> bool:
        return self.func(nums, 0, len(nums)-1, 0, {}) >= 0
        