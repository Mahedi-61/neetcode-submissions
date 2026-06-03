class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #path_visit to track cycle
        # visit to track visited or not
        if len(edges) < n - 1: return False

        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)
            for n_node in graph[node]:
                if n_node == parent:
                    continue

                if not dfs(n_node, node):
                    return False

            return True

        #building graph
        graph = defaultdict(list)
        for out_n, in_n in edges:
            graph[out_n].append(in_n)
            graph[in_n].append(out_n)

        visit = set()
        if not dfs(0, -1):
            return False

        for n_node in graph:
            if n_node not in visit:
                return False

        return True