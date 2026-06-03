# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        def do_reversal(node):
            if node is None:    return 
            values.append(node.val)
            do_reversal(node.left)
            do_reversal(node.right)

        do_reversal(root)
        return values