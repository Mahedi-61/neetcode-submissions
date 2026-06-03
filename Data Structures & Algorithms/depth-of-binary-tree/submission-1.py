# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node):
            if node == None: return 0

            l = traverse(node.left)
            r = traverse(node.right)
            return 1 + max(l, r)

        return traverse(root)