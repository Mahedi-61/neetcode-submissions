class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        dict_counter = {}
        for i, c in enumerate(s):
            dict_counter[c] = i

        max_last_idx = 0
        j = 0
        res = []
        for i in range(len(s)):
            max_last_idx = max(max_last_idx, dict_counter[s[i]])
            
            if i == max_last_idx:
                res.append(i - j + 1)
                j = i + 1

        return res
