# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # first DFS with recursion
        # def dfs(node):
        #     if node is None:
        #         return
            
        #     node.left, node.right = node.right, node.left
        #     dfs(node.left)
        #     dfs(node.right)

        # dfs(root)
        # return root

        # second BFS with queue
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node is None:
                continue
            
            node.left, node.right = node.right, node.left
            q.append(node.right)
            q.append(node.left)
            
        return root

