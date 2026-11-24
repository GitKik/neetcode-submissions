class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        new_itv = []
        intervals = sorted(intervals, key=lambda x: x[0])
        start, end = intervals[0]
        intervals.remove(intervals[0])
        while intervals :
            iv = intervals[0]
            if iv[0] <= end :
                if iv[1] > end : 
                    end = iv[1]
            else :
                new_itv.append([start,end])
                start, end = iv[0], iv[1]
            intervals.remove(iv)
        new_itv.append([start,end])
        return new_itv
