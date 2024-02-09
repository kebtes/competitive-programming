class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index_dict = {}

        for ind, char in enumerate(nums):
            index_dict[char] = ind
    
        for i, j in operations:
            current_index = index_dict[i]
            nums[current_index] = j
            
            index_dict.pop(i)
            index_dict[j] = current_index
    
        return nums