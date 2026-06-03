# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # dfs with recursion
        # iteration with stack and dfs
        # bfs with query

        def dfs(node):
            if val < node.val:
                if node.left:
                    dfs(node.left)
                else:
                    node.left = TreeNode(val)

            elif val > node.val:
                if node.right:
                    dfs(node.right)
                else:
                    node.right = TreeNode(val)

        if not root: return TreeNode(val)
        dfs(root)
        return root