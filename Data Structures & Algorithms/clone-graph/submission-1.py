"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        res = []
        if node is None:
            return node
       
        def bfs(q):
            while q:
                temp = q.popleft()
                ls_new = []
                for nbors in temp.neighbors:
                    if nbors not in visit:
                        new_nbors = Node(nbors.val)
                        q.append(nbors)
                        visit.update({nbors: new_nbors})
                    else:
                        new_nbors = visit[nbors]

                    ls_new.append(new_nbors)
                visit[temp].neighbors = ls_new

        q = collections.deque([node])
        visit = {node : Node(node.val)}
        bfs(q)
        return visit[node]

        