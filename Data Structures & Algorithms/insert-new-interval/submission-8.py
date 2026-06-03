class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #non-overlapping intervals 
        # sorted in asceding order by start_i

        res = [newInterval]
        for i in range(len(intervals)):
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])

            elif intervals[i][1] < res[-1][0]:
                res = res[:-1] + [intervals[i]] + [res[-1]]

            elif res[-1][0] < intervals[i][0] or (intervals[i][0] <= res[-1][0] and res[-1][0] <= intervals[i][1]):
                res[-1][0] = min(res[-1][0], intervals[i][0])
                res[-1][1] = max(res[-1][1], intervals[i][1])

        return res
