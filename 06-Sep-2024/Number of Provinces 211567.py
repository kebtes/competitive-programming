# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    graph[i].append(j)

        seen = set()
        output = 0
        for i in range(n):
            if i not in seen:
                queue = deque([i])
                while queue:
                    node = queue.popleft()

                    for edge in graph[node]:
                        if edge not in seen:
                            seen.add(edge)
                            queue.append(edge)

                output += 1

        return output