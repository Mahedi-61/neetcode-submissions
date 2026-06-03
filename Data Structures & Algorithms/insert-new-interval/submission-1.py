class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i 
        # and also intervals still does not have any overlapping intervals. 
        # You may merge the overlapping intervals if needed.
        # Return intervals after adding newInterval.
        if len(intervals) == 0: return [newInterval]
        a, b = newInterval
        res = []
        temp_a = temp_b = None 
        is_insert = False

        for iv in intervals:
            if iv[1] < a:
                res.append(iv)

            if temp_a is None and (a < iv[0] or iv[0] <= a <= iv[1]):
                temp_a = min(iv[0], a)

            if b > iv[1] or iv[0] <= b <= iv[1]:
                temp_b = max(iv[1], b) 
                if is_insert: res[-1][1] = temp_b     

            if not is_insert and temp_a is not None and temp_b is not None:
                is_insert = True
                res.append([temp_a, temp_b])

            if iv[0] > b:
                res.append(iv)

        if not is_insert:
            if b < intervals[0][0]:
                res.append([0, 0])
                res[1 : ] = res[ : -1]
                res[0] = newInterval

            elif intervals[-1][1] < a:
                res.append(newInterval)

        return res

