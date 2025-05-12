# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val = l1.val + l2.val
        carry = 0
        head = ListNode(val%10)
        carry = val//10
        last = head
        l2 = l2.next
        l1 = l1.next
        while l1 and l2:
            val = l1.val + l2.val + carry
            head.next = ListNode(val=val%10)
            carry = val//10
            l2 = l2.next
            l1 = l1.next
            head = head.next
        while l2:
            val = l2.val + carry
            head.next = ListNode(val=val%10)
            carry = val//10
            l2 = l2.next
            head = head.next
        while l1:
            val = l1.val + carry
            head.next = ListNode(val=val%10)
            carry = val//10
            l1 = l1.next
            head = head.next
        if carry:
            head.next = ListNode(val=1)
        return last