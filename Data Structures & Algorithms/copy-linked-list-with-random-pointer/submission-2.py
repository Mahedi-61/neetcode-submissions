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
        dummy = Node(0)
        curr = dummy
        org_head = head

        dict_nodes = {None: None} #org:new
        while org_head:
            temp = Node(org_head.val)
            curr.next = temp
            dict_nodes[org_head] = temp

            org_head = org_head.next
            curr = curr.next

        org_head = head
        curr = dummy.next
        while org_head:
            curr.random = dict_nodes[org_head.random]
            org_head = org_head.next
            curr = curr.next

        return dummy.next

