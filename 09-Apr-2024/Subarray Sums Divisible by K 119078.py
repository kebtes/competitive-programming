# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq_dict = {0:1}
        l = 0

        cnt = 0
        cum_sum = 0

        for r in range(len(nums)):
            cum_sum += nums[r]
            rem = (cum_sum % k + k) % k
            
            freq_dict[rem] = freq_dict.get(rem, 0) + 1

            if freq_dict[rem] > 1:
                cnt += freq_dict[rem] - 1

        return cnt

            