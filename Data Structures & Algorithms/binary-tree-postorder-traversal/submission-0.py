# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        def do_recurr(node):
            if node is None:
                return

            do_recurr(node.left)
            do_recurr(node.right)
            res.append(node.val)

        do_recurr(root)
        return res 
        