class Solution:
    def mySqrt(self, x: int) -> int:
        root = 1
    
        if x == 0:
            return 0

        for i in range(1, x//2 +1):
            if i*i <= x:
                root = i
            else:
                return root
        return root

