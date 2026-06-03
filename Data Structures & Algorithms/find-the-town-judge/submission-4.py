class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming_e = defaultdict(int)
        outgoing_e = defaultdict(int)

        for src, dst in trust:
            incoming_e[dst] = 1 + incoming_e[dst]
            outgoing_e[src] = 1 + outgoing_e[src]

        for i in range(1, n + 1):
            if incoming_e[i] == n-1 and outgoing_e[i] == 0:
                return i

        return -1
