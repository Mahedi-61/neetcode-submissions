class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = defaultdict(int)
        for c in s1:
            s1_dict[c] = 1 + s1_dict.get(c, 0)

        l = 0
        r = len(s1)

        while r <= len(s2):
            sub_str = s2[l : r]
            sub_str_dict = defaultdict(int)

            for c in sub_str:
                sub_str_dict[c] = 1 + sub_str_dict.get(c, 0)

            if sub_str_dict == s1_dict:
                return True
            else:
                l += 1
                r += 1
        return False