class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I' : 1, 'V' : 5, 'X' : 10, 
             'L' : 50, 'C' : 100, 'D' : 500, 'M': 1000}

        if len(s) == 1: return d[s]
        i = len(s) - 1
        total = 0

        total += d[s[i]]
        i -= 1

        while i > -1:
            if s[i] == "I" and s[i + 1] in ["V", "X"]:
                    total -= 1
                    i -= 1
                
            elif s[i] == "X" and s[i + 1] in ["L", "C"]:
                    total -= 10
                    i -= 1
            
            elif s[i] == "C" and s[i + 1] in ["D", "M"]:
                    total -= 100
                    i -= 1
            else:
                total += d[s[i]]
                i -= 1

        return total

