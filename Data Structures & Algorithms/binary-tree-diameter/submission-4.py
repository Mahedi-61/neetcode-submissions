# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # first solution: DFS with iteration
        # can be done using post-order traversal
        stack = [[root, False]]
        height = {}
        diameter = 0

        while stack:
            node, visit = stack.pop()
            if node:
                if visit == True:
                    h_l = height.get(node.left, 0)
                    h_r = height.get(node.right, 0)
                    height[node] = 1 + max(h_l, h_r)
                    diameter = max(diameter, h_l + h_r)

                else:
                    stack.append([node, True])
                    stack.append([node.right, False])
                    stack.append([node.left, False])

        return diameter