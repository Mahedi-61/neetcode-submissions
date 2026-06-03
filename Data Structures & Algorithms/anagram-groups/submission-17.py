class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]: return [[""]]
        
        dt_count = {}
        for s in strs:
            dt_s = {}
            for s_i in s:
                if s_i in dt_s:
                    dt_s[s_i] += 1
                else:
                    dt_s[s_i] = 1
            dt_count.update({s : dt_s})

        # second pass
        res = {}
        for s in strs:
            dt_s_key = dt_count[s]
            s_key = "".join(sorted(s))
            if s_key in res:
                res[s_key].append(s)
            else:
                res[s_key] = [s]

        return list(res.values())