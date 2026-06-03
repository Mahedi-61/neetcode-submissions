# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# post order traversal with iteration (node, status)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        if not root: return res
        stack = [(root, False)]
        height = {None : 0}

        while stack:
            node, status = stack.pop()
            print(node.val)
            if status:
                height[node] = 1 + max(height.get(node.left, 0), height.get(node.right, 0))
                res = res and abs(height[node.left] - height[node.right]) < 2
            else:
                if not node.right and not node.left:
                    height[node] = 1
                    continue

                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))

                if node.left:
                    stack.append((node.left, False))

                
        return res

