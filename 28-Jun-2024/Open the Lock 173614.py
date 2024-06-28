# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        
        queue = deque()

        if "0000" not in deadends:
            queue.append(('0000', 0))

        while queue:
            # print(queue)
            prev_comb, level = queue.popleft()

            if prev_comb == target:
                return level
            
            for i in range(4):
                new_comb = prev_comb[:i] + str((int(prev_comb[i]) + 1) % 10) + prev_comb[i+1:]
                if new_comb not in deadends:
                    deadends.add(new_comb)
                    queue.append((new_comb, level + 1))

                new_comb = prev_comb[:i] + str((int(prev_comb[i]) - 1) % 10) + prev_comb[i+1:]
                if new_comb not in deadends:
                    deadends.add(new_comb)
                    queue.append((new_comb, level + 1))
        
        return -1
                

        