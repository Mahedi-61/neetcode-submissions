"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0: return 0
        intervals.sort(key = lambda x: x.start)

        days = [[intervals[0]]] 
        for i in range(1, len(intervals)):

            done = False
            for day in days:
                if intervals[i].start >= day[-1].end:
                    day.append(intervals[i])
                    done = True
                    break

            if done == False:
                days.append([intervals[i]])

        return len(days)