class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs]

        dict_ag = {}
        for in_str in strs:
            if len(in_str) == 0:
                dict_ag["empty"] = [""] + dict_ag.get("empty", []) 
                continue

            sort_in_str = "".join(sorted(in_str)) #change later
            dict_ag[sort_in_str] = [in_str] + dict_ag.get(sort_in_str, [])

        return list(dict_ag.values())