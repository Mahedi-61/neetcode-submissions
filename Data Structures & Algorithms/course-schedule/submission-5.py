class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # preparing graph
        graph = defaultdict(list)
        state = {i:0 for i in range(numCourses)}
        
        for p in prerequisites:
            graph[p[0]].append(p[1])

        def dfs(node):
            if state[node] == 1:
                return False 
            elif state[node] == 2:
                return True 

            state[node] = 1
            for n_node in graph[node]:
                if not dfs(n_node):
                    return False

            state[node] = 2
            return True

        status = True
        for key, val in prerequisites:
            if state[key] < 2:
                if not dfs(key):
                    return False

        return True


