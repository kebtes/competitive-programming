# Problem: Reorganize String - https://leetcode.com/problems/reorganize-string/description/

class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        output = []
        heap = []

        for e, f in c.items():
            heap.append((-f, e))

        heapq.heapify(heap)

        last_checked = None    
        while len(heap) > 0:
            ch = heapq.heappop(heap)

            if ch[1] == last_checked:
                if len(heap) == 0:
                    return ""

                f, e = heapq.heappop(heap)
                f += 1

                output.append(e)

                if f != 0:
                    heapq.heappush(heap, (f, e))

                heapq.heappush(heap, ch)
                last_checked = e 

            else:
                f, e = ch

                output.append(e)
                f += 1

                if f != 0:
                    heapq.heappush(heap, (f, e))

                last_checked = e

        return "".join(output)
