# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        output = []

        for (a,b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def func(start, destination, visited, result):
            if start == destination: 
                return result

            visited.add(start)

            for neighbor, weight in graph[start]:
                if neighbor not in visited:
                    res = func(neighbor, destination, visited, result * weight)

                    if res != -1:
                        return res

            visited.remove(start)
            return -1.0

        for a,b in queries:
            if a not in graph or b not in graph:
                output.append(-1.0)
                continue

            result = func(a, b, set(), 1.0)
            output.append(result)

        return output
