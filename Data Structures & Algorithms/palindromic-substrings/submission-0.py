class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) < 2: return len(s)
        sub_count = 0

        for i in range(len(s)):
            sub_count += 1
            l = i - 1
            r = i + 1

            if l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                    sub_count += 1
                    l -= 1
                    r += 1
        
            l = i
            r = i + 1
            if r <= len(s)-1 and s[l] == s[r]:
                while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                    sub_count += 1
                    r += 1
                    l -= 1

        return sub_count