class Solution:
    def numSquares(self, n: int) -> int:
        squares = defaultdict(int)
        k = 1
        squares = {}
        while k*k <= n:
            squares[k] = k*k
            k += 1

        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            k = 1
            ls_nums = []

            while k in squares and squares[k] <= i:
                ls_nums.append(dp[i - squares[k]] + 1)
                k += 1

            dp[i] = min(ls_nums)
        return dp[n]