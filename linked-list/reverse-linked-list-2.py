# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]: 
        if left == right:
            return head
        dummy = ListNode()
        dummy.next = head
        leftNode = rightNode = curr = dummy
        i = 0

        while i != left:
            leftNode = curr
            curr = curr.next
            i+=1
        
        while i != right:
            curr = curr.next
            i+=1
        
        rightNode = curr.next
        curr.next = None

        def reverse(node):
            if node.next:
                tmp = reverse(node.next)
                node.next = None
                c = tmp
                while c.next:
                    c = c.next
                c.next = node
                return tmp
            return node
        
        leftNode.next = reverse(leftNode.next)
        curr = leftNode.next
        
        while curr.next:
            curr = curr.next
        curr.next = rightNode
        
        return dummy.next