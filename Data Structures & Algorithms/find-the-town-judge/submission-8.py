class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        incoming_e = defaultdict(int)
        outgoing_e = defaultdict(int)

        for src, dst in trust:
            outgoing_e[src] = outgoing_e[src] + 1
            incoming_e[dst] = incoming_e[dst] + 1

        for p in range(1, n+1):
            if outgoing_e[p] == 0 and incoming_e[p] == n-1:
                return p

        return -1