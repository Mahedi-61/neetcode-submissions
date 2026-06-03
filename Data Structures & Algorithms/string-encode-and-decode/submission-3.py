class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "_" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        print(s)
        t_len = ""

        while i < len(s):
            if s[i] != "_":
                t_len += s[i]
                i += 1

            else:
                i += 1
                res.append(s[i : i + int(t_len)])
                i += int(t_len)
                t_len = ""

        return res
