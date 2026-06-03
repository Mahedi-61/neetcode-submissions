class Solution:
    def climbStairs(self, n: int) -> int:
        # dp (bottom up)
        # dp = {}
        # dp[-1] = 0
        # dp[0] = 1

        # for i in range(1, n+1):
        #     dp[i] = dp[i - 1] + dp[i - 2]

        # return dp[n]

        # dp (top-down)
        def do_climb(n, count=0):
            if n == 0: return 1 
            elif n < 0: return 0 

            for i in [1, 2]:
                count += do_climb(n - i)

            return count
        return do_climb(n)

