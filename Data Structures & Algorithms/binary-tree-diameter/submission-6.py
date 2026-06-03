# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # first solution: BFS
        order = []
        if root:
            query = deque([root])

        while query:
            node = query.popleft()

            order.append(node)
            if node.left:
                query.append(node.left)

            if node.right:
                query.append(node.right)


        order = order[::-1]
        max_dm = 0
        height = {}
        for node in order:
            height_l = height.get(node.left, 0)
            height_r = height.get(node.right, 0)

            height_node = 1 + max(height_l, height_r)
            height[node] = height_node

            max_dm = max(max_dm, height_l + height_r)

        return max_dm 













