class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])

        a = cost[-1]
        b = cost[-2]

        for i in range(len(cost)-3, -1, -1):
            temp = b
            b = min(a + cost[i], b + cost[i])
            a = temp

        return min(a, b)