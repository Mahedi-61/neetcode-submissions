"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Two pass solution
        if not head: return None

        dt_nodes = {}
        dummy = Node(0)

        # first initialization
        temp = dummy
        org_ll = head

        # first pass 
        while org_ll:
            temp.next = Node(org_ll.val)
            temp = temp.next
            dt_nodes.update({org_ll : temp})
            org_ll = org_ll.next
             
        # second pass
        org_ll = head
        temp = dummy.next

        while org_ll:
            if org_ll.random == None:
                temp.random = None
            else: 
                temp.random = dt_nodes[org_ll.random]
                
            temp = temp.next
            org_ll = org_ll.next

        return dummy.next
