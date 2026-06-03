"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        q = deque()
        res = None
        graph = {}

        if node:
            clone = Node(node.val, [])
            q.append(node)
            graph[node] = clone
            res = clone

        while q:
            org = q.popleft()
            if not org: continue

            clone_node = graph[org] if org in graph else Node(org.val, [])

            for n_node in org.neighbors:
                clone_node_n = graph[n_node] if n_node in graph else Node(n_node.val, [])
                clone_node.neighbors.append(clone_node_n)

                if n_node not in graph:
                    q.append(n_node)
                    graph[n_node] = clone_node_n

        return res 