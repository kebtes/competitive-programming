# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)

        def func(permutation, indices):
            if len(permutation) == n:
                output.append(permutation[:])
                return

            for i in range(n):
                if i not in indices:
                    indices.add(i)
                    permutation.append(nums[i])
                    func(permutation, indices)
                    permutation.pop()
                    indices.remove(i)

        func([], set())
        return output



