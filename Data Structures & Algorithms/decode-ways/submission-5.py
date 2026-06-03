class Solution:
    def numDecodings(self, s: str) -> int:
        #dynammic programming
        if s[0] == "0": return 0
        if len(s) == 1: return 1

        dp = [0] * (len(s) + 1)
        dp[1] = 1

        for i in range(1, len(s)):
            if s[i] == "0":
                if s[i-1] == "0" or s[i-1] not in ["1", "2"]:
                    return 0
                if i == 1: dp[i + 1] = dp[i]
                else:
                    dp[i + 1] = dp[i-1]

            else:
                if 11 <= int(s[i-1 : i+1]) <= 26:
                    if i == 1: dp[i+1] = 2
                    if i > 1: dp[i + 1] = dp[i-1] + dp[i]

                else:
                    dp[i+1] = dp[i]

        return dp[-1]



