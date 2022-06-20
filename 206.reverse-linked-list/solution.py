# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        while(head is not None):
            headNext = head.next

            child = dummy.next
            head.next = child
            dummy.next = head
            head = headNext

        return dummy.next
