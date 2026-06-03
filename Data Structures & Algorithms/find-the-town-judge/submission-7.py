class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # set of pople set_n
        # set of people who have trust set_trust, dict_trustee
        # set_judge 

        set_n = set(list(range(1, n+1)))
        dict_trustee = defaultdict(set)
        set_trust = set()

        for t in trust:
            set_trust.add(t[0])
            dict_trustee[t[1]].add(t[0])

        set_judge = set_n - set_trust
        if len(set_judge) == 0:
            return -1
        
        for j in set_judge:
            set_people = dict_trustee[j]
            if set_n - set_people == {j}:
                return j
        return -1
