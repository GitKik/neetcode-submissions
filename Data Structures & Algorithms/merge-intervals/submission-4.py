class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        new_itv = []
        intervals = sorted(intervals, key=lambda x: x[0])
        start, end = intervals[0]
        for i in range(1, len(intervals)) :
            iv = intervals[i]
            if iv[0] <= end :
                if iv[1] > end : 
                    end = iv[1]
            else :
                new_itv.append([start,end])
                start, end = iv[0], iv[1]
        new_itv.append([start,end])
        return new_itv
