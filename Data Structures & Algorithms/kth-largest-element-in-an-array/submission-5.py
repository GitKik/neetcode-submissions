import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n<k:
            return min(nums)
        h = []
        heapq.heapify(h)

        for i in range(k):
            heapq.heappush(h, nums[i])
        smallest_in_heap = h[0]
        for i in range(k,n):
            v = nums[i]
            if v > smallest_in_heap :
                heapq.heappop(h)
                heapq.heappush(h,v)
                smallest_in_heap = h[0]
        return h[0]        