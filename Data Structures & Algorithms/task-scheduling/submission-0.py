
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-c for c in count.values()]
        heapq.heapify(max_heap)
        t = 0
        queue = deque()

        while max_heap or queue :
            t += 1 
            if max_heap :
                count = heapq.heappop(max_heap) + 1
                if count:
                    queue.append([count, t + n])

            if queue and queue[0][1] == t :
                heapq.heappush(max_heap, queue.popleft()[0])
                
        return t