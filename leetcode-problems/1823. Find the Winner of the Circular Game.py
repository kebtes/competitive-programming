class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [x for x in range(1,n+1)]
        i = 0

        while len(players) > 1:
            i = (i+k-1) % len(players)
            players.remove(players[i])

        return players[0]

        