class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 1
        i = 0
        if s == "": return 0
        save_dict = {s[0] : 0}

        for idx in range(1, len(s)):
            if s[idx] in save_dict:
                last_idx = save_dict[s[idx]]
                ls_tuples = list(save_dict.items())

                for key, val in ls_tuples:
                    if val <= last_idx:
                        del save_dict[key]

                save_dict[s[idx]] = idx
                i = last_idx + 1
            
            else:
                save_dict[s[idx]] = idx
                max_sub = max(max_sub, idx - i + 1)

        return max_sub
