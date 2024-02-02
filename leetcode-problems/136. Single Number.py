from collections import Counter

class Solution:
    def singleNumber(self, nums):
        count = Counter(nums)
        min_count = min(count.values())
        least = [x for x in count if count[x] == min_count]
        
        return least[0]