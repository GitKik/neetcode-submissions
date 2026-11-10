import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        heapq.heapify(h)
        
        for i in range(len(points)) :
            p = points[i]
            distance = math.sqrt(p[0]*p[0] + p[1]*p[1])
            heapq.heappush(h, (distance, p))
        print(h)
        return [hh[1] for hh in heapq.nsmallest(k, h)]
