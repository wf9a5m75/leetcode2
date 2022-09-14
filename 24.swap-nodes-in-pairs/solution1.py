# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = tail = ListNode(0)
        while(head):
            nextHead = head.next
            if nextHead:
                nextHead = nextHead.next
            else:
                tail.next = head
                tail = tail.next
                break

            tail.next = head.next
            tail.next.next = head
            head.next = nextHead
            tail = tail.next.next

            head = nextHead

        tail.next = None
        return result.next
