class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        output = [0] * n

        for i, num in enumerate(boxes):
            if num == "1":
                for x in range(n):
                    if x == i: continue
                    output[x] += abs(i-x)

        return output

        

        