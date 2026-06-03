# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(node):
            nonlocal res
            if node is None:
                return 0

            height_l = dfs(node.left)
            height_r = dfs(node.right)

            res = res and abs(height_l - height_r) < 2
            return  1 + max(height_l, height_r)

        dfs(root)
        return res