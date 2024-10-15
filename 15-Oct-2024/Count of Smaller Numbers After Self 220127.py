# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_list = SortedList()
        output = []

        for n in nums[::-1]:
            idx = SortedList.bisect_left(sorted_list, n)
            output.append(idx)
            sorted_list.add(n)

        return reversed(output)
