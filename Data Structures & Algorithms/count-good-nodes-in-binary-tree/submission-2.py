# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # iterative with in-order traverse node -> left_child
        if not root: return 0
        count = 0
        array = []

        def dfs(node):
            nonlocal count
            if node is None:
                return

            array.append(node.val)
            if node.val == max(array):
                count += 1

            dfs(node.left)
            dfs(node.right)
            array.pop()

        dfs(root)
        return count



        