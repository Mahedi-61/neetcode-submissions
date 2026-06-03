class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        seen = {i:0 for i in range(numCourses)}
        graph = defaultdict(list)
        for cour, pre in prerequisites:
            graph[cour].append(pre)

        def bfs(i):
            if seen[i] == 1:
                return False

            if seen[i] == 2:
                return True

            seen[i] = 1
            ls_pres = graph[i]
            for pre in ls_pres:
                if not bfs(pre):
                    return False

            seen[i] = 2
            if i not in res_set:
                res.append(i)
                res_set.add(i)
            return True

        res = []
        res_set = set(res)
        for i in range(numCourses):
            if seen[i] < 2:
                if not bfs(i):
                    return []

        for i in range(numCourses):
            if i not in res_set:
                res.append(i)
                res_set.add(i)

        return res
