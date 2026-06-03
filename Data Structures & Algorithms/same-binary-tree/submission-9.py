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

        if (not p and q) or (p and not q):
            return False

        query_p = deque([p])
        query_q = deque([q])

        while query_p or query_q:
            node_p = query_p.popleft()
            node_q = query_q.popleft()

            if (not node_p and node_q) or (node_p and not node_q):
                return False

            if not (node_p or node_q):
                continue

            if node_p.val != node_q.val:
                return False

            query_p.append(node_p.left)
            query_p.append(node_p.right)

            query_q.append(node_q.left)
            query_q.append(node_q.right)

        return True