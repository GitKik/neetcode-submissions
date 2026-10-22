import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums = sorted(nums)
        while len(nums) < k:
            nums.append(-1001)
        nums_trun = nums[-k:]
        print(nums_trun)
        heapq.heapify(nums_trun)
        self.heap = nums_trun

    def add(self, val: int) -> int:
        if val >= self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]
        
