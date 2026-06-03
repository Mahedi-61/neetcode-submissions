# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 1
        branch = []

        def dfs(node):
            nonlocal count
            if not branch:
                pass
            elif node.val >= max(branch):
                count += 1

            branch.append(node.val)
            if node.left:
                dfs(node.left)
                branch.pop()

            if node.right:
                dfs(node.right)
                branch.pop()

        dfs(root)
        return count