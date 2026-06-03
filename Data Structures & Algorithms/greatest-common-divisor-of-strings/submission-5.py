class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2: return str1
        if len(str1) > len(str2):
            a = str1
            b = str2
        else:
            a = str2
            b = str1
        
        if len(a) % len(b) == 0 and a == b * (len(a) // len(b)):
            return b

        mid = math.ceil(len(b) / 2)
        for i in range(mid+1, 0, -1):
            sub = b[ : i]
            if len(b) % len(sub) == 0 and len(a) % len(sub) == 0:
                count_b = len(b) // len(sub)
                count_a = len(a) // len(sub)
                print(count_a, count_b)
                if a == sub * count_a and b == sub * count_b:
                    return sub

        return ""