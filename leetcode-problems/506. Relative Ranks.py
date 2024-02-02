class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort = sorted(score, reverse=True)
        output = []

        for sco in score:
            ind = sort.index(sco)
            if ind == 0:
                output.append("Gold Medal")
            elif ind == 1:
                output.append("Silver Medal")
            elif ind == 2:
                output.append("Bronze Medal")
            else:
                output.append(f"{ind+1}")

        return output