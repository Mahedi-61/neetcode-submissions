class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2: return s
        max_pal = ""

        for i in range(1, len(s)):
            l, r = i-1, i+1
            temp_str = s[i]

            # odd palidrom
            if l >= 0 and r <= len(s)-1 and s[r] == s[l]:
                while l >= 0 and r <= len(s)-1 and s[r] == s[l]:
                    temp_str = s[l : r+1]
                    l, r = l-1, r+1

            if len(temp_str) > len(max_pal):
                max_pal = temp_str

            if l >= 0 and s[i] == s[l]:
                temp_str = s[l : i+1]
                l, r = i-2, i+1

                while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                    temp_str = s[l : r+1]
                    l, r = l-1, r+1

            elif r <= len(s)-1 and s[i] == s[r]:
                temp_str = s[i : r+1]
                l, r = i-1, i+2

                while l >=0 and r <= len(s)-1 and s[l] == s[r]:
                    temp_str = s[l : r+1]
                    l, r = l-1, r+1

            if len(temp_str) > len(max_pal):
                max_pal = temp_str

        return max_pal