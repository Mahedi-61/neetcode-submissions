"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# [(0,40),(5,10),(15,20)]
# [(5,10),(15,20), (0,40)] min_end_times = [20, ]
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 2: return len(intervals) 
        intervals.sort(key = lambda x: x.start)

        min_end_times = []
        count = 1
        heapq.heappush(min_end_times, intervals[0].end)

        for i in range(1, len(intervals)):
            if min_end_times[0] <= intervals[i].start:
                heapq.heappop(min_end_times)
                heapq.heappush(min_end_times, intervals[i].end)

            else:
                count += 1
                heapq.heappush(min_end_times, intervals[i].end)
        
        return count