class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        max_len = -1

        l, r = 0, 0
        seen[s[r]] = 1

        while r < len(s):
            max_val = max(seen.values())
            window_size =  r - l + 1

            if window_size - max_val <= k:
                max_len = max(max_len, window_size)
                r += 1
                if r < len(s): seen[s[r]] += 1
            else:
                seen[s[l]] -= 1
                l = l+1
            #print(seen)
        return max_len