# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #iterative solution DFS with stack
        stack = [[root, False]]
        res = []

        while stack:
            node, status = stack.pop()

            if node is None:
                continue
            if status == True:
                res.append(node.val)
                continue

            stack.append([node, True])
            if node.right:
                stack.append([node.right, False])
            if node.left:
                stack.append([node.left, False])

        return res