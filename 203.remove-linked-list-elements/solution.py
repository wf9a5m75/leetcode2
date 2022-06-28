# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        tail = result = ListNode(-100000)

        while(head):
            if (head.val != val):
                tail.next = head
                tail = tail.next
            head = head.next
        tail.next = None
        return result.next
