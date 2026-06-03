class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs]
        dict_ag = {}

        for in_str in strs:
            if in_str == "":
                dict_ag["key"] = [in_str] + dict_ag.get("key", [])
                continue

            count = [0] * 26
            for c in in_str:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)
            dict_ag[key] = [in_str] + dict_ag.get(key, [])
        return list(dict_ag.values())