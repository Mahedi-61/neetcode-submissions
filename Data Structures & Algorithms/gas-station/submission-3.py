class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        i = 0
        store = 0
        n = len(gas)

        while i < len(gas):
            j = i
            store = gas[j]

            while store >= cost[j]:
                store -= cost[j]
                j = (j + 1) % n
                if i == j:
                    return i

                store += gas[j] 

            i += 1

        return -1
        