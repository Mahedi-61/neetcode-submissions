# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p == root:
            return p
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not (node.left or node.right):
                continue

            elif node.left and not node.right:
                if p.val == node.val or q.val == node.val:
                    return node
                else:
                    queue.append(node.left)

            elif node.right and not node.left:
                if p.val == node.val or q.val == node.val:
                    return node
                else:
                    queue.append(node.right)

            if node.val > p.val and node.val > q.val:
                queue.append(node.left)

            elif node.val < p.val and node.val < q.val:
                queue.append(node.right)

            elif (p.val < node.val and node.val < q.val) or (p.val > node.val and node.val > q.val):
                return node

            elif p.val == node.val or q.val == node.val:
                return node

        return "sami"