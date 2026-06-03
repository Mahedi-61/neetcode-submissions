# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #using iterative BFS approach
        queue_p = deque([p])
        queue_q = deque([q])

        while queue_p:
            for _ in range(0, len(queue_p)):
                node_p = queue_p.popleft()
                node_q = queue_q.popleft()

                if node_p is None and node_q is None:
                    continue
                elif node_p is not None and node_q is not None:
                    pass
                else:
                    return False

                if node_p.val == node_q.val:
                    queue_p.append(node_p.left)
                    queue_p.append(node_p.right)

                    queue_q.append(node_q.left)
                    queue_q.append(node_q.right)
                else:
                    return False

        return True
