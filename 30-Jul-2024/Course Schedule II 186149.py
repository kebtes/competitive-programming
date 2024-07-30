# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        output = []

        for a, b in prerequisites:
            graph[b].append(a)

        def dfs(course, visited=set(), visiting=set()):
            if course in visiting:
                return False  

            if course in visited:
                return True

            visiting.add(course)
            for edge in graph[course]:
                if not dfs(edge):
                    return False
        
            visiting.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []  

        return output[::-1]