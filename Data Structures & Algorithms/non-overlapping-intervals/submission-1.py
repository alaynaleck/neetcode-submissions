class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # errr let's try sorting by the first
        intervals.sort(key = lambda x: x[0])

        # now that we're sorted we can see [1,2][1,4][2,4]
        # or [1,4][1,2][2,4]

        # min start, min end
        # if the start is less than the min end, it overlaps. 
        # options: 
        # start < min end and end < min_end: remove the other, update the current interval to this
        # start < min end and end >= min_end: remove this one, keep current interval
        # start >= min_end, move to the next one, update the min start and end
        min_start, min_end, remove = float("-inf"), float("-inf"), 0
        for start, end in intervals:
            if start < min_end and end < min_end:
                # keep the current interval as the smallest
                min_start = start
                min_end = end
                remove += 1
            elif start < min_end and end >= min_end:
                remove += 1
            else:
                min_start = start
                min_end = end
        return remove
        