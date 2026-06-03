class Solution:
    def countBits(self, n: int) -> List[int]:
        #DP _ bottom_up
        off = 1
        dp = [0] * (n+1)

        for num in range(1, n+1):
            if off  * 2 == num:
                off = off * 2
            
            #recurrence logic
            dp[num] = 1 + dp[num - off]
        return dp