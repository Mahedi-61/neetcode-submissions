# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # recursive solution
        if root is None:
            return TreeNode(val)

        def dfs(node):
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                    return root
                return dfs(node.left)

            elif val > node.val:
                if node.right is None:
                    node.right = TreeNode(val)
                    return root
                return dfs(node.right) 

        return dfs(root)