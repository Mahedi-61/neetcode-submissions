class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            tank = 0
            cancel = False 

            for j in range(len(gas) + 1):
                idx = (i + j) % len(gas)
                tank += gas[idx] 
                if tank < cost[idx]:
                    cancel = True
                    break
                else:
                    tank -= cost[idx]
                
            if not cancel and tank >= 0: return i
        return -1