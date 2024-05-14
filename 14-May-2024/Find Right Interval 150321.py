# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        output = []
        
        intervals_cpy = [(interval[0], interval[1], i) for i, interval in enumerate(intervals)]
        intervals_cpy.sort()

        for interval in intervals:
            l, r = 0, n - 1
            idx = -1

            while l <= r:
                mid = l + (r - l) // 2

                if intervals_cpy[mid][0] >= interval[1]:
                    idx = mid
                    r = mid - 1
                else:
                    l = mid + 1
            
            if idx != -1: output.append(intervals_cpy[idx][2])
            else: output.append(-1)

        return output
