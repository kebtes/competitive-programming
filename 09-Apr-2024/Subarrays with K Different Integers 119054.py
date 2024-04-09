# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def func(self, nums, k):
        output = 0
        freq_dict = {} 
        l = 0

        for r in range(len(nums)):
            freq_dict[nums[r]] = freq_dict.get(nums[r], 0) + 1

            while len(freq_dict) > k:
                freq_dict[nums[l]] -= 1

                if not freq_dict[nums[l]]:
                    del freq_dict[nums[l]]
                l += 1

            output += r - l + 1

        return output

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.func(nums, k) - self.func(nums, k - 1)
        
        