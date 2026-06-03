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
        org_list = []
        new_list = []
        new_head = Node(0)
        dummy = new_head

        while head:
            dummy.next = Node(head.val, next=None, random=head.random)
            org_list.append(head)
            new_list.append(dummy.next)

            head = head.next
            dummy = dummy.next

        dummy = new_head.next
        while dummy:
            if dummy.random is not None:
                dummy.random = new_list[org_list.index(dummy.random)]
            dummy = dummy.next

        return new_head.next