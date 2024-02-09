from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counted = Counter(nums)

        return [x for x,y in counted.items() if y > (len(nums)//3)]


        