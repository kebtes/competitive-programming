# Problem: Detonate the Maximum Bombs - https://leetcode.com/problems/detonate-the-maximum-bombs/description/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        output = 0
        
        def distance(x1, y1, x2, y2):
            return ((x1 - x2) ** 2 + (y1 - y2) ** 2)
        
        for i in range(len(bombs)):
            x1, y1, r1 = bombs[i]
            
            for j in range(len(bombs)):
                if i != j:
                    x2, y2, r2 = bombs[j]
                    if distance(x1, y1, x2, y2) <= r1 ** 2:
                        graph[i].append(j)
                    
                    if distance(x2, y2, x1, y1) <= r2 ** 2:
                        graph[j].append(i)

        def func(bomb, visited):
            visited.add(bomb)

            for neighbor in graph[bomb]:
                if neighbor not in visited:
                    func(neighbor, visited)

        for bomb in range(len(bombs)):
            visited = set()
            func(bomb, visited)
            output = max(output, len(visited))

        return output
