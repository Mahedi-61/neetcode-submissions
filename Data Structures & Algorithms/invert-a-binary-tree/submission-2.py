# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if root is None: return root 
        # queue = [root]

        # while queue:
        #     node = queue.pop()
        #     if node.left is not None and node.right is not None:
        #         node.left, node.right = node.right, node.left
        #         queue.append(node.left)
        #         queue.append(node.right)

        #     elif node.right is not None:
        #         node.left = node.right
        #         node.right = None
        #         queue.append(node.left)

        #     elif node.left is not None:
        #         node.right = node.left
        #         node.left = None
        #         queue.append(node.right)

        # return root
        node = root
        def do_traverse(node):
            if node is None: return 

            if node.left and node.right:
                node.left, node.right = node.right, node.left
                do_traverse(node.left)
                do_traverse(node.right)

            elif node.left is not None:
                node.right = node.left
                node.left = None
                do_traverse(node.right)

            elif node.right is not None:
                node.left = node.right
                node.right = None
                do_traverse(node.left)

        do_traverse(node)
        return root
