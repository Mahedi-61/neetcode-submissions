class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        #kadane's algorithm
        tank = 0
        idx = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                idx = i + 1
                tank = 0
        return idx
