# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_tree(node1, node2):
            if (node1 is None) and (node2 is None):
                return True

            elif (node1 == None and node2) or (node1 and node2==None):
                return False

            if node1.val != node2.val:
                return False

            return check_tree(node1.left, node2.left) and check_tree(node1.right, node2.right)



        def bfs(r_node, sub_node):
            if not r_node:
                return False

            query = collections.deque()
            query.append(r_node)

            while query:
                r_node = query.popleft()
 
                if check_tree(r_node, sub_node):
                    return True
                
                if r_node.left:
                    query.append(r_node.left)
                
                if r_node.right:
                    query.append(r_node.right)

            return False


        return bfs(root, subRoot)