# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length+=1
            curr = curr.next
        if length < 2:
            return head
        k = k%length
        if k == 0:
            return head
        dummy = ListNode()
        curr = head
        for i in range(length-k-1):
            curr = curr.next
        dummy.next = curr.next
        curr.next = None
        curr = dummy.next
        for i in range(k-1):
            curr = curr.next
        curr.next = head
        return dummy.next