# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def removeNode(head, n):
            if head.next:
                n, head.next = removeNode(head.next, n)
            if n == 1:
                return 0, head.next
            else:
                return n-1, head
        
        n, head = removeNode(head, n)
        return head