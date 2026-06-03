# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        visit = [False]

        while stack:
            node, v = stack.pop(), visit.pop()

            if node:
                if v:
                    res.append(node.val)
                else:
                    stack.append(node.right)
                    visit.append(False)

                    stack.append(node)
                    visit.append(True)

                    stack.append(node.left)
                    visit.append(False)

        return res