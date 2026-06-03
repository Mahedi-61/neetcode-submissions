# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same(root1, root2):
            if not root1 and not root2:
                return True
            
            if not root1 or not root2:
                return False

            if root1.val != root2.val:
                return False

            return is_same(root1.left, root2.left) and is_same(root1.right, root2.right)

        def dfs(node1, node2):
            if not node1 or not node2:
                return False

            if is_same(node1, node2):
                return True

            return dfs(node1.left, node2) or dfs(node1.right, node2)


        return dfs(root, subRoot)