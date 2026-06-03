# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #iterative solution
        node = root
        parent = None
        if node is None: return parent
        stack = [(node, parent)]

        while stack:
            node, parent = stack.pop()
            if node.val == key:
                if node.left is None and node.right is None:
                    if parent:
                        if parent.left == node: parent.left = None
                        elif parent.right == node: parent.right = None
                    else:
                        root = None
                    return root

                elif node.left is None:
                    if parent:
                        if parent.left == node: parent.left = node.right
                        elif parent.right == node: parent.right = node.right
                    else:
                        root = node.right
                    return root

                elif node.right is None:
                    if parent:
                        if parent.left == node: parent.left = node.left
                        elif parent.right == node: parent.right = node.left
                    else:
                        root = node.left
                    return root

                else:
                    if parent:
                        node.val = node.right.val
                    else:
                        root.val = node.right.val
                    key = node.right.val

            if node.left is not None and key <= node.left.val:
                stack.append((node.left, node))
            if node.right is not None and key >= node.right.val:
                stack.append((node.right, node))

        return root
                    