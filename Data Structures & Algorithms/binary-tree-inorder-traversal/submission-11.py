# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visit = [False]
        res = []

        while stack:
            node, status = stack.pop(), visit.pop()
            if node is None: continue

            if status == False:
                stack.append(node.right)
                visit.append(False)

                stack.append(node)
                visit.append(True)

                stack.append(node.left)
                visit.append(False)
            else:
                res.append(node.val)
        return res