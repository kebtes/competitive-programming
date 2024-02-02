from collections import Counter

class Solution:
    def majorityElement(self, nums):
        count = Counter(nums)

        highest = [x for x in count if count[x] > len(nums)/2]

        return highest[-1] 
        