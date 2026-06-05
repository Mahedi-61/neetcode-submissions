class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0
        i = 0
        max_sub = 1
        dict_save = {s[0] : 0}

        for idx in range(1, len(s)):
            if s[idx] in dict_save:
                last_iter_idx = dict_save[s[idx]]

                ls_items = list(dict_save.items())
                for key, val in ls_items:
                    if val <= last_iter_idx:
                        del dict_save[key]

                dict_save[s[idx]] = idx
                i = last_iter_idx + 1

            else:
                dict_save[s[idx]] = idx
                max_sub = max(max_sub, idx - i + 1)
                print(dict_save)

        return max_sub