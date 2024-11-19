# Problem: Dota2 Senate - https://leetcode.com/problems/dota2-senate/

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = deque()
        d_queue = deque()

        for i, s in enumerate(senate):
            if s == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)

        n = len(senate)
        while r_queue and d_queue:
            r_idx = r_queue.popleft()
            d_idx = d_queue.popleft()

            if r_idx < d_idx:
                r_queue.append(r_idx + n)
            else:
                d_queue.append(d_idx + n)

        return "Dire" if d_queue else "Radiant"