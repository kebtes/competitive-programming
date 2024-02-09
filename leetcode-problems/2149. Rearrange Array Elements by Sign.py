class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        output = []

        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        for p,n in zip(pos, neg):
            output.append(p)
            output.append(n)

        return output