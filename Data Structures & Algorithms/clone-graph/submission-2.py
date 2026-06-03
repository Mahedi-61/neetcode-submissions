"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        res, q = None, deque()
        graph = {}

        if node:
            clone = Node(node.val, [])
            res = clone
            graph[node] = clone
            q.append((node, clone))

        def bfs(q):
            while q:
                temp, clone = q.popleft()

                for n_node in temp.neighbors:
                    clone_n_node = graph[n_node] if n_node in graph else Node(n_node.val, [])
                    clone.neighbors.append(clone_n_node)

                    if n_node not in graph:
                        q.append((n_node, clone_n_node))

                    graph[n_node] = clone_n_node
        bfs(q)
        return res
