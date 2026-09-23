class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        results = []
        intervals.sort(key = lambda x: x[0])
        min_start, max_end = intervals[0][0], intervals[0][1]
        for start, end in intervals:

            if start <= max_end:
                max_end = max(max_end, end)
            else:
                results.append([min_start, max_end])
                min_start = start
                max_end = end

        results.append([min_start, max_end])
        return results
