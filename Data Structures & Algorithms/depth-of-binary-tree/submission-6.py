# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursion using dfs
        # iteration using bfs (queue)
        q = deque([root])
        count = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node is None:
                    continue

                else:
                    q.append(node.right)
                    q.append(node.left)

            if q: count += 1

        return count