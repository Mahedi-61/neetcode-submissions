class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # greedy solution | O(n^2) solution
        for i in range(len(gas)):
            tank = gas[i]
            j = i

            while tank >= cost[j]:
                tank -= cost[j]
                j = (j + 1) % len(cost)
                tank += gas[j]
                if j == i:
                    return i

        return -1