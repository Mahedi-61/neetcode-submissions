class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        state = {i:0 for i in range(numCourses)}

        # graph as course and pre
        graph = defaultdict(list)
        for p in prerequisites:
            graph[p[0]].append(p[1])

        def dfs(key):
            if state[key] == 1:
                return False
            
            if state[key] == 2:
                return True
            state[key] = 1

            for node in graph[key]:
                if not dfs(node):
                    return False
            state[key] = 2
            return True

        for key, pre in prerequisites:
            if state[key] != 2:
                if not dfs(key):
                    return False
        return True
