# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_same(node1, node2):
            if not (node1 or node2):
                return True

            if not (node1 and node2) or node1.val != node2.val:
                return False
            
            sl = is_same(node1.left, node2.left)
            sr = is_same(node1.right, node2.right)
            return sl and sr


        q = deque([root])
        while q:
            node = q.popleft()
            if is_same(node, subRoot):
                return True
            
            if node.right:
                q.append(node.right)

            if node.left:
                q.append(node.left)
            
        return False
