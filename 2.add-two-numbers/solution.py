# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        tail = result = l1

        carryUp = 0
        while l1 and l2:
            s = l1.val + l2.val + carryUp
            carryUp = s // 10
            l1.val = s % 10
            tail = l1

            l1 = l1.next
            l2 = l2.next

        rest = l1 if l2 is None else l2
        tail.next = rest
        while rest:
            s = rest.val + carryUp
            carryUp = s // 10
            rest.val = s % 10
            tail = rest
            rest = rest.next

        if (carryUp > 0):
            tail.next = ListNode(1)
        return result
