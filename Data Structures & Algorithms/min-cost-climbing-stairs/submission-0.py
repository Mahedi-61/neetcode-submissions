class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        top = len(cost)

        for i in range(len(cost)-2, -1, -1):
            
            if i + 1 < top:
                cost1 = cost[i] + cost[i + 1]
            else:
                cost1 = 0

            if i + 2 < top:
                cost2 = cost[i] + cost[i + 2] 
            else:
                cost2 = None

            if cost2 is not None:
                cost[i] = min(cost1, cost2)
            else:
                cost[i] = cost1

        return min(cost[0], cost[1]) 
            
