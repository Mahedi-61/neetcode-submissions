# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        while node:
            if not (node.left or node.right):
                continue

            if node.val > p.val and node.val > q.val:
                node = node.left

            elif node.val < p.val and node.val < q.val:
                node = node.right

            elif (p.val < node.val and node.val < q.val) or (p.val > node.val and node.val > q.val):
                return node

            elif p.val == node.val or q.val == node.val:
                return node