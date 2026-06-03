# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # first solution: DFS with recursion
        diameter = 0
        def dfs (node):
            nonlocal diameter
            if node is None:
                return 0
            
            depth_l = 1 + dfs(node.left)
            depth_r = 1 + dfs(node.right)
            depth = max(depth_l, depth_r)

            diameter = max(diameter, depth_l + depth_r - 2)
            return depth
        
        dfs(root)
        return diameter