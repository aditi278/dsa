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
        dummy_head = head
        dummy = curr = Node(0)
        i = 0
        m = {}
        while head:
            curr.next = Node(head.val)
            m[head] = curr.next
            head = head.next
            curr = curr.next
            
        
        curr = dummy.next
        head = dummy_head
        
        while curr:
            curr.random = m[head.random] if head.random else None
            curr = curr.next
            head = head.next

        return dummy.next
        