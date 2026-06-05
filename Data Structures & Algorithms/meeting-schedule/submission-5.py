"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        res = True
        if len(intervals) == 0: return res
        intervals.sort(key = lambda x: x.start)

        for idx in range(1, len(intervals)):
            last_end = intervals[idx-1].end
            next_start = intervals[idx].start

            if last_end > next_start:
                return False

        return res