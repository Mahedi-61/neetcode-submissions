# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iteration using bfs (queue)
        max_depth = 0
        if not root: return max_depth
        query = deque([root])

        while query:
            max_depth += 1
            for _ in range(len(query)):
                node = query.popleft()

                if node.left:
                    query.append(node.left)
                if node.right:
                    query.append(node.right)

        return max_depth

        # recursion using dfs
        # max_depth = 0
        # def dfs(node, depth):
        #     nonlocal max_depth
        #     if not node:
        #         return depth

        #     if node.left:
        #         dfs(node.left, depth + 1)
            
        #     if node.right:
        #         dfs(node.right, depth + 1)

        #     max_depth = max(max_depth, depth + 1)
        #     return depth + 1

        # dfs(root, 0)
        # return max_depth
