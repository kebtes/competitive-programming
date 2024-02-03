from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        output = [x for x,y in count.items() if y == 1]

        return output
        