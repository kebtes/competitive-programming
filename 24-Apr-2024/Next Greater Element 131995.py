# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ouput = []

        indices = {}

        for i in range(len(nums2)):
            indices[nums2[i]] = i

        for num in nums1:
            ind = indices[num]
            res = -1
    
            for i in range(ind+1, len(nums2)): 
                if nums2[i] > num:
                    res = nums2[i]
                    break
    
            ouput.append(res)
    
        return ouput