class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs]
        dict_ag = {}

        for in_str in strs:
            count = [0] * 26
            for c in in_str:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)
            if key not in dict_ag:
                dict_ag[key] = [in_str]
            else:
                dict_ag[key].append(in_str)
                
        return list(dict_ag.values())