# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        curr = ListNode(head.val - 1)
        curr.next = head
        head = curr
        lastVal = head.val - 1
        while head.next:
            if head.next.val == lastVal:
                head.next = head.next.next
            elif head.next.next and head.next.val == head.next.next.val:
                lastVal = head.next.val
                head.next = head.next.next
            else:
                head = head.next
        
        return curr.next