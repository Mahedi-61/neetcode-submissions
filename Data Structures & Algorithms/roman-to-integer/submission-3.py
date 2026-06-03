class Solution:
    def romanToInt(self, s: str) -> int:
        dt_vals = {"I":1,  "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        res = 0
        prev = 0
        i = len(s) - 1
        while i >= 0:
            if dt_vals[s[i]] < prev:
                res -= dt_vals[s[i]]

            else:
                res += dt_vals[s[i]]

            prev = dt_vals[s[i]]
            i -= 1

        return res