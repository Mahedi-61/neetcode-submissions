# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balance = True
        def dfs(node):
            nonlocal balance
            if node is None:
                return 0

            depth_l = dfs(node.left)
            depth_r = dfs(node.right)
            balance = balance and abs(depth_l - depth_r) < 2
            return 1 + max(depth_l, depth_r)

        dfs(root)
        return balance