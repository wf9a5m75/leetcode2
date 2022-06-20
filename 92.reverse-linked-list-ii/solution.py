# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        result = tail = ListNode(0)

        # ---------------
        # left side nodes
        # ---------------
        i = 1
        while(head is not None) and (i < left):
            tail.next = head
            tail = tail.next
            head = head.next
            i += 1

        # ----------------------------------
        # The nodes between left and right
        # ----------------------------------
        dummy = ListNode(0)
        while(head is not None) and (i <= right):
            headNext = head.next

            child = dummy.next
            head.next = child
            dummy.next = head
            head = headNext
            i += 1

        tail.next = dummy.next
        while(tail.next is not None):
            tail = tail.next

        # ---------------
        # right side nodes 
        # ---------------
        tail.next = head

        return result.next
