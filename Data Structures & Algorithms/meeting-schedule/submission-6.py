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

        temp = intervals[0]
        for i in range(1, len(intervals)):
            if temp.end > intervals[i].start:
                return False

            else:
                temp = intervals[i]

        return res