class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # #brute force approach
        # result = []
        # for num in range(0, n+1):
        #     c = 0
        #     for i in range(32):
        #         if num & (1 << i) > 0:
        #             c += 1
        #     result.append(c)

        # return result

        #DP__ bottom_up
        offset = 1
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset *= 2

            dp[i] = 1 + dp[i - offset]
        return dp 