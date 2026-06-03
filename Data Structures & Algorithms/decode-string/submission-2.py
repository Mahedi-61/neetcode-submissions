class Solution:
    def decodeString(self, s: str) -> str:
        num_dict = ["1", "2", "3", "4", "5", 
                    "6", "7", "8", "9", "10"]
        stack = []

        res = ""
        i = 0
        while i < len(s):
            if stack:
                if s[i] in num_dict:
                    if s[i + 1] == "[":
                        stack.append([s[i], ""])
                        i += 1

                    elif s[i+1] == "0" and s[i + 2] == "[":
                        stack.append([s[i] + "0", ""])
                        i += 2
                    
                    if s[i+1] == "0" and s[i + 2] == "0":
                        stack.append([s[i] + "00", ""])
                        i += 3

                elif s[i] == "]":
                    num, chunk = stack.pop()
                    temp = chunk * int(num)
                    if stack:
                        stack[-1][1] += temp
                    else:
                        res += temp
                else:
                    stack[-1][1] += s[i] 
            else:
                if s[i] in num_dict:
                    if s[i + 1] == "[":
                        stack.append([s[i], ""])
                        i += 1

                    elif s[i+1] == "0" and s[i + 2] == "[":
                        stack.append([s[i] + "0", ""])
                        i += 2
                    
                    if s[i+1] == "0" and s[i + 2] == "0":
                        stack.append([s[i] + "00", ""])
                        i += 3
                else:
                    res += s[i]
            i += 1

        return res