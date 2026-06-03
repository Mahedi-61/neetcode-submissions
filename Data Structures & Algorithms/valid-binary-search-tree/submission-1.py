# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, min_val, max_val):
            left = right = True
            if not (min_val < node.val and node.val < max_val):
                return False

            if node.left:
                if node.left.val > min_val and node.left.val < node.val:
                    left = dfs(node.left, min_val, node.val)
                else:
                    return False

            if node.right:
                if node.right.val > node.val and node.right.val < max_val:
                    right = dfs(node.right, node.val, max_val)
                else:
                    return False

            return left and right

        if not root:
            return True

        return dfs(root, float("-inf"), float("inf"))