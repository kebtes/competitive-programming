# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for start, destination in prerequisites:
            graph[start].append(destination)

        currently_visiting = set()

        def func(node):
            if node in currently_visiting: 
                return False

            if graph[node] == []:
                return True

            currently_visiting.add(node)

            for neighbour in graph[node]:
                if not func(neighbour):
                    return False

            currently_visiting.remove(node)
            graph[node] = []
            return True

        for node in range(numCourses):
            if not func(node):
                return False

        return True

        