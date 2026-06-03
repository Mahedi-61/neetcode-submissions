class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # writing dfs to handle cycle
        def dfs(node):
            if node in path_visit:
                return
            if node in visit:
                return

            path_visit.add(node)
            for n_node in graph[node]:
                dfs(n_node)

            visit.add(node)

        #building graph
        graph = defaultdict(list)
        for out_n, in_n in edges:
            graph[out_n].append(in_n)
            graph[in_n].append(out_n)

        # traversing graph
        visit = set()
        count = 0
        for i in range(n):
            if i not in visit:
                path_visit = set()
                dfs(i)
                count += 1
                
        return count