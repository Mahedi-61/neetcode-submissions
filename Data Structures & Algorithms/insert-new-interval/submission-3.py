class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i 
        # and also intervals still does not have any overlapping intervals. 
        # You may merge the overlapping intervals if needed.
        # Return intervals after adding newInterval.

        res = []
        for i, iv in enumerate(intervals):
            if  newInterval[1] < iv[0]:
                res.append(newInterval)
                return res + intervals[i :]

            elif iv[1] < newInterval[0]:
                res.append(iv)

            else:
                newInterval = [min(newInterval[0], iv[0]), max(newInterval[1], iv[1])]

        res.append(newInterval)
        return res 