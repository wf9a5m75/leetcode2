# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None):
            return head
        result = tail = head

        head = head.next
        while(head != None):
            if (tail.val != head.val):
                tail.next = head
                tail = tail.next

            head = head.next

        tail.next = None
        return result
