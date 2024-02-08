class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero_loss = set()
        one_loss = set()
        multiple_loss = set()

        for match in matches:
            winner, loser = match[0], match[1]

            if winner not in one_loss and winner not in multiple_loss:
                zero_loss.add(winner)

            if loser in zero_loss:
                zero_loss.remove(loser)
                one_loss.add(loser)
            elif loser in one_loss:
                one_loss.remove(loser)
                multiple_loss.add(loser)
            elif loser in multiple_loss:
                continue
            else:
                one_loss.add(loser)
            
        return [sorted(list(zero_loss)), sorted(list(one_loss))]