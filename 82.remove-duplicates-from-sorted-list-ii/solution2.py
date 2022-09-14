# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = tail = ListNode(-200)

        while(head):

            p = head
            head = head.next
            while(head) and (p.val == head.val):
                head = head.next
            if (p.next == head):
                tail.next = p
                tail = tail.next
        tail.next = None
        return result.next
