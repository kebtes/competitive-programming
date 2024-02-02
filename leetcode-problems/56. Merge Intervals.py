class Solution:
    def merge(self, intervals):
        intervals.sort(key= lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            if output[-1][1] >= start:
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start, end])
        
        return output