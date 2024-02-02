from collections import Counter
class Solution:
    def majorityElement(self, nums):
        counted = Counter(nums)
        compare = len(nums//3)
        output = []

        for num, count in counted.items():
            if count > compare:
                output.append(num)
                
        return output