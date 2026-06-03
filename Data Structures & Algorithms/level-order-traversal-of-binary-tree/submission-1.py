# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        if root:
            q = deque([root])
            while q:
                res.append([None] * len(q))
                for i in range(len(q)):
                    node = q.popleft()
                    res[-1][i] = node.val

                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)

        return res