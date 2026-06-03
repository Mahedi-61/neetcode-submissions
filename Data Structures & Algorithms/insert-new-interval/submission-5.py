class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0: return [newInterval]

        intervals.append(newInterval)
        intervals.sort()
        n = len(intervals)
        i = 1

        while i < n:
            start, end = intervals[i]
            if intervals[i-1][1] >= start:
                intervals[i-1][1] = max(end, intervals[i-1][1])
                del intervals[i]
                n -= 1
                continue

            i += 1

        return intervals

