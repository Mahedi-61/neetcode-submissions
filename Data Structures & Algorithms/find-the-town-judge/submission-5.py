class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        p_dict = defaultdict(int) # he/she loves
        l_dict = defaultdict(int) #being loved

        for t in trust:
            p_dict[t[0]] = 1 + p_dict.get(t[0], 0) 
            l_dict[t[1]] = 1 + l_dict.get(t[1], 0)

        for person in l_dict:
            if l_dict[person] == n-1 and p_dict[person] == 0:
                return person

        return -1
