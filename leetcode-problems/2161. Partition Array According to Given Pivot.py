from collections import deque

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        output = []
        greater_nums = deque()

        for num in nums:
            if num > pivot:
                greater_nums.append(num)
            elif num < pivot:
                output.append(num)
            else:
                greater_nums.appendleft(num)

        output.extend(greater_nums)

        return output