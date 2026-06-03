# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS with recursion
        # def dfs(p, q):
        #     if p is None and q is None:
        #         return True
            
        #     elif p is None or q is None:
        #         return False

        #     elif p.val != q.val:
        #         return False
                
        #     else:
        #         return dfs(p.left, q.left) and dfs(p.right, q.right)
        # return dfs(p, q)

        # BFS with iteration using queue
            queue_1 = deque([p])
            queue_2 = deque([q])
            status = True

            while queue_1 and queue_2:
                node1 = queue_1.popleft()
                node2 = queue_2.popleft()

                if node1 is None and node2 is None:
                    status = status and True
                
                elif not node1 or not node2:
                    status = status and False

                elif node1.val != node2.val:
                    status = status and False

                else:
                    queue_1.append(node1.right)
                    queue_1.append(node1.left)

                    queue_2.append(node2.right)
                    queue_2.append(node2.left)

            return status