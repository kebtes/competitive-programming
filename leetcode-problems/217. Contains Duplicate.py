import collections
class Solution:
    
    def containsDuplicate(self, nums):
        freq_dict = collections.Counter(nums)

        for x in freq_dict.values():
            if x >= 2:
                return True

        return False
        