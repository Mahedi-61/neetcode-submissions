# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs_traverse(node):
            if node is None: 
                return (0, True)

            l_d = dfs_traverse(node.left) #(1, True)
            r_d = dfs_traverse(node.right) #(2, True)

            prior_dec = l_d[1] and r_d[1]
            dec = abs(l_d[0] - r_d[0]) < 2 and prior_dec
            return (1 + max(l_d[0], r_d[0]), dec)

        h, d = dfs_traverse(root)
        return d