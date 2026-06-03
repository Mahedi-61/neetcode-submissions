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
        org_head = head
        dict_nodes = {None: None} #org:new
        while org_head:
            temp = Node(org_head.val)
            dict_nodes[org_head] = temp
            org_head = org_head.next


        org_head = head
        while org_head:
            curr = dict_nodes[org_head]
            curr.next = dict_nodes[org_head.next]
            curr.random = dict_nodes[org_head.random]
            org_head = org_head.next
            
        return dict_nodes[head]

