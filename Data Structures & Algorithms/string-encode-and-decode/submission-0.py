class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(in_str)) + "#" + in_str for in_str in strs])

    # 4#neet4#code
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        prev = 0

        while(i < len(s)): #1
            if s[i] == "#":
                str_len = int(s[prev : i])
                prev = i + 1 + str_len 

                result.append(s[i+1 : prev])
                i = prev 

            else:
                i += 1
        return result 