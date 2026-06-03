class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            dt_s = [0] * 26
            for s_i in s:
                dt_s[ord(s_i) - ord("a")] += 1 

            s_key = tuple(dt_s)
            if s_key in res:
                res[s_key].append(s)
            else:
                res[s_key] = [s]

        return list(res.values())