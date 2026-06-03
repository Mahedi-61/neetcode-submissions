# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root == None: return [] 

        def traverse(current):
            if current.left is not None:
                traverse(current.left)

            result.append(current.val)

            if current.right is not None:
                traverse(current.right)
        
        traverse(root)
        return result