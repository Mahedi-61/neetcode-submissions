class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        #brute-force solution
        delta = defaultdict(int) # he/she loves

        for t in trust:
            delta[t[0]] = - 1 + delta.get(t[0], 0) 
            delta[t[1]] =   1 + delta.get(t[1], 0)

        for person in delta:
            if delta[person] == n-1:
                return person

        return -1
