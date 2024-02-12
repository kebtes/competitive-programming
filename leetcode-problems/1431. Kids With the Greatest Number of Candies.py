class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        length = len(candies)
        max_num = max(candies)
        output = [False]*length

        for i in range(length):
            if candies[i] + extraCandies >= max_num:
                output[i] = True
            
        return output

        