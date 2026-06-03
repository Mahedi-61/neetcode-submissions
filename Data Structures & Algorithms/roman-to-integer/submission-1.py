class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        i = len(s) - 1
        total = 0

        while i >= 0:
            if s[i] == "I":
                while i >= 0 and s[i] == "I":
                    total += 1
                    i -= 1

            elif s[i] in ["V", "X"]:
                i -= 1
                if i >= 0 and s[i] == "I":
                    total += roman_dict[s[i+1]] - roman_dict["I"]
                    i -= 1
                else:
                    total += roman_dict[s[i+1]]

            elif s[i] in ["L", "C"]:
                i -= 1
                if i >= 0 and s[i] == "X":
                    total += roman_dict[s[i+1]] - roman_dict["X"]
                    i -= 1
                else:
                    total += roman_dict[s[i+1]]

            elif s[i] in ["D", "M"]:
                i -= 1
                if i >= 0 and s[i] == "C":
                    total += roman_dict[s[i+1]] - roman_dict["C"]
                    i -= 1
                else:
                    total += roman_dict[s[i+1]]
        return total