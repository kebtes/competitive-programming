# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_good_idx = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_good_idx:
                last_good_idx = i

        return last_good_idx == 0
        