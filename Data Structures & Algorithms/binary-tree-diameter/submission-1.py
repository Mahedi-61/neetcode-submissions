# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(node):
            if node is None: return 0

            depth_l = dfs(node.left)
            depth_r = dfs(node.right)
            res[0] = max(res[0], depth_l + depth_r)
            return 1 + max(depth_l , depth_r)

        dfs(root)
        return res[0]