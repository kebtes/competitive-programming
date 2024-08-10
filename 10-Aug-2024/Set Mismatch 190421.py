# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = [0] * n

        x = None
        c = None

        for num in nums:
            seen[num-1] += 1
            if seen[num-1] == 2:
                x = num

        for i in range(n):
            if seen[i] == 0:
                c = i + 1
                break

        return [x, c]