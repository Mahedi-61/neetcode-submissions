class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs]

        dict_ag = {}
        for in_str in strs:
            if len(in_str) == 0:
                if "empty" in dict_ag:
                    dict_ag["empty"].append(in_str)
                else:
                    dict_ag["empty"] = [in_str]
                continue

            sort_in_str = "".join(sorted(in_str)) #change later
            if sort_in_str in dict_ag:
                dict_ag[sort_in_str].append(in_str)
            else:
                dict_ag[sort_in_str] = [in_str]

        return list(dict_ag.values())