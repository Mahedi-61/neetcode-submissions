# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recurssion
        result = []

        def do_recurr(node):
            if node is None:
                return
            
            result.append(node.val)
            do_recurr(node.left)
            do_recurr(node.right)
                
        do_recurr(root)
        return result