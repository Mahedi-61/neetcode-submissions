class Solution:
    def romanToInt(self, s: str) -> int:
        dt_vals = {"I":1,  "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        res = 0
        i = len(s) - 1
        while i >= 0:
            if s[i] in ["V", "X"]:
                if i > 0 and s[i-1] == "I":
                    res += dt_vals[s[i]] - dt_vals[s[i-1]]
                    i -= 2
                else:
                    res += dt_vals[s[i]]
                    i -= 1


            elif s[i] in ["L", "C"]:
                if i > 0 and s[i-1] == "X":
                    res += dt_vals[s[i]] - dt_vals[s[i-1]]
                    i -= 2
                else:
                    res += dt_vals[s[i]]
                    i -= 1
            
            elif s[i] in ["D", "M"]:
                if i > 0 and s[i-1] == "C":
                    res += dt_vals[s[i]] - dt_vals[s[i-1]]
                    i -= 2
                else:
                    res += dt_vals[s[i]]
                    i -= 1

            else:
                res += 1
                i -= 1

        return res