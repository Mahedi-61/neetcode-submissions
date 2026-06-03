class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if len(trust) == 0: return -1
        ls_people = set(range(1, n+1))
        t_people = set([t[0] for t in trust])

        diff = list(ls_people - t_people)
        print(t_people)
        if len(diff) != 1: return -1
        else:
            judge = diff[0]
            final_people = set()
            for t in trust:
                if t[1] == judge:
                    final_people.add(t[0])

            diff = list(t_people - final_people)
            return judge if len(diff) == 0 else -1

        