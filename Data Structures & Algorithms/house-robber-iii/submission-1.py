# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        ## My solution: 2 steps
        # iterate vai the tree
        # write dp relation
        def dfs_not_rob(node):
            left, right = 0, 0
            if node in memo_rob:
                return memo_rob[node]

            if node.left:
                left = max(dfs_not_rob(node.left), dfs_rob(node.left))

            if node.right:
                right = max(dfs_not_rob(node.right), dfs_rob(node.right))
            
            memo_rob[node] = left + right
            return left + right

        def dfs_rob(node):
            left, right = 0, 0
            if node in memo_not_rob:
                return memo_not_rob[node]
            if node.left:
                left = dfs_not_rob(node.left)
            if node.right:
                right = dfs_not_rob(node.right)

            memo_not_rob[node] = node.val + left + right
            return node.val + left + right
           
        memo_rob = {}
        memo_not_rob = {}
        return max(dfs_rob(root), dfs_not_rob(root))


