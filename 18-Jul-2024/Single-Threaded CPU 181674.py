# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(start, duration, i) for i, (start, duration) in enumerate(tasks)])
        
        output, heap, idx, current_time = [], [], 0, tasks[0][0]

        while heap or idx < len(tasks):
            while idx < len(tasks) and current_time >= tasks[idx][0]:
                heapq.heappush(heap, (tasks[idx][1], tasks[idx][2])) 
                idx += 1

            if heap:
                duration, original_index = heapq.heappop(heap)
                current_time += duration
                output.append(original_index)
            else:
                current_time = tasks[idx][0]

        return output
