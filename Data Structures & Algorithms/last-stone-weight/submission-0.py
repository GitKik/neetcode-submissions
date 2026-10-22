import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap_ = [-s for s in stones]
        heapq.heapify(heap_)
        while len(heap_) > 1 :
            a = heapq.heappop(heap_)
            b = heapq.heappop(heap_)
            a -= b
            heapq.heappush(heap_,a)
        return -heap_[0]