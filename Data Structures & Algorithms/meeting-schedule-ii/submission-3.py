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
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]

        start.sort()
        end.sort()

        s = 0
        e = 0
        count = 0
        res = 0
        while s < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
                res = max(res, count)
            else:
                count -= 1
                e += 1
            

        return res
