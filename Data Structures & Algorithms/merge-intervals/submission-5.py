class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        res = [intervals[0]]
        for idx in range(1, len(intervals)):
            if res[-1][1] >= intervals[idx][0]:
                start = res[-1][0]
                end = max(res[-1][1], intervals[idx][1])
                
                res[-1] = [start, end]

            else:
                res.append(intervals[idx])

        return res