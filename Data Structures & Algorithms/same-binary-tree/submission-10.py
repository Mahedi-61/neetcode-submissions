# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not (p or q):
            return True

        query = deque([(p, q)])

        while query:
            node_p, node_q= query.popleft()

            if (not node_p and node_q) or (node_p and not node_q):
                return False

            if not (node_p or node_q):
                continue

            if node_p.val != node_q.val:
                return False

            query.append((node_p.left,  node_q.left))
            query.append((node_p.right, node_q.right))

        return True