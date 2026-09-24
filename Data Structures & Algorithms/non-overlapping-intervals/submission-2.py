class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        min_start, min_end, remove = float("-inf"), float("-inf"), 0
        for start, end in intervals:
            if start < min_end and end < min_end:
                # keep the current interval as the smallest
                min_start = start
                min_end = end
                remove += 1
            elif start < min_end and end >= min_end:
                # remove the current interval 
                remove += 1
            else:
                # onto the next window
                min_start = start
                min_end = end
        return remove
        