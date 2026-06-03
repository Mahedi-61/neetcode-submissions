# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # interative DFS solution
        stack = [(p, q)]

        while stack:
            node_p, node_q = stack.pop()
            if node_p is None and node_q is None:
                continue
            elif node_p is not None and node_q is not None:
                pass
            else:
                return False

            if node_p.val == node_q.val:
                stack.append((node_p.right, node_q.right))
                stack.append((node_p.left, node_q.left))
            else:
                return False
        return True
