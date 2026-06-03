class Solution:
    def cal_stairs(self, n, count=0):
        if n == 0: return 1
        elif n < 0 : return 0

        for i in [1, 2]:
            count += self.cal_stairs(n - i)

        return count

    def climbStairs(self, n: int) -> int:
        return self.cal_stairs(n)