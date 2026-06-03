# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #dfs with iteration

        #dfs with recursion (leaf -> root) | bottom-up approach
        is_balanced = True
        def dfs(node):
            nonlocal is_balanced
            if not node:
                return 0

            h_l = dfs(node.left)
            h_r = dfs(node.right)
            height = 1 + max(h_l, h_r)
            is_balanced = is_balanced and abs(h_l - h_r) <= 1
            return height

        dfs(root)
        return is_balanced

            