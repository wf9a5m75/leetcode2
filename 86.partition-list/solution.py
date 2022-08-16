# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = lessTail = ListNode()
        others = othersTail = ListNode()
        while(head):
            headNext = head.next
            head.next = None
            if (head.val < x):
                lessTail.next = head
                lessTail = lessTail.next
            else:
                othersTail.next = head
                othersTail = othersTail.next
            head = headNext

        lessTail.next = others.next
        return less.next
