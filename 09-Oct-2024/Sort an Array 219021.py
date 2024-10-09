# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_half,right_half) -> List[int]:
            l1, l2 = 0, 0
            output = []

            while l1 < len(left_half) and l2 < len(right_half):
                if left_half[l1] < right_half[l2]:
                    output.append(left_half[l1])
                    l1 += 1

                else:
                    output.append(right_half[l2])
                    l2 += 1

            if left_half[l1:]:
                output.extend(left_half[l1:])

            if right_half[l2:]:
                output.extend(right_half[l2:])

            return output

        if len(nums) <= 1:
            return nums

        m = len(nums) // 2
        left_part = self.sortArray(nums[:m])
        right_part = self.sortArray(nums[m:]) 

        return merge(left_part, right_part)