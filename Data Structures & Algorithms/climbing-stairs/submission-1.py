class Solution:
    def cal_stairs(self, n, count=0, memo={}):
        if n == 0: return 1
        elif n < 0 : return 0
        if n in memo: return memo[n]
        
        for i in [1, 2]:
            count += self.cal_stairs(n - i)

        memo[n] = count
        return count

    def climbStairs(self, n: int) -> int:
        return self.cal_stairs(n)