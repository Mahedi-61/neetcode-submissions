class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        # [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
        print(intervals)
        count = 0
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            print(res, count)
            if res[-1][1] > intervals[i][0]:
                if res[-1][1] > intervals[i][1]:
                    res.pop()
                    res.append(intervals[i])

                count += 1

            else:
                res.append(intervals[i])

        return count