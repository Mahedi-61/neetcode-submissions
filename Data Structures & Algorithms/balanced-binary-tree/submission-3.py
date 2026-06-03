# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs_recurse(node):
            if node is None: return (0, True)

            l_depth, l_isb = dfs_recurse(node.left)
            r_depth, r_isb = dfs_recurse(node.right)

            isb = abs(l_depth - r_depth) < 2 and (l_isb and r_isb)
            depth = 1 + max(l_depth, r_depth)
            return (depth, isb)

        depth, isb = dfs_recurse(root)
        return isb