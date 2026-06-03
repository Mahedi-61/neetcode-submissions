# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Brute force solution
        # have pre-order dfs traversal on both trees. 
        # Check whether they are equal or not

        def traverse(node1, node2):
            if node1 is None and node2 is not None:
                return False

            elif node1 is not None and node2 is None:
                return False
           
            elif node1 is None and node2 is None:
                return True

            elif node1.val != node2.val:
                return False

            res_l = traverse(node1.left, node2.left)
            res_r = traverse(node1.right, node2.right)
            if res_l is None: res_l = True
            if res_r is None: res_r = True
            return res_l and res_r

        return traverse(p, q)

            