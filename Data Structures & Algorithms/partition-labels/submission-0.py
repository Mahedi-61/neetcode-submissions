class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #two pass solution
        dt_char = {}
        for i, c in enumerate(s):
            if c in dt_char:
                dt_char[c].append(i)
            else:
                dt_char[c] = [i]
        
        res = []
        start, end = 0, 0
        while end < len(s):
            for i, c in enumerate(s):
                end = max(end, dt_char[c][-1])

                if i == end:
                    res.append(len(s[start : end + 1]))
                    start = end + 1
                    end = start
                    break
                   
        return res