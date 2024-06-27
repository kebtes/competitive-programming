# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited_cells = set()
        visited_cells.add(0)

        queue = deque([0])

        while queue:
            node = queue.popleft()

            for edge in rooms[node]:
                if edge not in visited_cells:
                    visited_cells.add(edge)
                    queue.append(edge)
        
        return len(visited_cells) == n


        