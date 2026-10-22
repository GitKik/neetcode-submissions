import heapq

class MedianFinder:

    def __init__(self):
        self.left_heap  = []
        self.right_heap  = []
        heapq.heapify(self.left_heap)
        heapq.heapify(self.right_heap)

    def addNum(self, num: int) -> None:
        if len(self.right_heap)== 0: 
            heapq.heappush(self.right_heap, num)
            return 
        if num >= self.right_heap[0]:
            heapq.heappush(self.right_heap, num)
        else : 
            heapq.heappush(self.left_heap, -num)
        # if one of the heaps is too big remove it's last elem 
        # and push it in the other heap 
        if len(self.left_heap) > len(self.right_heap) + 1 :
            value = heapq.heappop(self.left_heap)
            heapq.heappush(self.right_heap, - value)
        if len(self.right_heap) > len(self.left_heap) + 1 :
            value = heapq.heappop(self.right_heap)
            heapq.heappush(self.left_heap, - value)
        return 


    def findMedian(self) -> float:
        if len(self.left_heap) > len(self.right_heap) :
            return - self.left_heap[0]
        elif len(self.left_heap) < len(self.right_heap) :
            return self.right_heap[0]
        else : 
            return (- self.left_heap[0] + self.right_heap[0]) / 2
        
        